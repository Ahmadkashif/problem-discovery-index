# Medical Billing

## Profile
**Category:** Healthcare & Clinical
**Market Size:** $16B annually in the US (third-party billing services market)
**Tech Maturity:** Medium — clearinghouses and practice management systems handle claim submission, but denial management, payment posting, and AR follow-up remain heavily manual
**Workforce:** Medical billers, certified coders (CPC, CCS), accounts receivable specialists, denial management analysts, billing company owners, and client relationship managers

## Key Pain Themes
Denial management is the core profit-and-loss driver — the average first-pass claim denial rate is 5-10%, and each denied claim requires manual investigation to determine root cause (eligibility, coding error, missing authorization, timely filing), then reworking and resubmitting. Many billing companies work across dozens of provider clients, each with different EHR systems, payer mixes, and specialty-specific coding requirements, making it impossible to standardize workflows. Payment posting — matching EOBs/ERAs to specific claims and patient balances — involves reconciling data from multiple payers with different remittance formats, contractual adjustment logic, and patient responsibility calculations. Keeping up with payer-specific rule changes (LCD/NCD updates, modifier requirements, bundling edits) requires constant vigilance, and a missed update means preventable denials across an entire client's claims.

## Current Tech Landscape
Clearinghouses like Waystar, Availity, and Trizetto handle electronic claim submission and basic eligibility checks. Practice management systems (AdvancedMD, Kareo/Tebra, CollaborateMD) provide the billing workflow. Denial management is largely manual or uses basic worklists within the PM system. AI-powered coding tools (like Codify by AAPC) assist coders but don't close the loop on denial prevention. RCM automation platforms (Infinx, Olive AI) target large health systems, leaving SMB billing companies underserved.

## Problems
- [[problems/medical-billing/high-impact|🔴 High Impact: Predictive Denial Prevention Engine]]
- [[problems/medical-billing/low-impact-1|🟡 Low Impact: Payer Rule Change Monitoring]]
- [[problems/medical-billing/low-impact-2|🟡 Low Impact: Multi-Client ERA Reconciliation]]
- [[problems/medical-billing/worker-life-1|🟢 Worker Life: AR Follow-Up Call Burden]]
- [[problems/medical-billing/worker-life-2|🟢 Worker Life: Coding Specialist Context Switching]]

## Analysis
- [[problems/medical-billing/ml-opportunity|🧠 Machine Learning Opportunities]]
- [[problems/medical-billing/ai-agents-platforms|🤖 AI Agents & Platforms]]
