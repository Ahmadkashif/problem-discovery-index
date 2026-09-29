# Interpretations Are Published Without the Reasoning That Produced Them

**Niche:** [[niches/compliance-consulting/regulatory-content-publishers/profile|Regulatory Intelligence Publishers]]
**Industry:** [[industries/compliance-consulting|Compliance Consulting]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst weighs ambiguous statutory language, agency guidance, and enforcement history to conclude what a rule actually requires, and the corpus stores the conclusion — so when the ground shifts, nobody knows which conclusions depended on what.
**Tags:** #large-language-models #bert #transformers #graph-neural-networks #evaluation-metrics #word-embeddings #tacit-knowledge-ml #compliance #data-integration #worker-facing

## The Problem
The publisher's entire value over the free public text is interpretation: what this obligation means operationally, where the ambiguity is, and how a regulator has actually applied it. Producing that means an analyst reconciling statutory language with guidance, examination manuals, enforcement actions, and sometimes informal agency positions, and forming a view. The corpus stores the view. The reconciliation — which authorities were weighed, which were discounted and why, how confident the analyst was, what would change the answer — exists as working notes or not at all. Two consequences follow. When an enforcement action or a guidance update undermines one of the authorities an interpretation rested on, nobody can identify which interpretations are affected, because the dependency was never recorded. And an analyst inheriting a coverage area receives a body of conclusions they cannot interrogate, so they leave them alone, and interpretations calcify.

## Why It's Still Broken
The editorial system produces and versions published text, and interpretation is stored the way it is displayed — as prose. Under a publication cadence, recording the reasoning behind a conclusion reads as overhead against output, and the reasoning is not part of what the subscriber buys, so it loses. There is also a defensive instinct: an explicit record of confidence and of the authorities an interpretation depends on is a record that could be used against the publisher if the interpretation turns out to be wrong, which is a real if short-sighted concern in a product relied on for compliance decisions.

## What a Fix Looks Like
An interpretation record attached to every published position, captured as the analysis is done. It holds the authorities relied on with their weight, the authorities considered and discounted with the reason, the confidence, and the standing trigger — what development would cause this interpretation to change. That last field converts the corpus from static text into a dependency network: when an enforcement action lands or guidance is revised, every interpretation that named it surfaces for review automatically instead of waiting for a coverage cycle. Across the corpus, the accumulated records support things that are impossible today — finding interpretations that rest on a single ageing authority, measuring consistency between analysts on comparable questions, and showing a subscriber not only what the publisher concludes but on what basis, which is a materially stronger product than an assertion.

## Who Feels the Pain
Analysts inheriting conclusions they cannot reconstruct and therefore do not revisit; editorial leadership with no instrument to measure consistency across a corpus whose whole value is consistency; subscribers making compliance decisions on interpretations whose confidence is invisible; and the publisher, whose most damaging failure mode is a subscriber discovering a stale interpretation before it does.

## Impact If Fixed
Turns a body of conclusions into a body of reasoning, which is the more defensible product and the one that supports everything else — impact routing, coverage prioritization, and change response all require knowing what each interpretation depends on. It also directly attacks the failure that most damages a regulatory subscription, which is content that was right when written and quietly stopped being right.
