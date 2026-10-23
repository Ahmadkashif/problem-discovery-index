# Dose-Level Reconciliation Across Fridge, Chart, Registry and Claim

**Niche:** [[niches/physician-practices/independent-pediatric-practices/profile|Independent Pediatric Practices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every vaccine dose leaves four records (stock count, EHR entry, registry report and claim), and no product checks that all four agree for the same lot, child and eligibility.
**Tags:** #data-integration #descriptive-statistics #hypothesis-testing #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a pediatric practice's vaccine stock reconciled across VFC and private inventory, with every dose billed under the right administration codes, and whoever leaves the fewest doses wasted, borrowed or unbilled takes the account.

## The Problem
A busy pediatric office gives hundreds of doses a week (estimate). A private dose given to a Medicaid child must be logged as borrowing and repaid. A dose recorded in the chart but not billed is lost revenue. A count that does not match the VFC ordering report triggers questions from the state programme and can put the practice's enrolment at risk.

## Why Nobody Has Built This
The four records live in four systems owned by different parties: the practice EHR, the state registry, the VFC ordering portal and the clearinghouse. Pediatric practices are a small software segment. Vendors build immunisation modules that record, not reconcile.

## What to Build
A nightly reconciliation that matches each dose by lot number, child and date across EHR, registry export, inventory counts and claims. It flags eligibility mismatches, unlogged borrowing, unbilled administrations and expiring lots, and produces the VFC borrowing and wastage reports the state requires.

## Target Customer
Independent pediatric groups of 2–20 clinicians and pediatric IPAs that buy on their members' behalf.

## Impact If Built
Recovering unbilled administrations and cutting wastage from expired or misallocated lots is worth ~$10,000–$30,000 a year per pediatrician (estimate). It also removes the paper logs behind most VFC compliance findings.
