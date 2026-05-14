"""Career-Ops Streamlit dashboard — Phase 1 MVP."""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "reports"
OUTPUT_DIR = ROOT / "output"
APPS_FILE = ROOT / "data" / "applications.md"
RUN_HISTORY = ROOT / "data" / "run_history.jsonl"

st.set_page_config(page_title="Career-Ops", layout="wide")


# ---- Data loaders --------------------------------------------------------


@st.cache_data(ttl=30)
def load_reports() -> pd.DataFrame:
    rows: list[dict] = []
    if not REPORTS_DIR.exists():
        return pd.DataFrame(rows)
    for path in REPORTS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")

        def find(pat: str, flags: int = 0) -> str:
            m = re.search(pat, text, flags)
            return m.group(1).strip() if m else ""

        title = find(r"^#\s*Evaluation:\s*(.+)$", re.MULTILINE)
        if " — " in title:
            company, role = title.split(" — ", 1)
        elif " - " in title:
            company, role = title.split(" - ", 1)
        else:
            company, role = title, ""
        try:
            score = float(find(r"\*\*Score:\*\*\s*([\d.]+)/5") or 0)
        except ValueError:
            score = 0.0
        rows.append(
            {
                "file": path.name,
                "company": company.strip(),
                "role": role.strip(),
                "score": score,
                "archetype": find(r"\*\*Archetype:\*\*\s*(.+)"),
                "url": find(r"\*\*URL:\*\*\s*(\S+)"),
                "legitimacy": find(r"\*\*Legitimacy:\*\*\s*(.+)"),
                "date": find(r"\*\*Date:\*\*\s*(\S+)"),
                "mtime": path.stat().st_mtime,
            }
        )
    return pd.DataFrame(rows)


@st.cache_data(ttl=30)
def load_applications() -> pd.DataFrame:
    if not APPS_FILE.exists():
        return pd.DataFrame(
            columns=["num", "date", "company", "role", "score", "status", "pdf", "report", "notes"]
        )
    rows: list[dict] = []
    for line in APPS_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] == "#" or not cells[0]:
            continue
        try:
            int(cells[0])
        except ValueError:
            continue
        while len(cells) < 9:
            cells.append("")
        rows.append(
            {
                "num": int(cells[0]),
                "date": cells[1],
                "company": cells[2],
                "role": cells[3],
                "score": cells[4],
                "status": cells[5],
                "pdf": cells[6],
                "report": cells[7],
                "notes": cells[8],
            }
        )
    return pd.DataFrame(rows)


@st.cache_data(ttl=30)
def load_output_folders() -> set[str]:
    if not OUTPUT_DIR.exists():
        return set()
    return {p.name for p in OUTPUT_DIR.iterdir() if p.is_dir()}


@st.cache_data(ttl=30)
def load_run_history() -> pd.DataFrame:
    if not RUN_HISTORY.exists():
        return pd.DataFrame()
    rows: list[dict] = []
    for line in RUN_HISTORY.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return pd.DataFrame(rows)


def status_for(company: str, role: str, apps_df: pd.DataFrame) -> str:
    if apps_df.empty:
        return ""
    prefix = role.strip()[:24]
    matches = apps_df[apps_df["company"].str.strip() == company.strip()]
    for _, a in matches.iterrows():
        if a["role"].strip().startswith(prefix):
            return a["status"]
    return ""


# ---- Sidebar -------------------------------------------------------------

st.sidebar.title("Career-Ops")

if st.sidebar.button("▶ Run scan now", use_container_width=True):
    with st.spinner("Running scan…"):
        try:
            result = subprocess.run(
                ["node", "scan.mjs"], cwd=ROOT, capture_output=True, text=True, timeout=900
            )
            if result.returncode == 0:
                st.sidebar.success("Scan complete.")
                st.cache_data.clear()
            else:
                st.sidebar.error(f"Scan failed (exit {result.returncode}).")
                st.sidebar.code(result.stderr[:600] or result.stdout[:600])
        except FileNotFoundError:
            st.sidebar.error("`node` not found on PATH. Install Node or run scan locally.")
        except subprocess.TimeoutExpired:
            st.sidebar.error("Scan timed out after 15 min.")

reports_df = load_reports()
apps_df = load_applications()
folders = load_output_folders()
history_df = load_run_history()

st.sidebar.divider()
st.sidebar.metric("Roles scored", len(reports_df))
st.sidebar.metric("Roles tailored", len(folders))
live_statuses = ["Applied", "Interview", "Offer", "Rejected", "Responded"]
applied_count = (
    int(apps_df["status"].isin(live_statuses).sum()) if not apps_df.empty else 0
)
st.sidebar.metric("Applications", applied_count)

last_run = ""
if not history_df.empty:
    col = "started_at" if "started_at" in history_df.columns else "at"
    if col in history_df.columns:
        last_run = history_df[col].dropna().iloc[-1] if not history_df[col].dropna().empty else ""
if last_run:
    st.sidebar.caption(f"Last run: {last_run}")

page = st.sidebar.radio("Page", ["Home", "Runs", "Pipeline"])


# ---- Pages ---------------------------------------------------------------

if page == "Home":
    st.header("Today's top roles")
    if reports_df.empty:
        st.info("No reports in `reports/` yet. Run a scan.")
    else:
        c1, c2, c3 = st.columns(3)
        score_range = c1.slider("Score range", 0.0, 5.0, (3.0, 5.0), 0.1)
        arch_options = ["(all)"] + sorted({a for a in reports_df["archetype"] if a})
        arch = c2.selectbox("Archetype", arch_options)
        status_options = ["(all)"] + (sorted({s for s in apps_df["status"] if s}) if not apps_df.empty else [])
        status_sel = c3.selectbox("Status", status_options)

        df = reports_df.copy()
        df["status"] = df.apply(lambda r: status_for(r["company"], r["role"], apps_df), axis=1)
        df["tailored"] = df.apply(
            lambda r: "Y" if f"{r['company']} - {r['role']}" in folders else "N", axis=1
        )
        df = df[(df["score"] >= score_range[0]) & (df["score"] <= score_range[1])]
        if arch != "(all)":
            df = df[df["archetype"] == arch]
        if status_sel != "(all)":
            df = df[df["status"] == status_sel]
        df = df.sort_values("score", ascending=False)

        view = df[["company", "role", "score", "archetype", "legitimacy", "status", "tailored", "url"]]
        st.dataframe(
            view,
            use_container_width=True,
            hide_index=True,
            column_config={"url": st.column_config.LinkColumn("Apply")},
        )

        st.subheader("Actions")
        if df.empty:
            st.caption("No rows match the current filters.")
        else:
            labels = df.apply(lambda r: f"{r['company']} — {r['role']}", axis=1).tolist()
            sel_label = st.selectbox("Select a role", labels)
            target_row = df[
                df.apply(lambda r: f"{r['company']} — {r['role']}" == sel_label, axis=1)
            ].iloc[0]

            a1, a2 = st.columns(2)
            if a1.button("Tailor this role", use_container_width=True):
                folder = OUTPUT_DIR / f"{target_row['company']} - {target_row['role']}"
                folder.mkdir(parents=True, exist_ok=True)
                st.success(
                    f"Folder created: `output/{folder.name}/`. "
                    f"Run the tailoring CLI from the repo to generate PDFs + metadata."
                )
                st.cache_data.clear()

            if a2.button("Mark applied", use_container_width=True):
                today = datetime.now().strftime("%Y-%m-%d")
                next_num = int(apps_df["num"].max() + 1) if not apps_df.empty else 1
                report_prefix = target_row["file"].split("-")[0]
                row = (
                    f"\n| {next_num} | {today} | {target_row['company']} | {target_row['role']} "
                    f"| {target_row['score']:.1f}/5 | Applied | ✅ | "
                    f"[{report_prefix}](reports/{target_row['file']}) | (marked from dashboard) |"
                )
                with APPS_FILE.open("a", encoding="utf-8") as f:
                    f.write(row)
                st.success(f"Marked applied as row #{next_num}.")
                st.cache_data.clear()

elif page == "Runs":
    st.header("Scan history")
    if history_df.empty:
        st.info("No runs recorded yet. `data/run_history.jsonl` will populate on first cron run.")
    else:
        sort_col = "started_at" if "started_at" in history_df.columns else history_df.columns[0]
        st.dataframe(
            history_df.sort_values(sort_col, ascending=False),
            use_container_width=True,
            hide_index=True,
        )

elif page == "Pipeline":
    st.header("Application pipeline")
    if apps_df.empty:
        st.info("`data/applications.md` has no rows yet.")
    else:
        funnel_states = ["Evaluated", "Applied", "Responded", "Interview", "Offer", "Rejected", "Discarded", "SKIP"]
        funnel = {k: int((apps_df["status"].str.strip() == k).sum()) for k in funnel_states}
        cols = st.columns(len(funnel))
        for col, (k, v) in zip(cols, funnel.items()):
            col.metric(k, v)
        st.dataframe(
            apps_df[["num", "date", "company", "role", "score", "status", "notes"]],
            use_container_width=True,
            hide_index=True,
        )
