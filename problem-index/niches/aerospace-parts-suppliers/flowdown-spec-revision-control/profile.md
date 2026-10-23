# Customer Flowdown & Specification Revision Control

**Parent Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn each purchase order's quality clauses and specification revisions into checked requirements on the router before a job is released, and whoever catches the most clause and revision mismatches before parts are made takes the account.

## Profile
**Market Size:** ~$350M a year in contract-review, specification-control and planning labour plus tools at US aerospace suppliers (estimate)
**Share of Parent Industry:** ~0.5% of the two codes' receipts (estimate)
**Digital Adoption:** Low — PO clauses read by a person; specification revisions tracked in spreadsheets or a subscription library nobody cross-checks
**Target Buyer:** Quality manager or contracts manager
**Automation Potential:** High for extraction and cross-checking; interpretation of ambiguous clauses stays human

## What Makes This a Distinct Niche
Every aerospace purchase order carries a list of quality clauses and referenced documents: the prime's supplier quality requirements (such as Boeing's D6-82479, GE Aerospace's S-1000 or Pratt & Whitney's ASQR-01, recalled), process specifications at a stated revision (SAE AMS, customer process specs), DFARS clauses on defence work (specialty metals, cybersecurity under 252.204-7012, with CMMC certification paused at Phase 2 since 13 July 2026 but still flowed down by some primes), and ITAR markings. AS9100 requires contract review before acceptance. The work is mechanical and unforgiving: a plating spec at revision F when the shop's procedure is at E is a nonconformance, whatever the part looks like.

## Current Tools & Gaps
QMS suites manage documents and contract-review checklists; specification subscription services supply standards; ERPs hold routings. Nothing reads the PO's clause list, resolves each reference to the current revision, compares it with the shop's procedures and routing, and blocks release on a mismatch. ITAR and CMMC programme management for small shops is already covered in [[niches/contract-manufacturing/veteran-owned-defense-contractors/profile|Veteran-Owned Defense Contractors]] and [[niches/electronics-contract-mfg/defense-itar-ems/profile|Defense & ITAR-Compliant EMS]].

## Problems
- [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/build|🔨 Build: A Clause-to-Router Checker]]
- [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/buy|🛒 Buy: QMS Document Control Linked to the Purchase Order]]
- [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/fix|🔧 Fix: The Spec Revision That Changed Last Month]]
