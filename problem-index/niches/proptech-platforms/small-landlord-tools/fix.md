# The Security Deposit Handled Wrong

**Niche:** [[niches/proptech-platforms/small-landlord-tools/profile|Small Landlord Tools]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Security deposit rules differ by state on where the money must be held, whether it earns interest, how fast it must be returned and how deductions must be itemised, and small landlords get them wrong routinely in ways that cost them statutory damages and cost residents money they are owed.
**Tags:** #descriptive-statistics #evaluation-metrics #compliance #workflow-orchestration #automation #worker-facing #quick-win #confidence-intervals
**Contested on:** Every serious competitor selling to small landlords is fighting to get a person with four units from an empty unit to a compliant lease, a working ledger and a filed tax return without hiring anyone — and whoever makes that path unassisted takes the segment.

## The Problem
A resident moves out. The landlord intends to return the deposit less the cost of repainting a wall. They are busy; five weeks pass. In their state the deadline was twenty-one days, the deduction required an itemised statement with receipts, and normal wear does not include repainting after a three-year tenancy. The resident, who needed that money for their next deposit, has not received it and may not know they have a remedy. The landlord, when challenged, discovers they owe the full deposit plus statutory damages. Neither party understood the rule and the money involved is significant for both.

## Why It's Still Broken
Deposit handling is a sequence of dated obligations with no prompt attached to any of them. The software records a deposit as a payment and has no concept of the custodial duty that goes with it. The rules are state-specific and in some states locally modified, which puts them in the same content maintenance category as everything else in this niche. And the failure is asymmetric in visibility: most residents do not pursue it, so the landlord's error usually has no consequence, which means nothing corrects the practice.

## What a Fix Looks Like
Model the deposit as a custodial obligation with a clock. At collection, the product applies the jurisdiction's rules on amount, account type and any required notice. Through the tenancy it tracks interest where required. At move-out it starts the statutory clock and prompts, with the deadline stated plainly and the consequence of missing it stated equally plainly. Deductions must be itemised with evidence attached — the move-in and move-out inspection photographs the product already holds — and the product should flag deductions that look like ordinary wear given the tenancy length, which is the most commonly disputed category and the one where a lay landlord has no reference. The itemised statement generates automatically and the return payment is initiated from the same screen. The resident sees the same record, which is the part that changes behaviour most.

## Who Feels the Pain
Residents owed deposits they do not receive, who need that money to secure the next home; landlords facing statutory damages for a deadline they did not know about; and both parties in disputes that turn on documentation neither assembled.

## Impact If Fixed
Deposit disputes are among the most common landlord-tenant conflicts and are almost entirely procedural — the rules are knowable and the evidence exists. Putting the clock, the itemisation and the evidence into one flow resolves most of them before they start, and it protects the party with the least capacity on each side: the resident who cannot chase it and the landlord who did not know.
