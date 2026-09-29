# Everything Correlates and Nothing Explains

**Niche:** [[niches/observability-vendors/incident-diagnosis/profile|Incident Diagnosis]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** At three in the morning the tooling shows an engineer everything that moved and leaves them to work out which thing moved first and why, which is the whole job and the part the category does not do.
**Tags:** #graph-neural-networks #causal-inference #change-point-detection #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to meet the engineer at the page with a ranked explanation rather than a dashboard — and whoever does that takes the account, because time to diagnosis is the largest component of incident duration and the moment the category's value is either delivered or not.

## The Problem
A page fires at 03:12. Checkout latency is up. The engineer opens the dashboard: eleven services show elevated latency, three show elevated errors, the database shows increased connection wait, and a cache hit rate has fallen. All of these are true and most of them are consequences. Somewhere is a deployment forty minutes ago, or a configuration change, or an upstream provider degrading, or a slow leak that crossed a threshold. Finding it takes twenty-five minutes of an engineer's attention at the least reliable hour of their day, and the same failure mode has occurred at four hundred other companies this year.

## Why Nobody Has Built This
Automated root cause has been claimed by the category for a decade and delivered mostly as correlation dressed as causation, which produced a durable and reasonable scepticism — one confidently wrong diagnosis at the most expensive possible moment destroys trust in the feature permanently. Doing it properly requires the service dependency graph at fine resolution, which only became widely available with tracing adoption and which many customers still lack. The cross-customer corpus is where the real leverage is and is contractually awkward, so vendors have declined to use it rather than working out the form in which they could. And confirmed root causes come from post-incident reviews, which are inconsistent, often absent and rarely structured, which is the binding labelling constraint.

## What to Build
Hypotheses, not verdicts. Establish what moved first and how it propagated, using temporal precedence at fine resolution over the dependency graph derived from tracing — which is the closest thing to causal evidence available in this setting and is what separates an explanation from a correlation. Enumerate and rank the changes preceding the incident: deployments, configuration, feature flags, infrastructure events, dependency releases, since a large majority of incidents follow a change and the change stream is collected and unjoined. Match the anomaly's shape against abstracted failure signatures from the cross-customer corpus, which is the vendors' unique asset and requires abstraction away from customer service names and semantics to be contractually usable — a legal and communications project as much as a technical one. Return three candidate explanations with their evidence and an explicit calibrated confidence, because an engineer evaluates a hypothesis in thirty seconds and cannot evaluate a conclusion. Add blast radius, since the first questions asked of an on-call engineer are always who is affected and how many. And capture the confirmed cause afterwards in a structured form, which is the only way the system improves and is currently left to prose.

## Target Customer
Observability vendors, incident response platforms, and engineering organisations with a meaningful on-call rota — where the argument is made on incident duration rather than on features.

## Impact If Built
Time to diagnosis is the largest component of incident duration and the category's products do not address it. Top-three accuracy with calibrated confidence is the right target, and the cross-customer signature corpus is leverage no single organisation can replicate.
