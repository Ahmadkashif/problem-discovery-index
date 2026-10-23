# A Disallowance Map From Every Commission Order

**Niche:** [[niches/electric-utilities/rate-cases-revenue-requirement/profile|Rate Cases & Revenue Requirement]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Commission orders say exactly which costs and arguments were disallowed and why, and no utility has a structured record of them to plan its next filing.
**Tags:** #large-language-models #transformers #logistic-regression #causal-inference #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a revenue requirement through a contested case with the fewest disallowances, and whoever builds the evidentiary record that survives discovery and intervenor cross-examination takes the account.

## The Problem
Every final order explains which adjustments were accepted, reduced or rejected and on what evidence: incentive compensation, storm reserves, vegetation management levels, capital projects found not used and useful, return on equity. Regulatory teams know their own commission's habits from experience, but the record across cases, states and sister utilities is read once and forgotten.

## Why Nobody Has Built This
Orders are long, inconsistently structured PDFs across fifty commissions. Rate case tracking services summarise headline outcomes for investors, not line-item reasoning for the people writing the next filing.

## What to Build
A corpus of final orders and settlements from public dockets, extracted into issue-level records: cost category, amount requested and allowed, the evidence the commission cited, the intervenor who raised it. Models then estimate disallowance risk for each proposed adjustment, given the commission, the issue and the evidence planned. The output is a pre-filing review that ranks adjustments by risk and shows the precedent behind each.

## Target Customer
Regulatory affairs and rates directors at investor-owned utility holding companies filing in several states.

## Impact If Built
Recovering even ~1% more of a typical request avoids millions of dollars of disallowance per case for a mid-sized utility (estimate). It also puts evidence where it matters before filing and grounds settlement positions in precedent rather than memory.
