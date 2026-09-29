# Build: Does the Simulation Predict Anything

**Niche:** Programme Outcome Measurement
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Join simulation results to gateway telemetry, real reporting and incident records — inside a customer and across an installed base — and establish whether simulated performance predicts real resistance.
**Tags:** #causal-inference #logistic-regression #bayesian-inference #evaluation-metrics #confidence-intervals #survival-analysis #hypothesis-testing #data-integration
**Contested on:** Whether simulated performance predicts resistance to real attacks.

## The Problem

The category's central claim is that the programme makes a workforce more resistant to phishing. The evidence offered is that click rates on the programme's own tests fall.

The claim is testable and the test has not been run. Three datasets sit alongside each other inside every large customer.

The simulation platform knows who clicked what and when. The email gateway knows which real phishing arrived, who it was sent to, which was delivered past the filters, and in many deployments whether links were clicked. And the incident record knows which compromises occurred and how the attacker got in.

Joining them answers the question directly. Do people who click simulations also interact with real phishing? Does an improving organisational click rate correspond to fewer successful compromises? Does the reporting rate on simulations predict the reporting rate on real messages, which is the behaviour that actually helps?

Incidents are rare inside one organisation, which limits what a single customer can establish. A vendor with tens of thousands of customers has no such limitation, and is the only party who could answer it convincingly.

## Why Nobody Has Built This

**The current metric improves reliably and the real one might not.** This is the central reason and it is not subtle.

**The join requires customer telemetry.** Gateway and incident data sit with the customer and would need to be shared or processed under clear terms, which is an integration and a governance project.

**Incidents are rare per customer.** The single-customer version is underpowered, which is a real limitation and also the argument for the cross-customer study nobody has run.

**Attribution is genuinely hard.** Compromises fall when awareness improves, when the gateway improves, when attacks shift elsewhere, or when the organisation changes. Isolating the programme's contribution requires a design nobody has attempted.

**No customer or regulator asks.** Insurers accept the programme as a control, auditors accept completion, and nobody in the chain has ever required evidence of effect.

**A negative result would be difficult.** If simulated performance turns out to predict little, the category's core claim is undermined — which is the most important finding available and the least welcome.

## What to Build

**Start with the reporting correlation.** Does simulation reporting rate predict real reporting rate? Both are frequent enough to be well powered inside a single large customer, both are behaviours rather than failures, and the join is straightforward. This is the tractable first study and it is informative either way.

**Join simulation results to gateway interaction data.** Where the gateway records interaction with delivered real phishing, the individual-level correlation with simulation behaviour is directly estimable and is the sharpest available test.

**Run the cross-customer study.** With a large installed base, incident rates against programme characteristics — maturity, difficulty, cadence, punitive design — with the organisational confounders modelled. Only a vendor can do this and it would be the category's first outcome evidence.

**Compare programme designs, not just presence.** The more useful question is which designs work: reporting-focused versus click-focused, punitive versus supportive, spaced versus annual. Variation across customers supplies the natural experiment.

**Use the anchored difficulty scale.** Outcome research on an uncalibrated metric is worth little, so this depends on the calibration work in [[niches/security-awareness-training/difficulty-calibration/profile|🎯 Difficulty Calibration]].

**Publish honestly, including nulls.** The credibility of any result depends on the nulls being published, and a vendor publishing a partial or self-serving finding would be correctly discounted.

**Structure it as research with external collaborators.** A vendor evaluating its own product's efficacy needs independence to be believed, and academic collaboration is the obvious route.

## Target Customer

Vendors with large installed bases, who are the only parties able to run the cross-customer study and for whom a credible positive result would be the strongest claim in the category.

Cyber insurers, who accept awareness programmes as a control, price them without evidence, and have both the outcome data and the strongest interest in knowing whether it works.

Security leadership at large organisations, who could run the reporting-correlation study inside their own environment and would learn something immediately.

## Impact If Built

The category's central claim becomes testable, and it is testable with data every customer already holds.

The reporting correlation is the tractable first study — well powered, straightforward to join, and informative regardless of the result.

And comparing programme designs rather than presence would answer the question that matters most to a practitioner: not whether to run a programme, but which kind to run — which is currently decided entirely by vendor convention.
