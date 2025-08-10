def detect_process_and_checklist(filenames):
    # Simple logic — improve later
    required_docs = {
        "Company Incorporation": [
            "Articles of Association",
            "Memorandum of Association",
            "Board Resolution",
            "UBO Declaration",
            "Register of Members and Directors"
        ]
    }

    matched = []
    for name in filenames:
        for doc in required_docs["Company Incorporation"]:
            if doc.lower().replace(" ", "_")[:5] in name.lower():
                matched.append(doc)

    missing = list(set(required_docs["Company Incorporation"]) - set(matched))
    return "Company Incorporation", {"uploaded": len(matched), "required": 5, "missing": missing}
