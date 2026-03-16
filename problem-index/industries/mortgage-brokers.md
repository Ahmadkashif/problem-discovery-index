# Mortgage Brokers

## Profile
**Category:** Financial Services
**Market Size:** ~$2T in annual US mortgage originations; brokers handle ~25% (~$500B); ~15,000 brokerage firms
**Tech Maturity:** Medium — Encompass (ICE Mortgage Technology), Byte, and Calyx dominate the LOS market; CRM tools like Jungo and Surefire exist but decision intelligence around lender selection, rate timing, and pipeline risk is almost entirely absent
**Workforce:** Loan officers (origination and borrower relationships), loan processors (file assembly, condition clearing), delegated underwriters, compliance officers, and closers

## Key Pain Themes
The core value proposition of a mortgage broker is knowing which of 30-50 wholesale lenders will approve a specific borrower profile at the best rate and terms — but this knowledge lives entirely in the heads of experienced loan officers and is lost when they leave. Loan processors spend 40-60% of their time chasing borrowers for missing documents and clearing underwriting conditions, a manual loop that delays closings and burns out staff. Rate lock timing is a high-stakes guessing game: lock too early and you leave basis points on the table, lock too late and rates move against you, and brokers have no systematic framework for the decision. TRID/RESPA compliance documentation is a constant overhead that adds hours of manual review to every file.

## Current Tech Landscape
Encompass and Byte handle loan origination workflows but are essentially structured databases with regulatory templates — they don't advise on lender selection or flag pipeline risk. CRM tools automate borrower communication but don't integrate with lender rate sheets or approval matrices. Document collection is partially automated by tools like Blend and SimpleNexus on the consumer-facing side, but the broker-side extraction and verification of paystubs, tax returns, and bank statements remains largely manual.

## Problems
- [[problems/mortgage-brokers/high-impact|🔴 High Impact: Lender-Borrower Matching Intelligence]]
- [[problems/mortgage-brokers/low-impact-1|🟡 Low Impact: Loan Document Extraction & Assembly]]
- [[problems/mortgage-brokers/low-impact-2|🟡 Low Impact: Rate Lock Timing Optimization]]
- [[problems/mortgage-brokers/worker-life-1|🟢 Worker Life: Condition Clearing Automation]]
- [[problems/mortgage-brokers/worker-life-2|🟢 Worker Life: TRID/RESPA Compliance Burden]]

## Analysis
- [[problems/mortgage-brokers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/mortgage-brokers/ai-agents-platforms|🤖 AI Agents & Platforms]]
