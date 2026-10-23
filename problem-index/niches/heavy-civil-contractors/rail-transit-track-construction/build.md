# A Window Planner That Learns Production per Outage

**Niche:** [[niches/heavy-civil-contractors/rail-transit-track-construction/profile|Railroad & Transit Track Construction]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A track contractor plans each outage from experience; nobody records how many feet of track, turnouts or panels a gang actually installs per window under which conditions, so window requests and bids are guesses.
**Tags:** #tacit-knowledge-ml #gradient-boosting #optimization-fundamentals #survival-analysis #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to finish new track, turnouts and yard work inside the outage windows the host railroad or transit agency grants, and whoever returns track to service on time in the largest share of granted windows takes the account.

## The Problem
Rail superintendents know that a six-hour window (illustrative) yields far less than half a twelve-hour one once set-up and testing are counted, and that night windows in winter run slow. Those numbers live in their heads.

## Why Nobody Has Built This
Window outcomes are logged by the railroad, production by the contractor's foreman, and the two never meet. Rail is a small slice of each estimating vendor's market.

## What to Build
A production model per window type (length, time of day, season, crew, access, equipment) trained on the contractor's own window records. It feeds a planner that sizes window requests and sequences the work to the host railroad's operating plan, and flags windows at risk of overrun. A demo can run on synthetic window logs.

## Target Customer
Rail division managers and estimators at contractors building ~$20M+ a year of track (estimate).

## Impact If Built
If overrun windows fall by a third (estimate), the contractor avoids the penalty, reputational cost and replanning of each blown outage.
