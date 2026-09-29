# Outcomes Measurement Adapted to a Benefit Nobody Is Assigned To

**Niche:** [[niches/gyms-independent/fitness-benefit-network-analytics/profile|Fitness Benefit Network Analytics]]
**Industry:** [[industries/gyms-independent|Independent Gyms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard programme evaluation assumes an intervention someone was assigned to, and a fitness benefit is one people opt into precisely because they were already going to use it.
**Tags:** #causal-inference #hypothesis-testing #logistic-regression #evaluation-metrics #compliance

## The Problem
Every renewal turns on a version of the same claim: members who used the benefit cost less than members who did not. It is almost always calculated as a straight comparison of the two groups, and it is almost always wrong in the same direction. People who join a gym benefit are healthier, more motivated, and more engaged with their health than people who ignore it — before they take a single class. The comparison measures who signed up, not what the benefit did.

Sophisticated buyers know this. Health plan actuaries have been discounting wellness ROI claims for years, and the discount they apply is larger than the effect most programmes could plausibly have. The result is a market where the analysis carries less weight each cycle because nobody believes the method.

## What Already Exists
Causal inference is a mature field with mature tooling: propensity score methods, difference-in-differences, instrumental variables, regression discontinuity, and the modern machine-learning estimators for heterogeneous treatment effects, all available in well-tested open-source packages. Clinical outcomes research uses them routinely.

## The Customization Gap
The methods exist; the adaptation to this setting does not.

**Selection is the whole problem, and it is on an unobserved variable.** Motivation is what drives both enrolment and the outcome, and it appears in no claims file. Propensity matching on age, sex, region, and prior claims does not touch it. What this setting has instead, and clinical research usually does not, is a rich behavioural pre-period — the network sees how a member engaged with the benefit before the outcome window, and that engagement pattern is a far better proxy for motivation than any demographic.

**The natural experiments are specific to benefit design.** Networks are added mid-year, facilities enter and leave, eligibility rules change at plan boundaries, and geographic coverage is uneven. Each of those is an identification strategy — a plausibly exogenous change in access that is not a change in the member. A generic evaluation platform has no idea these exist; the network's own operations calendar is a list of them.

**Dose, not enrolment, is the treatment.** Almost every study in this space compares enrolled to not-enrolled. The interesting question is whether visits three through twelve did anything, which is a dose-response problem with the same selection issue at every level of dose.

**The output has to survive an actuary.** A plan's actuarial team will read the method section. That means pre-specification, sensitivity analysis, and honestly reported bounds — closer to a regulatory submission than a marketing deck, and nothing off the shelf produces that shape.

## Target Customer
Head of Outcomes Research or VP of Analytics at a fitness benefit network, particularly one selling into Medicare Advantage, where the plan's own quality and cost incentives make the question sharper.

## Impact If Solved
A number the buyer believes. The current claim is discounted to near zero by the people who matter, which means the analysis costs money and moves nothing. A defensible causal estimate — even a smaller one — is worth more than an inflated correlational one, because it can be used in a bid.
