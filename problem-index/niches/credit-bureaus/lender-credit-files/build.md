# Retro Studies Run as a Product, Not a Project

**Niche:** [[niches/credit-bureaus/lender-credit-files/profile|Consumer Credit Files for Lending]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The test that allocates a lender's inquiry volume between bureaus is rebuilt by hand for every lender, and the bureau learns why it lost only after the volume has moved.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #hypothesis-testing #confidence-intervals #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to win the lender's retro study — the archive test in which each bureau's file and attributes are scored against the lender's own booked and declined applicants — and whoever shows the most lift on that population takes the account.

## The Problem
A lender considering a change of primary bureau sends each bureau a sample of past applicants. Each bureau returns archived files and attributes as of each application date, and the lender's analysts build models on each and compare separation, approval rates at constant loss and coverage of thin-file applicants. The process takes weeks, is run with different samples, horizons and metrics at every lender, and ends in a decision the losing bureau sees only as lost inquiries.

## Why Nobody Has Built This
Bureaus treat retro studies as sales support, staffed by analysts who rebuild the same work for each prospect. Lenders guard their performance data and want to run the test themselves. And the honest answer — where a bureau's file is weaker for a given population — is commercially uncomfortable to produce.

## What to Build
A standard retro harness: the lender uploads an archive sample under a defined protocol, and the bureau returns point-in-time attributes, a standard set of challenger models, lift at constant loss with confidence intervals, coverage diagnostics by segment, and an attribution of lift to data sources (trended data, alternative data, furnisher coverage). The same harness runs internally as a standing benchmark of where the bureau's file underperforms, by lender type and population.

## Target Customer
Heads of analytics and sales engineering at the nationwide bureaus; credit risk analytics leaders at lenders who run several retros a year.

## Impact If Built
Retros that take days rather than weeks (estimate), comparable across lenders, and a bureau that knows its weak segments before a competitor's retro tells the lender.
