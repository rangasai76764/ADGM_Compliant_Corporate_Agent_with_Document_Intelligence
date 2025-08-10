ADGM Corporate Agent – Document Intelligence Tool

Overview

The ADGM Corporate Agent is an AI-powered legal assistant that helps review, validate, and prepare documentation for business incorporation and compliance within the Abu Dhabi Global Market (ADGM) jurisdiction.

The system uses Retrieval-Augmented Generation (RAG) with provided ADGM legal references to ensure legal accuracy and compliance.

Key Features:

Accepts .docx legal documents.

Detects missing mandatory documents for ADGM processes.

Identifies legal red flags and inconsistencies.

Inserts contextual comments directly into .docx files.

Suggests improvements for common legal clauses.

Generates a structured JSON summary report.

Folder Structure

adgm_corporate_agent/
│
├── app.py                          # Main Gradio/Streamlit app entry point
├── requirements.txt                # Dependencies list
├── README.md                       # Setup & usage instructions
├── Folder_Structure.txt            # Documentation of folder layout
├── Output_Image.png                 # Screenshot or diagram of output
│
├── config/
│   ├── checklist.json               # ADGM required documents & rules
│   └── clause_suggestions.json      # Clause improvement suggestions
│
├── reference_docs/
│   ├── Document_Upload_Categories.pdf  # Provided reference doc
│   └── other_reference_links.txt       # ADGM law links
│
├── data/
│   ├── example_input.docx           # Example document BEFORE review
│   ├── example_output.docx          # Example document AFTER review
│   ├── example_output.json          # Structured JSON summary
│   ├── Memorandum_of_Association.docx
│   ├── Articles_of_Association.docx
│   ├── Register_of_Members_and_Directors.docx
│   ├── UBO_Declaration.docx
│   └── Board_Resolution.docx
│
├── rag/
│   ├── __init__.py
│   ├── vectorstore.py               # FAISS/Chroma setup for RAG
│   └── retriever.py                 # RAG retrieval functions
│
├── processors/
│   ├── __init__.py
│   ├── doc_parser.py                # Reads & extracts .docx content
│   ├── compliance_checker.py        # Checks document completeness
│   ├── redflag_detector.py          # Detects legal issues
│   ├── comment_inserter.py          # Adds inline comments to .docx
│   └── clause_suggester.py          # Suggests legal clause improvements
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py                # File handling helpers
│   └── json_reporter.py             # Generates JSON summary
│
└── tests/
    ├── test_doc_parser.py
    ├── test_checker.py
    ├── test_full_pipeline.py
    ├── test_rag_retriever.py
    └── test_clause_suggester.py


Prerequisites

Python 3.9+
VS Code
pip package manager
Internet connection (for RAG model retrieval)

Setup Instructions

1. Clone the Repository

git clone (https://github.com/rangasai76764/ADGM_Compliant_Corporate_Agent_with_Document_Intelligence.git)
cd adgm_corporate_agent

2. Open in VS Code

Launch VS Code.

Go to File → Open Folder and select the adgm_corporate_agent folder.

Install the Python VS Code extension if not already installed.

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

Windows:

venv\Scripts\activate
Mac/Linux:

source venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

Running the Application

You can run the project using either Gradio or Streamlit (depending on how app.py is built).

Option 1: Run with Gradio

python app.py
This will start a local web server and provide a URL (e.g., http://127.0.0.1:7860) where you can interact with the app.

Option 2: Run with Streamlit

streamlit run app.py

How It Works

Upload Input File

The .docx file to be reviewed should be placed in the data folder.
Example: data/example_input.docx

Processing

The system parses the file, checks completeness against ADGM rules, detects red flags, and inserts comments.

Outputs Generated

Reviewed .docx file with inline comments.
example_output.json — structured report summarizing findings.
Console / UI display showing detected issues and missing documents.

Example Output JSON

{
    "process": "Company Incorporation",
    "documents_uploaded": 4,
    "required_documents": 5,
    "missing_documents": ["Register of Members and Directors"],
    "issues_found": [
        {
            "document": "Articles of Association",
            "section": "Clause 3.1",
            "issue": "Jurisdiction clause does not specify ADGM",
            "severity": "High",
            "suggestion": "Update jurisdiction to ADGM Courts."
        }
    ]
}
Notes

Place your input .docx files inside the data folder before running. [ Already i have give input .docx file ]


The system automatically detects which process you’re following (e.g., Company Incorporation) and checks compliance.
