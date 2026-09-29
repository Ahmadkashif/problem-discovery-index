# Document Version Control Meets the Employee Roster

**Niche:** [[niches/esignature-document-workflow/workforce-document-flows/profile|Workforce Document Flows]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Version control, effective-dating, rule engines and semantic document diffing are all solved elsewhere, and workforce document compliance uses none of them.
**Tags:** #bert #word-embeddings #graph-theory #logistic-regression #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to prove, on demand and for the whole workforce, that every required document is signed against its current version by the right person at the right time — and whoever can produce that evidence in a minute takes the account.

## The Problem
Software has had version control, effective-dated records and bitemporal query for decades; finance has had them longer. Determining whether two versions of a document differ materially is document comparison plus semantic similarity, both mature. Deciding which employees a rule applies to is a rule engine. Workforce document compliance needs precisely these four and is run on spreadsheets and quarterly exports.

## What Already Exists
Version control systems and content-addressed storage; bitemporal data modelling with a full academic and practitioner literature; open-source rule engines with policy-as-code tooling; document diffing at the structural and textual level; and sentence embedding models that judge whether two clause versions say the same thing. HR systems expose employee attributes and effective-dated changes through APIs. The parts are all commodity.

## The Customization Gap
The adaptation is to employment documents with legal effective dates. It requires: (1) bitemporal correctness in both directions — what was required on a date, and what the record says now about what was required then, which is the distinction that matters when the record was corrected retroactively and is the one naive implementations miss; (2) applicability rules over employee attributes that are themselves effective-dated, so a transfer on the twelfth changes the requirement set from the twelfth rather than from when someone noticed; (3) material change classification tuned to employment documents, where the meaningful categories are narrow — arbitration, non-compete, at-will language, pay and leave terms, safety obligations — which makes a targeted classifier practical where a general "is this change important" model would not be; (4) jurisdiction rules maintained as content, since state requirements change and a rule set that is not maintained is worse than none because it is trusted; and (5) evidence output built for a legal audience, meaning a defensible chain with timestamps and version hashes rather than a dashboard.

## Target Customer
HR technology and signature platform vendors, employment compliance providers, and large multi-state employers with in-house compliance functions.

## Impact If Solved
Every component is commodity and the assembly is absent, which is the recurring shape in this part of the vault. Bitemporal modelling and material change classification are the two pieces that require care, and both have direct precedent — the first in finance, the second in the narrowness of the clause categories that actually matter.
