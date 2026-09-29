# Where Is My Payment

**Niche:** [[niches/ap-automation-vendors/the-supplier/profile|The Supplier]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The supplier's only way to find out when they will be paid is to phone the AP team, which is the AP team's biggest interruption.
**Tags:** #quick-win #workflow-orchestration #automation #worker-facing #evaluation-metrics #descriptive-statistics #data-integration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the supplier's side of the transaction worth their cooperation — and whoever does it gets accurate invoices, current details and reachable contacts, which is most of the buyer's problem solved.

## The Problem
A supplier is owed money and does not know when it will arrive. The portal, if they can find their login, says the invoice is received or in process, which has been true for three weeks. So they email or call AP. The clerk stops what they are doing, looks up the invoice, finds it waiting on an approval, and tells them they do not know. Both sides of that call are wasted, it repeats hundreds of times a month, and it is the largest single category of inbound contact in most AP teams.

## Why It's Still Broken
The status was implemented as a workflow state, so it reports where the invoice sits internally rather than what the supplier asked — a system exposing its own state model has answered a different question. Exposing a date requires committing to one, which nobody wanted to do. Supplier contact volume is absorbed by AP. And nobody counted the calls.

## What a Fix Looks Like
Answer the actual question. Show a meaningful status in the supplier's terms — approved and scheduled, waiting on approval, on hold for a query — rather than an internal workflow state, which is the fix and is a translation rather than a build. Publish an expected payment date once approved, since that is the question and the payment run schedule already determines it. Notify proactively when status changes, because the call is triggered by silence. Say what is blocking when an invoice is held, as a supplier who knows a purchase order reference is missing can fix it immediately. Give the supplier a route to resolve rather than only to ask, which converts a call into a correction. Report inbound status contact volume, which will demonstrate the cost and is not measured anywhere. Aggregate across buyers for suppliers on the platform, since that is what makes the portal worth logging into. Send remittance detail that reconciles, because unreconcilable remittances generate a second call. Make the status accurate before making it visible, as a wrong date is worse than none. And measure the reduction in inbound contact, since that is the return and it will be large.

## Who Feels the Pain
Suppliers chasing payments they cannot see; AP clerks interrupted by calls they cannot answer; small suppliers whose cashflow depends on knowing; and buyers whose supplier relationships erode over information they already have.

## Impact If Fixed
The status reports the internal workflow state, which answers a different question from the one the supplier asked. Translating it into supplier terms and publishing an expected date removes the largest source of inbound contact in AP.
