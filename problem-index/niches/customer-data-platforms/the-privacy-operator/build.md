# Thirty Days and a Probabilistic Graph

**Niche:** [[niches/customer-data-platforms/the-privacy-operator/profile|The Privacy Operator]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A privacy operator has thirty days to delete everything about a person from every downstream system, using an identity graph that is a set of probabilistic guesses about who that person is.
**Tags:** #compliance #graph-theory #workflow-orchestration #confidence-intervals #evaluation-metrics #automation #bayesian-inference #data-integration
**Contested on:** Every serious competitor in this niche is fighting to let one person fulfil a deletion across every downstream system within a statutory window, using an identity graph that is a set of guesses — and whoever does that turns an unverifiable obligation into a provable one.

## The Problem
A deletion request arrives with an email address. The operator must determine everything the organisation holds about that person, which means trusting the identity graph — a probabilistic structure that may have merged this person with a household member, in which case deleting the profile deletes someone else's data, or may have split them across three profiles, in which case two survive the deletion. They then propagate to forty downstream systems, most of which acknowledge the request and some of which do nothing. Thirty days later they attest that the request was fulfilled. The attestation is a statutory statement made on an unverified basis.

## Why Nobody Has Built This
Privacy tooling was built around request workflow rather than around fulfilment verification, because the workflow is what a compliance audit inspects — the process is auditable and the outcome is not, so the product optimised for the inspection. Identity scope is inherited from a graph nobody measures. Downstream systems vary enormously in what they support. And nobody has been penalised yet for unverified fulfilment, which is a matter of time rather than of design.

## What to Build
Make fulfilment provable. Determine the identity scope with explicit confidence, showing the operator which records are certain and which are probabilistic, which is the fix and lets a deliberate decision be made rather than an implicit one — the current situation is that the graph decides and the operator signs. Handle the over-merge case specifically, since deleting a merged profile can remove another person's data and that is a worse outcome than incomplete deletion. Propagate to every downstream system with a verified outcome rather than an acknowledgement, which is the fix note's subject. Cover derived data — segments, models, aggregates, backups — which is where most unfulfilled deletion actually lives and which request workflows generally ignore. Track the request to completion with evidence, producing a package that would satisfy a regulator, which is what the operator needs and currently assembles by hand if at all. Distinguish deletion from suppression, since some systems cannot delete and the honest answer is a documented alternative rather than a claimed deletion. Handle the graph changing after deletion, because a record arriving later may re-link to a deleted person and re-establish what was removed. Support the whole family of rights, since access and portability requests have the same identity scoping problem. Report the fulfilment rate by downstream system, which tells the organisation where its actual exposure is. And measure unverified attestations, because that number is the organisation's honest compliance position and nobody currently computes it.

## Target Customer
Privacy and compliance operations, customer data platform vendors, and the organisations attesting to fulfilment they cannot verify.

## Impact If Built
The process is auditable and the outcome is not, so the product optimised for the inspection. Showing which records are certain and which are probabilistic lets the operator decide rather than having the graph decide and the operator sign.
