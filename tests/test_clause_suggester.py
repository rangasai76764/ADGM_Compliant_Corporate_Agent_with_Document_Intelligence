import unittest
from processors.clause_suggester import ClauseSuggester

class TestClauseSuggester(unittest.TestCase):
    def setUp(self):
        self.suggester = ClauseSuggester()

    def test_known_issue(self):
        issue_type = "jurisdiction_missing"
        suggestion = self.suggester.suggest_clause_fix(issue_type)
        self.assertIn("ADGM Companies Regulations", suggestion)

    def test_unknown_issue(self):
        issue_type = "non_existent_issue"
        suggestion = self.suggester.suggest_clause_fix(issue_type)
        self.assertEqual(suggestion, "No suggestion available for this issue.")

if __name__ == "__main__":
    unittest.main()
