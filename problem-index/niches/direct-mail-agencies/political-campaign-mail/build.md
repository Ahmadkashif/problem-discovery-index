# Ballot-Timed Drop Planning per Voter

**Niche:** [[niches/direct-mail-agencies/political-campaign-mail/profile|Political Campaign Mail]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Campaign mail is scheduled by drop date for the whole universe, when what matters is whether each voter's piece lands before that voter's ballot does.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to land an approved, disclaimer-compliant piece in target voters' homes before their ballots arrive — and whoever turns an approved script into in-home mail fastest in the final weeks takes the campaign.

## The Problem
In states with widespread mail voting, ballots go out on different dates by county and voter, and many voters return them within days. A mail programme planned as "five pieces, one a week, last drop ten days out" lands its closing argument after a large share of the target universe has already voted.

## Why Nobody Has Built This
Ballot mailing schedules and return files come from hundreds of election offices in different formats, delivery times for Marketing Mail vary by facility, and campaigns rebuild their operation every cycle. Mail consultants plan from experience, which is good on average and blind to county-level timing.

## What to Build
A planner that estimates, for each target voter, when their ballot arrives (county mailing schedule, ballot request date, postal delivery time) and when they are likely to return it (vote history, prior return timing), then forecasts in-home dates for each candidate drop from entry point and scan history. It sequences pieces so persuasion lands before ballot arrival and turnout reminders before the voter's likely return date, and updates nightly from return files.

## Target Customer
Political mail consulting firms and party committees running programmes across many races in mail-voting states.

## Impact If Built
More of each programme's pieces land while the voter is still deciding, which is the only time they can matter, and wasted postage on voters who have already returned ballots falls.
