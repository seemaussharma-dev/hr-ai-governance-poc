import unittest
from pathlib import Path

from policy_search import PolicySearchEngine
from response_builder import build_response


class ResponseBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = PolicySearchEngine.from_directory(
            Path(__file__).resolve().parents[1] / "policies"
        )

    def test_answer_has_source(self):
        question = "How many vacation days do employees receive?"
        response = build_response(question, self.engine.search(question))
        self.assertEqual(response.status, "answered")
        self.assertIn("15 paid vacation days", response.answer)
        self.assertEqual(
            response.source_title,
            "ABC Horizon Media Vacation and Leave Policy",
        )
        self.assertTrue(response.source_section)
        self.assertTrue(response.source_version)

    def test_unsupported_question_escalates(self):
        question = "What is the parental leave policy?"
        response = build_response(question, self.engine.search(question))
        self.assertEqual(response.status, "escalated")
        self.assertIn("Human Resources", response.answer)
    def test_company_parental_leave_question_escalates(self):
        question = "What is the company's parental leave policy?"
        response = build_response(question, self.engine.search(question))

        self.assertEqual(response.status, "escalated")
        self.assertIn("Human Resources", response.answer)
        # self.assertIsNone(response.source_title)
        self.assertEqual(response.source_title, "")
    def test_response_is_extractive(self):
        question = "When must I submit an expense report?"
        response = build_response(question, self.engine.search(question))
        source_texts = [
            result.chunk.text for result in self.engine.search(question)
            if result.chunk.title == response.source_title
            and result.chunk.section == response.source_section
    
        ]
        self.assertTrue(any(response.answer in text for text in source_texts))


if __name__ == "__main__":
    unittest.main()
