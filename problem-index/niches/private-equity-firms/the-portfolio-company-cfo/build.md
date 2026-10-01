# Three Versions of EBITDA, Reconciled by Hand

**Niche:** [[niches/private-equity-firms/the-portfolio-company-cfo/profile|The Portfolio Company CFO]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Management EBITDA, covenant EBITDA under the credit agreement and the sponsor's adjusted EBITDA are three numbers from one ledger, and the CFO reconciles them every month in a spreadsheet.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #worker-facing #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to let a sponsor-backed CFO maintain one mapping from the company's ledger to the sponsor's, the lender's and the board's definitions — and whoever does that owns the reporting relationship between owner and company.

## The Problem
Each consumer defines EBITDA its own way: the credit agreement permits specific add-backs subject to caps, the sponsor applies its fund-wide adjustments, and management reports operating reality. The CFO maintains the bridge manually and defends it in three meetings.

## Why Nobody Has Built This
Credit agreement definitions are long legal text; FP&A tools model plans, not covenant definitions; and the sponsor's monitoring platform receives the output, not the logic.

## What to Build
Extract EBITDA definitions, caps and add-back baskets from the credit agreement into structured rules; encode the sponsor's adjustment conventions; compute all three from the mapped ledger every month with a single bridge; and forecast covenant headroom forward from the budget.

## Target Customer
CFOs and controllers at sponsor-backed companies; sponsors deploying it across a portfolio.

## Impact If Built
The bridge that consumes days of senior finance time every month becomes a reviewed output, and covenant risk is visible months earlier.
