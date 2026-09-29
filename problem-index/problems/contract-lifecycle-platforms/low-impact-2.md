# Third-Party Paper Review

**Industry:** [[contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every CLM product reviews contracts against a playbook, and the review that matters is of the counterparty's paper — where the risky term is the one that is absent, and absence is what checklist review misses.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance

## The Problem
When a company signs on its own template, the terms are known. When it signs on the counterparty's paper — which is most of the time when buying from a larger vendor, and increasingly common generally — counsel must read an unfamiliar document and find what is wrong with it.

That review has two halves. The first is checking the terms that are present against what the company will accept: liability caps, indemnities, governing law, termination rights, payment terms. Automated review handles this reasonably and the products do it.

The second half is what is missing, and it is where the risk actually concentrates. No limitation of liability at all. No termination for convenience. No data protection terms. No cap on price increases at renewal. An absent clause does not appear in any extraction output, and a checklist-driven review looks for problems in what is written rather than for silence where something should be.

The third dimension is context. Whether a particular indemnity is acceptable depends on what is being bought, at what value, with what data involved and under what regulatory exposure — and generic review does not know any of that.

## What Already Exists
Contract review features exist in every CLM product and in specialists (LegalOn, Spellbook, Robin AI). Clause extraction is mature. Playbook comparison is standard. Redlining and version comparison work well. Large language models have made drafting suggestions genuinely useful in the last two years.

## The Customisation Gap
Absence detection requires a model of what should be present for this type of agreement in this context, and that model does not exist in any product. Building it is tractable — the company's own executed agreements and its playbook define expectations, and the vendor's cross-customer corpus defines what is typical for this agreement type — and it is the highest-value gap in review.

Risk is also uncalibrated. Reviews return findings without any indication of which matter. An unusual indemnity in a hundred-thousand-dollar agreement involving personal data is not the same as an odd notice provision in a small subscription, and every experienced lawyer prioritises instinctively while the tooling lists everything equally.

Achievable positions are the third gap and connect to the playbook problem. Knowing that this counterparty has accepted a mutual cap in eleven of fourteen prior negotiations across the vendor's customer base is worth more than knowing the company's stated preference.

And escalation should be predicted rather than triggered by keywords: which contracts genuinely need senior review is learnable from which ones senior counsel actually changed.

## Impact If Solved
Third-party paper is where companies accept terms they did not choose, and automated review looks at what is written rather than at what is missing. Absence detection with contextual risk calibration is what would make review useful rather than thorough, and the cross-customer evidence on achievable positions is available only to the platform.
