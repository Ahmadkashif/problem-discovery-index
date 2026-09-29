# The Transaction That Still Needs a Room

**Niche:** [[niches/esignature-document-workflow/regulated-industry-signing/profile|Regulated Industry Signing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Electronic execution has been legally routine for two decades and the most consequential transactions still end with several people, a table and a pen, because the formalities around the signature were never addressed.
**Tags:** #graph-theory #logistic-regression #bert #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #data-integration
**Contested on:** Every serious competitor here is fighting to finish a regulated transaction without a room — and that contest splits by transaction type rather than by regulation, which is why this niche is not terminal and is decomposed below.

## The Problem
The signature is the easy part and has been for twenty years. What keeps regulated transactions on paper is everything attached to it: a document that must be notarised, another that must be witnessed by two people not party to the transaction, a third that must be recorded with a county office that accepts a specific electronic format or none at all, a fourth where the regulator's guidance on electronic delivery is ambiguous enough that counsel says use paper. The parties are in different organisations with different systems and different regulators. Somebody assembles the package by hand, chases the pieces, and books the room.

## Why Nobody Has Built This
General signature platforms sell horizontally and treated regulated requirements as configuration, which handles retention and audit trails and does nothing about a statutory formality. The requirements are jurisdiction-specific and change, so maintaining them is a content operation rather than a software feature, and software companies are structurally bad at content operations. The coordination spans organisations, so no single buyer controls the whole transaction. And the residual formalities differ so completely between a mortgage closing and a clinical consent that a general solution to "regulated signing" resolves into two unrelated products — which is the finding that decomposes this niche.

## What to Build
The common layer rather than the general product: a requirements engine that knows, for a given document type, jurisdiction and transaction, what formalities attach — notarisation, witnessing, delivery method, recording format, retention, original-document rules — and orchestrates the parties and artefacts needed to satisfy them. Document classification to identify what each item in a package is, since packages arrive as unlabelled PDFs. Requirement lookup from maintained jurisdiction content. Multi-party orchestration with a dependency order, because these packages have real sequencing — the appraisal before the disclosure, the notarised instrument before the recording. Exception routing when a formality cannot be satisfied electronically, which is the honest and necessary part. That layer is what the two sub-niches below build on, and each of them supplies the transaction-specific half that makes it a product.

## Target Customer
Signature platform vendors moving up-market into regulated verticals, vertical closing and consent platforms who need the requirements layer and are building it privately, and the compliance functions who currently hold this knowledge in people's heads.

## Impact If Built
The residual paper is concentrated in high-value transactions, which makes this where the category's remaining value is. The requirements engine is the reusable half and is currently reimplemented per vertical, per vendor, from counsel's memory.
