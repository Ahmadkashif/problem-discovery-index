# The Health Score Nobody Has Validated

**Niche:** [[niches/crm-platforms/customer-success-post-sale/profile|Customer Success & Post-Sale]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Health scores are configured by choosing inputs and weights in a settings screen, they drive account prioritisation across the whole customer success organisation, and almost nobody has checked whether they predict anything.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #logistic-regression #cross-validation #quick-win #automation
**Contested on:** Every serious competitor in customer success software is fighting to identify a renewal at risk early enough that intervention still works — and whoever predicts churn with real lead time takes the account.

## The Problem
The health score is 40% product usage, 25% support ticket volume, 20% executive engagement and 15% survey response, with thresholds at 70 and 40. Those numbers were chosen in a workshop two years ago. Since then the organisation has had several hundred renewal outcomes, which is more than enough to check whether the score separates the accounts that renewed from the ones that did not. Nobody has run the check. The score prioritises the whole team's attention, appears in board reporting, and has never been tested against the outcome it claims to predict — and in some organisations that have quietly checked, it turns out that ticket volume, weighted as a negative, is positively associated with retention, because engaged customers file tickets.

## Why It's Still Broken
Validation requires joining scores as they were at a point in time to outcomes months later, and the score is stored as a current value that is overwritten — the same snapshot problem as the sales forecast. Nobody owns the question: the platform vendor supplies a configurable score and treats the configuration as the customer's business, and the customer treats the score as the vendor's product. And a validation that shows the score does not work invalidates a lot of accumulated process, which is a finding with organisational consequences.

## What a Fix Looks Like
Snapshot the score and check it. Retain the score and its components at regular intervals, then compare against the renewal, expansion and churn outcomes that follow. Report the discrimination — does a red account churn more often than a green one, and by how much — and the calibration, and do it per component so the organisation learns which inputs carry signal and which are noise or worse. Report lead time explicitly: at what point before churn did the score first turn red, distributionally, which is the property the score is actually for. Where a component turns out to be inverted, say so plainly rather than quietly reweighting, because the belief behind it is probably operating elsewhere in the organisation's practice too. The validation is a query over snapshots and a logistic regression, and it is the cheapest possible correction to a heuristic that currently directs an entire function's attention.

## Who Feels the Pain
Customer success managers prioritising accounts by a score nobody has tested; leaders reporting a health distribution to a board as though it meant something; and the customers in accounts the score calls green while they are leaving.

## Impact If Fixed
Score validation costs a snapshot job and an afternoon of analysis and frequently shows that a major component is uninformative or inverted. Correcting it redirects the attention of the entire function, which is worth more than any improvement to the playbooks that attention feeds into — and it establishes the measurement discipline the learned model in the build note has to be judged against.
