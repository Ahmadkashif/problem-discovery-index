# Enormous Spend on an Unmeasured Claim

**Niche:** [[niches/developer-tools-vendors/productivity-attribution/profile|Productivity Attribution]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The industry is committing enormous spend to coding assistants on demonstrations and enthusiasm, and neither vendors nor buyers can say what happened to throughput, defect rates or maintenance burden.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #cross-validation #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor here is fighting to attribute a change in engineering output to a specific tool or practice — and whoever does that credibly takes the category, because every purchase in it is justified by a claim nobody can currently substantiate.

## The Problem
A company rolls an assistant out to nine hundred engineers. Twelve months later the spend is up for renewal and the question is whether it worked. Deployment frequency is up eleven percent, and so is headcount. Pull request volume is up substantially, and review latency with it. Incident rate is flat. Developers say they like it. The vendor's case study cites acceptance rates. Nobody in the room can say whether the company is better off, and the renewal is decided on sentiment — which is how a large fraction of engineering budget is now allocated.

## Why Nobody Has Built This
The naive metrics are known to be bad, which produced a widely shared belief that measurement itself is the error — a defensible reaction to lines-of-code management that hardened into a norm against measuring at all. The rollouts are also designed to be unmeasurable: everyone gets the tool at once, because staging a rollout feels like withholding a benefit, which destroys the comparison before it exists. Vendors have no incentive to fund a rigorous answer. And the consequences that matter most — maintenance burden, defect rates in code written with assistance, comprehension of code nobody wrote by hand — surface over quarters rather than weeks.

## What to Build
Attribution built on design rather than on dashboards. Staged rollout as the default deployment pattern, with teams randomised or sequenced into cohorts, which costs the organisation a few weeks of delayed access and is the difference between an answer and an argument — and which a vendor could make the standard way its product is deployed. A measurement set that spans the trade-off rather than one side of it: throughput, review burden, defect and incident rates attributable to changed code, rework within thirty and ninety days, and maintenance cost on the code produced. Difference-in-differences and synthetic control methods over the cohorts, which handle the confounding that defeats before-and-after comparison. Long-horizon follow-up, because the maintenance consequence is the contested part and is invisible at three months. Honest reporting including nulls and negatives, since a measurement programme that only ever confirms the purchase will be recognised as marketing within a year. And a per-organisation answer rather than an industry one, since the effect plausibly varies enormously by codebase, language and team, and the buyer's question is about their own engineers.

## Target Customer
Engineering leadership and finance at organisations with material tooling spend; and the vendors with the confidence to be measured, for whom a credible effect is the strongest possible position in a category of unsubstantiated claims.

## Impact If Built
The category's central question is now an expensive one and remains unanswered by design rather than by necessity. Staged rollout is the whole unlock and costs almost nothing, and measuring the maintenance side is what distinguishes an honest answer from a flattering one.
