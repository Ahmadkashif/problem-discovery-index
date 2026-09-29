# Compliance as a Property of the Document

**Niche:** [[niches/procurement-spend-platforms/public-sector-procurement/profile|Public Sector Procurement]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A public solicitation must satisfy requirements from statute, regulation, agency policy and funding source at once, and it is assembled by copying the last one and hoping it was right.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in public procurement software is fighting to let an agency run a compliant, protest-resistant solicitation without a specialist assembling it from precedent — and whoever makes compliance a property of the process takes the account.

## The Problem
A school district issues a request for proposals for technology services, partly funded by a federal programme. The required clauses include the district's own standard terms, state procurement code requirements, federal uniform guidance provisions applicable because of the funding source, and specific certifications. The procurement officer assembles the document from a prior solicitation for a different service under different funding, adjusts what she recognises, and issues it. Three of the federal provisions are absent. The award is made, an auditor identifies the omission a year later, and the funding is questioned — which is a worse outcome for the district than any procurement inefficiency the commercial world worries about.

## Why Nobody Has Built This
The rule sets are numerous, overlapping and published as legal text rather than as structured requirements — the same executable-content gap that recurs throughout this vault, here with four overlapping sources rather than one. The buyers are small agencies with small budgets, so the market has not funded deep content maintenance. And the failure mode is slow: an omitted clause surfaces in an audit years later, which removes the urgency that a fast-failing problem would create.

## What to Build
Requirement sets as maintained executable content, and solicitation assembly as composition rather than copying. Each applicable source — state procurement code, agency policy, funding programme conditions, contract type — contributes a set of required provisions, certifications, notice periods and process steps. The officer states what they are buying, the funding sources, the contract type and the value, and the applicable requirement set is composed, with conflicts between sources surfaced rather than silently resolved. The document is assembled from maintained clause content rather than from a prior file, so an updated provision reaches every subsequent solicitation automatically. Compliance is checked continuously as the document is edited rather than at a final review. The process steps carry their own clocks — notice periods, question windows, protest windows — which are the deadlines most commonly missed. And the award file assembles itself as the process runs, so the documentation that would defend a protest exists at award rather than being reconstructed when one arrives.

## Target Customer
Public procurement platform vendors, state and local agencies, school districts and higher education, and the cooperative purchasing organisations that serve them.

## Impact If Built
An omitted funding-source provision can put a grant at risk, which for a small agency is a materially worse outcome than any commercial procurement error. Composing requirements rather than copying precedent stops errors propagating between solicitations, and the self-assembling award file addresses the protest exposure that shapes every decision these officers make.
