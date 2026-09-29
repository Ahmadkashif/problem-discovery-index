# Incident Diagnosis

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to meet the engineer at the page with a ranked explanation rather than a dashboard — and whoever does that takes the account, because time to diagnosis is the largest component of incident duration and the moment the category's value is either delivered or not.

## Profile
**Market Size:** ~$2.1B US attributable to incident diagnosis and root cause capability
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** Low in substance — automated root cause is claimed widely and trusted narrowly
**Target Buyer:** Engineering leadership and site reliability functions
**Automation Potential:** Very High, gated by the labelling of confirmed root causes

## What Makes This a Distinct Niche
During an incident everything correlates. Latency rose, error rates rose, queue depth rose, a dozen dashboards turned red, and the engineer must separate cause from consequence under time pressure at whatever hour it is. The category's products present all of it and assert nothing, which is honest and unhelpful. Meanwhile the vendors hold the most detailed record of how production software fails that exists anywhere: telemetry from millions of services across thousands of organisations, with incidents, their propagation and their resolutions attached. Failure modes repeat across companies far more than any individual engineer can see, since each one experiences only their own outages. The contest is a ranked, evidenced explanation at page time — not a verdict, which nobody can evaluate, but two or three hypotheses an engineer can check in thirty seconds each.

## Current Tools & Gaps
Dashboards, alerting, tracing-derived service maps, change event feeds, and automated root cause features whose claims exceed their use. The gaps: correlation is presented as causation, which is why the existing features are distrusted after the first confident wrong answer; temporal precedence over the dependency graph is the closest thing to causal evidence available and is underused; change streams are collected and rarely joined to incidents; the cross-customer corpus is the vendors' unique asset and is contractually awkward to use, which has meant not using it at all rather than finding the workable form; and post-incident reviews, which are the only source of confirmed root causes, are written inconsistently and rarely in a structured form.

## Problems
- [[niches/observability-vendors/incident-diagnosis/build|🔨 Build: Everything Correlates and Nothing Explains]]
- [[niches/observability-vendors/incident-diagnosis/buy|🛒 Buy: Causal Structure From the Dependency Graph]]
- [[niches/observability-vendors/incident-diagnosis/fix|🔧 Fix: The Change Stream Nobody Joins to the Incident]]
