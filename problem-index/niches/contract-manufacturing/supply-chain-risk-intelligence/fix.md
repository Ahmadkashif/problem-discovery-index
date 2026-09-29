# Alerts Are Never Scored Against Whether Anything Happened

**Niche:** [[niches/contract-manufacturing/supply-chain-risk-intelligence/profile|Multi-Tier Supply Chain Risk Intelligence]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** The vendor issues thousands of disruption alerts a year, most of which resolve into nothing and a few of which were the warning that mattered, and it keeps no record distinguishing them.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #causal-inference #change-point-detection #descriptive-statistics #cross-validation #data-integration #revenue-impact

## The Problem
Every alert is an implicit prediction that a client's supply is at risk, and every one of them resolves — the fire was contained and shipments continued, or the plant was down for six weeks and the client scrambled. That resolution is knowable, sometimes from public information and always from the client, and it is not collected. The consequence is the failure mode every alerting product eventually reaches: volume rises because missing an event is more visible than crying wolf, clients begin discounting alerts, and the one that mattered arrives in a stream nobody trusts. Neither the vendor nor the client can say what the false positive rate is, so neither can argue about whether the volume is right.

## Why It's Still Broken
Outcome data lives with the client, arrives late, and is unstructured — often the only record is that a sourcing manager checked and moved on. Nothing in the product asks for it, and clients have no incentive to report a non-event. Internally, alerting is an operations function measured on latency and coverage, both of which push volume up, and nobody is measured on precision. And the vendor has a straightforward disincentive: a measured false positive rate is a number a competitor can attack in a bake-off, so the safe posture has been not to have one.

## What a Fix Looks Like
Outcome capture built into the alert itself, at the lowest possible cost to the client — a one-click disposition when an alert is reviewed, recording whether it was relevant, whether action was taken, and whether disruption actually followed. Public resolution supplements it where available, so the record does not depend entirely on client diligence. With that, precision and recall become measurable by event type, region, supplier tier, and severity band, which turns alert thresholds from a guess into a tuned parameter and lets clients set their own tolerance rather than receiving the vendor's. The most valuable output is the one nobody can produce today: which classes of event actually predict disruption and which do not, which is the empirical foundation the whole product implicitly claims and has never established. Clients get their own alert-to-action record back, which is both the incentive to participate and a genuinely useful artefact for demonstrating due diligence.

## Who Feels the Pain
Risk managers triaging alert volume they cannot calibrate; the vendor's product team tuning thresholds by instinct; sales teams facing a bake-off with no precision claim; and the client who eventually misses a real disruption because the stream had trained them to skim it.

## Impact If Fixed
Turns the central claim of a risk intelligence product from an assertion into a measurement, in a category where every competitor sells the same assertion. It also produces the empirical basis for what actually predicts disruption — which improves the product itself far more than any additional data feed would, and cannot be replicated without the same alert and outcome history.
