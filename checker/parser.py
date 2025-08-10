from docx import Document

def extract_text_from_docx(file_obj):
    doc = Document(file_obj)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    return full_text
