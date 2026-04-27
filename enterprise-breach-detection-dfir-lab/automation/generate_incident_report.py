#!/usr/bin/env python3
"""
Starter Markdown report generator.

This will be improved once real alerts, timeline, and evidence are available.
"""

from pathlib import Path
from datetime import datetime

OUTPUT = Path("automation/sample-output/generated_incident_report.md")

def main():
    report = f"""# Generated Incident Report

Generated: {datetime.utcnow().isoformat()}Z

## Summary
TBD after importing real alert evidence.

## Timeline
See `generated_timeline.csv`.

## Findings
TBD

## MITRE Mapping
TBD

## Containment
TBD
"""
    OUTPUT.write_text(report, encoding="utf-8")
    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    main()
