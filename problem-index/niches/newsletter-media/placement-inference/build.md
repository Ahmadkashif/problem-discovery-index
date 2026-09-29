# Estimating Placement From Behaviour

**Niche:** [[niches/newsletter-media/placement-inference/profile|Placement Inference]]
**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Placement is unobservable and its consequences are not, which makes it an inference problem rather than an impossibility.
**Tags:** #change-point-detection #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting #causal-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to estimate where a send actually landed, per provider and per segment, from behaviour rather than from a seed test — and whoever does it replaces a few dozen synthetic mailboxes with the publisher's own hundred thousand.

## The Problem
Nobody will tell a publisher where their mail landed. But placement has consequences that are visible: a segment that suddenly clicks less while an otherwise identical segment on another provider does not, a cohort whose engagement decays faster than its history predicts, a change that coincides with a sending change. Those patterns are in every publisher's data and are exactly the kind of signal that supports inference. The industry's answer instead is a test on synthetic mailboxes that behave nothing like real subscribers.

## Why Nobody Has Built This
The absence of a direct measurement was taken to mean no measurement was possible, so nobody framed it as inference — an unobservable variable with observable consequences is a standard problem and it was never posed as one. Seed tests exist and feel like an answer. Publishers have no analytical capacity. And the platforms that could do it across their whole customer base have not.

## What to Build
Treat the provider as the control. Model each provider-segment's expected engagement from its own history, which is the core and turns an absolute question into a deviation question. Detect divergence between providers on the same send, since content quality affects all providers and placement affects one — that contrast is the strongest available identification. Detect within-provider change points against the segment's own baseline, because a gradual placement decline is the common failure and it is invisible in aggregate metrics. Incorporate the partial direct evidence from postmaster tools as calibration, as some ground truth anchored to inference beats either alone. Estimate placement as a probability rather than a verdict, since the inference is genuine but imperfect and a confident wrong answer is expensive. Pool across publishers on the same platform to characterise provider behaviour, which no single publisher can observe and which makes every individual estimate better. Attribute a detected change to a plausible cause — a sending change, a content change, a list change, a provider change — because the estimate is only useful if it points somewhere. Alert within a send or two, as the cost of a placement problem compounds daily. Validate against the cases where placement is eventually confirmed, so the method is checkable. And report placement alongside engagement, since the two are currently conflated in every report.

## Target Customer
Publisher and data leadership, sending platforms, deliverability vendors selling seed tests, and advertisers whose impressions depend on it.

## Impact If Built
An unobservable variable with observable consequences is a standard inference problem and it was never posed as one here. Comparing providers on the same send is a natural control that identifies placement change more reliably than any synthetic mailbox test.
