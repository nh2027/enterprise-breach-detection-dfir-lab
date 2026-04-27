# Attack Story

## Scenario
A simulated finance user account is targeted with repeated failed logins. One successful login occurs on a domain workstation. Suspicious PowerShell activity follows. A persistence mechanism is created. The attacker accesses the FinanceShare. Several files are copied or modified. The host shows suspicious outbound network traffic. The SOC detects, investigates, contains, and reports the incident.

## Attack Chain
1. Credential access attempt
2. Suspicious successful logon
3. Discovery
4. Suspicious PowerShell
5. Persistence
6. Sensitive file access
7. Ransomware-like file modification simulation
8. Suspicious outbound connection
9. Detection and triage
10. DFIR collection
11. Containment
12. Final report
