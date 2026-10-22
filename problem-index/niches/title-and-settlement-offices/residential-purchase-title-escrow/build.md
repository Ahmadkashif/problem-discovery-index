# A Day-One Curative Forecast for Every Purchase File

**Niche:** [[niches/title-and-settlement-offices/residential-purchase-title-escrow/profile|Residential Purchase Title & Escrow]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A purchase file's curative workload is knowable the day the search comes back, yet offices discover it requirement by requirement over the following weeks.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to take a purchase file from open order to clear-to-close with every Schedule B-I requirement met before the contract closing date, and whoever scopes and clears curative fastest without a post-closing surprise wins the listing and buyer's agents who choose the title company.

## The Problem
The commitment lists the B-I requirements, but not how hard each will be. A payoff from a large servicer clears in days; a release of a 2004 second mortgage from a lender that failed in 2009 can take months; a deceased co-owner means probate or an affidavit of heirship; a municipal code lien means calling a city that answers once a week. Offices learn which kind of file they have when the closing date is already close.

## Why Nobody Has Built This
Production systems record requirements as text from a library and mark them satisfied; they do not record the clearance path or its duration in a form anyone has modelled. Individual agencies have too few files of each rare type, and the underwriters that see more volume are focused on claims, not cycle time.

## What to Build
At order open, read the search package and the draft commitment, classify each requirement by curative path, and predict its clearance time from the agency's own history and counterparty baselines (servicer, court, municipality, HOA). Produce a file-level probability of closing on the contract date and a list of the requirements that drive the risk, then start the curative requests for the long-lead items the same day. Each cleared requirement feeds back into the model.

## Target Customer
Multi-office agencies closing 200+ purchase files a month, where escrow managers allocate processors and want to protect agent relationships.

## Impact If Built
Long-lead curative starts on day one rather than in week three, fewer closings slip on the contract date, and the agency can show agents a track record of on-time closings — the metric agents actually choose on.
