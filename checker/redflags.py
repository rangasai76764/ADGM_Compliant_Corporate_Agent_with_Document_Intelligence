def detect_red_flags(text):
    issues = []

    if "UAE" in text and "ADGM" not in text:
        issues.append({
            "section": "Jurisdiction Clause",
            "issue": "Mentions 'UAE' instead of 'ADGM'",
            "severity": "High",
            "suggestion": "Change jurisdiction to ADGM."
        })

    if "signatory" not in text.lower():
        issues.append({
            "section": "Signatory",
            "issue": "Missing signatory section",
            "severity": "Medium",
            "suggestion": "Add appropriate signature section."
        })

    return issues
