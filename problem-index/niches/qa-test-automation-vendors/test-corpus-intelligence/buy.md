# Cross-Customer Learning With No Customer Content

**Niche:** [[niches/qa-test-automation-vendors/test-corpus-intelligence/profile|Test Corpus Intelligence]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Transfer learning and federated approaches exist precisely to learn from many parties without pooling their data, and the category has not attempted cross-customer learning at all.
**Tags:** #transfer-learning #gradient-boosting #k-means-clustering #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #compliance
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of tests, failures, repairs and the changes that caused them — and whoever does that can distinguish a cosmetic change from a regression, which is the capability the whole category is missing.

## The Problem
Learning a general model from many parties' data, and adapting it to each, is a developed area: transfer learning, multi-task learning, and federated approaches that avoid pooling raw data at all. The testing category has a problem that is ideal for it — a shared underlying phenomenon, per-customer variation, and a governance constraint on pooling — and has attempted none of it, defaulting instead to per-customer heuristics.

## What Already Exists
Transfer and multi-task learning with mature implementations; federated learning frameworks with production deployments; privacy-preserving aggregation; domain adaptation methods for handling per-customer distribution shift; and the software engineering research on cross-project defect prediction, which is the closest methodological precedent and documents the difficulties honestly.

## The Customization Gap
The adaptation is to a structural representation across heterogeneous applications. It requires: (1) a representation that abstracts away from any customer's specifics while preserving what determines the outcome — change type, framework, binding strategy — which is the foundational design and is what makes the whole thing both learnable and governable; (2) honest treatment of cross-project transfer difficulty, since the defect prediction literature documents repeatedly that models transfer poorly between projects without adaptation, and assuming otherwise is the obvious failure; (3) per-customer adaptation on top of the general model, since each organisation's conventions differ and a purely general model will be mediocre everywhere; (4) a federated option for customers who will not permit even structural data to leave, which is a real segment in regulated industries and is exactly what federated approaches exist for; and (5) evaluation that distinguishes what the fleet contributed from what the customer's own data contributed, since the commercial claim rests on the first and it must be demonstrable.

## Target Customer
Test automation vendors, the quality engineering functions in regulated industries who would need the federated option, and the research community studying cross-project transfer.

## Impact If Solved
A developed set of methods exists for exactly this situation and has not been applied in a category whose central classification is data-starved per customer and data-rich per fleet. The structural representation is the design decision that makes it both effective and governable, and the federated option reaches the customers who would otherwise be excluded.
