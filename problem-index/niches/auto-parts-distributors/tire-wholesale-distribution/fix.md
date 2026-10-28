# Substitutions the Dealer Didn't Ask For

**Niche:** [[niches/auto-parts-distributors/tire-wholesale-distribution/profile|Replacement Tire Wholesale Distribution]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** A wholesaler short on the ordered brand ships an "equivalent" to protect its fill rate, and the dealer who sold the customer a specific tire has to make the call it dreads.
**Tags:** #logistic-regression #k-nearest-neighbors #feature-engineering #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep independent tire dealers' size-and-brand orders filled from the nearest warehouse, and whoever fills the largest share of a dealer's tire orders as ordered, without substitution, takes the account.

## The Problem
Tire dealers often sell a specific brand and line to a consumer before ordering it. When the wholesaler substitutes, by brand, tread pattern or load rating, the dealer must explain the change to a customer waiting in the lobby, or refuse the delivery and lose the sale. The wholesaler's fill-rate report counts the substitution as filled.

## Why It's Still Broken
Substitution rules live in the warehouse and in counter habits, not in the dealer's account settings, and fill-rate metrics reward shipping something over shipping what was ordered.

## What a Fix Looks Like
Per-dealer substitution rules (never substitute brand, allow same-tier, allow with approval), a pre-shipment text or portal prompt when a substitution is proposed, and a fill-rate report that separates as-ordered from substituted fills. A small model predicts which dealers accept which substitutions, from past refusals.

## Who Feels the Pain
Tire dealers and their customers; wholesalers' customer-service desks handling refused deliveries and returns.

## Impact If Fixed
If refused or returned substitutions fell by ~half from ~3% of lines (estimate), a wholesaler delivering ~10,000 lines a day would avoid ~150 return trips daily.
