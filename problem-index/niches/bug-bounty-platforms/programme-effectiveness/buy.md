# Buy: Marketing Measurement Applied to Security Spend

**Niche:** Programme Effectiveness Measurement
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Marketing spent two decades learning to separate incremental effect from activity and to estimate saturation curves, and security budgets are still set on last year's number plus a percentage.
**Tags:** #causal-inference #bayesian-inference #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact
**Contested on:** Whether a programme can show that its spend bought security, or only that it bought submissions.

## The Problem

Deciding how much to spend on a channel, how much of the observed result that channel actually caused, and where returns start diminishing is a problem marketing has worked on intensively. The apparatus is well developed: incrementality testing, geographic and temporal holdouts, media mix modelling with saturation and adstock curves, and a mature scepticism about attributed conversions that would have happened anyway.

Security spend is allocated with none of it. A bounty programme's budget is set by what it spent last year, adjusted by how the year felt. Its reported results are attributed conversions in the marketing sense — submissions the programme received, with no counterfactual about whether the same weaknesses would have surfaced through another channel.

The parallel is closer than it first appears. Both are channels competing for a fixed budget against alternatives. Both report activity that correlates with spend by construction. Both have diminishing returns nobody measures. And both have a well-understood failure mode of crediting a channel for outcomes it did not cause.

## What Already Exists

Marketing measurement: media mix modelling platforms and open-source implementations with saturation and carryover curves; incrementality testing platforms; geographic holdout methodology; the extensive literature on attribution bias and the well-documented failure of last-touch attribution.

Causal inference generally: synthetic control methods, difference-in-differences and matched-market designs, all developed for exactly this question of what a spend caused.

Security-adjacent: risk quantification approaches such as FAIR, which model loss exposure in financial terms and are used for security budget allocation without any channel-level effectiveness input.

Platform reporting: the bounty platforms' own dashboards and peer benchmarking, which report activity comparably across programmes.

## The Customization Gap

**The outcome variable is rare and not directly observable.** Marketing measures conversions, which are frequent. Security wants to measure incidents, which are rare and confounded. The adaptation has to work with intermediate outcomes — novel findings, time-to-discovery, weakness classes reaching production — which is a substantive modelling change rather than a direct transfer.

**Holdouts are ethically and practically awkward.** Marketing runs geographic holdouts routinely. Deliberately excluding part of an estate from a security programme to measure the difference is a harder argument, though scope is already partial everywhere, which means natural variation exists and could be exploited rather than manufactured.

**Saturation curves need cross-programme data.** Media mix models estimate saturation from spend variation over time and across markets. A single bounty programme has too little variation; the platform's portfolio has plenty, which puts the modelling capability on the platform rather than on the customer.

**Channel comparison is the natural framing and nobody uses it.** Bounties, contracted testing, internal application security headcount and tooling are four channels buying the same outcome. Media mix modelling exists precisely to allocate across channels, and this allocation is currently made on intuition.

**Attribution scepticism has to be imported wholesale.** The most valuable thing marketing learned is that attributed results overstate incremental effect, often dramatically. Security has not yet had that reckoning and the bounty channel's reporting looks very much like last-touch attribution.

**FAIR gives the loss model and no effectiveness input.** Risk quantification can price what a weakness class would cost; combining that with channel effectiveness would produce an actual expected-value allocation, and the two halves have never been joined.

## Target Customer

The bounty platforms, for the portfolio-level saturation modelling that only they can do, and which would let them advise rather than merely report.

Security leadership at organisations spending meaningfully across several channels, who face the allocation question annually with no analytical basis.

A measurement specialist entrant sitting across channels would be more credible than any single platform, since a platform modelling its own channel's returns has an obvious interest in the answer.

## Impact If Solved

Two decades of hard-won scepticism about attributed results reaches an industry currently reporting activity as outcome, in almost exactly the form marketing used to.

Saturation estimation would tell programmes something none of them knows: whether their next dollar buys a novel finding or a duplicate, which is the central budget question.

And cross-channel allocation modelling would let a security leader defend a portfolio rather than defending each line item separately against the others — which is how the budget conversation actually happens and how it is currently least informed.
