#!/usr/bin/env python3
"""
Starter parser for Wazuh alerts.

Input: alerts JSON file exported from Wazuh.
Output: grouped alert summary JSON.

This is a starter. We will improve it after you have real alert exports.
"""

import json
from collections import defaultdict
from pathlib import Path

INPUT = Path("automation/sample-output/sample_wazuh_alerts.json")
OUTPUT = Path("automation/sample-output/alert_summary.json")

def main():
    if not INPUT.exists():
        print(f"Missing input file: {INPUT}")
        print("Export sample Wazuh alerts later and save them here.")
        return

    alerts = json.loads(INPUT.read_text(encoding="utf-8"))
    summary = defaultdict(lambda: {"count": 0, "rules": defaultdict(int)})

    for alert in alerts:
        host = alert.get("agent", {}).get("name", "unknown-host")
        rule = alert.get("rule", {}).get("description", "unknown-rule")
        summary[host]["count"] += 1
        summary[host]["rules"][rule] += 1

    clean = {
        host: {"count": data["count"], "rules": dict(data["rules"])}
        for host, data in summary.items()
    }

    OUTPUT.write_text(json.dumps(clean, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    main()
