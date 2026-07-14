"""Privacy-minimized audit evidence.

The raw question, answer text, names, and personal identifiers are never written.
"""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Iterable, Optional


def log_event(
    *,
    event_type: str,
    decision: str,
    controls: Iterable[str],
    categories: Iterable[str] = (),
    source_document: Optional[str] = None,
    log_path: Path | str = "logs/audit.jsonl",
) -> dict:
    event = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "decision": decision,
        "controls": sorted(set(controls)),
        "categories": sorted(set(categories)),
        "source_document": source_document,
        "raw_question_stored": False,
        "answer_text_stored": False,
        "personal_data_intentionally_stored": False,
    }

    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")
    return event
