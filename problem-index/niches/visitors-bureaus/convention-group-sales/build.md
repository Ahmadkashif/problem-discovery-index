# A Bid Ledger Closed by the Housing Report

**Niche:** [[niches/visitors-bureaus/convention-group-sales/profile|Convention & Group Sales]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every group bid a bureau makes is a forecast of stays, and no bureau keeps a record that joins the forecast to what happened.
**Tags:** #gradient-boosting #survival-analysis #evaluation-metrics #feature-engineering #tacit-knowledge-ml #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to turn group demand into hotel room nights that actually happen, but a citywide convention bid and a single-hotel group lead are won on different things: a credible pickup forecast and incentive offer years ahead for the first, speed and hotel fit within days for the second. Decomposed into contested sub-niches below.

## The Problem
A bureau's sales team makes hundreds of group decisions a year: which leads to send where, which citywides to bid for, what incentive to offer, how big a block to recommend. Each is implicitly a forecast that a group will come and stay. The CRM records the lead and its outcome, but not the forecast, and the outcome it records is the contract, not the stay. So the bureau cannot say which kinds of groups it overestimates, whether incentives win business that would have come anyway, or whether its best director is better than a simple rule.

## Why Nobody Has Built This
Destination CRMs were built to log activity and pipeline for reporting, not to grade forecasts. Pickup data lives with housing companies and hotels, not with the bureau. And a ledger that shows overstated room nights is uncomfortable for a team paid on booked room nights.

## What to Build
A bid ledger inside the CRM: at the tentative stage, a short record of expected pickup, confidence, competing cities and incentive logic, drafted from the RFP and notes and confirmed in seconds. After the meeting, the record is closed from the housing report and, where groups agree, hotel actuals matched to registrations. On top, a conversion and pickup model trained across a pool of bureaus, reported beside the director's own forecasts. The sub-niches below define what it must do for citywides and for single-hotel leads.

## Target Customer
Vice presidents of sales at bureaus with a convention centre, and the destination CRM vendors as the channel.

## Impact If Built
Incentive money follows groups that will actually stay, block sizes stop setting groups up for attrition penalties, and the bureau reports room nights its funders can check.
