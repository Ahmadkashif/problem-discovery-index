# Measuring Click Rate on a Test You Set the Difficulty Of

**Industry:** [[security-awareness-training|Security Awareness Training]]
**Type:** High Impact
**One-liner:** The headline metric is performance on simulations the vendor and customer design, it improves reliably, and nobody has related it to whether anyone resists a real attack.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #survival-analysis #gradient-boosting #evaluation-metrics #compliance

## The Problem
A security awareness programme reports click rate on simulated phishing. It starts high, falls over the first year, and settles low. That trend is the product, and it is what leadership, auditors and insurers are shown.

The trend is partly an artefact of the instrument. Difficulty is chosen by the vendor's template library and the customer's configuration, and there is no external standard for what a difficulty-controlled click rate means. A programme that runs progressively more recognisable simulations, or that pre-announces campaigns, or that selects templates employees have seen before, will show the same improving line as one that genuinely built resistance.

Nothing links it to reality. The organisation runs an email security gateway that records what real phishing actually looks like when it arrives, has an incident record of actual compromises, and receives employee reports of real suspicious messages. The relationship between simulated performance and any of those is estimable and is estimated by nobody.

There are reasons to expect the relationship to be weak. Real attacks against a specific organisation are targeted, contextually plausible and timed; simulations are generic and scheduled. Resistance to a generic test may not transfer, and there is published academic work suggesting simulated click rates relate poorly to real susceptibility.

And the behaviour that actually protects an organisation is not click avoidance, it is reporting. A message that is clicked and reported immediately is far less damaging than one that is neither clicked nor reported and lands with three other people. Reporting rate is measured far less prominently and is the metric a programme should be optimising.

## Why It's Unsolved
The current metric improves reliably and the honest one might not, which is a complete explanation for the market's behaviour. Vendors sell an improving line; customers buy something that satisfies an auditor and reassures leadership; and a vendor that introduced difficulty control and outcome linkage would report worse numbers than competitors who did not.

Real compromise is rare, which makes outcome measurement statistically hard at any single organisation. That is an argument for cross-customer pooling, which a vendor is uniquely positioned to do and which raises the same confidentiality questions as every cross-customer corpus in this vault.

Attribution is genuinely difficult. A compromise that did not happen cannot be counted, and one that did may be attributable to a gateway failure, a targeted attack that would have caught anyone, or a control gap rather than to awareness. Disentangling that needs care.

And the intervention has known harms that the metric does not capture. Punitive programmes produce lower click rates and worse reporting cultures, so a category optimising the visible number can be actively degrading the outcome — and would not know.

## What a Solution Looks Like
Control difficulty. A calibrated difficulty scale, with templates rated on measurable properties — contextual plausibility, personalisation, urgency framing, sender legitimacy, presence of the cues training teaches — turns click rate into a comparable measure. Reporting click rate at fixed difficulty is the minimum standard for the number to mean anything.

Measure the real-world relationship. Within a large customer, employee susceptibility can be related to what actually happens: reports of real phishing, gateway-detected attempts against that individual, and incidents. Across customers, a vendor can pool it. Even a weak measured relationship is more than the field has, and a null result would be the most important finding in the category.

Optimise reporting, not click avoidance. Reporting rate, reporting speed and reporting accuracy are the behaviours that reduce harm, they are measurable, and they respond to programme design in ways click rate does not. A programme reporting them as primary would be measuring the thing that helps.

Measure the harms alongside. Trust in the security function, willingness to report mistakes and self-reported distress are measurable with light survey instruments, and a category that reported them would be able to distinguish programme designs that build resistance from ones that build silence.

## Impact If Solved
This is a multi-billion-dollar category whose central metric is performance on a test it designs, reported to auditors and insurers as evidence of resilience. Difficulty control makes the number comparable; real-outcome linkage tells the field whether any of it works; and shifting the primary metric to reporting aligns the programme with the behaviour that actually limits damage — while measuring the harms would let customers choose designs that do not achieve their numbers by making people afraid to speak.
