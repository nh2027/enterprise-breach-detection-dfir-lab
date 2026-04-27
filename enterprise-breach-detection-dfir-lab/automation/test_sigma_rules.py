#!/usr/bin/env python3
"""
Basic Sigma rule quality checker for the lab.

This starter script checks:
- YAML parses correctly
- Required fields exist
- Rule IDs are unique
- ATT&CK tags are present
- Each rule has false positives and level
"""

from pathlib import Path
import sys
import yaml

RULE_DIR = Path("detections/sigma")
REQUIRED_FIELDS = ["title", "id", "status", "description", "author", "date", "logsource", "detection", "falsepositives", "level", "tags"]

def main() -> int:
    if not RULE_DIR.exists():
        print(f"Missing rule directory: {RULE_DIR}")
        return 1

    rule_files = sorted(RULE_DIR.glob("*.yml")) + sorted(RULE_DIR.glob("*.yaml"))

    if not rule_files:
        print("No Sigma rules found yet. Add rules in detections/sigma/")
        return 0

    seen_ids = set()
    failed = False

    for path in rule_files:
        print(f"Checking {path}")
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"  ERROR: YAML parse failed: {exc}")
            failed = True
            continue

        if not isinstance(data, dict):
            print("  ERROR: Rule is not a YAML object")
            failed = True
            continue

        for field in REQUIRED_FIELDS:
            if field not in data or data[field] in (None, "", []):
                print(f"  ERROR: Missing required field: {field}")
                failed = True

        rule_id = data.get("id")
        if rule_id:
            if rule_id in seen_ids:
                print(f"  ERROR: Duplicate rule id: {rule_id}")
                failed = True
            seen_ids.add(rule_id)

        tags = data.get("tags", [])
        if not any(str(tag).startswith("attack.") for tag in tags):
            print("  ERROR: Missing MITRE ATT&CK tag")
            failed = True

    if failed:
        print("Sigma validation failed.")
        return 1

    print("All Sigma rule checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
