# Buy: Pricing and Estimation Tooling Adapted to Task Duration

**Niche:** [[niches/crowdsourcing-platforms/pay-setting-and-rate/profile|Pay Setting & the Realised Rate]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Effort estimation and pricing guidance exist in project software and marketplace pricing tools; neither predicts how long a stranger will take on a task designed by someone else.
**Tags:** #gradient-boosting #confidence-intervals #evaluation-metrics #descriptive-statistics #time-series-forecasting #data-integration #automation #revenue-impact
**Contested on:** Whether estimation tooling from other domains helps with a duration the platform can simply measure.

## The Problem

Estimation and pricing guidance exist in several forms. Project management tools offer effort estimation from historical task data. Marketplaces provide pricing suggestions from comparable listings. Survey platforms estimate completion time from question count.

None of them addresses the specific structure here, which is that the platform has millions of precisely measured completion times for tasks of known composition, and the requester setting a price has none of that information. This is not an estimation problem in the usual sense — it is a disclosure problem with a small modelling component, and the tooling from other domains is aimed at the modelling.

## What Already Exists

Project estimation features in work management platforms. Marketplace pricing suggestion engines. Survey platform completion time estimators, which use question counts and are crude. A/B and pricing experimentation tools. The platform's own completion telemetry, which is the actual asset and is not exposed anywhere.

## The Customization Gap

**The data is measured, not estimated, and nothing exposes it.** Survey tools estimate from question count because they have no timing data. The crowdsourcing platform has the actual distributions. The adaptation is almost entirely an exposure and interface problem rather than a modelling one, which is the opposite of what the tooling category assumes.

**The designer's time is systematically unrepresentative.** Estimation tools frequently anchor on the creator's own trial run. Here that is the single most misleading input available, and the design should avoid it rather than solicit it.

**Unpaid time belongs in the denominator.** Instruction reading, qualification tests and abandoned attempts are the worker's cost and appear in no estimation framework. Including them changes the number materially and requires joining several telemetry sources.

**The output is a rate with an ethical reference, not a price suggestion.** Marketplace pricing engines suggest a price that will sell. Here the useful output is the implied hourly rate compared to a floor, which is a different framing and one that a pricing engine optimising for conversion will never produce.

**The distribution matters more than the point estimate.** Some tasks have a long tail of slow completions, frequently the careful workers. A median-based rate understates their position, and showing the distribution — what the slowest quartile earns — is what makes the disclosure honest.

## Target Customer

Crowdsourcing platforms building a requester pricing experience, and the survey and research platforms serving the academic segment, where ethics compliance makes the implied rate a required artefact. Also worker-tooling builders, who currently approximate this from community data.

## Impact If Solved

The estimation and pricing interface patterns get reused, and the measured-duration exposure, designer-time avoidance, unpaid-time inclusion, ethical reference framing and distributional honesty get built. Concretely: a pricing screen that tells the requester the rate they are setting, from data the platform has always had.
