# Confirmed Fraud Outcomes as the Missing Label Set

**Niche:** [[niches/freight-brokerage/carrier-vetting-fraud-prevention/profile|Carrier Vetting & Freight Fraud Prevention]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Brokers discover fraud after the load disappears, and that discovery — the only ground truth in the entire product — reaches the vetting provider as an anecdote if at all.
**Tags:** #gradient-boosting #logistic-regression #graph-neural-networks #evaluation-metrics #cross-validation #confidence-intervals #feature-engineering #contrastive-learning #compliance #data-integration

## The Problem
A vetting determination is a prediction that this carrier is legitimate. The prediction resolves — the load delivers, or it does not and the broker discovers a fictitious pickup, a double-brokered shipment, or an identity-cloned carrier. That outcome is the only labelled data in the domain, and it stays with the broker who suffered it. Some report it to industry channels, most quietly absorb the loss and move on. So models are tuned on identity signals and rules built from known fraud patterns, while the stream of confirmed outcomes that would train them properly is dispersed across thousands of brokers. False negatives are catastrophic and uncounted; false positives block legitimate carriers and are also uncounted.

## Why Nobody Has Built This
Fraud losses are embarrassing and frequently absorbed rather than reported, so the natural reporting rate is low. Reporting is also slow — a broker may not know for days — and the report, when it comes, arrives as a phone call or an email rather than as structured data tied to the vetting decision that preceded it. And in a competitive vetting market, the outcome data a provider holds is exactly what it does not want to make comparable across vendors.

## What to Build
Structured outcome capture designed so reporting is nearly free and clearly worth it. When a broker vets a carrier through the platform, the load is tracked to a disposition — delivered, disputed, or fraudulent — with a one-click report and, where the broker's systems allow, automatic resolution. In exchange the broker receives what they cannot get otherwise: their own fraud exposure benchmarked against comparable brokers, and immediate network alerting when a carrier they used is later confirmed fraudulent elsewhere, which is the single most valuable thing a vetting network can offer. On the provider side, precision and recall become measurable by carrier type, signal, and fraud method; the specific patterns that precede confirmed fraud become learnable rather than assumed; and the emergence of a new method becomes visible as a cluster of confirmed outcomes that existing rules missed — which is the earliest possible warning in a domain where methods change faster than rules.

## Target Customer
Chief product officers and VPs of risk at carrier vetting providers running 50-300 analysts, and the broker operations leaders who currently absorb fraud losses without any mechanism for the industry to learn from them.

## Impact If Built
Creates the only ground truth in the domain and turns a rules-based product into a learning one. The network effect is unusually strong here — each additional broker reporting outcomes improves protection for all of them — which makes the outcome corpus both the moat and the reason to join.
