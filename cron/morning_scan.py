"""Morning scan: run scan.mjs, diff reports/, email digest, log to run_history.jsonl."""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lib.notify import send_email  # noqa: E402


def parse_report(path: Path) -> dict:
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
    score_raw = find(r"\*\*Score:\*\*\s*([\d.]+)/5")
    try:
        score = float(score_raw) if score_raw else 0.0
    except ValueError:
        score = 0.0
    return {
        "file": path.name,
        "company": company.strip(),
        "role": role.strip(),
        "score": score,
        "archetype": find(r"\*\*Archetype:\*\*\s*(.+)"),
        "url": find(r"\*\*URL:\*\*\s*(\S+)"),
        "legitimacy": find(r"\*\*Legitimacy:\*\*\s*(.+)"),
    }


def run_scan(root: Path) -> None:
    """Invoke the existing Node scanner. scan.mjs hits ATS APIs directly."""
    subprocess.run(["node", "scan.mjs"], cwd=root, check=True, timeout=900)


def format_digest(roles: list[dict]) -> tuple[str, str]:
    high = [r for r in roles if r["score"] >= 4.0]
    subject = f"☀️ Career-Ops: {len(roles)} new roles today, {len(high)} scoring ≥4.0"
    dashboard_url = os.environ.get("DASHBOARD_URL", "")

    def li(r: dict) -> str:
        label = f"{r['company']} — {r['role']}" if r["role"] else r["company"]
        return (
            f'<li><b>{r["score"]:.1f}/5</b> · {r["archetype"] or "?"} · '
            f'<a href="{r["url"]}">{label}</a></li>'
        )

    top10 = "\n".join(li(r) for r in roles[:10]) or "<li>(none)</li>"
    link = f'<p><a href="{dashboard_url}">Open dashboard</a></p>' if dashboard_url else ""
    body = f"""<h3>Morning scan complete</h3>
<p><b>{len(roles)}</b> new roles found. <b>{len(high)}</b> scored ≥ 4.0.</p>
<h4>Top 10</h4>
<ol>{top10}</ol>
{link}
"""
    return subject, body


def main() -> None:
    started = time.time()
    start_iso = datetime.now(timezone.utc).isoformat()
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(exist_ok=True)
    before = {p.name for p in reports_dir.glob("*.md")}

    try:
        run_scan(ROOT)
    except Exception as err:  # scan failures get an alert email then re-raise
        send_email(
            "⚠️ Career-Ops morning scan failed",
            f"<pre>{type(err).__name__}: {err}</pre>",
        )
        raise

    after = list(reports_dir.glob("*.md"))
    new_files = [p for p in after if p.name not in before]
    new_roles = sorted(
        (parse_report(p) for p in new_files), key=lambda r: -r["score"]
    )

    subject, body = format_digest(new_roles)
    send_email(subject, body)

    history = ROOT / "data" / "run_history.jsonl"
    history.parent.mkdir(parents=True, exist_ok=True)
    with history.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "type": "morning_scan",
                    "started_at": start_iso,
                    "duration_sec": round(time.time() - started, 2),
                    "new_roles_found": len(new_roles),
                    "roles_4plus": sum(1 for r in new_roles if r["score"] >= 4.0),
                }
            )
            + "\n"
        )


if __name__ == "__main__":
    main()
