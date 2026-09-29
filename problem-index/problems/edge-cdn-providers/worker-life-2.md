# The Engineer Who Cannot Tell If It Is Working

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Type:** Worker Life Changing
**One-liner:** The engineer who owns the CDN configuration has no way to know whether a change improved anything, so the rule set accumulates and nobody dares remove a line.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #time-series-forecasting #gradient-boosting #evaluation-metrics #automation #worker-facing

## The Problem
Someone at every company owns the CDN configuration, usually as one responsibility among many. They inherited a rule set from a predecessor, a solutions engineer, or an incident three years ago.

They cannot evaluate it. A change to a cache rule affects hit ratio, origin load and user-perceived latency, and all three move constantly for unrelated reasons — traffic mix, a deployment, a marketing campaign, a regional network event. Making a change and looking at a dashboard afterwards tells you almost nothing, because the counterfactual is unobservable and the noise is larger than most effects.

So the rational behaviour is to change nothing. The rule set grows because adding an exception for a specific problem is safe, and shrinks never, because removing a line risks an outcome nobody can predict or measure.

The same applies to the bigger decisions. Is the security configuration blocking legitimate users? Would a longer time-to-live help? Is the bot challenge costing conversions? Each is answerable in principle and unanswered in practice, so the configuration is a monument to past incidents rather than a current design.

## Why It Matters to the Worker
Owning something you cannot measure is professionally uncomfortable. The engineer is accountable for performance and availability at the edge, and their only feedback is complaints — which arrive when something is wrong and never when something could be better.

It also makes them conservative in a way they can tell is suboptimal. They know the rule set contains dead weight and cannot prove which parts, so they carry it. That is a low-grade, permanent professional dissatisfaction.

And it makes the vendor relationship strange. The provider recommends changes, the engineer cannot verify whether previous recommendations helped, and so recommendations accumulate unactioned. The provider experiences this as low adoption and the engineer experiences it as reasonable caution.

## What a Solution Looks Like
Experimentation as a platform capability. A CDN is uniquely well placed to run a genuine split — the same change applied to a random subset of requests or clients, with the remainder as control — because it sits in the request path and can route deterministically. No customer can build this and the provider can offer it as a feature.

Effect measurement on outcomes that matter: real user latency, origin load, error rate and, where the customer permits, conversion. Reported with intervals, so a change with no detectable effect is reported as such rather than as a small improvement.

Rule inventory with evidence. Which rules have matched traffic, how often, and what would change if each were removed — which turns a monument into a maintainable artefact.

Recommendation with predicted effect and a way to test it, rather than an assertion, so a suggestion arrives as a hypothesis the engineer can evaluate cheaply.

And regression detection, so a change that degrades something is caught by the platform rather than by a complaint.

## Impact If Solved
CDN configuration is owned by people who cannot measure it, which is why rule sets only grow and why vendor recommendations go unadopted. Built-in experimentation is uniquely available to a provider sitting in the request path, and it is what converts edge configuration from accumulated folklore into engineering.
