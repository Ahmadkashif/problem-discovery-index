# Certifying on a Self-Completed Questionnaire

**Niche:** [[niches/data-marketplace-brokers/the-provenance-reviewer/profile|The Provenance Reviewer]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A provenance reviewer is asked to certify that a supplier's data was lawfully collected with valid consent, on the basis of a questionnaire the supplier filled in about itself.
**Tags:** #compliance #evaluation-metrics #descriptive-statistics #worker-facing #graph-theory #data-integration #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to give the reviewer something better than a supplier's self-assessment to certify against — and whoever does that takes the account, because this signature is the gate every data purchase now passes through.

## The Problem
A reviewer receives a forty-question form completed by a supplier, stating that data was collected with consent, that individuals were given notice, and that onward transfer is permitted. There is no evidence attached to any answer. The supplier licensed two-thirds of the dataset from other parties who completed their own forms, which the reviewer has not seen and cannot request. The reviewer's choices are to approve on the form, which is not a basis for anything, or to decline, which blocks a purchase the business has already planned around. They approve, note their reservations in an email, and hope.

## Why Nobody Has Built This
The evidence the reviewer needs is not produced by anyone in the chain, so the questionnaire is not a lazy substitute for evidence — it is a substitute for evidence that does not exist. Vendor risk platforms were built for software suppliers and assess operational and security risk rather than lawfulness of collection. Auditing a data supplier's collection practices requires access nobody grants. And the reviewer has no leverage, since declining is escalated and overridden.

## What to Build
Give the reviewer evidence and a defensible framework. Structure the assessment around specific evidence rather than assertions — the actual notice text presented to individuals, the consent mechanism, the collection method, the upstream chain with each party named — so a review is against artefacts and a missing artefact is a finding rather than an unanswered question. Require the upstream chain to be declared and assessed, since that is where the risk concentrates and it is currently outside the review entirely. Build a shared supplier assessment utility, so that the same supplier is not independently reviewed by four hundred buyers with the same questions and no better answers — the duplication is enormous and a shared assessment is the obvious structural answer. Verify what is externally verifiable: corporate registration, jurisdiction, public privacy notices, regulatory actions, litigation history, and whether the public notice language actually covers the use being sold. Score risk on a comparable scale, so a reviewer can say this supplier is materially riskier than that one rather than approving each in isolation. Produce a defensible record of what was reviewed and concluded, which is what a regulator asks for two years later. Support conditional approval with stated limits — this data, this use, not model training — since it is frequently the correct answer and the binary approve-or-decline forces the wrong one. And give the reviewer a basis to decline that the business cannot simply override, because a gatekeeper with no standing is not a control.

## Target Customer
Compliance, vendor risk and legal functions; the reviewers themselves; the marketplaces whose transactions stall here; and the assurance firms for whom data supplier certification is an unclaimed service.

## Impact If Built
The questionnaire substitutes for evidence that nobody in the chain produces. A shared supplier assessment utility removes an enormous duplication, and conditional approval with stated limits is frequently the right answer that a binary decision forces out.
