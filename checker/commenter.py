from docx import Document
import os

def insert_comments_into_docx(input_path, issues):
    doc = Document(input_path)

    for para in doc.paragraphs:
        for issue in issues:
            if issue["section"].lower() in para.text.lower():
                para.text += f"  [Comment: {issue['issue']} | Suggestion: {issue['suggestion']}]"

    output_path = input_path.replace(".docx", "_reviewed.docx")
    doc.save(output_path)
    return output_path
