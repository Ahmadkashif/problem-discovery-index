# The Cancellation That Reaches the Office but Not the Truck

**Niche:** [[niches/repossession-services/known-address-recoveries/profile|Known-Address Recoveries]]
**Industry:** [[industries/repossession-services|Repossession Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A borrower pays or agrees an extension at 6 p.m., the lender cancels the order, and the agent who hooks the car at 4 a.m. never heard.
**Tags:** #workflow-orchestration #data-integration #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to recover a car whose address is known on the first attempt, without an objection, a damage claim or a recovery on a cancelled order, and whoever posts the highest clean first-attempt recovery rate on the forwarder's scorecard takes the account.

## The Problem
Holds and cancellations travel through the same channels as assignments, which for many agencies means RDN plus forwarder portals plus emails and phone calls from direct clients. A cancellation posted after the run-list was printed, or sent to an inbox nobody reads at night, is invisible to the truck. The result is a wrongful repossession: the CFPB's 2022 supervisory findings and Wells Fargo's 2022 order, which paid a base $4,000 per wrongly repossessed car, show what it costs a lender, and the lender passes the blame down.

## Why It's Still Broken
RDN's On-Hook Status solves it for files on RDN viewed in Clearplan; direct clients and some forwarders have no equivalent, and agencies working several sources check status by memory.

## What a Fix Looks Like
One status check, run automatically seconds before each hook, that queries every source the file came from and blocks the attempt in the field app if any reports a hold, cancellation, payment or bankruptcy flag — with the check itself logged as evidence.

## Who Feels the Pain
Agents who take the car and the blame; agencies that lose panels; borrowers who paid and lost their car anyway.

## Impact If Fixed
Recoveries on cancelled orders, the most indefensible error in the business, fall towards zero, and each recovery carries a timestamped proof that the order was live.
