import unittest
from processors.doc_parser import parse_docx_document

class TestDocParser(unittest.TestCase):

    def test_parse_simple_docx(self):
        # Provide path to an example docx file (ensure example_input.docx exists)
        filepath = "data/example_input.docx"
        content = parse_docx_document(filepath)

        self.assertIsInstance(content, dict)  # Expecting dict with parsed content
        self.assertIn("document_type", content)
        self.assertIn("text", content)
        self.assertGreater(len(content["text"]), 0)  # Non-empty text

if __name__ == "__main__":
    unittest.main()
