# Schema Matching and Master Data

**Niche:** [[niches/spend-management-platforms/gl-coding-and-erp/profile|GL Coding & ERP Integration]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Schema matching and master data management solved mapping between differently-named representations of the same thing, and spend platforms do it by interview.
**Tags:** #transfer-learning #word-embeddings #data-integration #evaluation-metrics #large-language-models #confidence-intervals #automation #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to code transactions correctly into a chart of accounts unique to every customer without rebuilding the model from scratch each time — and whoever transfers learning across customers makes implementation weeks instead of months.

## The Problem
Mapping one organisation's schema onto another's is a studied problem with real methods: semantic matching using names, structure and instance data; canonical models with per-source mappings; reference data management; and match confidence with human review of the uncertain. Data integration has been doing this for decades. Spend platform implementation does it by asking a controller questions and writing rules.

## What Already Exists
Schema and ontology matching algorithms; master data management with canonical models; reference data governance; instance-based matching; and match confidence with stewardship review workflows.

## The Customization Gap
The adaptation is to accounting semantics with continuous feedback. It requires: (1) a canonical model of expense semantics that does not yet exist, which is the substantive contribution and is what makes everything else mechanical; (2) instance data in the form of transactions rather than records, so the matching evidence is behavioural — how a customer actually codes — rather than structural; (3) continuous correction signal from controllers, which schema matching rarely gets and which makes this unusually learnable; (4) accounting rules and tax treatments that constrain valid mappings, so a semantically plausible match can still be wrong; and (5) thousands of source schemas to learn from, where integration projects typically have a handful.

## Target Customer
Implementation and product leadership, ERP integration specialists, controllers, and data integration vendors for whom accounting semantics are unmodelled.

## Impact If Solved
The method is mature and the spend version has better evidence than most integration projects ever get. The missing piece is a canonical expense semantics, and building it makes every subsequent mapping mechanical.
