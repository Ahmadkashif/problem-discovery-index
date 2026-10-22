# Realised Margin per Project, Item by Item

**Niche:** [[niches/interior-design-firms/residential-full-service-studios/profile|Residential Full-Service Studios]]
**Industry:** [[industries/interior-design-firms|Interior Design Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio knows the markup it proposed on every item and almost never knows the margin it actually kept after freight, restocking, damage, client concessions and remakes.
**Tags:** #gradient-boosting #feature-engineering #descriptive-statistics #evaluation-metrics #revenue-impact #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to become the single record from proposal to client invoice — selections, client deposits, purchase orders and markup — and whoever holds that record holds the studio's margin and its books.

## The Problem
The proposal shows a 30% markup on a dining table. Then the vendor raises the price between proposal and order, freight comes in at twice the estimate, the table arrives with a damaged leg and the remake ships at the studio's expense, and the principal knocks a few hundred dollars off the final invoice to keep the client happy. None of these events is joined to the item. At year end the studio sees revenue and gross profit in QuickBooks and cannot say which vendors, categories, project types or clients eroded margin.

## Why Nobody Has Built This
The costs arrive in different systems at different times: vendor invoices, freight bills, receiving-warehouse charges, credit memos and client invoice adjustments. Studio software records the proposal and the PO; the ledger records the cash. Joining them at item level needs document reading and matching that has only recently become cheap.

## What to Build
An item-level margin ledger that attaches every subsequent cost and concession to the original proposal line by reading vendor invoices, freight bills, warehouse charges and credit memos as they arrive. Roll it up by vendor, category, project type, designer and client, and add a model that predicts realised margin at proposal time so the studio can price freight and risk into the quote for vendors and categories with a history of erosion.

## Target Customer
Principals and operations managers at residential studios with three to twenty staff and more than ~$1M a year in product resale (estimate).

## Impact If Built
Seeing that a handful of vendors and categories account for most margin leakage lets a studio re-price or drop them; recovering even two or three points of product margin on ~$1–3M of resale (estimate) is worth more than most studios' annual software spend.
