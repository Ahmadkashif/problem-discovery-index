# An Instrument for an Invisible Channel

**Niche:** [[niches/newsletter-media/deliverability/profile|Deliverability]]
**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The business depends on a channel it cannot observe, and the publisher holds years of send characteristics against engagement that would let it infer what it cannot measure.
**Tags:** #gradient-boosting #change-point-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #causal-inference #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to get the newsletter into the inbox rather than the promotions tab or the spam folder — and the contest splits cleanly enough that it is not terminal.

## The Problem
Placement is decided by systems that report almost nothing. Publishers respond by buying seed list tests, which deliver a handful of synthetic mailboxes to a few dozen accounts and generalise from them to a list of hundreds of thousands across dozens of providers. Meanwhile the publisher holds the actual evidence — every send's characteristics, every subscriber's engagement, by provider, by segment, over years — and nobody treats that as the measurement instrument it could be.

## Why Nobody Has Built This
Deliverability was treated as a vendor service, so publishers bought a test rather than building a capability — and a purchased proxy suppresses the demand for a real measurement. Providers do not report placement, which made inference look impossible rather than merely indirect. The privacy change removed the metric everyone had leaned on and nothing replaced it. And the publishers with the data are small and have no data function.

## What to Build
Infer what cannot be measured, and manage what can. Model placement from engagement behaviour by provider and segment, which is the core — a sudden divergence in click behaviour for one provider's subscribers while others hold steady is a placement change and is detectable. Build the baseline from the publisher's own history, since every publisher's normal differs and the signal is the deviation. Use the provider dimension as the natural control, because a change affecting one provider and not others is almost certainly placement rather than content. Separate the inference problem from the reputation operations problem, which is the decomposition below and lets each be solved properly. Manage the inputs that governed placement — complaint rate, authentication, unsubscribe handling, sending patterns, list hygiene — against the published thresholds rather than by folklore. Detect a placement change within a send or two rather than after a month of declining revenue. Combine the inference with what postmaster tools do report, since partial direct evidence calibrates the indirect estimate. Pool across publishers to establish what provider behaviour looks like generally, which no single publisher can see. Express confidence honestly, because a confident wrong deliverability diagnosis sends a publisher down an expensive wrong path. And report placement as an operating metric, since it is the one number that governs the business and nobody has it.

## Target Customer
Publisher and growth leadership, sending platforms whose customers fly blind, deliverability service vendors selling seed tests, and advertisers whose impressions depend on placement.

## Impact If Built
A purchased proxy suppresses the demand for a real measurement, so publishers bought seed tests instead of building an instrument. Years of send characteristics against engagement by provider is the evidence that makes placement inferable without being told.
