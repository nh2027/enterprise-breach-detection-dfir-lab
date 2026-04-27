#!/usr/bin/env python3
"""
Starter incident timeline generator.

Input: Wazuh alerts JSON.
Output: CSV timeline.
"""

import csv
import json
from pathlib import Path

INPUT = Path("automation/sample-output/sample_wazuh_alerts.json")
OUTPUT = Path("automation/sample-output/generated_timeline.csv")

def main():
    if not INPUT.exists():
        print(f"Missing input file: {INPUT}")
        return

    alerts = json.loads(INPUT.read_text(encoding="utf-8"))

    rows = []
    for alert in alerts:
        rows.append({
            "timestamp": alert.get("timestamp", ""),
            "host": alert.get("agent", {}).get("name", ""),
            "rule": alert.get("rule", {}).get("description", ""),
            "level": alert.get("rule", {}).get("level", ""),
            "mitre": ",".join(alert.get("rule", {}).get("mitre", {}).get("id", [])) if isinstance(alert.get("rule", {}).get("mitre", {}), dict) else "",
            "summary": alert.get("full_log", "")[:200],
        })

    rows.sort(key=lambda x: x["timestamp"])

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "host", "rule", "level", "mitre", "summary"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    main()
