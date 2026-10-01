# Add-Backs Tested by Sample on a Ledger Available in Full

**Niche:** [[niches/private-equity-firms/quality-of-earnings-review/profile|Quality of Earnings Review]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The full general ledger sits in the data room, and add-backs are still tested by pulling a sample of invoices.
**Tags:** #large-language-models #gradient-boosting #feature-engineering #change-point-detection #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to establish a defensible adjusted EBITDA — which add-backs are real and which are recurring costs relabelled — inside the exclusivity window, because that number multiplied by the multiple is the price.

## The Problem
A QoE team receives three years of general ledger detail — often hundreds of thousands of lines — and a seller's add-back schedule. Under deadline, it tests add-backs by pulling supporting invoices for the largest items and a sample of the rest, and analyses revenue and margin trends at the account level. Patterns that would show an add-back recurring — the same vendor categorised as "one-time consulting" every year, legal costs that track headcount — sit unexamined below the sample threshold.

## Why Nobody Has Built This
Every target's chart of accounts is different and memo fields are free text, so full-population analysis requires mapping that used to cost more than sampling. Providers price by the engagement and staff it with associates; automation reduces billable hours. And there is no labelled corpus of which add-backs later proved recurring.

## What to Build
Full-population ledger analytics for each engagement: LLM-assisted mapping of the target's chart of accounts to a standard taxonomy; classification of every transaction memo and vendor; recurrence detection across years for every proposed add-back category; and change-point analysis on monthly margins to find the quarter the business changed. Output an add-back scorecard with evidence links for each item, ranked by likelihood of recurrence, so the team's sample is spent where the risk is.

## Target Customer
Transaction advisory practice leaders at accounting firms and QoE boutiques; sponsors with in-house financial diligence teams.

## Impact If Built
Add-backs commonly account for a material share of adjusted EBITDA in lower-middle-market deals. Testing the full population rather than a sample changes the precision of the price-setting number at little extra time.
