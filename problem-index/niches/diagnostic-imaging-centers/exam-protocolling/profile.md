# Exam Protocolling

**Parent Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to attach the right protocol to every order before the patient arrives, and whoever cuts radiologist protocolling minutes per order most, with no rise in protocol-attributable repeats or recalls, takes the account.

## Profile
**Market Size:** ~$0.3B a year of radiologist and technologist protocolling time plus protocol-management and decision-support tools at freestanding centres (estimate)
**Share of Parent Industry:** ~1% of centre revenue (estimate)
**Digital Adoption:** Medium — protocols are chosen in the RIS or PACS, but from memory, binders and site-specific lists, with no record of why
**Target Buyer:** Radiology group's chief of quality or medical director; operator's chief medical officer
**Automation Potential:** High for routine orders; deliberately low for contrast, implant and paediatric sedation decisions

## What Makes This a Distinct Niche
Every advanced-imaging order must be translated into a protocol (sequences, coverage, contrast) before the scan. That is the tacit judgement at the heart of [[problems/diagnostic-imaging-centers/high-impact|The Protocol Read]]. It is mechanical for most orders and expert for the rest, and it consumes scarce radiologist minutes. The appropriateness question sits beside it. CMS paused the Appropriate Use Criteria programme and rescinded its regulations from 1 January 2024, with no date to resume, so the ACR's 279 Appropriateness Criteria topics are now a reference, not a mandate. Radiology benefit managers apply their own guidelines at authorization (see [[niches/health-insurance-carriers/utilization-management/profile|🔵 Utilization Management & Prior Authorization]]). The winner is whoever takes the most radiologist minutes out of each order without a rise in protocol-attributable repeats or recalls.

## Current Tools & Gaps
RIS and PACS protocolling screens, site protocol binders, OEM protocol trees on the scanner, CareSelect Imaging for ordering-side appropriateness in health-system EHRs, early protocol-suggestion features in reading platforms. Gaps: no protocol ledger joining decision to outcome; no confidence or abstention; appropriateness checked against criteria the payer does not use.

## Problems
- [[niches/diagnostic-imaging-centers/exam-protocolling/build|🔨 Build: A Protocol Ledger and Suggester That Abstains on Contrast]]
- [[niches/diagnostic-imaging-centers/exam-protocolling/buy|🛒 Buy: Ordering-Side Decision Support Turned Into Reading-Side Protocolling]]
- [[niches/diagnostic-imaging-centers/exam-protocolling/fix|🔧 Fix: The Referrer Who Always Means an Arthrogram]]
