# Contract Extraction Has Become Good Enough

**Niche:** [[niches/contract-lifecycle-platforms/back-catalogue-obligations/profile|Back Catalogue Obligations]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clause extraction from contracts has public benchmarks, strong open models and mature commercial products, and the back catalogue is still read by people or not at all.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #cross-validation #compliance
**Contested on:** Every serious competitor in this niche is fighting to make the executed back catalogue answerable — what have we promised, to whom, and where — and whoever does that takes the account, because it is the question the category was bought to answer and the one every implementation declares out of scope.

## The Problem
Extracting parties, dates, terms and named clause types from contracts is a benchmarked task with published datasets, strong open models and several mature commercial products. Accuracy on the common clause types is now high enough for production use with a review layer. The back catalogue remains unstructured not because the technology is missing but because nobody has made the economics and the workflow work.

## What Already Exists
Contract understanding benchmarks and public annotated datasets; legal-domain language models; general models that extract clauses and answer questions about contracts well; document layout models for scanned material; and several commercial extraction platforms with established accuracy. Optical character recognition for the scanned portion of the estate is commodity.

## The Customization Gap
The adaptation is to a legacy estate at scale under a cost constraint. It requires: (1) calibrated per-field confidence rather than a single accuracy figure, since the operational question is which extractions can be trusted unreviewed and which need a person — this is what determines the cost of the whole exercise and is what aggregate accuracy conceals; (2) review routed by consequence, so an uncertain liability cap gets human attention and an uncertain notice address does not, which is how the review budget is made to go far enough; (3) handling of the difficult minority — scanned faxes, handwritten amendments, non-English agreements, bespoke paper — which is where accuracy collapses and where most of the risk concentrates; (4) amendment chain resolution, since extraction products treat documents independently and the operative term is frequently in the third amendment; and (5) provenance on every extracted value, linking back to the clause and page, because a lawyer will not act on a term they cannot see in the original.

## Target Customer
CLM vendors, legal process outsourcers whose manual review this would restructure, extraction vendors, and large in-house legal functions.

## Impact If Solved
The technology has crossed the viability threshold and the estate remains unstructured for economic and workflow reasons rather than technical ones. Confidence-routed review and consequence-based prioritisation are what turn an affordable partial pass into a useful one.
