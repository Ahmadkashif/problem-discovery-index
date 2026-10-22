# The Eligibility Clerk on the First of the Month

**Industry:** [[self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Worker Life Changing
**One-liner:** The fund-office clerk who decides each month whether a union member and their family have health coverage gets back the hours spent chasing late contractor reports, and the calls from members turned away at the pharmacy counter.
**Tags:** #gradient-boosting #k-nearest-neighbors #large-language-models #feature-engineering #worker-facing #automation #data-integration

## The Problem
In a Taft-Hartley health fund, coverage is earned by hours. A carpenter or electrician qualifies for next month's coverage if contributing employers reported enough hours, or if the hour bank holds enough reserve. The Southern California IBEW-NECA plan requires 100 hours a month. The Northern California Laborers grant initial eligibility after 440 banked hours and deduct 110 a month. TeamCare's hourly plan grants coverage in the second month after the month worked. The hours arrive on employer remittance reports, many from small contractors, some electronic, some keyed from spreadsheets or paper. The eligibility clerk at the fund office or the TPA runs the monthly eligibility cycle, sends terminations and COBRA self-pay notices, and fields what follows.

What follows is the phone. A member's coverage lapsed because one contractor reported late. Their child's prescription was rejected at the pharmacy that morning. The clerk has to find the missing remittance, call the contractor's bookkeeper, decide whether the late hours can restore eligibility (the IBEW-NECA plan credits contributions more than three months late to the month received, because its vendor contracts forbid retroactive eligibility), and explain it all to a frightened member in plain language. The same week, the clerk processes self-payments, reciprocity transfers from other funds when members travel for work, and retro-terminations when an audit reverses hours. In the busy weeks around the first of the month, the queue runs to dozens of calls a day (estimate).

## Why It Matters to the Worker
The clerk is the person who, in effect, tells a family whether they are insured. Mistakes are human and visible: cut off someone who was eligible and a member is billed for a hospital visit; leave someone on who was not and the fund pays claims it may never recover. The rules are a stack of trustee resolutions, plan amendments and reciprocity agreements that live mostly in senior clerks' memories. New clerks take months to trust their own decisions, and senior ones spend their days firefighting rather than training.

## What a Solution Looks Like
A worklist, not a queue. Before each eligibility run, the system predicts which members are at risk of a lapse because an employer's report is late or short against its own history. It drafts the call or email to that employer's bookkeeper and pre-stages the member notice. When a member calls, the clerk sees the member's hour history, the missing report, the rule that applies and a plain-language explanation drafted from the plan text, with the governing provision cited. Retro-terminations and reinstatements show their effect on paid claims before they are posted.

## Impact If Solved
Clerks could reclaim several hours a week (estimate) now spent chasing remittances and rebuilding eligibility histories by hand, and members would hear about a coming lapse before the pharmacy counter tells them. New clerks would learn the fund's rules from cited explanations rather than from whoever sits next to them.
