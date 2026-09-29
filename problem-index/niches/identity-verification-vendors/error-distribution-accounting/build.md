# Producing the Uncomfortable Number

**Niche:** [[niches/identity-verification-vendors/error-distribution-accounting/profile|Error Distribution Accounting]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The measurement is routine, the data is in hand, and the reason it does not exist is that the answer will be uncomfortable.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #causal-inference #cross-validation #concentration-inequalities
**Contested on:** Every serious competitor in this niche is fighting to be the first to publish how its error rates are distributed across the populations it decides about — and whoever produces that number defines the standard everyone else is then measured against.

## The Problem
Verification is the gate to the financial system, and how often it wrongly excludes people — and which people — is not published by anyone in the industry. Public face recognition evaluations have documented demographic differentials across algorithms for years, and the other stages of the pipeline add their own: document age, device quality, address stability, file depth. Each vendor could compute its own distribution this quarter from data it already holds.

## Why Nobody Has Built This
The number will be uncomfortable and there is no competitive benefit to being first with bad news, which is a coordination problem rather than a technical one — every participant is better off if nobody measures, until one of them does. Rejections produce no outcome, so the false reject rate needs deliberate ground truth work. Collecting demographic data raises legitimate privacy questions that need answering rather than avoiding. And no customer or regulator currently requires it.

## What to Build
Measure honestly and publish. Obtain ground truth on rejections through follow-up, alternative-path outcomes and manual adjudication, which is the core dependency — without it the false reject rate stays an estimate. Disaggregate by the attributes that drive error: document type and age, device class, capture condition, address tenure, file depth, and the demographic groupings public evaluations already use, handled under an explicit privacy basis. Report confidence intervals and sample sizes honestly, since small subgroups produce unstable estimates and false precision is its own harm. Separate the pipeline stages, because knowing whether exclusion comes from capture, matching or data resolution determines the remedy. Compare against the customer's own applicant population rather than a vendor benchmark. Establish a methodology that others can follow and critique, as a standard is more valuable than a single result. Invite independent verification, since a self-reported fairness number carries limited weight. Target improvement where errors concentrate and report the movement, which turns measurement into a product programme. Handle the demographic data question properly — inferred, self-reported or proxied, each with different validity — and state which was used. And publish regularly rather than once, because a single disclosure is a press release and a series is a standard.

## Target Customer
Data and policy leadership, institutions accountable for access, regulators and researchers, and every competitor whose distribution remains unpublished.

## Impact If Built
Every participant is better off if nobody measures, until one of them does — which is a coordination problem, not a technical one. The data is in hand and the method is routine, and publishing first sets the standard the rest of the category is measured against.
