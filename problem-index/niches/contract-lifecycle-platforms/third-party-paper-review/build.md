# The Risk Is the Clause That Is Not There

**Niche:** [[niches/contract-lifecycle-platforms/third-party-paper-review/profile|Third-Party Paper Review]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every contract review product checks the clauses that are present against a standard, and the dangerous term in a counterparty's agreement is usually the one that was left out.
**Tags:** #large-language-models #bert #graph-theory #transformers #evaluation-metrics #confidence-intervals #compliance #tacit-knowledge-ml
**Contested on:** Every serious competitor here is fighting to find the risk in a counterparty's contract, where the dangerous term is usually the one that is absent — and whoever detects absence takes the review, because checklist review structurally cannot.

## The Problem
A supplier's standard agreement arrives. Every clause in it is unremarkable and the review tool reports no deviations. What it does not report is that there is no limitation of liability anywhere in the document, that the indemnity the company gives is uncapped as a result, that there are no data processing terms although the supplier will hold customer records, and that nothing addresses ownership of the configuration work the supplier will produce. A junior lawyer reviewing against the tool's output signs it off. A senior lawyer would have noticed within two minutes, because they hold the list of what must be present and the tool does not.

## Why Nobody Has Built This
Review products were built by extending playbook comparison, which is inherently about clauses that exist, and absence requires a different question: what should be here. That question needs the company's minimum requirements written down, conditioned on the deal — data terms only if personal data is involved, intellectual property terms only if work product is created — and almost no company has written that down, because it lives in professional judgement. Interaction effects require reasoning across the document rather than clause by clause, which extraction-shaped architectures do not do. And the failure is invisible: a review that missed an absent clause produces a clean report.

## What to Build
Review that starts from what should be present. An expected-provision model conditioned on the transaction: what type of agreement, what is being exchanged, whether personal data is involved, whether work product is created, the value and the jurisdiction — from which the set of provisions that ought to appear follows, which is the piece that must be built and is the durable asset. Detect absence against that set, reported by consequence rather than as a list of missing items, since the useful statement is that the company's indemnity is uncapped rather than that a limitation of liability section was not found. Model interaction explicitly — an uncapped indemnity beside a broad one, an exclusivity with no termination right, a most-favoured-nation clause with no expiry — because the compounding is where the real exposure is and no product looks for it. Elicit the company's own minimum standard by observing what senior lawyers actually insist on across reviews, rather than asking them to write it down, since they cannot easily and the evidence is in their redlines. And escalate by exposure rather than by count, so a review returns the two things that matter rather than fourteen observations.

## Target Customer
In-house legal functions reviewing counterparty paper at volume, legal operations, and the contract review vendors whose products currently cannot see absence.

## Impact If Built
The dangerous term in third-party paper is usually missing rather than wrong, which is precisely the case present-clause review cannot detect, and it is why this review has not scaled. The expected-provision model is the asset, and eliciting it from senior lawyers' behaviour rather than their recall is what makes it obtainable.
