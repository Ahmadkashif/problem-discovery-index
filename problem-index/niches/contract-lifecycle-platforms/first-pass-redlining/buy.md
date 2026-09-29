# Generation With a Refusal Boundary

**Niche:** [[niches/contract-lifecycle-platforms/first-pass-redlining/profile|First-Pass Redlining]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Selective prediction — abstaining when uncertain — is a developed area of machine learning with established methods, and legal review products answer everything.
**Tags:** #large-language-models #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #hypothesis-testing #transformers #compliance
**Contested on:** Every serious competitor in automated redlining is fighting to make the routine edits correctly without counsel and to know reliably when a provision is not routine — and whoever holds that boundary takes the legal function, because being wrong once on the wrong clause ends the deployment.

## The Problem
Deciding when a model should decline to answer is selective prediction, with a substantial literature: risk-coverage trade-offs, conformal methods that give distribution-free guarantees, calibration techniques, and ensemble disagreement as an uncertainty signal. Legal review products, where the cost of a wrong answer is high and the cost of an abstention is low, use almost none of it.

## What Already Exists
Selective prediction and learning-to-defer research; conformal prediction, which provides coverage guarantees without distributional assumptions and is directly applicable; calibration methods including temperature scaling and isotonic regression; ensemble and self-consistency approaches for uncertainty from language models; and retrieval-grounded generation with citation, which supports verification. All published, most with open implementations.

## The Customization Gap
The adaptation is to legal provisions with asymmetric and heterogeneous costs. It requires: (1) a per-provision cost model, since abstaining on a governing law clause and abstaining on a liability cap have very different value, and a uniform risk threshold is wrong in both directions; (2) conformal guarantees expressed in terms a general counsel can act on — this system will be wrong on at most this proportion of the provisions it handles, at this confidence — which is exactly what conformal methods provide and what no vendor offers; (3) calibration on the customer's own reviewed contracts, because the boundary depends on their policy and their paper and a vendor-wide calibration will be wrong for most customers; (4) distinguishing the several sources of uncertainty, since an unusual clause, an ambiguous policy and an out-of-distribution document type all warrant escalation and warrant different messages; and (5) an evaluation set that the customer's lawyers build and hold, since a vendor-reported boundary is not evidence and legal buyers know it.

## Target Customer
Contract review and CLM vendors, legal technology providers, and the in-house legal functions evaluating these products.

## Impact If Solved
A mature abstention literature addresses precisely the property that determines this product's value and is unused. Conformal coverage statements and customer-specific calibration are the two adaptations, and both are directly implementable.
