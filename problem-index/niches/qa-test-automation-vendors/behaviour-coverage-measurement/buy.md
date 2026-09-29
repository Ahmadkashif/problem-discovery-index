# Requirements Traceability, Which Regulated Industries Already Do

**Niche:** [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/profile|Behaviour Coverage Measurement]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medical device and aerospace software maintain traceability from every requirement to the tests that verify it, because regulators require it, and everyone else measures lines.
**Tags:** #graph-theory #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting to tell a team which behaviours that matter are actually verified — and whoever does that takes the quality function, because the universal metric reports lines executed and answers a different question.

## The Problem
Regulated software industries already answer the question this niche poses: every requirement is traced to the design that implements it and the tests that verify it, and coverage is reported against requirements rather than against lines. The practice is mandated, the tooling exists, and it is maintained by hand at a cost that ordinary software organisations would never accept. The practice is right and the cost is the reason nobody else does it.

## What Already Exists
Requirements traceability tooling from the regulated industries; traceability matrix methodology; the safety standards prescribing it; requirements extraction research; and language models capable of relating a requirement statement to the code and tests that address it — which is the link that was previously maintained manually and is the cost.

## The Customization Gap
The adaptation is to organisations without formal requirements. It requires: (1) deriving the requirement set from what exists rather than assuming a document, since most organisations have issues, user stories, acceptance criteria and code comments instead of a specification, and these are a usable and imperfect substitute; (2) automatic link inference rather than manual maintenance, which is the entire cost of the regulated practice and is what has kept it confined there; (3) tolerance of incompleteness, because a partial behaviour inventory with an honest coverage statement is useful and a demand for a complete one will prevent adoption; (4) continuous rather than milestone-based maintenance, since the regulated practice assumes a documented baseline and ordinary software changes continuously; and (5) risk weighting, which the regulated version handles through criticality classification and which the general version needs in a lighter form driven by usage and consequence.

## Target Customer
Quality engineering functions, test tooling vendors, the requirements management vendors serving regulated industries, and the organisations in the regulated sectors who would rather maintain this automatically.

## Impact If Solved
The practice exists, is mandated where the stakes are highest, and is confined there entirely by its manual cost. Automatic link inference removes that cost, which is what would let the rest of the industry measure what it verifies rather than what it executes.
