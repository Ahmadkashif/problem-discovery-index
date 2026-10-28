# Payer Mix Nobody Models Before a Grant Is Withheld

**Niche:** [[niches/community-health-centers/title-x-family-planning-centers/profile|Title X & Independent Family Planning Centres]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** When a Title X award is withheld or a Medicaid payment bar takes effect, a family planning centre learns which sites and services lose money only as cash runs out.
**Tags:** #monte-carlo-methods #time-series-forecasting #descriptive-statistics #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to replace unstable grant dollars with insurer payments without breaking Title X confidentiality, and whoever bills the largest share of confidential visits to an insurer takes the account.

## The Problem
In 2025, 16 of 86 Title X grants had funds withheld for most of a year, and Medicaid payments to some providers were barred (search summary). Centres closed sites before knowing which could be kept open by billing insurers.

## Why It's Still Broken
Revenue reports show payer source after the fact. Nobody models each site's visits by payer, confidentiality need and grant dependence ahead of a funding shock.

## What a Fix Looks Like
A site-by-service model of revenue under scenarios: Title X lost, Medicaid barred, confidential billing enabled. It shows which visits could move to insurers and which sites depend on grants alone, updated monthly from the EHR.

## Who Feels the Pain
CEOs and boards deciding closures, and patients whose nearest site closes.

## Impact If Fixed
Knowing three months earlier that a site could cover 70% of its costs from insurer billing (estimate) is the difference between closing it and keeping ~5,000 patient visits a year.
