# Player Evaluation That Survives a Patch

**Industry:** [[esports-organizations|Esports Organizations]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The roster is the largest controllable cost and is assembled on statistics that depend on patch, meta, role and teammates, and therefore do not transfer to the team doing the signing.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #graph-neural-networks #hypothesis-testing #transfer-learning #evaluation-metrics #causal-inference

## The Problem
Signing a player is the biggest financial decision an esports organisation makes, and the evidence is a set of in-game statistics from a different context. A player's kill participation, damage, economic efficiency or objective contribution are produced within a specific patch, a specific meta, a specific role assignment, alongside specific teammates, in a league of a specific strength. Change any of those and the numbers mean something else.

Patches are the sharpest version. Competitive titles are rebalanced regularly, sometimes substantially, and a player whose strengths matched the previous meta may not match the next one. Historical statistics spanning multiple patches are an average over incomparable conditions.

Teammate dependence is the subtler one. In team titles, individual statistics are strongly shaped by role allocation and by what teammates do — a player fed resources by a supportive structure produces numbers a player in a sacrificial role cannot, and the two may be equally valuable. Naive comparison systematically rewards the former.

So evaluation falls back on scouting relationships, coach judgement and reputation, which are real skills and are also how the sector repeatedly pays large sums for players who do not reproduce their form.

## What Already Exists
Publisher APIs and demo parsing give rich event-level data for major titles. Statistics sites — HLTV for Counter-Strike, Oracle's Elixir and similar for League of Legends, and title-specific equivalents — publish aggregated performance data and are widely used. Larger organisations employ analysts who build bespoke models. Coaching staff run film review and structured scouting. Some titles have established rating systems that attempt to normalise for context, with mixed acceptance.

## The Customisation Gap
The available statistics describe output, not contribution, and the adjustment for context is where all the difficulty lies. Separating a player's contribution from their role, their teammates, the patch and the league requires modelling the environment explicitly — a structure familiar from other sports analytics and applied unevenly here, largely because each title's data is different enough that nothing transfers between them and each requires its own build.

Patch-robustness is the title-specific problem worth solving. Evaluating a player on the characteristics that persist across metas — mechanical ceiling, decision speed, adaptation rate after a patch, versatility across roles — rather than on output within one meta, is what would make an evaluation transferable. Adaptation rate in particular is directly measurable from the weeks following each patch and is rarely computed.

Fit is the third gap and is where the money is lost. A signing's value depends on the team's existing structure and playstyle, and there is no model of synergy anywhere in the sector — rosters are assembled from individually-evaluated players and the team either works or does not.

And the evaluation needs uncertainty. Competitive samples are small, seasons are short, and a confident point rating on forty matches is overstating what the data supports, particularly for the younger players whose signings carry the most risk.

## Impact If Solved
Roster spend is the largest line in an esports organisation's budget and is committed on multi-year contracts against evidence that does not transfer. Context-adjusted contribution, patch-robust traits including measured adaptation rate, and an explicit model of fit would improve the single most consequential decision these organisations make — in a sector that no longer has the capital to absorb the mistakes it used to.
