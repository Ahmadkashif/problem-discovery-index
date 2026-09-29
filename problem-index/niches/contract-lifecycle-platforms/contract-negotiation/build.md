# The Same Twelve Edits, Forever

**Niche:** [[niches/contract-lifecycle-platforms/contract-negotiation/profile|Contract Negotiation]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A playbook states what the company will accept and a lawyer applies it by hand to every contract, which is how the most expensive hours in the business are spent on the twelve edits that are always the same.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to get to an agreed contract faster and on better terms — and that contest splits between removing the routine edits and knowing which positions are achievable, which is why this niche is not terminal and is decomposed below.

## The Problem
A counterparty's standard agreement arrives. Counsel reads it and makes the edits: cap the indemnity, strike the automatic renewal, add the data processing terms, narrow the exclusivity, fix the governing law, adjust the notice period. Nine of the twelve edits are the same ones they made yesterday on a different contract, from the same playbook, in the same language. The remaining three require judgement about this specific counterparty and this specific deal, and they receive the same attention as the nine because the process does not distinguish them. Legal's capacity is consumed by the part that requires no legal skill.

## Why Nobody Has Built This
Playbooks were implemented as reference documents because that is what they were before software, and nobody reframed them as executable policy. Applying them automatically requires identifying a clause's substance rather than its text, which needed language-model-grade comprehension and is now feasible. The category is also cautious, correctly, about automating legal work, and the caution has been applied uniformly rather than to the cases that warrant it — which is why the routine nine are treated with the same ceremony as the consequential three. And the measure of success in the category is cycle time, which a faster lawyer improves and which does not reveal how the lawyer's time was spent.

## What to Build
The layer both sub-niches sit on: a machine-readable playbook and a triage that separates routine from consequential. Encode the playbook as structured policy — for each provision, the preferred position, the acceptable fallbacks, the walk-away, and the conditions under which each applies by deal size, counterparty type and jurisdiction — which is work the legal team must do once and which converts a document into something a system can act on. Classify every provision in an incoming contract against that policy: compliant, within fallback, outside policy, or absent. Route accordingly, so the provisions within policy are handled without counsel and the ones outside it are surfaced with the specific deviation described. Measure the split — what proportion of a contract is routine — which is the number that justifies the investment and which nobody currently produces. And make the policy the single source, so that the clause library, the automated redlining of the first sub-niche and the achievability evidence of the second all reference the same definitions rather than drifting apart, which is the failure documented in the clause library niche.

## Target Customer
General counsel and legal operations at companies with meaningful contract volume, and the CLM vendors whose playbook features are currently documents with a search box.

## Impact If Built
The routine share of a negotiation is large and consumes the most expensive hours available, and separating it from the consequential share is the prerequisite for everything else. A structured playbook is also the artefact that keeps the library, the automation and the evidence aligned.
