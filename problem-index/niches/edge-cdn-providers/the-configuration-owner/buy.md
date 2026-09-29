# Traffic Replay and Shadow Evaluation

**Niche:** [[niches/edge-cdn-providers/the-configuration-owner/profile|The Configuration Owner]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Shadow traffic and replay testing are established practices for validating a change against real requests without affecting them, and CDN configuration is tested by deploying it.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #cross-validation #automation #workflow-orchestration
**Contested on:** Every serious competitor that takes this seriously is fighting to let the person who owns the rule set know whether a change helped — and whoever does that takes them, because without it the rule set only ever grows and nobody dares remove a line.

## The Problem
Running a proposed change against real traffic without affecting the response is shadow evaluation, and it is standard practice for validating service changes at scale. Replaying recorded traffic against a candidate configuration is equally established. The edge is the ideal place for both — it sees every request and can evaluate a second configuration cheaply — and configuration changes are validated by deploying them to a staging environment that receives no real traffic and then to production.

## What Already Exists
Shadow traffic and dark launch patterns with published descriptions; traffic replay tooling; request mirroring in proxies and service meshes; statistical comparison frameworks; and the experimentation infrastructure the edge already has for other purposes. The primitives exist in the edge software itself.

## The Customization Gap
The adaptation is to configuration evaluation rather than to code deployment. It requires: (1) evaluating a candidate configuration against live requests without serving its result, which is cheap at the edge — it is rule evaluation rather than a backend call — and produces a comparison of decisions rather than of responses; (2) comparing decisions rather than outcomes for the shadow case, since the candidate's caching decision can be compared to the current one without actually serving differently, and the projected hit rate follows; (3) replay against a recorded trace for the cases where the decision's consequence depends on state, which requires a trace with enough fidelity to reproduce key computation; (4) statistical treatment of the comparison, because traffic varies and a naive before-and-after over two hours mostly measures the time of day; and (5) a safety check for rules that would change behaviour in ways the customer did not intend, which is the specific fear that makes removal impossible and which a decision-level comparison answers directly.

## Target Customer
Edge and CDN providers, configuration management tooling vendors, and the platform teams maintaining large rule sets.

## Impact If Solved
The primitives are in the edge software already and the practice is established elsewhere, which leaves productisation as the gap. Decision-level shadow comparison is cheap and answers the question that makes rule removal frightening.
