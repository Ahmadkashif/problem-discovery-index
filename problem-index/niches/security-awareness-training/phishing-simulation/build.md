# Build: A Simulation That Measures Something

**Niche:** Phishing Simulation
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Simulations with objectively calibrated difficulty anchored to the real phishing an organisation receives, designed within stated harm limits, producing a click rate that is comparable over time and between organisations.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #logistic-regression #bert #compliance #worker-facing
**Contested on:** Whether the simulation is a measuring instrument or a number the vendor and customer jointly produce.

## The Problem

A programme reports that click rate fell from thirty per cent to four per cent over eighteen months. Everyone treats this as learning.

It might be. It is also what happens if the campaigns got easier, if the templates became recognisable through repetition, if the sender domains were whitelisted so messages arrived looking different, if employees learned to recognise the simulation platform rather than phishing, or if the campaigns were quietly pre-announced to reduce complaints.

Nothing in the programme distinguishes these. Difficulty is a label the vendor applies to a template, not a measured property. Two campaigns labelled the same may differ enormously. Two organisations with the same reported click rate may be running completely different tests. And published industry benchmarks compare numbers produced by incomparable instruments.

The second half is design. The lures that produce the strongest responses exploit real anxiety about money, employment and health, and using them has repeatedly caused genuine distress and public controversy. So the programme faces a trade nobody has characterised: the most discriminating tests are the most harmful ones, and nobody has established what discrimination is available within acceptable limits.

The data to resolve both is in the platform. Millions of responses across templates, organisations and populations, which is exactly the dataset item response theory was built for.

## Why Nobody Has Built This

**The uncalibrated metric improves reliably.** A number that reliably goes down is a good number commercially, and calibration risks revealing that some of the improvement was the test.

**Difficulty labelling is a product feature, not a measurement.** Vendors label templates to help customers choose, not to make campaigns comparable, and nobody has asked for comparability.

**Benchmarks are a marketing asset.** Published industry click rates are a sales instrument, and acknowledging that they compare incomparable tests undermines them.

**Anchoring to real phishing requires the customer's gateway data.** The organisation's email security records the real attempts, and joining that to simulation design is an integration nobody has built.

**Harm measurement produces bad news.** A vendor reporting distress and complaint rates from its own campaigns has generated a number no competitor reports.

**The effective lures are the harmful ones.** The trade is real, which makes it uncomfortable to characterise, and the honest answer may be that some discrimination has to be given up.

## What to Build

**Calibrate difficulty from response data.** Item response theory estimates item difficulty and respondent ability jointly from response patterns, which is exactly this problem. A template's difficulty becomes a measured parameter rather than a label, and a person's susceptibility becomes an estimate separable from which templates they happened to receive.

**Anchor to real phishing.** Sample the organisation's actual received phishing from the gateway, characterise its sophistication, and design campaigns at comparable difficulty. This turns the simulation into a proxy for the real threat rather than for the vendor's template library.

**Report ability, not click rate.** With calibrated difficulty, the reportable quantity is the workforce's estimated ability, which is comparable across campaigns and across time in a way a raw click rate is not.

**Set and publish harm limits.** Categories excluded — compensation, employment status, health, bereavement, family — stated as policy, applied by default, with deviation requiring explicit approval. The controversies in this category have followed a recognisable pattern and it is entirely avoidable.

**Measure the harm.** Complaint rates, distress reports, and survey measures of trust in the security function, tracked per campaign. A vendor that reports these is offering something no competitor does and would be able to say which designs achieve discrimination without damage.

**Standardise notification and consent practice.** Workforce notification that simulation occurs, its purpose, and how results are used. This is standard in research ethics and varies arbitrarily here.

**Measure the reporting rate as the primary metric.** The behaviour that helps an organisation is reporting a suspicious message. Reporting rate is a positive metric, is not gameable by making tests easier, and rewards the behaviour that matters.

## Target Customer

Security leadership at organisations that have had a simulation controversy, or that have works councils or employee representation asking questions — both populations are growing.

Vendors positioning on rigour, for whom calibrated difficulty is a genuine product claim and the first defensible measurement in the category.

Cyber insurers, who accept awareness programmes as a control and currently cannot distinguish a rigorous programme from one producing a comfortable number.

## Impact If Built

The headline metric becomes a measurement rather than a joint production, which is the precondition for anything else in this category meaning anything.

Anchoring difficulty to the organisation's real received phishing makes the simulation a proxy for the actual threat rather than for a template library.

And measuring the reporting rate rather than the click rate would reward the behaviour that actually helps, which is the change most likely to improve outcomes and the least likely to be gamed.
