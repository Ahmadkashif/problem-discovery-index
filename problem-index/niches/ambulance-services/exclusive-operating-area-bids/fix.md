# Bid Assumptions Lost Between the Bid Team and Billing

**Niche:** [[niches/ambulance-services/exclusive-operating-area-bids/profile|Exclusive Operating Area Bids & Contract Pricing]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** The collection rate a bid assumed is never handed to the billing team that has to achieve it, so a shortfall shows up a year later as a contract that "underperformed".
**Tags:** #data-integration #linear-regression #workflow-orchestration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a county's exclusive 911 franchise from its call volume, payer mix and collection history, and whoever has the lowest share of won contracts losing money in their first full year takes the account.

## The Problem
The bid team's model lives in a spreadsheet on a shared drive. Billing, often an outside firm, reports collections by payer for the whole company. Nobody compares the two until the annual review, when the gap is too old to explain.

## Why It's Still Broken
Bids and billing report to different executives, and billing firms report in their own format. There is no shared contract identifier across the bid model, CAD and billing system.

## What a Fix Looks Like
Store the bid's key assumptions (payer mix, collection rate by payer, transports a year) against a contract identifier the billing system also carries. Then send a monthly variance report to both teams, so a payer-mix shift is seen in month two, not month fourteen.

## Who Feels the Pain
Regional presidents defending contract results; bid teams who never learn which assumption failed; billing managers blamed for revenue the bid never should have assumed.

## Impact If Fixed
Catching a 3-point payer-mix shift in month two rather than month fourteen (an estimate) gives an operator most of the first year to renegotiate rates or subsidy on a contract worth ~$30M a year, before that year closes at a loss.
