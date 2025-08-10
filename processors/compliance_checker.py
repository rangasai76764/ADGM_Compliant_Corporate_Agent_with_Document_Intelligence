from processors.clause_suggester import ClauseSuggester

def check_compliance(documents):
    """
    Example function to:
    - Analyze documents for issues
    - Return a list of detected issues with suggestions
    """
    issues_found = []

    # Instantiate the clause suggester
    suggester = ClauseSuggester()

    # Example issue detection logic (replace with your actual logic)
    for doc in documents:
        # Dummy checks for demonstration
        if "signatory" not in doc.lower():
            issues_found.append({
                "document": doc,
                "section": "Signatory",
                "issue": "Missing signatory section",
                "issue_type": "missing_signatory_section",
                "severity": "Medium"
            })
        if "uae federal courts" in doc.lower():
            issues_found.append({
                "document": doc,
                "section": "Jurisdiction Clause",
                "issue": "Incorrect jurisdiction (references UAE Federal Courts)",
                "issue_type": "incorrect_jurisdiction",
                "severity": "High"
            })

    # Add suggestions for each issue found
    for issue in issues_found:
        issue_type = issue.get('issue_type')
        issue['suggestion'] = suggester.suggest_clause_fix(issue_type) if issue_type else "No suggestion available."

    return issues_found
