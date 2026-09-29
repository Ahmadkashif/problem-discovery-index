# Conformance Checking Between Policy and Practice

**Niche:** [[niches/contract-lifecycle-platforms/clause-library-drift/profile|Clause Library Drift]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process mining's conformance checking exists to compare what an organisation says it does against what it actually does, and legal policy has never been checked that way.
**Tags:** #descriptive-statistics #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #word-embeddings #bert #compliance
**Contested on:** Every serious competitor here is fighting to keep the clause library and the playbook aligned with what the company has actually been agreeing to — and whoever closes that gap takes legal operations, because a library that describes a fiction makes every feature built on it wrong.

## The Problem
Conformance checking — comparing a documented process model against the event log of what actually happened, and quantifying the deviation — is a mature part of process mining with commercial products and an academic literature. A clause library is a documented model of intended behaviour and the executed contract estate is the log of actual behaviour, and no product compares them.

## What Already Exists
Conformance checking algorithms with alignment-based deviation measurement; process mining products that do this routinely for operational processes; change-point detection for identifying when behaviour shifted; embedding-based semantic comparison for the text side; and statistical methods for comparing distributions over time. All published and available.

## The Customization Gap
The adaptation is to positions rather than to process steps. It requires: (1) a normalised position representation so that policy and practice are comparable objects, which is the enabling work shared with the benchmarking sub-niche and should be built once rather than twice; (2) deviation expressed as a distribution rather than as a binary, because a position achieved in seventy percent of contracts is neither conformant nor violated and the useful statement is the rate; (3) segmentation before conclusion, since a global deviation rate frequently decomposes into two segments each internally consistent, and reporting the aggregate would hide the actual finding; (4) temporal analysis, because when the drift began is usually what explains it and a static comparison cannot say; and (5) an explicit distinction between drift that should update the policy and drift that should be corrected, which is a legal judgement the product must present for rather than resolve.

## Target Customer
CLM vendors, legal operations platforms, process mining vendors with an adjacent domain, and large in-house legal functions.

## Impact If Solved
A discipline built to compare stated and actual behaviour maps directly onto a problem nobody has framed that way. Distributional deviation and segmentation are the two adaptations, and the shared position normalisation makes this and the benchmarking capability one investment.
