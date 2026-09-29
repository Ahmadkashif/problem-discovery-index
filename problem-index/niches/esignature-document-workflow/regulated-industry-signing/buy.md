# Regulatory Requirement Rules as Maintained Content

**Niche:** [[niches/esignature-document-workflow/regulated-industry-signing/profile|Regulated Industry Signing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Tax, payroll and sales tax vendors solved the problem of maintaining fifty states' rules as a product decades ago, and signature formalities are maintained by asking a lawyer.
**Tags:** #bert #large-language-models #logistic-regression #word-embeddings #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor here is fighting to finish a regulated transaction without a room — and that contest splits by transaction type rather than by regulation, which is why this niche is not terminal and is decomposed below.

## The Problem
Fifty states plus territories, each with its own rules on remote notarisation, witnessing, electronic recording and permissible delivery, all amended periodically. Sales tax vendors track a comparably fragmented rule set across far more jurisdictions and sell the result as a maintained service that customers subscribe to rather than replicate. Signature formalities are handled by emailing outside counsel and writing the answer in a runbook.

## What Already Exists
The maintained-rules-as-a-product model is proven across sales tax, payroll tax, employment compliance and licensing, with a well-understood operating pattern: a research team, a versioned rule store, an effective-dated API, and customer indemnification. Legal research platforms track statutory change. Language models read statutory text and legislative updates well enough to flag a change for a human to confirm. Document classification over standard instrument types is straightforward.

## The Customization Gap
The adaptation is to execution formalities rather than to tax computation. It requires: (1) a rule model that captures what actually varies — who may notarise, whether remote notarisation is permitted and under what conditions, witness count and eligibility, permissible delivery, recording format acceptance, retention duration — which is a narrow and enumerable schema and is what makes this tractable; (2) effective dating with prospective changes, since a state's remote notarisation authority often has a future commencement date and a transaction closing next month needs the rule that will apply then; (3) county-level granularity for recording, because acceptance of electronic recording varies by county rather than by state and that is the single most operationally painful variation; (4) change monitoring over legislative and administrative sources with a model proposing and a human confirming, which is the only sustainable operating cost structure; and (5) conservatism as an explicit design stance — an unknown rule returns unknown and routes to a person, because a confidently wrong answer here invalidates an instrument.

## Target Customer
Signature and closing platform vendors, title and lending technology providers, health system compliance functions, and the legal content publishers for whom this is an adjacent product.

## Impact If Solved
Every vendor in every regulated corner maintains this knowledge privately and incompletely, which is the classic signature of a content product that should exist once. The schema is narrow, the model is proven in adjacent categories, and the county-level recording data is the piece with the most immediate operational value.
