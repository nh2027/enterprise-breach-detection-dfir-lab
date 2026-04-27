# Detection Coverage Matrix

| ID | Detection | MITRE Technique | Log Source | Rule Type | Triggered? | False Positive Risk | Confidence | Evidence |
|---|---|---|---|---|---|---|---|---|
| DET-001 | Multiple failed logons | T1110 | Windows Security | Sigma/Wazuh | Planned | Medium | TBD | TBD |
| DET-002 | Failed followed by success | T1110 | Windows Security | Sigma | Planned | Medium | TBD | TBD |
| DET-003 | New local user created | T1136 | Windows Security | Sigma/Wazuh | Planned | Low | TBD | TBD |
| DET-004 | User added to privileged group | T1098 | Windows Security | Sigma | Planned | Medium | TBD | TBD |
| DET-005 | Suspicious PowerShell encoded command | T1059.001 | PowerShell/Sysmon | Sigma/Wazuh | Planned | Medium | TBD | TBD |
| DET-006 | PowerShell remote content request | T1059.001 | PowerShell/Sysmon | Sigma | Planned | Medium | TBD | TBD |
| DET-007 | Suspicious parent-child process | T1059 | Sysmon | Sigma | Planned | Medium | TBD | TBD |
| DET-008 | Scheduled task created | T1053.005 | Security/Sysmon | Sigma/Wazuh | Planned | Low | TBD | TBD |
| DET-009 | Registry Run key modified | T1060/T1547.001 | Sysmon | Sigma/Wazuh | Planned | Medium | TBD | TBD |
| DET-010 | New service created | T1543.003 | System/Security | Sigma | Planned | Medium | TBD | TBD |
| DET-011 | Sensitive share access | T1005 | Security | Sigma | Planned | Medium | TBD | TBD |
| DET-012 | Mass file modification | Impact | Wazuh FIM/Sysmon | Sigma/Wazuh | Planned | Medium | TBD | TBD |
| DET-013 | Unusual outbound connection | Command and Control | Zeek/Sysmon | Sigma | Planned | Medium | TBD | TBD |
| DET-014 | Suspicious DNS query pattern | Command and Control | Zeek DNS | Sigma | Planned | Medium | TBD | TBD |
| DET-015 | SSH brute-force against Ubuntu | T1110 | auth.log/Wazuh | Sigma/Wazuh | Planned | Low | TBD | TBD |
