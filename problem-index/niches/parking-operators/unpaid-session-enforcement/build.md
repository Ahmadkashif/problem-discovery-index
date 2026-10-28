# An Unpaid-Session Ledger From Gate to Notice

**Niche:** [[niches/parking-operators/unpaid-session-enforcement/profile|Unpaid-Session Recovery & Private-Property Enforcement]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators cannot say what share of sessions at a gateless lot go unpaid, how many were recovered at exit or by notice, and how many were lost to misreads or disputes.
**Tags:** #survival-analysis #logistic-regression #feature-engineering #compliance #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn unpaid parking sessions into collected revenue. That produces two contests with different winners: making payment happen before the car leaves, won by camera and PARCS platforms on the share of sessions paid without a notice, and recovering the sessions that slip through by mailed notice, won by notice processors on the share of notice value collected under each state's rules. Decomposed into contested sub-niches below.

## The Problem
The camera platform knows sessions, the payment apps know payments, and the notice processor knows notices and collections. The owner sees a single revenue line and cannot tell whether leakage is 3% or 15%.

## Why Nobody Has Built This
The three halves belong to different vendors, and notice processors are often paid a share of what they collect, so nobody has an incentive to report what was never pursued.

## What to Build
A ledger keyed on the session that follows each unpaid session through every state: unpaid at exit, prompted to pay, paid late, sent to notice, held for misread risk, blocked by state rule, disputed, paid, written off. Survival curves show how long recovery takes; a per-lot dashboard shows leakage and the cause of every lost dollar.

## Target Customer
Operators and owners with gateless facilities; notice processors that want to prove performance.

## Impact If Built
Knowing the true leakage per lot lets an operator move a lot from 10% to 5% unpaid (estimate); on a lot collecting $500K a year that is ~$25K recovered.
