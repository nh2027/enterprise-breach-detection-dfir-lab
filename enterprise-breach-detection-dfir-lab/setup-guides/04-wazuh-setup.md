# 04 - Wazuh Setup

## Goal
Use Wazuh as the SIEM layer for endpoint alerting.

## Agents
Install agents on:
- DC01
- WIN11-CLIENT01
- UBUNTU-SRV01

## Collect
- Windows Security logs
- Sysmon logs
- PowerShell logs
- Defender logs
- Linux auth logs
- Linux syslog
- FIM events

## Evidence to Capture
- Agents active
- Windows logs visible
- Sysmon events visible
- Linux auth events visible
- FIM alerts visible
