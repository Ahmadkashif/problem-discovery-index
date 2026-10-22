# Gain-on-Sale Attribution in a Generic BI Stack

**Niche:** [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/profile|Secondary Marketing & Pipeline Risk]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lenders already pipe origination data into Power BI or Tableau; what the dashboards cannot do is say which decisions between lock and sale made or lost the margin.
**Tags:** #descriptive-statistics #feature-engineering #causal-inference #data-integration #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to forecast which locked loans will fund and to sell each one at its best execution, and whoever earns the most margin per locked loan net of hedge cost and lock concessions takes the account.

## The Problem
The monthly capital markets report shows gain on sale in basis points by channel and product. When it falls, nobody can say whether the cause was the rate sheet margin, hedge slippage, concessions, extension fees waived, a worse execution choice, or loans that aged on warehouse and sold at a discount.

## What Already Exists
General BI platforms (Power BI, Tableau, Looker) connected to the origination system's reporting database, plus the pricing engine's and hedge advisor's own reports.

## The Customization Gap
The mortgage layer is a loan-level margin waterfall: price at lock from the rate sheet; changes from relocks, renegotiations and extensions; the hedge result allocated to the loan by lock date and product; investor price and fees at sale versus the best available execution on the same day; and warehouse carry. It needs joins across the origination system, pricing engine, hedge advisor files and investor purchase advices, with consistent loan keys and lock-date conventions. Each lender builds this differently, and most stop at totals.

## Target Customer
CFOs and capital markets heads at lenders large enough to run a BI team, and the hedge advisors who report results to them.

## Impact If Solved
A loan-level waterfall turns a falling gain-on-sale number into named causes the desk can act on within the same month, rather than a debate at the quarterly board meeting.
