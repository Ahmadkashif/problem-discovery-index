# Adversaries Who Adapt Within Days

**Niche:** [[niches/edge-cdn-providers/bot-and-abuse-management/profile|Bot & Abuse Management]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every provider sells bot management built on signatures, fingerprints and behavioural heuristics, and every one of them is in a race against adversaries who adapt within days of a rule shipping.
**Tags:** #gradient-boosting #change-point-detection #contrastive-learning #k-means-clustering #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in bot management is fighting to keep up with adversaries who adapt within days of a rule shipping — and whoever detects the adaptation as it happens across their whole customer base takes the market, because no single customer can see it.

## The Problem
A research team ships a rule that identifies a scraping operation by a combination of fingerprint characteristics. It works. Within a few days the traffic changes: the fingerprint is randomised, the timing is jittered, the request order is shuffled. The rule's match rate falls and its effectiveness with it, and nobody notices for a fortnight because a falling match rate looks like a declining attack. The next rule takes a week to research and ship. The cycle repeats, and the provider is permanently a step behind an adversary who can test against the defence continuously and iterate in hours.

## Why Nobody Has Built This
Detection has been built as a research-and-ship pipeline, which is the natural way to build it and produces a cycle time structurally slower than the adversary's. The cross-customer signal — the same adaptation appearing simultaneously across many properties — is used to inform the research team's next rule rather than to detect the adaptation automatically, which discards the provider's one structural advantage. A falling match rate is ambiguous between a defeated rule and a departed adversary, and nobody has separated them. And the false positive side is measured by complaint rather than by instrument, which biases every threshold decision toward blocking.

## What to Build
Detect the adaptation rather than the adversary. Monitor each detection's effectiveness continuously — match rate, and crucially the downstream outcome the detection was protecting, since a rule that still matches and no longer prevents the abuse has been routed around rather than defeated. Distinguish a defeated rule from a departed adversary by watching the abuse outcome rather than the match count, which is the ambiguity that currently hides every adaptation. Use the cross-customer view as the primary detector: an adaptation appears as a correlated shift in traffic characteristics across many unrelated properties at once, which is unmistakable in aggregate and invisible to any single customer, and is the provider's unique position. Learn continuously from confirmed outcomes — completed fraud, confirmed scraping, verified legitimate users — rather than shipping static rules, and treat the label scarcity honestly since confirmations are sparse. Model the asymmetric cost explicitly, because the current thresholds are set by a research team with an intuition about the trade-off and the two error costs differ by customer and by endpoint. And measure the false positive side properly, which the fix note below addresses and which changes every threshold in the system.

## Target Customer
Edge and security providers, the fraud and security functions who buy this, and the customers whose legitimate users are currently being blocked at an unmeasured rate.

## Impact If Built
The cycle time asymmetry is structural and the cross-customer view is the only available answer to it, and it is used to inform a human research process rather than to detect automatically. Watching the protected outcome rather than the match rate is what makes an adaptation visible at all.
