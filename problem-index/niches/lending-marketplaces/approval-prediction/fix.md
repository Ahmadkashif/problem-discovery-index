# The Funding Notifications Nobody Uses

**Niche:** [[niches/lending-marketplaces/approval-prediction/profile|Approval Prediction]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Some lenders do send funding notifications, and they go into a billing reconciliation file and nowhere else.
**Tags:** #data-integration #quick-win #evaluation-metrics #automation #descriptive-statistics #logistic-regression #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict which lender approves this borrower and on what terms, from outcomes that are observed only for the borrowers who were already routed — and whoever handles that censoring best predicts approval for everyone else.

## The Problem
The industry's account of itself is that outcome data does not come back. It partly does. Lenders on funded-loan commercial terms send funding notifications because that is how the marketplace gets paid. Those files identify which borrower, which lender, which product and often which amount — a genuine, if partial, outcome signal. They are consumed by finance for invoicing and are not joined to the routing data at all.

## Why It's Still Broken
The notifications arrive as a billing artefact, so they were routed to finance and the data team never saw them — the file's purpose determined its destination and nobody asked what else it contained. Formats differ by lender and the files are messy. Nobody framed the funded set as training data. And the narrative that outcomes never return removed the motivation to look.

## What a Fix Looks Like
Join the file to the route. Match funding notifications back to the originating route, which is the fix and is a straightforward join on records both sides already hold. Report funded rate per lender per borrower segment, since that single table is the first outcome-based picture the marketplace has ever had. Use the funded set as a positive class immediately, because even a biased positive-only signal beats the click. Normalise the notification formats once, as the messiness is a one-off engineering cost blocking a permanent asset. Ask lenders to add the decision and terms to a file they already send, which is a far smaller request than a new data feed and is the natural opening for the commercial conversation. Backfill historical notifications, since years of them are sitting in finance systems. Compare funded rate against click rate per lender, which will show immediately how poorly the current objective proxies the outcome. Share the segment-level funded rates with lenders, because it is useful to them and builds the case for more. Measure how much of total volume is covered by funded reporting, as that defines how far the signal reaches. And put the joined dataset in front of the ranking team, since it is the training data they have been told does not exist.

## Who Feels the Pain
Data teams told outcomes never return; lenders whose leads are ranked without reference to funding; borrowers routed on clicks; and a marketplace paying for a signal it already receives and discards.

## Impact If Fixed
The file's purpose sent it to finance and nobody asked what else it contained. Joining funding notifications to routes produces the category's first outcome-based measurement from data already arriving every month.
