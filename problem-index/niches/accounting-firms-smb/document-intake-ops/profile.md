# Client Document Intake & Processing Operations

**Parent Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Category:** Highly Automatable

## Profile
**Market Size:** $6-10B (embedded cost across all CPA firms)
**Share of Parent Industry:** Embedded function — represents 20-30% of staff time across the industry
**Digital Adoption:** Low-Medium — receipt scanning tools (Dext, Hubdoc) handle individual documents, but end-to-end intake pipeline automation is absent
**Target Buyer:** Office manager or operations lead at a mid-size CPA firm (5-20 staff)
**Automation Potential:** High — document classification, data extraction, and routing are well-defined ML tasks with structured output requirements

## What Makes This a Distinct Niche
Document intake is not a segment of the accounting industry — it is a cross-cutting operational function that consumes 20-30% of total staff capacity. It encompasses receiving client documents from multiple channels (email, portal, mail, text), classifying each document by type, extracting relevant data fields, routing documents to the correct engagement, flagging incomplete submissions, and preparing structured data for input into tax prep or accounting software. Every firm does this work, and every firm does it manually. The volume scales linearly with client count and is concentrated during tax season, creating the primary capacity constraint for the entire industry.

## Current Tools & Gaps
Dext (formerly Receipt Bank) and Hubdoc scan and extract data from individual business expense receipts. SafeSend and Liscio provide upload portals. Some tax software offers basic OCR import for common forms. The gap is the full pipeline: no tool handles the journey from "client sends a batch of mixed documents via email" to "each document is classified, extracted, validated, and routed to the correct engagement file with structured data ready for import." The existing tools solve individual steps but do not orchestrate the pipeline.

## Problems
- [[niches/accounting-firms-smb/document-intake-ops/build|🔨 Build: End-to-End Document Intake Pipeline with ML Classification]]
- [[niches/accounting-firms-smb/document-intake-ops/buy|🛒 Buy: Multi-Channel Document Collection Aggregator]]
- [[niches/accounting-firms-smb/document-intake-ops/fix|🔧 Fix: Document-to-Engagement Matching and Routing]]
