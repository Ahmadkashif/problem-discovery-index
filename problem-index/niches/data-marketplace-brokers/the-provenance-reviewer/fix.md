# The Upstream Supplier Nobody Can See

**Niche:** [[niches/data-marketplace-brokers/the-provenance-reviewer/profile|The Provenance Reviewer]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Most datasets are assembled from other datasets, the review covers only the immediate seller, and the risk sits with parties the reviewer is never told about.
**Tags:** #compliance #graph-theory #evaluation-metrics #data-integration #descriptive-statistics #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to give the reviewer something better than a supplier's self-assessment to certify against — and whoever does that takes the account, because this signature is the gate every data purchase now passes through.

## The Problem
A reviewer assesses the company selling the data. That company aggregates from six upstream sources, two of which are themselves aggregators. The consent, the collection method and the jurisdictional exposure all originate several steps up, with parties the reviewer has never heard of and whose existence the immediate seller may not disclose. The review examines the last link in a chain and concludes about the whole thing. When something surfaces later, it is almost always upstream, which everyone involved could have predicted.

## Why It's Still Broken
Suppliers treat their sourcing as commercially confidential, and disclosing upstream parties invites disintermediation. Reviewers have no contractual right to ask beyond their counterparty. Questionnaires do not have a field for it, so the question is not even posed. And the practice of reviewing only the direct supplier is so established that its inadequacy reads as normal.

## What a Fix Looks Like
Make the chain a required disclosure. Require declaration of all upstream sources as a condition of purchase, at minimum their identity and collection method, which is the fix — a supplier unwilling to name their sources has told the reviewer something important, and that refusal is itself a usable finding. Assess inherited risk explicitly, treating an aggregator with undisclosed sources as higher risk than a primary collector, which is a scoring change that changes behaviour. Permit disclosure under confidentiality where commercial sensitivity is genuine, which removes the main objection while preserving the information. Require the chain to be maintained rather than stated once, since suppliers change sources without notice. Map supplier chains across an organisation's whole portfolio, which reveals that a dozen purchases share one upstream source and that the concentration risk nobody measured is substantial. Flag circular and self-referential chains, which occur and are a sign of nothing good. Push marketplaces to make chain declaration a listing requirement, since they are the party able to impose it. And record the declared chain in the review artefact, so a later question can be traced rather than reconstructed.

## Who Feels the Pain
Reviewers certifying a chain they cannot see; the organisations carrying inherited risk they have not measured; and the individuals whose data entered the chain under a notice nobody downstream has read.

## Impact If Fixed
The review examines the last link and concludes about the whole chain. Requiring source declaration makes a refusal into a finding, and mapping chains across a portfolio exposes concentration risk that no individual review could reveal.
