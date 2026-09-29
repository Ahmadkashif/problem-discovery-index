# Self-Service Diagnosis From Support Deflection

**Niche:** [[niches/edge-cdn-providers/cdn-support-engineer/profile|The CDN Support Engineer]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Support deflection, guided diagnosis and knowledge article suggestion are mature capabilities in the support tooling market, and CDN support runs on a human reading logs.
**Tags:** #bert #k-means-clustering #logistic-regression #word-embeddings #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to tell a customer why their content missed the cache before they open a ticket — and whoever does that takes the support organisation, because that single explanation is most of its volume.

## The Problem
Classifying an incoming issue, matching it to a known cause and presenting the resolution before a human is involved is standard support tooling, deployed widely and working reasonably. CDN support has an unusually favourable version of this problem — the causes are few, the evidence is complete and machine-readable in the logs, and the diagnosis is deterministic rather than probabilistic — and it is performed by an engineer reading logs for each ticket.

## What Already Exists
Support deflection and suggested-answer platforms; text classification for ticket routing; log analysis and clustering; knowledge base search; and the whole guided-diagnosis pattern from consumer technical support. All mature and much of it deployed by these same providers for their general support.

## The Customization Gap
The adaptation is to a diagnosis that is deterministic from data the provider holds. It requires: (1) diagnosis from the logs rather than from the ticket text, since the customer's description is imprecise and the evidence is exact — which inverts the usual deflection approach, where the input is what the user typed; (2) the customer's specific instance rather than a general article, because the answer is not that private headers prevent caching but that this path is returning that header on this property, and the specific version is the one that resolves the ticket; (3) proactive rather than reactive delivery, since the same analysis is far more valuable before the customer notices, which is a delivery change rather than an analytical one; (4) high precision on the provider-versus-customer attribution, because telling a customer the fault is theirs when it is not is a specific and damaging error; and (5) a taxonomy of causes maintained from the support corpus, so the classifier's classes reflect what actually happens rather than a category list designed years ago.

## Target Customer
Delivery providers, support platform vendors, and the observability vendors whose log analysis capabilities this uses.

## Impact If Solved
The diagnosis is deterministic and the evidence is complete, which makes this an unusually favourable deflection problem that has not been attempted. Diagnosing from logs rather than from ticket text and delivering proactively are the two changes that convert deflection into prevention.
