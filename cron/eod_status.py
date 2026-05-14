"""EOD status: summarize today's applications + pipeline, email digest, log."""

import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lib.notify import send_email  # noqa: E402


CANONICAL_STATES = [
    "Evaluated",
    "Applied",
    "Responded",
    "Interview",
    "Offer",
    "Rejected",
    "Discarded",
    "SKIP",
]


def parse_applications(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
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
    return rows


def main() -> None:
    today = date.today().isoformat()
    apps = parse_applications(ROOT / "data" / "applications.md")
    applied_today = [
        a for a in apps
        if a["status"].strip().lower() == "applied" and a["date"].startswith(today)
    ]
    pipeline = {k: 0 for k in CANONICAL_STATES}
    for a in apps:
        st = a["status"].strip()
        if st in pipeline:
            pipeline[st] += 1

    subject = f"🌆 Career-Ops EOD: {len(applied_today)} applied today"

    def li(a: dict) -> str:
        return f"<li>{a['company']} — {a['role']} (score {a['score']})</li>"

    today_list = "".join(li(a) for a in applied_today) or "<li>No applications today.</li>"
    pipeline_rows = "".join(
        f"<li>{k}: {v}</li>" for k, v in pipeline.items() if v
    ) or "<li>(empty)</li>"

    body = f"""<h3>End of day · {today}</h3>
<p><b>{len(applied_today)}</b> applications sent today.</p>
<ul>{today_list}</ul>
<h4>Pipeline</h4>
<ul>{pipeline_rows}</ul>
"""
    send_email(subject, body)

    history = ROOT / "data" / "run_history.jsonl"
    history.parent.mkdir(parents=True, exist_ok=True)
    with history.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "type": "eod_status",
                    "at": datetime.now(timezone.utc).isoformat(),
                    "applied_today": len(applied_today),
                    "pipeline": pipeline,
                }
            )
            + "\n"
        )


if __name__ == "__main__":
    main()
