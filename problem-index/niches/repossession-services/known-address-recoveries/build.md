# The Hour the Car Is Home and the Borrower Is Not

**Niche:** [[niches/repossession-services/known-address-recoveries/profile|Known-Address Recoveries]]
**Industry:** [[industries/repossession-services|Repossession Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agents run known-address files at the same pre-dawn hours by habit, when each borrower's car is home and unwatched at different times that the agency's own attempts and hits could reveal.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #bayesian-inference #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to recover a car whose address is known on the first attempt, without an objection, a damage claim or a recovery on a cancelled order, and whoever posts the highest clean first-attempt recovery rate on the forwarder's scorecard takes the account.

## The Problem
The textbook window is 2 to 5 a.m., and much of the industry runs it. But a night-shift nurse's car is home at 10 a.m., a contractor's truck is at a job site by 6, and an apartment lot fills and empties on its own rhythm. Veteran agents read these patterns from the assignment and from a drive-by; newer agents run the textbook window and find empty driveways or awake borrowers. Every failed first attempt lowers the clean first-attempt rate the forwarder scores, and every second visit to a known address raises the chance of a confrontation.

## Why Nobody Has Built This
Agencies have never logged attempts in a structured way — the status update says "vehicle not present", not when and why that hour was chosen — and the plate-scan history that would show presence by hour belongs to the camera network.

## What to Build
A presence-by-hour model for each known-address file, trained on the agency's own attempts and outcomes, its camera hits on its assignments, address type, employment signals in the assignment, and neighbourhood and parking features. It recommends the first-attempt window, flags when a daylight or workplace attempt is the better bet, and explains itself in the veteran's terms. The attempt ledger it needs is captured from the field app's GPS trace and one-tap reasons.

## Target Customer
Agencies of three or more trucks whose allocation depends on forwarder scorecards.

## Impact If Built
More first-attempt recoveries, fewer repeat visits to the same driveway, and fewer confrontations — the three things the scorecard and the agent both care about.
