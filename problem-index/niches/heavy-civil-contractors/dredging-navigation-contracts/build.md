# Where the Government Estimate Will Land

**Niche:** [[niches/heavy-civil-contractors/dredging-navigation-contracts/profile|Dredging & Navigation Channel Contracts]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A dredging bid fails if it's over 125% of a sealed Corps estimate, and every past letting's bids and award are public, but no contractor models where that estimate is likely to fall.
**Tags:** #bayesian-inference #linear-regression #gradient-boosting #feature-engineering #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to have a DQM-certified dredge of the right type mobilised near the work when the Corps advertises, at a price under 125% of the government estimate, and whoever books the most working dredge-days a year at awardable prices takes the account.

## The Problem
The Corps' estimate is built with CEDEP, its own dredging cost program, and stays sealed until bid opening. A contractor that needs a high price, because its nearest suitable dredge is far away, doesn't know whether that price will be awardable. Unawarded lettings cost everyone a re-advertisement.

## Why Nobody Has Built This
The data is scattered across Navigation Data Center spreadsheets, SAM.gov awards and district bid abstracts. The government estimate is published unevenly. Dredging contractors are few and each relies on its own estimators.

## What to Build
A model of the government estimate and the low bid per letting, using quantity, material, placement distance, dredge type, region, season, district and the history of abstracts and awards. It reports the probability that a given bid is awardable and where the field will price. A two-week demo can run on public NDC abstracts and SAM.gov awards.

## Target Customer
Estimating heads at the ~56 firms that won Corps dredging work in FY2023, especially the 34 small businesses (DCA, via search summary).

## Impact If Built
If a contractor avoids one non-awardable bid and one under-priced win a year (estimate), it saves the re-bid effort and the loss on a job worth ~$10M–$50M (estimate). Fewer unawarded lettings also help the Corps.
