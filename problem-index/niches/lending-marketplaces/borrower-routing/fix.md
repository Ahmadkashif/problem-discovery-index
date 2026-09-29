# Routed to a Lender Who Declines Them

**Niche:** [[niches/lending-marketplaces/borrower-routing/profile|Borrower Routing]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The borrower's profile makes approval at that lender essentially impossible and the marketplace shows them the offer anyway.
**Tags:** #quick-win #logistic-regression #evaluation-metrics #automation #compliance #descriptive-statistics #confidence-intervals #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to send each borrower to the lender who will actually approve them on the best terms — and the contest splits cleanly enough that it is not terminal.

## The Problem
A borrower with a credit score below a lender's published floor, or in a state that lender does not serve, or seeking an amount outside its range, is routed to it anyway. They apply, absorb an inquiry, and are declined for reasons that were knowable before the click. This is not a subtle modelling failure — it is a filter that is either not applied or applied to a stale rule — and it happens at meaningful volume in a business whose lenders are simultaneously complaining about lead quality.

## Why It's Still Broken
Eligibility rules live in the catalogue and the catalogue is maintained by hand, so rules are incomplete and stale — and the routing layer applies whatever the catalogue happens to say. Showing more lenders increases clicks, which is what is measured. Declines are invisible to the marketplace. And nobody reports the share of routes that violate a lender's own published criteria.

## What a Fix Looks Like
Apply the rules that already exist. Enforce hard eligibility filters — state, amount, minimum score, loan purpose — before ranking, which is the fix and is the most basic thing the system can do. Report how many routes violate a published rule, since it is one query against the catalogue and the number will justify everything else. Keep the rules current, which connects directly to the catalogue niche and is where most of the failure originates. Let lenders verify their own rules as displayed, because they know them exactly and are never asked to check. Treat a hard decline as a routing failure in reporting, as it is one and is currently counted as a successful handoff. Use declines the marketplace does learn about to correct the rules, since some notifications do return and are discarded. Tell the borrower why a lender is not shown, which is better service and reduces the re-shop. Separate hard ineligibility from low probability, because the first should filter and the second should rank. Sample routes for manual review, as a small audit will surface systematic errors quickly. And give partner managers the violation report, since it is the one lead quality conversation they can currently win.

## Who Feels the Pain
Borrowers absorbing inquiries for loans they could never receive; lenders paying for structurally unqualified leads; partner managers with no answer; and a marketplace whose quality complaints are partly self-inflicted.

## Impact If Fixed
The routing layer applies whatever the hand-maintained catalogue says, so stale and incomplete rules become wasted inquiries. Enforcing published eligibility before ranking is the most basic available fix and removes the least defensible failures.
