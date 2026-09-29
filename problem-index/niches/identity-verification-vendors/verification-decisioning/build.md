# A Decision With a Known Error Distribution

**Niche:** [[niches/identity-verification-vendors/verification-decisioning/profile|Verification Decisioning]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The gate to the financial system is a model whose error rates across populations nobody in the industry publishes.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #cnns #compliance #descriptive-statistics #causal-inference #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to confirm that a person is who they claim to be in seconds — and the contest splits cleanly enough that it is not terminal.

## The Problem
Passing verification is a precondition for a bank account, a payment app, a loan, a marketplace listing and increasingly a government benefit. The decision is made in seconds. Published evaluations have documented demographic differentials in face recognition error rates for years, older and less standard documents read worse than modern ones, and stable address histories resolve better than those of people who move often or have thin files. Every vendor holds the images, scores, outcomes and retry behaviour needed to measure their own distribution, and none publishes it.

## Why Nobody Has Built This
The measurement produces a number that is uncomfortable, so nobody wants to be first — and a metric that only creates exposure has no internal champion. Rejected applicants generate no outcome data, which makes the false reject rate genuinely harder to establish than the false accept rate. Customers buy on pass rate and conversion. And no regulator currently requires the disclosure.

## What to Build
Measure the distribution and build the decision around it. Measure error rates by document type, device, capture condition and, where lawful and appropriate, by the demographic groupings published evaluations already use — which is the core and is technically routine on data every vendor holds. Obtain ground truth on rejections through follow-up, manual adjudication and retry outcomes, since the missing labels are the real obstacle and are partially recoverable. Separate the vision decision from the data decision in the score, because they fail for different people and a blended score hides which. Encode the cost of a false reject explicitly, as a decision optimised only against fraud will always tighten and the person excluded is not in the objective. Report confidence intervals rather than point estimates, since subgroup sample sizes vary enormously and false precision is its own harm. Target improvement where errors concentrate, because a model improved on average can worsen for the groups already worst served. Publish the methodology and the results, since the vendor that produces the number first defines the standard everyone else is measured against. Support the customer in setting thresholds against their own population rather than a default. Monitor the distribution continuously as documents, devices and models change. And treat a person's inability to verify as a product failure rather than as an outcome, which is the framing that makes all of it coherent.

## Target Customer
Data science and policy leadership, regulated customers accountable for access, regulators and researchers, and every competitor publishing a pass rate.

## Impact If Built
A metric that only creates exposure has no internal champion, so nobody measures what is technically routine. The vendor that publishes its error distribution first defines the standard the rest of the category is then measured against.
