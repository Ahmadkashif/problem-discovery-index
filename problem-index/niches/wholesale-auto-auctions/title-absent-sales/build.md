# A Title-Risk Score at Check-In

**Niche:** [[niches/wholesale-auto-auctions/title-absent-sales/profile|Title-Absent & Title-Defect Sales]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The auction learns a title will be late only after the car has sold, when the cheapest fixes (announce it, require the payoff, hold the car) are no longer available.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to get a negotiable title from seller to buyer before the auction's title window lets the buyer hand the car back, and whoever has the fewest title-related sale cancellations per thousand units sold takes the account.

## The Problem
At check-in the auction records whether the title is present. It does not estimate how long an absent title will take. A dealer trade with a local bank lien and an electronic title clears in days. An out-of-state fleet unit with a paper title held at headquarters can take weeks. A lender's repossession waiting on a state's repossession title process can take longer.

## Why Nobody Has Built This
Title events are timestamped but rarely modelled, and lienholder names are messy free text. The title department works the queue after the sale. Check-in staff do not see title outcomes.

## What to Build
A time-to-title model run at check-in. Its inputs are seller type and history, lienholder (normalised), issuing state and ELT status, whether the payoff is requested, and the vehicle's title history. The output is a predicted days-to-title and breach probability for the auction's window, with actions by band: announce title-absent, require payoff confirmation before the car runs, or hold it for a later sale. Seller scorecards go to account managers monthly.

## Target Customer
Title department managers and operations VPs at auction chains; commercial consignors with recurring title delays.

## Impact If Built
If 1–2% of units at a 25,000-unit auction end in a title return (estimate), and acting at check-in prevents a third, that is ~80–170 fewer cancellations a year at ~$500–1,500 each, ~$40,000–250,000 saved.
