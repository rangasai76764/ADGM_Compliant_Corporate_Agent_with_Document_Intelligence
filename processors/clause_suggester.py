class ClauseSuggester:
    def __init__(self):
        # Mapping keywords to suggested fixes
        self.suggestion_map = {
            "signatory": "Add signatory block with name, title, signature date and capacity.",
            "jurisdiction": "Update jurisdiction to ADGM Courts.",
            "ambiguous": "Clarify language to make obligations binding and explicit.",
            "missing": "Include the required clause as per ADGM regulations.",
            # Add more mappings as needed
        }

    def suggest_clause_fix(self, issue_text: str) -> str:
        issue_text_lower = issue_text.lower()
        for keyword, suggestion in self.suggestion_map.items():
            if keyword in issue_text_lower:
                return suggestion
        return "No suggestion available for this issue."
