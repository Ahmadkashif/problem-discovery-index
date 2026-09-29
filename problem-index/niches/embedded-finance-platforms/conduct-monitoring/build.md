# Inferring Conduct From API Calls

**Niche:** [[niches/embedded-finance-platforms/conduct-monitoring/profile|Conduct Monitoring]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform must know whether a programme is treating its customers fairly and can observe only accounts opened, money moved, fees posted and accounts closed.
**Tags:** #gradient-boosting #change-point-detection #graph-theory #confidence-intervals #evaluation-metrics #compliance #descriptive-statistics #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to infer how a programme treats its customers from the API calls it makes — and whoever detects a problem before the bank's examiner does defines what oversight from this layer can mean.

## The Problem
The platform cannot read the programme's marketing, use its app, or hear its support calls. What it has is the behavioural trace: how many accounts are opened and how many are abandoned midway, what fees are posted and in what patterns, how often customers are charged twice in a day, how quickly accounts close after opening, how disputes arrive, and how all of that compares to the same product built by someone else on the same rails. That trace contains a great deal of information about how customers are being treated, and the monitoring applied to it is a set of anti-money-laundering rules written for a bank's own retail book.

## Why Nobody Has Built This
Monitoring was inherited from the bank context and was about financial crime rather than conduct, so the tooling answers a different question — the question the platform now needs answered was never the one the software was built for. Conduct signals require modelling rather than rules and nobody has defined them. The comparison across programmes is the obvious instrument and raises commercial questions about using one customer's data to assess another. And detection has been incident-driven, which means the capability is only exercised after a failure.

## What to Build
Define and detect the conduct signals. Model the behavioural signatures of poor treatment — fee patterns inconsistent with plausible disclosure, onboarding abandonment concentrated at a particular step, rapid account closure after opening, balances systematically drained by charges, disputes clustering on one product feature — which is the core and is a definitional exercise the category has not done. Use the cross-programme comparison as the primary instrument, since a programme whose numbers differ markedly from every comparable programme on identical rails is the strongest signal available and is visible only here. Analyse onboarding outcomes by population where the data permits, because a flow failing disproportionately for some groups is a serious exposure and is detectable. Detect the change rather than the level, since a programme whose behaviour shifts after a product change is the most actionable finding. Model each programme's own baseline, so a product that is legitimately unusual is not permanently alarming. Rank findings by customer harm rather than by rule count, which is what makes the output usable by a small team. Investigate with evidence assembled, connecting to the analyst niche. Distinguish a programme design problem from an execution problem, since the remedies differ. Handle the data governance explicitly, because cross-programme comparison is the method and its legitimacy must be established rather than assumed. And report detection performance, since an oversight function that never catches anything before an incident is not detecting.

## Target Customer
Platform risk and data leadership, sponsor banks relying on this detection, and the conduct risk vendors whose products assume a direct customer relationship.

## Impact If Built
The monitoring was inherited from a financial crime context and answers a different question from the one the obligation now poses. Cross-programme comparison on identical rails is the strongest available conduct signal and is visible only from this position.
