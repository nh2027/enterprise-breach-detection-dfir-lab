# IP Plan

Network: `10.10.10.0/24`

| Hostname | Role | IP Address | Notes |
|---|---|---:|---|
| DC01 | Windows Server / Domain Controller / DNS | 10.10.10.10 | Domain: `neilcorp.local` |
| WIN11-CLIENT01 | Domain-joined Windows workstation | 10.10.10.20 | Main endpoint target |
| UBUNTU-SRV01 | Ubuntu server | 10.10.10.30 | Linux target, SSH, test web server |
| WAZUH-SRV01 | Wazuh SIEM | 10.10.10.40 | Manager, dashboard, alerts |
| SECURITYONION01 | Network monitoring | 10.10.10.50 | Zeek / Suricata |
| VELO-SRV01 | Velociraptor server | 10.10.10.60 | DFIR server |
| ATTACKER01 | Lab-only simulation VM | 10.10.10.90 | Kali or Ubuntu |

## Virtual Network Mode
Use Host-only/Internal Network for the lab.

NAT can be used temporarily for updates/downloads, then disabled.
