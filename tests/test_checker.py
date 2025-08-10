import unittest
from processors.compliance_checker import check_completeness

class TestComplianceChecker(unittest.TestCase):

    def test_check_completeness_missing_doc(self):
        # Simulate uploaded docs list for company incorporation
        uploaded_docs = ["Articles of Association", "MoA", "Board Resolution", "Incorporation Application"]
        required_docs = 5  # From config checklist

        result = check_completeness(uploaded_docs, required_docs)

        self.assertFalse(result["all_present"])
        self.assertIn("missing_document", result)
        self.assertEqual(result["missing_document"], "Register of Members and Directors")

    def test_check_completeness_all_present(self):
        uploaded_docs = [
            "Articles of Association",
            "MoA",
            "Board Resolution",
            "Incorporation Application",
            "Register of Members and Directors"
        ]
        required_docs = 5

        result = check_completeness(uploaded_docs, required_docs)

        self.assertTrue(result["all_present"])
        self.assertIsNone(result.get("missing_document"))

if __name__ == "__main__":
    unittest.main()
