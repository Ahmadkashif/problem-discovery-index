# The 14-Day Window Spent Finding Evidence

**Niche:** [[niches/facilities-management-firms/federal-base-operations-support/profile|Federal Base Operations Support Contracts]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A CPARS evaluation arrives with a weak narrative, and the program team spends its 14-day comment window searching for the records that would have answered it.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to carry an Exceptional or Very Good CPARS record from the option years into the recompete, and whoever documents performance against the surveillance plan well enough that the government's evaluation cannot drift to Satisfactory takes the account.

## The Problem
Under FAR 42.1503 a contractor has up to 14 calendar days from notification to comment on an evaluation, after which it becomes available to source selection officials. A narrative that rates a service Satisfactory, or cites a discrepancy the contractor fixed months ago, needs a factual rebuttal. The program team reconstructs it from CMMS exports, QC files and email while running the contract.

## Why It's Still Broken
Evaluations arrive annually or at contract end, so nobody keeps the evidence organised for them in between. The records exist but are filed by system and date, not by the claim they would support.

## What a Fix Looks Like
Keep a running file per rating element, populated automatically from work orders, QC inspections and closed corrective actions. When an evaluation arrives, parse its narrative into claims, retrieve the records that bear on each one, and draft the comment with citations for the program manager to edit and submit well inside the window.

## Who Feels the Pain
Program managers, quality managers and the capture team, who inherit whatever the record says at the next bid.

## Impact If Fixed
Rebuttals become routine and evidenced rather than rushed, and fewer evaluations settle at a rating the contractor's own records contradict.
