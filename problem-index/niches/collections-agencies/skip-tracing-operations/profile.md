# Skip Tracing Operations

**Parent Industry:** [[industries/collections-agencies|Collections Agencies]]
**Category:** Highly Automatable

## Profile
**Market Size:** ~$1.5B in skip tracing labor and vendor costs across collection agencies
**Share of Parent Industry:** N/A (operational function, not a revenue segment)
**Digital Adoption:** Medium — skip trace vendors provide batch and real-time APIs, but the decisioning layer (which vendor to query, when to re-trace, how to prioritize multiple results) is manual or rule-based
**Target Buyer:** Skip trace manager or data analyst at mid-to-large collection agencies
**Automation Potential:** High — skip tracing is a data-lookup and scoring workflow with clear inputs (debtor identity) and outputs (ranked contact information) that is highly amenable to ML optimization

## What Makes This a Distinct Niche
Skip tracing is the process of locating debtors whose contact information is outdated or missing. Agencies subscribe to multiple skip trace vendors (LexisNexis, TLO, Accurint, TransUnion TLOxp) at costs of $0.10-$2.00 per query. Each vendor returns different results with varying accuracy. The skip trace team must decide which vendor to query (and in what order), how to evaluate conflicting results, when to re-trace an account after failed contact attempts, and how to prioritize multiple returned phone numbers and addresses. These decisions are currently made using static rules or individual judgment.

## Current Tools & Gaps
Skip trace vendor APIs return data efficiently, but the orchestration layer — when to query, which vendor, how to merge and score results — is managed through manual processes or simple rules in the collection platform. No tool optimizes the skip trace workflow across vendors based on historical accuracy data, debtor demographics, and cost-per-result. Re-trace timing is calendar-based (every 30/60/90 days) rather than triggered by contact probability decay.

## Problems
- [[niches/collections-agencies/skip-tracing-operations/build|🔨 Build: Multi-Vendor Skip Trace Orchestration and Scoring Engine]]
- [[niches/collections-agencies/skip-tracing-operations/buy|🛒 Buy: Skip Trace Result Deduplication and Merge Tool]]
- [[niches/collections-agencies/skip-tracing-operations/fix|🔧 Fix: Wasteful Re-Trace Timing on Non-Contacted Accounts]]
