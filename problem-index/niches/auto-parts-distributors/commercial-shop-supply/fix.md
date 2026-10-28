# The Quoted Price and the Invoiced Price Don't Match

**Niche:** [[niches/auto-parts-distributors/commercial-shop-supply/profile|Commercial Parts Supply to Independent Repair Shops]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** A shop sees one price in its e-catalog quote, another on the invoice and a third on its monthly statement, and every gap becomes a credit request and a reason to try another supplier.
**Tags:** #k-nearest-neighbors #feature-engineering #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the independent shop's first call for the part a car on the lift needs, and whoever fills the largest share of the shop's first requests with the correct part takes the account.

## The Problem
Commercial pricing runs on matrices: tiers by shop, category discounts, promotions, programme rebates paid monthly. The price a shop sees in an e-catalog quote is computed by one system, the counter may override it, and the invoice and statement come from another. Mismatches turn into credit requests the rep must chase and into a shop's suspicion that it is being overcharged.

## Why It's Still Broken
E-catalog networks, business systems and rebate programmes each hold part of the price logic, and overrides at the counter are rarely logged with a reason. Nobody reconciles quote, invoice and statement line by line.

## What a Fix Looks Like
A reconciliation that joins each quote to its invoice line, flags price differences above a threshold with the cause (override, matrix change, promotion expiry), auto-issues credits within policy, and reports overrides by counter person and shop.

## Who Feels the Pain
Shop owners and service writers who bill their customers off the quote; outside reps who spend visits on credits; controllers who see margin leak through ad hoc credits.

## Impact If Fixed
If price-dispute credits fall from ~1% to ~0.3% of commercial sales (estimate), a store selling ~$3M a year to shops keeps ~$21K of margin and its reps get back ~2 hours a week.
