# The 24-Hour Traceback Workbench

**Niche:** [[niches/telecom-resellers/robocall-mitigation-kyc/profile|Robocall Mitigation, KYC & Traceback Response]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A traceback request names a call by time, calling and called number, and a small provider has 24 hours to find it in its records, identify the customer or upstream carrier, and answer with evidence, usually by hand.
**Tags:** #large-language-models #graph-theory #feature-engineering #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche (STIR/SHAKEN signing vendors, call-analytics firms, customer-vetting tools and compliance consultants) is fighting to give a provider records that show the FCC and downstream carriers no illegal traffic originates on or passes through its network, and whoever catches the bad customer before the first traceback takes the account.

## The Problem
When the ITG traces an illegal campaign, each provider in the path receives a request: identify where this call came from. The engineer searches CDRs across switches and time zones, matches the call, identifies the customer account or the upstream carrier, and replies through the traceback portal. A provider that answers late or not at all is named as non-responsive (77 were in 2024) and invites FCC attention. The SK Teleco determination in April 2026 shows where that leads. A good answer also needs evidence of what the provider did about the customer.

## Why Nobody Has Built This
Tracebacks are infrequent for any one provider, so the work is improvised each time. Call records sit in switch-specific formats, the customer record sits in billing and CRM, and the onboarding evidence sits in email. Vendors sell call signing and call analytics, not response.

## What to Build
A workbench that receives the request, finds the matching call across CDR sources despite clock skew and number formatting, resolves the account or upstream carrier, and pulls that account's onboarding record, traffic history, complaints and prior tracebacks into one view. It drafts the response with the evidence attached and proposes the action (suspend, terminate, demand documentation), logging what was done. It also maps repeat upstream sources so the next contract renewal is informed.

## Target Customer
Compliance officers and network abuse leads at wholesale, gateway, SIP-trunk and white-label platform providers.

## Impact If Built
Traceback responses go out in hours, complete and documented, and the record of action taken becomes the evidence behind the next RMD recertification.
