# Build: Difficulty as a Measured Parameter

**Niche:** Difficulty Calibration
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Estimate template difficulty and individual susceptibility jointly from response data, anchor the scale to real received phishing, and report an ability estimate instead of a raw click rate.
**Tags:** #bayesian-inference #maximum-likelihood-estimation #evaluation-metrics #confidence-intervals #logistic-regression #hypothesis-testing #automation #data-integration
**Contested on:** Whether a simulation's difficulty is a measured property, so that click rates can be compared.

## The Problem

A person clicks a simulated phishing email. What does that tell you?

It depends entirely on the email. A crude message with a misspelled sender and an implausible pretext tells you a great deal. A well-crafted message referencing a real internal system, apparently from a colleague, arriving during a busy afternoon, tells you almost nothing about that person relative to anyone else.

The platform records both as a click. The individual is placed on the same list, assigned the same training, and counted the same way in the organisation's click rate.

The same confusion runs upward. An organisation's click rate is the average over whatever templates were sent, so two organisations with the same number may have very different workforces or very different campaign designs. A programme's trend over time mixes any real change with whatever drift occurred in campaign difficulty. And a vendor's published benchmark averages across customers running different tests.

All of this is exactly the problem educational testing solved. The response data these platforms hold — who saw which template and what they did — is precisely the input item response theory consumes, and it is used to compute an average.

## Why Nobody Has Built This

**The uncalibrated number is more flattering.** Calibration would separate genuine improvement from difficulty drift, and some of the improvement in most programmes is drift.

**Benchmarks would become harder to publish.** A calibrated scale reveals that current benchmarks compare different tests, which removes a sales asset.

**Individual susceptibility estimates are sensitive.** A model estimating each employee's susceptibility is a more accurate and more uncomfortable artefact than a list of who clicked, and its use would need careful governance.

**Cross-customer calibration raises data questions.** The strongest calibration uses response data across customers, which requires clear contractual basis.

**It requires a discipline the category does not have.** Psychometrics is not a capability these vendors were built with, and the value of acquiring it is not obvious to a product team whose metric already improves.

**Nobody is asking.** No customer, auditor or insurer has ever asked whether the difficulty scale is calibrated.

## What to Build

**Fit an item response model to the existing data.** Template difficulty and individual susceptibility estimated jointly from response patterns. The data exists at scale and the method is standard.

**Report ability, not click rate.** A workforce susceptibility estimate on a stable scale, comparable across campaigns and years regardless of which templates were used. This is the product of the whole exercise.

**Maintain a calibrated item bank.** Templates with estimated difficulty parameters, re-estimated as data accumulates, with exposure tracked so an overused template's degradation is visible.

**Control exposure deliberately.** A template seen repeatedly in an organisation stops measuring anything. Testing has managed this for decades and the practice transfers directly.

**Anchor the scale to real phishing.** Characterise the organisation's actually-received phishing and place it on the same difficulty scale, so the programme can say whether it is testing at, above or below the real threat level.

**Separate susceptibility from exposure in individual results.** A person who clicked a hard template is not equivalent to one who clicked an easy one, and the current list treats them identically. This matters directly to the employee described in [[niches/security-awareness-training/the-employee-who-clicked/profile|🟣 The Employee Who Clicked]].

**Publish the methodology and the scale.** A calibrated scale is only useful if it becomes a standard, and the vendor that publishes first defines it.

## Target Customer

Vendors positioning on rigour, for whom calibrated difficulty is a defensible product claim and the first real measurement in a category that has none.

Cyber insurers and auditors, who accept awareness programmes as a control and currently cannot distinguish a rigorous programme from a comfortable number.

Large security organisations, who run these programmes at scale and would immediately use an ability estimate that survives a change of vendor.

## Impact If Built

The category acquires a comparable metric, which is the precondition for benchmarks, for trend claims and for any outcome research.

Separating individual susceptibility from template difficulty would make the individual results fairer and more accurate, which matters because those results are used to assign training and sometimes worse.

And anchoring the scale to real received phishing would tell every programme whether it is testing against the threat or against its vendor's template library.
