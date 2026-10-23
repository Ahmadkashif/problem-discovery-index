# Hotel Fit Scoring for Every Lead

**Niche:** [[niches/visitors-bureaus/single-hotel-group-leads/profile|Single-Hotel Group Lead Distribution]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A bureau sends each lead to whichever partner hotels look plausible, when its own history shows which hotels respond to and win which kinds of groups.
**Tags:** #logistic-regression #k-nearest-neighbors #word-embeddings #large-language-models #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put each planner's RFP in front of the two or three partner hotels that fit it and get a proposal back inside the planner's deadline, and whoever converts the most RFPs into contracted blocks per sales-manager hour takes the account.

## The Problem
A sales manager reads an RFP and picks the hotels to send it to. Send too few and the planner gets a thin proposal; send too many and hotels learn to ignore bureau leads. The choice depends on space-to-rooms ratio, room pattern, rate, dates and which general managers actually answer, and it is made by memory, differently by each manager.

## Why Nobody Has Built This
CRM lead distribution was designed as a fair-share list for partner hotels who pay dues, not as a ranking. Response and win data sits in the CRM but nobody has modelled it, and ranking hotels is politically delicate for a bureau that serves all its partners.

## What to Build
Extract each RFP's requirements automatically, then score every partner hotel on its probability of responding competitively and winning, using the bureau's own lead history, hotel space specs and rate history. The manager sees a ranked list with reasons, sends to the top fits, and the proposal is drafted from the responses. Fairness rules (every partner sees leads matching its profile) are applied explicitly rather than by habit.

## Target Customer
Directors of sales at mid-sized and large bureaus handling several hundred leads a year.

## Impact If Built
Faster, stronger proposals to planners and fewer wasted hotel responses, measured as contracted blocks per lead and per sales-manager hour.
