# 02 - Active Directory Setup

## Goal
Build a small enterprise-style Active Directory domain.

## Domain
`neilcorp.local`

## Domain Controller
`DC01`

## Organizational Units
- NEILCORP/Workstations
- NEILCORP/Servers
- NEILCORP/Users
- NEILCORP/Groups
- NEILCORP/Service Accounts
- NEILCORP/Disabled Users

## Users
- j.smith
- a.khan
- m.patel
- s.ali
- helpdesk.user
- finance.user
- backup.svc

## Groups
- Finance
- IT Support
- HR
- Remote Access Users
- Local Admin Test Group

## File Share
Path: `C:\Shares\Finance`  
Share: `\\DC01\FinanceShare`

Files:
- `payroll_test_data.txt`
- `invoice_test_data.txt`
- `finance_notes.txt`

All data must be fake test data.

## Evidence to Capture
- Domain created
- OU structure
- User list
- Group list
- FinanceShare permissions
- WIN11-CLIENT01 joined to domain
