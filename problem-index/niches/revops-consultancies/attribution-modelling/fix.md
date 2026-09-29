# The Model Changed and So Did the Budget

**Niche:** [[niches/revops-consultancies/attribution-modelling/profile|Attribution Modelling]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Fix (Pain Point)
**One-liner:** Switching from last-touch to multi-touch moved a fifth of the budget and nobody asked which allocation was right.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #confidence-intervals #causal-inference #revenue-impact #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to say which activities produced revenue, using a model whose output nobody has ever checked against a controlled test — and whoever validates it takes the account.

## The Problem
An organisation changes its attribution model. Channels that looked strong now look weak, budget moves accordingly, and teams are rewarded or penalised on the change. Nothing about the actual effectiveness of any channel changed — only the rule for assigning credit. The magnitude of the reallocation is the clearest possible evidence that the model is doing the deciding, and it is never presented that way.

## Why It's Still Broken
The model's output is reported as fact — an attributed number presented without the rule that produced it looks like a measurement, so nobody asks what would change under a different rule. Sensitivity is never shown. The new model is assumed better because it is newer. And the reallocation is attributed to insight.

## What a Fix Looks Like
Show the answer under several rules before deciding anything. Report channel contribution under first-touch, last-touch and multi-touch side by side, which is the fix and takes a query against data already held. Quantify how much budget allocation would change under each, which is the number that reframes the whole conversation. Show which channels are most sensitive to the rule, as those are the ones where the model is deciding rather than measuring. State the model's assumptions on the face of the report rather than in documentation. Flag channels with few tracked touches, where the model is weakest and most confident. Run one holdout on the largest channel, which is a single test with a large payoff. Keep reporting under the old model in parallel for a period after a change, so the shift is attributable. Record which model produced any historical figure, since comparisons across a model change are currently invalid and made anyway. Present contribution as a range across models rather than a point. And require a reason beyond novelty before changing the model.

## Who Feels the Pain
Teams whose budget moved because of a rule change; leaders reallocating on a convention; channels that are effective and unmeasurable; and the marketing spend, allocated by an unvalidated choice.

## Impact If Fixed
An attributed number presented without the rule that produced it looks like a measurement, so nobody asks what would change under a different rule. Reporting contribution under three rules side by side reframes the decision.
