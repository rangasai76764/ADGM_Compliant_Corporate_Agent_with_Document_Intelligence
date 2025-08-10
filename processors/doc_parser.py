from docx import Document

def extract_docx_text(docx_path):
    """
    Extract text content and basic structure from a .docx file.
    Returns a dictionary mapping paragraphs and headings.
    """
    doc = Document(docx_path)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return content

def identify_document_type(doc_text):
    """
    Basic heuristic to identify document type from its text.
    For example, if 'Articles of Association' in text, return 'AoA'.
    """
    joined_text = " ".join(doc_text).lower()
    if "articles of association" in joined_text:
        return "Articles of Association"
    elif "memorandum of association" in joined_text:
        return "Memorandum of Association"
    elif "board resolution" in joined_text:
        return "Board Resolution Template"
    elif "shareholder resolution" in joined_text:
        return "Shareholder Resolution Template"
    elif "incorporation application" in joined_text:
        return "Incorporation Application Form"
    elif "ubo declaration" in joined_text:
        return "UBO Declaration Form"
    elif "register of members and directors" in joined_text:
        return "Register of Members and Directors"
    elif "change of registered address" in joined_text:
        return "Change of Registered Address Notice"
    else:
        return "Unknown Document Type"
