import json
from typing import Dict, Any

def save_json_report(data: Dict[str, Any], filepath: str) -> None:
    """
    Save a dictionary as a pretty-printed JSON file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_json_report(filepath: str) -> Dict[str, Any]:
    """
    Load JSON content from a file into a dictionary.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
