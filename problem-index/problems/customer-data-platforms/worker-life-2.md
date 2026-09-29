# Fulfilling a Deletion Request Against a Probabilistic Graph

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Type:** Worker Life Changing
**One-liner:** A privacy operator has thirty days to delete everything about a person from every downstream system, using an identity graph that is a set of probabilistic guesses about who that person is.
**Tags:** #graph-neural-networks #bayesian-inference #confidence-intervals #gradient-boosting #large-language-models #evaluation-metrics #compliance #worker-facing

## The Problem
A data subject submits a deletion or access request. The operator must find every record about that person across the customer data platform and every downstream system it has ever fed — the email platform, the ad platforms, the support desk, the warehouse, the analytics tools, the backups — and act on all of them within a statutory window.

The first step is already uncertain. Finding the person means resolving their identity, using the same probabilistic graph that assembles profiles. Its errors now have legal consequences in both directions. An over-merge means deleting or disclosing data belonging to someone else, which is itself a breach. An under-merge means leaving records behind, which is a failure to fulfil, and the operator has no way to know that the remaining fragments exist.

The second step is worse. Downstream systems received exports, audiences and syncs going back years. Some accept deletion requests through an API; some require a support ticket; some retain data in ways nobody in the organisation fully understands. Whether a given person's data reached a given system is often not recorded at all, so the operator asks every system to delete rather than knowing which ones hold anything.

Access requests add disclosure risk. Compiling everything an organisation holds about someone, from a profile whose membership is a probability, and sending it to them, is a decision with real exposure made under time pressure by a person with limited tooling.

## Why It Matters to the Worker
The operator carries personal and organisational risk on a determination they cannot verify. They are asked to certify completeness for a process whose underlying identity resolution has never been measured, and the honest answer — we believe this is everything about the person we think this is — is not a form field.

Volume makes it worse. Requests arrive continuously, each with a clock, and the work is manual: look up, resolve, enumerate systems, submit, chase, confirm, document. There is no batching and no leverage, and the documentation burden is high because the process must be defensible to a regulator later.

And the edge cases are frequent and genuinely hard. Shared household email addresses. A person who used a partner's account. A request from someone whose identifiers partially match an existing profile. Each requires judgement with real consequences either way, made by someone who usually has no way to escalate.

## What a Solution Looks Like
Carry match confidence into the privacy process explicitly. A resolved subject should come with its constituent records and a confidence for each, and the marginal ones should be presented for adjudication rather than silently included or excluded — which turns an invisible risk into a decision someone actually made and can defend.

Track where data went. A propagation record — which systems received which profiles and when — is straightforward to maintain at the point of export and transforms fulfilment from broadcast-and-hope into an enumerable checklist with evidence of completion.

Automate the mechanics. API-based deletion, ticket generation for systems without APIs, status tracking, chasing, and the compiled evidence pack are all mechanical, and they are the majority of the clock.

Give the hard cases a rubric and a record. Shared households and partial matches recur constantly; a documented decision framework with the precedent attached makes the judgement consistent across operators and defensible afterwards, which is what a regulator actually asks for.

## Impact If Solved
Privacy request fulfilment is a legal obligation performed with tooling that assumes the identity question is already solved, by operators who bear the risk of it not being. Confidence-aware resolution, propagation tracking and automated mechanics reduce both the failure rate and the time per request, and — more importantly — produce a defensible record of what was decided and why, which is the thing the organisation currently cannot produce if asked.
