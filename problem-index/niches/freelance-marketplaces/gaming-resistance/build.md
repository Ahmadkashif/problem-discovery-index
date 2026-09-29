# Build: Manipulability Scoring for Ranking Features

**Niche:** [[niches/freelance-marketplaces/gaming-resistance/profile|Gaming Resistance]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Score every ranking feature by how cheaply it can be moved without improving the underlying work, and weight the model accordingly before the exploitation rather than after it.
**Tags:** #causal-inference #gradient-boosting #graph-theory #hypothesis-testing #feature-engineering #evaluation-metrics #confidence-intervals #automation
**Contested on:** Whether the cost of faking a signal can be estimated before anyone has faked it at scale.

## The Problem

A ranking feature is selected because it predicts a good outcome in historical data. That historical data was generated in a world where nobody was optimising against that specific feature's weight. The moment the feature carries ranking weight, a fraction of the supply side begins moving it directly — and the correlation that justified including it degrades, silently, in a way that offline evaluation against historical data cannot detect.

The platform discovers this when an integrity analyst notices an implausible pattern, or when clients start complaining that top-ranked freelancers deliver badly. By then the feature has been carrying weight for quarters, and the accounts that exploited it hold rankings they did not earn.

## Why Nobody Has Built This

Feature selection is owned by the search quality team and manipulation is owned by trust and safety, and the artifact that would connect them — a per-feature manipulability score — belongs to neither. Search quality is measured on relevance metrics that a gamed feature improves. Trust and safety is measured on detected abuse and has no input into the model that creates the incentive.

It is also methodologically unfamiliar. The question "how expensive is it to fake this signal" is an economic question about the adversary, not a statistical question about the data, and the ML team has no established method for it. The literature on adversarial robustness is about perturbations to inputs, not about a rational actor choosing between improving and faking based on relative cost.

## What to Build

A manipulability scoring system that sits between feature engineering and the ranker, and that produces a defensible cost-to-fake estimate per feature.

Start with what is already observable. For each candidate feature, use the platform's own historical record to find the accounts whose movement on that feature is inconsistent with movement on outcomes — freelancers whose completion rate rose while contract values collapsed to nothing, whose response rate hit 100% with reply latencies too uniform to be human, whose rating distribution has no variance across clients who have no other activity. These are the signature of a faked signal, and their prevalence is a direct empirical estimate of how exploitable the feature already is.

Then estimate the economics explicitly. For each feature, enumerate the cheapest known route to moving it by a meaningful amount and price it: the platform fees for the throwaway contracts, the cost of an account network, the time cost of the automation. Set that against the ranking benefit the feature currently confers, computed from the model itself. A feature where a $40 outlay buys a large placement gain is a feature that will be exploited, and this is knowable before it is.

Build the graph layer properly, because most serious manipulation is relational rather than individual. Reciprocal contract structures, rating exchanges, client accounts with no independent activity, and shared payment or device infrastructure all show up as structure in a bipartite client-freelancer graph long before any individual account looks anomalous. Score features by how much of their variance is explained by within-cluster activity, which is a direct measure of how much of the signal comes from collusion.

Feed the scores back as model constraints. Cap the weight a highly manipulable feature can carry. Prefer costly-to-fake alternatives — a completion signal weighted by contract value and client independence rather than a raw count; a rating that counts only clients with independent history on the platform. Re-score quarterly, because the adversary moves.

Measure the thing that matters: for freelancers who rose on each feature, what happened to their subsequent completion and repeat-client outcomes. A feature whose risers underperform is being gamed, and that test runs continuously on data already collected.

## Target Customer

Search quality and marketplace integrity teams at platforms large enough that organised manipulation is economically worthwhile — which in practice is any marketplace above a few hundred million in gross services volume. The buyer is whoever is accountable for both ranking quality and abuse, which at most platforms is nobody, and naming that owner is part of the sale.

## Impact If Built

The ranker stops depending on signals whose only defence is that nobody has attacked them yet. Manipulation becomes economically unattractive rather than merely detectable, which is the only durable outcome against an adaptive adversary. And the ranking becomes robust enough to explain — which is the precondition for the other half of this niche ever being built.
