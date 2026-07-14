import unittest
from pathlib import Path

from policy_search import PolicySearchEngine


class PolicySearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = PolicySearchEngine.from_directory(
            Path(__file__).resolve().parents[1] / "policies"
        )

    def test_loads_only_approved_synthetic_policies(self):
        self.assertGreater(len(self.engine.chunks), 0)
        for chunk in self.engine.chunks:
            self.assertEqual(chunk.status, "Approved for POC")
            self.assertEqual(chunk.classification, "Internal Synthetic")

    def test_vacation_question_retrieves_leave_policy(self):
        results = self.engine.search("How many vacation days do employees receive?")
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0].chunk.document_id, "HR-LEAVE-001")

    def test_remote_question_retrieves_remote_policy(self):
        results = self.engine.search("How do I request remote work?")
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0].chunk.document_id, "HR-REMOTE-001")

    def test_expense_question_retrieves_expense_policy(self):
        results = self.engine.search("When must I submit an expense report?")
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0].chunk.document_id, "FIN-EXPENSE-001")

    def test_source_has_traceability_metadata(self):
        result = self.engine.search("vacation request approval")[0]
        self.assertTrue(result.chunk.title)
        self.assertTrue(result.chunk.section)
        self.assertTrue(result.chunk.version)


if __name__ == "__main__":
    unittest.main()
