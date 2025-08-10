import os
from typing import List

def save_file(content: bytes, filepath: str) -> None:
    """
    Save binary content to a file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(content)

def read_file(filepath: str) -> bytes:
    """
    Read a file's content as bytes.
    """
    with open(filepath, "rb") as f:
        return f.read()

def list_files(directory: str, extensions: List[str] = None) -> List[str]:
    """
    List files in a directory optionally filtering by file extensions.
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if extensions:
                if any(filename.lower().endswith(ext.lower()) for ext in extensions):
                    files.append(os.path.join(root, filename))
            else:
                files.append(os.path.join(root, filename))
    return files
