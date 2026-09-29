# Build: Interpretable Results and a Batch Diagnosis

**Niche:** [[niches/crowdsourcing-platforms/the-requester/profile|The Requester]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Return labels with per-item uncertainty and a diagnosis of why the contested items were contested, instead of a flat file and a kappa.
**Tags:** #bayesian-inference #expectation-maximization #confidence-intervals #evaluation-metrics #hypothesis-testing #large-language-models #descriptive-statistics #tacit-knowledge-ml
**Contested on:** Whether the reasons for disagreement can be diagnosed and returned in a form a non-specialist can act on.

## The Problem

A requester downloads their results: one row per item, one label per item, plus an agreement statistic somewhere in the summary. From this they must decide whether the data is usable.

They cannot. A kappa of 0.62 could mean a competent crowd on a genuinely hard task, a mixed crowd on an easy one, or clear instructions with three ambiguous categories. Each implies a completely different action — use the data, filter it, rewrite the instructions and rerun, or restructure the task — and nothing distinguishes them.

Most requesters are not annotation specialists and have nobody to ask. So they use the data as delivered, or discard the batch and blame the crowd, and in a meaningful share of cases the problem was their own instructions.

## Why Nobody Has Built This

Platforms deliver raw responses because that is what the transaction is, and the interpretation is treated as the requester's business. The methods that would improve it are in the crowdsourcing and psychometrics literature and have not crossed into platform practice.

There is also a mild disincentive: a diagnosis frequently concludes that the requester's task design was the problem, which is a less comfortable message than one about crowd quality — though it is the message that produces a better rerun and a repeat customer.

And the requester population is fragmented, one-off and non-specialist, so nobody has represented its interests in platform product decisions.

## What to Build

An aggregation and diagnosis layer over the raw responses.

**Return labels with uncertainty.** Not a majority vote but a posterior from a joint model of worker ability and item difficulty, with a per-item confidence. The requester can then filter by confidence, weight by it, or examine the contested items — all of which are better than treating every label as equally certain.

**Flag contested items and say why.** Structured disagreement along an interpretable line means ambiguity; random disagreement means difficulty or noise; disagreement concentrated among low-ability workers means a quality issue. These are distinguishable from the response matrix and they imply different actions.

**Diagnose the batch.** A short report: your agreement is X, which for this task type is at the Yth percentile; the disagreement concentrates in categories B and C; the boundary between them appears to be read two ways, here are five examples; your pay implied Z per hour, which predicts the attention level you received; your qualification excluded W% of the pool. Each finding with a recommended action.

**Compare to a reference.** Agreement statistics are meaningless without a benchmark. Percentile against comparable task types on the platform is the reference every requester needs and none has.

**Recommend the rerun.** Where the diagnosis points at instructions, generate the specific rewording with the ambiguity resolved. A requester who receives a diagnosis and a fix will rerun; one who receives a statistic will move on and use the data.

**Teach through the interface.** The requester population is non-specialist, one-off and will not read documentation. Guidance delivered in context, on their own batch, with their own examples, is the only form that reaches them.

## Target Customer

Platforms serving academic and ML requesters, where data quality is the purchase criterion and where a diagnosis is a strong differentiator. Also the annotation tooling vendors, and research infrastructure providers serving the academic segment directly.

## Impact If Built

The requester learns what their agreement statistic means and what to do about it, with the specific items and the suggested rewording. Ambiguous items get preserved as a finding rather than averaged away. And the requester-side errors that generate most of the harm to workers — unclear instructions, misjudged pay, indiscriminate rejection — get caught by the person who can fix them.
