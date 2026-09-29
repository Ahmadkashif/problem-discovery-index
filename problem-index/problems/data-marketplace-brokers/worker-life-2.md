# Provenance Reviewer Signing Off a Supplier

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Worker Life Changing
**One-liner:** A provenance reviewer is asked to certify that a supplier's data was lawfully collected with valid consent, on the basis of a questionnaire the supplier filled in about itself.
**Tags:** #large-language-models #bert #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #compliance #worker-facing

## The Problem
Before a marketplace lists a dataset, or an enterprise buys one, somebody reviews its provenance. Where did this data come from, was it collected lawfully, was consent obtained, does the chain of rights support the licence being granted, and can it be used for the buyer's purpose — increasingly including model training.

The reviewer's evidence is a questionnaire the supplier completed, a privacy policy, contractual warranties, and a conversation. Occasionally a data protection impact assessment. Rarely anything that could be independently verified.

The chain is frequently long. A supplier aggregates from other suppliers who aggregate from publishers or apps or panel operators. Each link warrants the one below. Nobody at any link has visibility more than one step down, and the reviewer is assessing the whole chain from the top.

The consequences of getting it wrong have grown. Privacy enforcement now reaches purchasers, not only collectors. Litigation over training data has made the training question specifically acute. A buyer who acquires improperly sourced data may face regulatory exposure, may have to delete models trained on it, and may face claims from the individuals concerned.

## Why It Matters to the Worker
This is accountability without verification capability. The reviewer signs, the organisation relies on the signature, and the underlying evidence is a supplier describing itself.

The technical questions are genuinely hard and outside most reviewers' training. Whether a consent flow satisfies a particular jurisdiction's standard, whether a lawful basis was correctly asserted, whether an app's disclosure covered the onward sale — these require legal analysis on facts that are not available.

The commercial pressure is real and one-directional. The business wants the data, the supplier has strong incentives to present the strongest reading, and the reviewer is the only person in the process whose role is to raise objections.

And the ground shifts constantly. Privacy law, enforcement priorities and litigation outcomes change what is acceptable, so a supplier approved two years ago may no longer be, and nothing prompts a re-review.

## What a Solution Looks Like
Structured provenance capture rather than a free-text questionnaire. Collection method, jurisdiction, consent mechanism, disclosure language, chain of intermediaries and permitted onward uses recorded as fields, so that assessment is comparable across suppliers and re-assessable when rules change.

Automated review of the artefacts that do exist. Privacy policies, terms of service and consent flow descriptions are documents, and extracting whether they disclose onward sale, whether they cover the buyer's intended use, and whether they name the relevant jurisdictions is a well-shaped extraction task that currently consumes reviewer hours.

Inconsistency detection across the chain. Where a supplier's warranty conflicts with the disclosure of the source it names, that is detectable by comparison and is exactly the signal a reviewer is trying to find by reading.

Continuous monitoring rather than point-in-time approval. Regulatory changes, enforcement actions and litigation against a supplier are public signals that should trigger re-review, and no organisation watches for them systematically.

Portfolio-level risk view: which purchased datasets rest on the weakest provenance, so remediation can be prioritised rather than discovered.

## Impact If Solved
Provenance risk has moved from a compliance formality to a material exposure that reaches buyers directly, and it is currently managed by one person reading a self-assessment. Structuring the evidence and monitoring continuously gives the reviewer something to actually assess, and it makes re-review possible when the rules move — which they now do constantly.
