# L1 Ticket Triage and Automated Resolution

**Parent Industry:** [[industries/it-managed-services|IT Managed Services]]
**Category:** Highly Automatable

## Profile
**Market Size:** $10-15B (embedded cost across all MSPs)
**Share of Parent Industry:** Embedded function — L1 tickets represent 60-70% of total ticket volume industry-wide
**Digital Adoption:** Medium — keyword-based routing exists but intelligent classification and automated resolution are in early adoption
**Target Buyer:** Service delivery manager or NOC lead at a 10-50 person MSP looking to automate repetitive ticket resolution
**Automation Potential:** High — 40-50% of L1 tickets follow predictable resolution paths that can be fully automated with script execution via RMM agents

## What Makes This a Distinct Niche
L1 ticket volume is the single largest operational cost for MSPs: password resets, printer issues, VPN connectivity, basic Office 365 problems, and simple network troubleshooting. A 500-endpoint MSP may process 800-1,200 tickets monthly, with 60-70% being L1 issues that a technician can resolve in 5-15 minutes using a known procedure. The cost is not the 10 minutes of resolution — it is the context switching, the scheduling, the SLA timer, and the technician distraction from higher-value L2/L3 work. Automating these tickets does not just save labor; it fundamentally changes the MSP's service delivery economics by removing the work that creates the least value and the most burnout.

## Current Tools & Gaps
ConnectWise Automate and Datto RMM enable script execution on managed endpoints. Rewst provides no-code automation workflows. Some MSPs use basic keyword rules in their PSA to auto-route tickets. The gap is intelligent classification: determining from an unstructured ticket description whether this is a password reset (auto-resolve), a printer driver issue (auto-resolve), or a "can't print" that is actually a network problem (route to L2). The classification must be accurate enough that automated resolution does not break things — executing a printer driver reset when the real issue is a DNS failure makes the problem worse.

## Problems
- [[niches/it-managed-services/l1-ticket-automation/build|🔨 Build: NLP-Driven Ticket Classifier with Automated Resolution Orchestration]]
- [[niches/it-managed-services/l1-ticket-automation/buy|🛒 Buy: Pre-Built L1 Resolution Script Library with PSA/RMM Integration]]
- [[niches/it-managed-services/l1-ticket-automation/fix|🔧 Fix: False-Positive Automation That Breaks More Than It Fixes]]
