def detect_red_flags(doc_text: list):
    """
    Scan document text for red flags such as missing clauses,
    incorrect jurisdiction, ambiguous language, etc.
    Returns a list of issues detected with details.
    """
    issues = []

    full_text = " ".join(doc_text).lower()

    # Example checks:
    if "adgm" not in full_text:
        issues.append({
            "section": "General",
            "issue": "Jurisdiction clause does not specify ADGM",
            "severity": "High",
            "suggestion": "Update jurisdiction to ADGM Courts."
        })

    if "signatory" not in full_text and "signature" not in full_text:
        issues.append({
            "section": "Signature Section",
            "issue": "Missing signatory or signature section",
            "severity": "High",
            "suggestion": "Include appropriate signatory blocks."
        })

    # Placeholder for ambiguous or non-binding language check (simplified)
    ambiguous_phrases = ["may", "might", "could", "should"]
    for phrase in ambiguous_phrases:
        if phrase in full_text:
            issues.append({
                "section": "General",
                "issue": f"Ambiguous language detected: '{phrase}'",
                "severity": "Medium",
                "suggestion": "Use definitive language to ensure binding clauses."
            })
            break

    # Add more rules as needed...

    return issues
