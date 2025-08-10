def summarize_issues(results, process, checklist_result):
    all_issues = []
    for r in results:
        for issue in r["issues"]:
            all_issues.append({
                "document": r["file"],
                "section": issue["section"],
                "issue": issue["issue"],
                "severity": issue["severity"],
                "suggestion": issue["suggestion"]
            })

    return {
        "process": process,
        "documents_uploaded": checklist_result["uploaded"],
        "required_documents": checklist_result["required"],
        "missing_documents": checklist_result["missing"],
        "issues_found": all_issues
    }
