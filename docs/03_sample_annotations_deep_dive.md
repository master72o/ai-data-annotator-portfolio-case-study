# Module 3: Sample Annotations Deep-Dive (Before vs After)

## 3.1 Sample 1: Code Generation with Negative Constraints

### User Prompt
> "Write a Python function `parse_json_config(file_path)` that reads a JSON file and returns a dictionary. Do NOT use any external third-party libraries like `pandas` or `requests`. Include error handling for missing files."

---

### Baseline Response (Low Quality / Rejected)
```python
import pandas as pd # ❌ VIOLATION: Used external library

def parse_json_config(file_path):
    # Reads json using pandas
    df = pd.read_json(file_path)
    return df.to_dict()
```
*Annotator Note: Failed negative constraint by importing `pandas`. Failed error handling requirement for missing files.*

---

### Gold Standard SFT Response (Chosen)
```python
import json
import os

def parse_json_config(file_path: str) -> dict:
    """Reads a JSON configuration file and returns a dictionary.
    
    Raises:
        FileNotFoundError: If file_path does not exist.
        json.JSONDecodeError: If JSON formatting is invalid.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found at: {file_path}")
        
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
```
*Annotator Note: Adheres to all negative constraints (uses standard library `json` and `os` only). Includes explicit error handling and type hints.*
