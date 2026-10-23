# A Performance Ledger Mapped to the Surveillance Plan

**Niche:** [[niches/facilities-management-firms/federal-base-operations-support/profile|Federal Base Operations Support Contracts]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A BOS contractor generates thousands of performance records a month and cannot show, element by element, how it is performing against the plan the government rates it on.
**Tags:** #large-language-models #bert #transformers #descriptive-statistics #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to carry an Exceptional or Very Good CPARS record from the option years into the recompete, and whoever documents performance against the surveillance plan well enough that the government's evaluation cannot drift to Satisfactory takes the account.

## The Problem
The performance work statement and QASP define standards and acceptable quality levels for dozens of services. Government quality assurance evaluators sample performance and raise discrepancies. The contractor's own work orders, PM completions, QC inspections and corrective actions describe its performance in far more detail than the government's sample, but they are stored by system, not by rating element.

## Why Nobody Has Built This
Proposal and contract-management tools serve the bid and the deliverables schedule, and CMMS tools serve the work. Nothing reads the PWS and maps operational records to it, because that required reading natural-language requirements, which until recently only people could do.

## What to Build
A ledger that parses the PWS and QASP into rating elements and standards, classifies every work order, inspection and corrective action against them, and computes performance per element monthly against acceptable quality levels. It flags elements trending toward a Marginal rating while there is time to recover, and keeps a cited evidence pack per element for interim and final evaluations and for the past-performance volume of the next proposal.

## Target Customer
Program managers and quality managers on BOS contracts; capture and proposal leads who reuse the record.

## Impact If Built
Ratings rest on the contractor's full record rather than the government's sample, problems are fixed before they are rated, and the recompete proposal's past-performance narrative is evidenced rather than asserted.
