# 01 - Virtual Network Setup

## Goal
Create a fully isolated virtual network for the lab.

## Steps
1. Create an Internal Network or Host-only network in VirtualBox/VMware.
2. Use network range `10.10.10.0/24`.
3. Connect all lab VMs to this isolated network.
4. Use NAT only temporarily for updates/downloads.
5. Disable NAT once tools are installed.

## Evidence to Capture
- Virtual network settings
- VM adapter settings
- Successful ping tests
- IP configuration for each VM

## Notes
Do not expose the lab to the public internet.
