import json
from pathlib import Path
import tempfile
import unittest

from audit import log_event


class AuditTests(unittest.TestCase):
    def test_log_excludes_raw_question_and_answer(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = Path(temp_dir) / "audit.jsonl"
            event = log_event(
                event_type="question_evaluated",
                decision="blocked",
                controls=["personal_data_minimization"],
                categories=["email_address"],
                log_path=log_path,
            )
            stored = json.loads(log_path.read_text(encoding="utf-8").strip())
            self.assertFalse(event["raw_question_stored"])
            self.assertFalse(event["answer_text_stored"])
            self.assertFalse(event["personal_data_intentionally_stored"])
            self.assertNotIn("question", stored)
            self.assertNotIn("answer", stored)


if __name__ == "__main__":
    unittest.main()
