# Two Providers Disagree and Somebody Guessed

**Niche:** [[niches/data-marketplace-brokers/schema-and-entity-resolution/profile|Schema & Entity Resolution]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** When two providers report different values for the same field, the pipeline picks one according to a preference order somebody chose in the first week, and nobody ever checks which was right.
**Tags:** #hypothesis-testing #bayesian-inference #evaluation-metrics #descriptive-statistics #confidence-intervals #data-integration #quick-win #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to make four providers covering the same entities into one coherent view without the buyer writing four pipelines and a resolution layer — and whoever does that takes the account, because every multi-source buyer builds this and nobody sells it.

## The Problem
Provider A says the company has four hundred employees; provider B says eleven hundred. The pipeline prefers A because A was integrated first and somebody wrote a preference order in week one. It does this across two hundred fields and several million entities, silently, thousands of times a day. Nobody has ever checked whether A is actually more accurate for employee count — B might be right on that field and wrong on revenue. The disagreements are a continuous stream of evidence about relative provider quality, and every one of them is resolved by a rule and then discarded.

## Why It's Still Broken
Resolving by preference order is simple and produces a value, which is what the pipeline needs. Checking which provider was right requires ground truth the buyer does not have for most fields. The disagreement is not logged, so even retrospective analysis is impossible. And the preference order was set once by someone reasonable and has the unexamined authority of anything that has been there a long time.

## What a Fix Looks Like
Log the disagreement and learn from it. Record every conflict with both values and the field, which costs a small amount of storage, requires no new logic, and creates the evidence base this entire fix depends on — most organisations could start today. Establish per-field accuracy using whatever ground truth exists: internal records, public registries, sampled manual verification, and later-confirmed outcomes — a few hundred verified cases per field is enough to rank providers meaningfully. Set survivorship from measured accuracy per field rather than a global preference order, since providers are reliably better at different things and a single order is wrong for most fields by construction. Report disagreement rates per provider pair per field, which is a strong quality signal even without ground truth, since a provider who disagrees with everyone else is usually the outlier. Propagate uncertainty rather than silently choosing, so a downstream consumer of a heavily-contested field knows it is contested. Surface high-value conflicts for human review, since a disagreement on a large account is worth a person's minute. Use the accuracy record in renewal decisions, which turns an operational artefact into a commercial one. And feed the findings back to providers, who frequently do not know they are wrong and can fix it.

## Who Feels the Pain
Analysts building on values chosen by a week-one rule; businesses acting on the wrong number where a better one was available in the same pipeline; and providers who are accurate on a field and never preferred for it.

## Impact If Fixed
Every conflict is evidence about relative provider quality and every one is discarded. Logging them costs almost nothing and a few hundred verified cases per field is enough to replace a global preference order with per-field measured accuracy.
