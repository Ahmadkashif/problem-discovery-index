# Title-Absent Sales Chased From a Spreadsheet

**Industry:** [[wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document-tracking software is solved, but no generic tool knows that an auction's title clerk is racing a title window the auction set, a lienholder payoff the seller controls and a buyer's right to hand the car back.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #workflow-orchestration #automation #compliance

## The Problem
A large share of wholesale cars sell before the auction holds a negotiable title (an estimated 5–15% at some auctions). A dealer's trade-in still carries the customer's loan. A repossession's title sits with the lender's custodian. A fleet unit's title is at a corporate office two states away. The NAAA policy framework gives the seller a number of days the auction chooses to deliver title. After that the buyer may return the car or wait. The seller can still cure by the close of the next business day after notice, and the guarantee lapses at 90 days (search summary). The car is supposed to be announced "title absent" under a blue light, and when it is not, the buyer can arbitrate for title.

The title clerk works this queue by hand. They hold a spreadsheet or a report from the auction system listing sold units with no title received, sorted by sale date. Each morning they phone or email sellers, check payoff status with lienholders, chase overnight envelopes and answer buyers who want their title or their money back. ACV's careers page on 2026-10-28 listed title clerk roles in Elm Mott and Longview, Texas. Its 10-K says titles are processed "by a dedicated ACV team or automated through machine learning".

## What Already Exists
Document management and workflow tools (DocuSign, Box, Salesforce cases), the auctions' own title modules, electronic lien and title (ELT) systems in the states that run them, and lienholder payoff services used by dealers. Loan servicing has mature "trailing document" tracking for mortgage files, and dealers' title processing is mapped at [[niches/auto-dealers-independent/title-registration-processing/profile|Title & Registration Processing]].

## The Customisation Gap
The generic tools track a document; the auction needs to track a deadline it does not own. The auction-specific logic includes:
- the auction's own title window, the buyer's return option and the 90-day lapse, per sale;
- which state issued the title, whether it is electronic or paper, and that state's typical release time once a lien is paid;
- the lienholder's payoff behaviour, whether the seller is a dealer, captive, fleet or lender, and that seller's history of late titles;
- whether the sale was announced title-absent, because an unannounced car is an arbitration risk, not just a delay;
- a ranked call list each morning: units most likely to breach the window, with the reason and the next action.

The sub-niche that owns this contest is [[niches/wholesale-auto-auctions/title-absent-sales/profile|Title-Absent & Title-Defect Sales]].

## Impact If Solved
A returned car for no title costs a transport back, a relisting, a rerun fee and a week or more of depreciation, often $500–1,500 a unit (estimate). Ranking the title queue by breach risk could cut title-related cancellations by a third at a busy auction (estimate), and spare a clerk working 300–500 open titles an hour or more of blind phone calls a day.
