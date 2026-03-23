# Client Environment Standardization Assessment Tool

**Niche:** [[niches/it-managed-services/smb-managed-transition/profile|SMB Break/Fix-to-Managed Transition MSPs]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** RMM network assessment tools exist but produce generic device inventories, not the MSP-specific "standardization readiness" report that identifies what must be fixed before a client can be efficiently managed.
**Tags:** #automation #data-integration #workflow-orchestration #quick-win

## The Problem
Before onboarding a new managed client, an MSP needs to assess the client's environment: how many endpoints, what OS versions, is there a domain controller, are backups running, is there an aging firewall, are workstations standardized or is every machine a unique snowflake? This assessment determines the onboarding cost (project hours to bring the environment to standard), the ongoing support cost (non-standard environments generate 2-5x more tickets), and the contract price. Today, a technician runs an RMM scan, gets a raw device inventory, and manually evaluates the environment against the MSP's standards — a process that takes 4-8 hours and varies in quality based on the technician's experience.

## What Already Exists
ConnectWise Automate, Datto RMM, and NinjaRMM can run network discovery scans. Liongard provides automated IT documentation. Network assessment tools like Rapidfire Tools (Kaseya) and Netsurion offer security and infrastructure assessments. These produce device inventories and vulnerability reports.

## The Customization Gap
MSPs need an assessment tool that evaluates the client environment against their specific standards — not generic best practices but the MSP's defined stack: "we require Windows 11 23H2, domain-joined, SentinelOne agent installed, Datto backup configured, and Meraki firewall." The output should be a standardization gap report: "14 of 47 workstations are running Windows 10 (EOL), 8 machines have no backup agent, the firewall firmware is 3 versions behind." Costed remediation steps should be auto-generated, producing a project scope for pre-onboarding standardization that feeds directly into the contract pricing model.

## Target Customer
MSP owners and vCIOs conducting 2-5 prospect assessments per month who need to quickly identify standardization gaps and cost the remediation.

## Impact If Solved
Reduces assessment time from 4-8 hours to 1-2 hours, produces consistent assessments regardless of which technician runs them, and directly informs contract pricing by quantifying the cost of bringing a non-standard environment to manageable state.
