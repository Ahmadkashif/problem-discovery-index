# Knowing Who You Actually Recruited

**Niche:** [[niches/player-research-firms/participant-sampling/profile|Participant Sampling]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The findings describe the players the game is for, and the participants are the people who answer screeners.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #causal-inference #probability-distributions #data-integration #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to generalise from whoever answered the screener and turned up, when those people are systematically not the people the game is for — and whoever fixes the sample takes the account.

## The Problem
Research participants are recruited from panels and communities and self-select into studies. They are more available, more interested in games research, and frequently more engaged than the population the game targets. The findings are then written as statements about players. The gap between the recruited sample and the target population is not measured, not reported, and not corrected, in a discipline that is otherwise careful.

## Why Nobody Has Built This
The target population is frequently not characterised anywhere, so there is nothing to compare against. Reaching under-represented participants costs more per head. Sample size is constrained by session cost regardless. And clients do not ask about representativeness.

## What to Build
Characterise the target, measure the gap and report it. Define the target player population explicitly with the client at kickoff, which is the core — a sample cannot be assessed against a population nobody has described. Compare recruited participants against that definition on the dimensions that matter for the research question, rather than on demographics alone. Measure and report recruitment funnel bias — who was screened out, who declined, who did not attend — since the losses are where the skew is created. Build recruitment routes into under-represented groups, as the panel is the bias and no amount of screening fixes it. Weight or stratify where the sample size allows, and say when it does not. State generalisability explicitly in the report rather than leaving it implied. Match the sample to the research question rather than to a generic profile, because different questions need different people. Track sample composition across a client's studies, which reveals a consistent skew nobody sees study by study. Use telemetry-derived population profiles where the client has them, which is the best available definition of the target. And report the sample honestly even when it is poor, which is the professional position and is currently softened.

## Target Customer
Games user research firms and platforms, in-house research functions, playtesting platforms, and participant recruitment providers.

## Impact If Built
A sample cannot be assessed against a population nobody has described, so the skew is never visible. Defining the target with the client and measuring the recruitment funnel makes generalisability a statement rather than an assumption.
