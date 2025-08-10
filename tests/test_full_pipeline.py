import unittest
from processors.doc_parser import parse_docx_document
from processors.compliance_checker import check_completeness
from processors.redflag_detector import detect_issues
from processors.comment_inserter import insert_comments
from utils.json_reporter import generate_report

class TestFullPipeline(unittest.TestCase):

    def test_end_to_end_review(self):
        filepath = "data/example_input.docx"

        # Parse document
        parsed = parse_docx_document(filepath)
        self.assertIsNotNone(parsed)

        # Check completeness
        uploaded_docs = parsed.get("document_types", [])
        completeness_result = check_completeness(uploaded_docs, required_docs=5)
        self.assertIn("all_present", completeness_result)

        # Detect red flags
        issues = detect_issues(parsed)
        self.assertIsInstance(issues, list)

        # Insert comments in doc (simulate, maybe load original doc)
        reviewed_doc_path = "data/example_output.docx"
        insert_comments(filepath, issues, reviewed_doc_path)

        # Generate JSON report
        report = generate_report(parsed, completeness_result, issues)
        self.assertIn("process", report)
        self.assertIn("issues_found", report)

if __name__ == "__main__":
    unittest.main()
