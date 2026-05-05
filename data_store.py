import json
from datetime import datetime, timezone
from pathlib import Path


DATA_FILE = Path("leads.json")


def save_lead(lead: dict) -> dict:
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                data = []
        except (json.JSONDecodeError, OSError):
            data = []
    else:
        data = []

    lead = dict(lead)
    lead["created_at"] = datetime.now(timezone.utc).isoformat()

    data.append(lead)
    DATA_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return lead