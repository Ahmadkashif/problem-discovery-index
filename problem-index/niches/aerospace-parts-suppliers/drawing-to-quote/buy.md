# Quoting Software Taught Aerospace Cost Drivers

**Niche:** [[niches/aerospace-parts-suppliers/drawing-to-quote/profile|Drawing-to-Quote for Aerospace RFQs]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine-shop quoting software prices geometry and machine time; the costs that make aerospace quotes go wrong sit in the notes and the PO.
**Tags:** #large-language-models #transformers #feature-engineering #revenue-impact #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn an RFQ drawing package into a priced, routed quote inside the customer's window, and whoever's estimates land closest to the shop's own job actuals takes the account.

## The Problem
A quote built from geometry misses the passivation and penetrant inspection called out in note 4, the FAI on a ~180-characteristic part, the source inspection clause in the PO, and the minimum buy on a titanium bar size. The estimator adds these by memory, inconsistently.

## What Already Exists
Paperless Parts and ERP estimating modules handle geometry, routings, machine rates and material prices; CADDi finds similar past drawings.

## The Customization Gap
An aerospace layer that reads notes and PO clauses into cost items: outside special processes priced from the shop's processor history, FAI and inspection hours from characteristic counts, source inspection, certification and traceability costs, alloy minimums and lead times, and DFARS specialty-metals constraints on material choice. Each item appears as a visible quote line the estimator can accept or change.

## Target Customer
Shops already using a quoting platform that serve aerospace customers.

## Impact If Solved
Capturing the hidden cost lines consistently could remove ~3–8% of margin leakage on aerospace jobs (estimate) without changing the quoting workflow.
