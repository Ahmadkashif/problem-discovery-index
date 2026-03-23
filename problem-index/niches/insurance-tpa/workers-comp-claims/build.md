# Predictive Claim Severity Scoring at First Notice of Loss

**Niche:** [[niches/insurance-tpa/workers-comp-claims/profile|Workers' Comp Claims TPA]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product today scores incoming workers' comp claims at FNOL to predict total incurred cost and litigation probability within the first 24 hours.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
When a workers' comp claim is filed, examiners manually review the initial report and assign it to a handling track. High-severity claims that receive standard handling in the first 48 hours cost 3-5x more to resolve than those triaged early. Current systems assign claims based on simple rules (body part, injury type) that miss the multivariate patterns — claimant demographics, employer history, provider network, day-of-week, and description language — that experienced examiners intuitively weight.

## Why Nobody Has Built This
Training data requires linking FNOL intake fields to final claim outcomes, which means 3-5 years of closed-claim history with consistent data capture. Most mid-market TPAs have fragmented data across system migrations, and large TPAs treat their predictive models as proprietary competitive advantages rather than productizing them.

## What to Build
A standalone scoring API that ingests structured FNOL data (injury type, body part, claimant age, employer industry, treating provider, claim description text) and returns a severity score (estimated total incurred) plus a litigation probability. Integrates via webhook with any claims management system. Dashboard shows score distribution, model confidence, and recommended handling track.

## Target Customer
Mid-market TPAs processing 5,000-50,000 workers' comp claims per year who lack data science teams but have 3+ years of historical claim data.

## Impact If Built
Reduces average claim cost by 12-18% through early intervention on high-severity claims. A TPA handling 20,000 claims at $15,000 average incurred could save $36M-$54M annually for their clients.
