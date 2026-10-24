# Purchaser Statements Reconciled to Well Allocations Before Close

**Niche:** [[niches/oil-and-gas-producers/production-revenue-jib-accounting/profile|Production, Revenue & JIB Accounting]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Volumes the operator allocated to its wells and volumes the purchaser paid for disagree every month, and the variances are found after owners have been paid.
**Tags:** #gradient-boosting #feature-engineering #large-language-models #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to close each production month with every purchaser dollar booked to the right well and every owner and partner paid or billed correctly, and whoever leaves the fewest dollars in prior-period adjustments and unexplained suspense takes the account.

## The Problem
Oil is sold by run ticket and gas through meters owned by midstream companies, and each purchaser sends a statement with volumes, quality, price and deductions by meter or lease. The operator allocates measured volumes back to wells from its own field data. The two rarely match exactly: meter factors change, a well is mapped to the wrong meter, a gathering contract's deduction moves, a run ticket is missing. Revenue accountants chase the biggest variances by hand and book the rest, and the errors return as prior-period adjustments that ripple through every owner's check.

## Why Nobody Has Built This
Accounting vendors load statements but leave reconciliation to the customer. Statement formats vary by purchaser, and the knowledge of which variances are normal sits with experienced accountants.

## What to Build
A reconciler that ingests purchaser and midstream statements in any format, maps them to wells and meters, and compares them with the operator's allocation and contract terms. It learns each meter's normal variance from history, flags breaks with a likely cause (meter mapping, missing ticket, price or deduction change) and drafts the correcting entry. It runs daily as statements arrive, not after close.

## Target Customer
Revenue accounting managers at operators with hundreds of wells and several purchasers.

## Impact If Built
An operator with ~$500M a year of sales and ~1% of revenue moving through prior-period adjustments (estimate) has ~$5M a year re-flowing through owner checks. Halving that removes thousands of corrected owner payments and the calls they generate.
