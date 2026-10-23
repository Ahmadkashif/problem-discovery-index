# Spending Tagged to the Funder's Rules at Entry

**Niche:** [[niches/visitors-bureaus/hotel-tax-tid-administration/profile|Hotel Tax & Tourism Improvement District Administration]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bureaus re-code a year of transactions into their funders' categories at report time, when the rules could be applied as each invoice is entered.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to produce, for every hotel-tax and assessment dollar, a record that ties the spending to an eligible purpose and to the overnight stays it produced, and whoever's record holds up through the city audit and the district renewal vote takes the account.

## The Problem
A bureau may answer to three rulebooks at once: the city contract, the district plan and a state statute. Each defines eligible categories, caps on administration and sometimes required percentages for sales versus marketing. The general ledger uses the bureau's own chart of accounts. At year end the finance lead maps every transaction to each funder's categories by hand.

## Why Nobody Has Built This
The market is small, with a few hundred bureaus large enough to have a finance lead, and each funder's rules differ. Accounting vendors serve nonprofits generally and do not encode municipal tourism law.

## What to Build
A rules layer beside the accounting system: each funder's categories and caps encoded once; invoices read and tagged with a proposed category and reason as they are entered; running totals against caps and plan percentages; and a report generator in each funder's format. Language models handle the reading; the rules stay explicit and auditable.

## Target Customer
CFOs and COOs of bureaus with mixed city, district and state funding.

## Impact If Built
Year-end compliance reporting becomes a by-product of bookkeeping, and the bureau sees cap breaches during the year instead of after.
