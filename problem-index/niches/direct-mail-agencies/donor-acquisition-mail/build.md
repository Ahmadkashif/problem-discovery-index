# Second-Gift Models for Acquisition Selection

**Niche:** [[niches/direct-mail-agencies/donor-acquisition-mail/profile|Donor Acquisition Mail]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Acquisition lists are chosen for the probability that a name gives once; the client needs the probability that it gives twice.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find first-time donors who go on to give a second gift, at an acquisition cost the client can recover from that later giving — and whoever predicts second-gift donors rather than first-gift responders takes the account.

## The Problem
A nonprofit's acquisition plan ranks sources by cost per new donor. Sources that attract one-time responders to a premium or an emergency appeal rank well, and the housefile later fills with donors who never give again. The agency sees the first-gift result within weeks; the second-gift result arrives a year later and is rarely tied back to the source.

## Why Nobody Has Built This
Second-gift labels take ~12–18 months to mature (estimate), sit in the client's CRM rather than the agency's campaign files, and differ by organisation. Co-ops optimise what their members ask for, which is response.

## What to Build
A model trained on the nonprofit's own acquisition history — source, list select, package, premium, first-gift amount and channel — predicting the probability and timing of a second gift, with survival methods so recent cohorts count. Score candidate sources and co-op deciles on expected net value per piece over two years, and use it to set the next season's quantities.

## Target Customer
Acquisition strategists at fundraising agencies and directors of acquisition at nonprofits mailing 250,000+ acquisition pieces a year (estimate of the threshold where the data supports a model).

## Impact If Built
Shifting volume toward sources whose donors stay raises the number of retained donors per acquisition dollar, the measure that decides whether the programme is worth running.
