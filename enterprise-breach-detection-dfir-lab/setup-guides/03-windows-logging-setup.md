# 03 - Windows Logging Setup

## Goal
Enable useful endpoint and identity telemetry.

## Enable
- Windows Security auditing
- PowerShell Script Block Logging
- PowerShell Module Logging
- PowerShell Transcription
- Sysmon
- Command-line process logging

## Systems
- DC01
- WIN11-CLIENT01

## Evidence to Capture
- Sysmon installed
- PowerShell logging enabled
- Security audit policy enabled
- Wazuh receiving Windows logs
- Wazuh receiving Sysmon logs
