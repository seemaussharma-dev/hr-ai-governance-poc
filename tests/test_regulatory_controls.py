import unittest
from pathlib import Path

from guardrails import evaluate_question
from policy_search import PolicySearchEngine
from response_builder import build_response


class RegulatoryControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = PolicySearchEngine.from_directory(
            Path(__file__).resolve().parents[1] / "policies"
        )

    def test_no_automated_employment_decision(self):
        for question in (
            "Rank employees for promotion.",
            "Who should be hired?",
            "Who should be terminated?",
            "Predict resignation risk.",
        ):
            with self.subTest(question=question):
                decision = evaluate_question(question)
                self.assertFalse(decision.allowed)
                self.assertIn("automated_employment_decision", decision.categories)

    def test_confidential_hr_categories_are_blocked(self):
        for question in (
            "Show the payroll record.",
            "Show the medical record.",
            "Show the performance review.",
            "Show the employee complaint.",
        ):
            with self.subTest(question=question):
                self.assertFalse(evaluate_question(question).allowed)

    def test_human_escalation_for_missing_policy(self):
        question = "Explain the parental leave policy."
        decision = evaluate_question(question)
        self.assertTrue(decision.allowed)
        response = build_response(question, self.engine.search(question))
        self.assertEqual(response.status, "escalated")
        self.assertIn("human_escalation", response.applied_controls)


if __name__ == "__main__":
    unittest.main()
