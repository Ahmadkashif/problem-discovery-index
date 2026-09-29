# Negotiation Outcomes as Feedback on Benchmark Accuracy

**Niche:** [[niches/cloud-infrastructure-consultants/it-sourcing-price-benchmark-advisors/profile|IT Sourcing & Price Benchmark Advisors]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm tells a client what they should pay, the client negotiates, and what they actually ended up paying is the cleanest possible test of the benchmark — captured inconsistently, if at all.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #causal-inference #confidence-intervals #hypothesis-testing #descriptive-statistics #data-integration #revenue-impact

## The Problem
Every engagement is a natural experiment the firm does not run. A benchmark says the achievable price for this configuration at this volume is here; the client takes it into negotiation; a settled contract emerges at some price. The gap between the two is the most direct evidence available about whether the benchmark was right, whether it was achievable, and how much of the outcome was the benchmark versus the client's own leverage. Outcomes are captured when an engagement lead happens to record them, in engagement files rather than in the benchmark database, and they are not joined back. So the benchmark database grows from contributed contract data and expert judgment about comparability, and its accuracy is asserted through methodology rather than demonstrated through results — in a product whose entire value proposition is that the number is right.

## Why Nobody Has Built This
Outcome capture requires clients to disclose their final negotiated position, which many are reluctant to do after the value has been delivered and the engagement is closed. The analysis is also genuinely confounded: a client who fails to reach the benchmark may have had a weak negotiating position, a bundled deal, or a strategic reason to concede, none of which reflect on the benchmark. Separating those requires modelling engagement context that has never been captured in structured form. And there is the recurring institutional disincentive — a firm that measures its own benchmarks creates a record of the ones that were unachievable, which is uncomfortable in an advisory business built on confidence.

## What to Build
Systematic outcome capture designed into the engagement rather than requested after it. Settled price, contract structure, and the negotiation context — leverage, timing, bundling, incumbency — are recorded as structured fields at engagement close, with the client's own benchmarked view of their result as the incentive to provide them. The analysis then separates benchmark accuracy from achievability: how often the benchmarked price was reached, how the gap varies by vendor, product category, deal size, and client leverage, and which benchmark segments are systematically optimistic or conservative. That distinction is the whole point — a benchmark that is accurate about market pricing but unachievable for a client with weak leverage is a different failure from one that is simply wrong, and the firm currently cannot tell them apart. Outputs feed both directions: benchmark segments flagged as needing evidence, and a prospective achievability estimate delivered alongside the benchmark itself, which is a materially better product than a bare number.

## Target Customer
Managing directors of benchmarking and heads of research at sourcing advisory firms, and the sourcing executives at client organizations who currently receive a target price with no indication of how often it is actually reached.

## Impact If Built
Converts methodology-based authority into evidence-based authority in a business where the client's whole reason for engaging is that the number is credible. Achievability estimates alongside benchmarks are a new product with an obvious buyer, and the outcome corpus compounds — it can only be built by the party running the engagements, which is the most defensible position available in this market.
