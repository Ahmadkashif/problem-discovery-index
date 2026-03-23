# Client Portal with Document Completeness Tracking

**Niche:** [[niches/accounting-firms-smb/seasonal-tax-prep/profile|Seasonal Tax Preparation Practices]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic secure file-sharing portals exist but none understand what a complete tax return package looks like for each client's specific situation.
**Tags:** #bert #multiclass-classification #nlp #automation #data-integration

## The Problem
Tax clients need to submit 5-25 documents depending on their situation (W-2s, 1099s, K-1s, mortgage interest, property tax, charitable receipts, health insurance forms). Firms send a generic checklist to every client, but a single freelancer with a 1099-NEC needs a completely different set than a retiree with pension distributions and rental properties. Clients submit partial packages, the firm chases missing items through 3-5 rounds of email, and returns sit incomplete for weeks because neither side knows exactly what is still needed.

## What Already Exists
SafeSend, Liscio, Canopy Client Portal, and SmartVault provide secure upload portals. These tools let clients upload files and let firms organize them into folders. Some offer basic checklists. None of them know what documents a specific client actually needs based on their prior-year return profile, nor can they classify uploaded documents to determine what has been received vs. what is still missing.

## The Customization Gap
The portal needs to generate a per-client document request list by analyzing the prior-year return (if they had a Schedule C, they need 1099-NECs and expense records; if they had a Schedule E, they need rental income statements). When a client uploads a file, the system should classify it (is this a W-2 or a 1099-INT?) and check it off the list automatically. The remaining-items list should be visible to both the client and the firm, with automated reminders that reference specific missing documents by name rather than sending generic "please upload your documents" emails.

## Target Customer
Office managers and administrative staff at 5-15 person CPA firms who currently spend 20-30 hours per week during tax season on manual document chase across email, portal, and text.

## Impact If Solved
Reduces document collection cycle time from 3-4 weeks average to 1-2 weeks per client, eliminating the bottleneck that delays 30-40% of returns past the initial filing deadline.
