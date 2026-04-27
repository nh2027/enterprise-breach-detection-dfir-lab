# Logging Architecture

## Windows Logs
Collected from:
- DC01
- WIN11-CLIENT01

Sources:
- Windows Security logs
- Sysmon logs
- PowerShell Operational logs
- Defender logs
- System logs
- Application logs

## Linux Logs
Collected from:
- UBUNTU-SRV01

Sources:
- `/var/log/auth.log`
- `/var/log/syslog`
- SSH authentication events
- File Integrity Monitoring paths

## Network Logs
Collected by:
- Security Onion

Sources:
- Zeek connection logs
- Zeek DNS logs
- Suricata alerts

## DFIR Evidence
Collected by:
- Velociraptor

Artifact types:
- Running processes
- Scheduled tasks
- Autoruns
- PowerShell history
- Recent files
- Network connections
- Local users/groups
