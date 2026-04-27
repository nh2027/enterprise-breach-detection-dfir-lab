# Asset Inventory

| Asset | OS | Purpose | Logging Enabled | Agent Installed |
|---|---|---|---|---|
| DC01 | Windows Server | AD DS, DNS, FinanceShare | Security, Sysmon, PowerShell | Wazuh, Velociraptor |
| WIN11-CLIENT01 | Windows 11 | Domain workstation | Security, Sysmon, PowerShell | Wazuh, Velociraptor |
| UBUNTU-SRV01 | Ubuntu Server | SSH/Linux target | auth.log, syslog, FIM | Wazuh, Velociraptor |
| WAZUH-SRV01 | Ubuntu | SIEM | Wazuh logs | N/A |
| SECURITYONION01 | Security Onion | Network monitoring | Zeek, Suricata | N/A |
| VELO-SRV01 | Ubuntu | DFIR server | Velociraptor logs | N/A |
| ATTACKER01 | Kali/Ubuntu | Lab-only simulation | Optional | Optional |
