# Score-Choice Simulation per Loan

**Niche:** [[niches/credit-bureaus/mortgage-merged-reports/profile|Mortgage Merged Reports & Score Transition]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lenders can now choose between score models for agency loans, and none can see, loan by loan, what the choice does to the borrower's price, eligibility and the lender's execution.
**Tags:** #gradient-boosting #monte-carlo-methods #evaluation-metrics #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to deliver the merged report and whichever score set each lender's investors now accept — Classic FICO, VantageScore 4.0, later FICO 10T — straight into the lender's pricing and underwriting engines, and whoever re-plumbs the score transition without breaking a lender's pricing or pull-through takes the account.

## The Problem
Under the April 2026 rollout, approved lenders may use VantageScore 4.0 or Classic FICO on a tri-merge report. The two models score borrowers differently, price grids are keyed to score bands, and the cost of the scores differs. A lender deciding whether to switch has portfolio-level comparisons from vendors, but no way to see the effect on its own pipeline.

## Why Nobody Has Built This
Score vendors argue for their own model; resellers deliver whatever is ordered; pricing engines take one score as input. Historical score data for the new models only began to be published from summer 2026.

## What to Build
For each loan, pull or estimate both score sets, run them through the lender's pricing, eligibility and agency rules, and show price, eligibility and pull-through differences; aggregate to a pipeline view with uncertainty, so secondary marketing can decide which model to use for which loans as investor rules allow.

## Target Customer
Secondary marketing and capital markets heads at agency lenders; resellers offering it as a differentiator.

## Impact If Built
Score choice made on the lender's own book rather than on vendor claims, at a moment when the choice is new and the rules are still changing.
