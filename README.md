# Enterprise Breach Detection, DFIR and Detection-as-Code Lab

## Overview
This project builds an isolated enterprise-style cybersecurity lab to simulate, detect, investigate, and document a realistic breach scenario.

The lab will include:
- Active Directory domain controller
- Domain-joined Windows workstation
- Ubuntu server
- Wazuh SIEM
- Sysmon telemetry
- Security Onion network monitoring
- Velociraptor DFIR collection
- Sigma and Wazuh detections
- GitHub Actions detection-as-code testing
- Python alert triage and incident report automation

## Project Goal
Move beyond a basic SIEM homelab by building a full SOC workflow:
1. Build an enterprise lab.
2. Simulate a safe multi-stage attack.
3. Collect endpoint, identity, Linux, and network logs.
4. Write and test detections.
5. Investigate the incident.
6. Collect DFIR evidence.
7. Automate triage and reporting.
8. Produce a professional incident report.

## Safety Scope
This lab is for defensive learning only. All simulations must be run inside an isolated virtual lab network. No real malware, public targets, or unauthorized systems should be used.

## Architecture
See:
- `architecture/ip-plan.md`
- `architecture/asset-inventory.md`
- `architecture/logging-architecture.md`

## Final Deliverables
- 15+ Sigma detections
- 8+ Wazuh rules/queries
- Positive and benign test logs
- GitHub Actions detection tests
- Full incident report
- DFIR evidence table
- Python timeline/report automation
- Polished screenshots and documentation
