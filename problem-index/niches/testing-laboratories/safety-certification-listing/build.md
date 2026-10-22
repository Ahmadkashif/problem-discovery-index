# Risk-Ranked Factory Follow-Up Inspections

**Niche:** [[niches/testing-laboratories/safety-certification-listing/profile|Safety Certification & Listing]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Certifiers visit every listed factory on roughly the same calendar, when a minority of factories and product types produce most of the non-conformities.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #feature-engineering #compliance
**Contested on:** Every serious competitor in this sub-niche is fighting to have its mark be the one retailers, insurers and inspectors ask for while running each listing's factory follow-up at the lowest cost to the manufacturer, and whoever's mark is demanded with the least disruptive follow-up keeps the product for its whole life.

## The Problem
A large certification body runs tens of thousands of factory follow-up visits a year (estimate). Each visit checks that critical components, markings and construction match the listing and may pull samples for retest. Visits are largely calendar-driven. Factories with a clean history get the same attention as factories that change suppliers monthly, and field representatives' time — the cost centre of the listing business — is spread evenly over uneven risk.

## Why Nobody Has Built This
The certifier holds the data — every visit, every variation notice, every retest failure — but it sits in operational systems built for scheduling and billing, and contractual and accreditation rules require a minimum visit frequency, which discourages anyone from modelling beyond it.

## What to Build
A model that predicts the probability of a non-conformity at the next visit from factory history, product category, component churn, ownership changes, recent standard revisions and field representative notes; uses it to rank visits within the required frequency and target which products to sample; and records the reasoning for the accreditation body.

## Target Customer
Heads of follow-up services at certification bodies and OSHA-recognised testing laboratories.

## Impact If Built
The same field force finds more non-conformities, low-risk manufacturers see less disruption — which is part of what the contest is about — and the certifier can evidence that its surveillance is risk-based.
