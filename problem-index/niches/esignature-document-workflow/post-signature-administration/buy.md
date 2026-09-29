# Clause and Obligation Extraction Below the Enterprise Tier

**Niche:** [[niches/esignature-document-workflow/post-signature-administration/profile|Post-Signature Administration]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Contract extraction products are mature and priced for legal departments with thousands of agreements, and the company with two hundred contracts and one administrator uses a spreadsheet.
**Tags:** #bert #transformers #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor moving from signature to agreement platform is fighting to turn the executed document into structured obligations that drive a calendar and a system of record — and whoever does that stops being a signature vendor, which is the whole strategic question in the category.

## The Problem
Contract intelligence is a real and functioning category: extraction of parties, dates, terms, renewal mechanics and clause types from executed agreements, at good accuracy, with public benchmarks. It is sold with an implementation, a taxonomy configuration and a price that assumes a legal department. The company with a few hundred agreements and one person administering them — which is most companies — is left with the spreadsheet, despite having the same problem at a scale where it is entirely tractable.

## What Already Exists
Clause classification and extraction models, public contract benchmark datasets, layout-aware document models, and language models that extract structured terms from legal text reliably. Several mature commercial products. Open implementations of most of the components. The accuracy question is settled for the common term types.

## The Customization Gap
The adaptation is to the mid-market and to self-service. It requires: (1) a fixed, opinionated term set rather than a configurable taxonomy, since taxonomy configuration is where the implementation cost lives and twelve well-chosen fields — parties, effective date, term, renewal type, notice period, notice address, value, payment terms, liability cap, termination rights, assignment, governing law — cover the overwhelming majority of what a mid-market administrator needs; (2) confidence-routed review rather than assumed accuracy, with low-confidence extractions queued for a person, since an unreviewed wrong renewal date is worse than an empty field and the administrator can verify far faster than they can type; (3) amendment chain resolution, which is where mid-market agreements are messiest and where extraction products underperform because they treat each document independently; (4) output into the tools actually used — a calendar, a spreadsheet, an accounting system — rather than into a contract repository nobody will adopt; and (5) a price and onboarding that assume no implementation project, which is a packaging problem and is the actual barrier.

## Target Customer
Signature platform vendors serving the mid-market, accounting and finance platforms whose customers depend on contract terms, and contract intelligence vendors with an unserved tier below their current floor.

## Impact If Solved
The technology question is settled and the packaging question is not, which is why a capability that works is unavailable to most of the companies that need it. The fixed term set and confidence-routed review are what make it deliverable without an implementation, and the amendment chain is the piece that would distinguish it.
