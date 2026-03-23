# Buyer-Profile-Based F&I Product Recommendation Engine

**Niche:** [[niches/rv-dealerships/rv-finance-extended-warranty/profile|RV F&I Product Sales]]
**Industry:** [[industries/rv-dealerships|RV Dealerships]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool recommends which F&I products to prioritize for a specific buyer based on their RV type, usage pattern, financing terms, and demographic profile — the F&I manager presents a generic menu to every customer.
**Tags:** #gradient-boosting #recommendation #tabular-ml #revenue-impact #automation

## The Problem
An F&I manager has 45-60 minutes to present 6-10 products and close as many as possible. Product selection and sequencing matter enormously: leading with extended warranty for a first-time buyer makes sense (they're worried about breakdowns); leading with interior protection for a full-timer makes sense (they'll live on those surfaces daily). But F&I managers present the same menu in the same order to every buyer because no tool recommends a personalized approach. Top performers develop intuition for which products to lead with for which buyer — this is tacit knowledge that takes 2-3 years to develop.

## Why Nobody Has Built This
F&I product attachment data is highly sensitive — dealers don't share it publicly, and F&I product providers (IWS, Protective, NWAN) see only their own product penetration, not the full menu performance. Building a recommendation engine requires aggregating deal-level data across hundreds of dealers: which products were presented, in which order, to which buyer profile, on which unit type, and which were purchased. This dataset doesn't exist in aggregated form.

## What to Build
A recommendation engine that takes the buyer's profile (first-time vs. experienced, usage intent, financing terms, demographic data), the unit being purchased (type, age, price, manufacturer warranty terms), and the dealer's historical attachment rate data, then recommends: (1) which products to present (skip irrelevant ones), (2) in which order (highest-value/highest-attachment-probability first), and (3) with which pricing (optimal monthly payment impact). The system learns from every closed deal: which presentations converted and which didn't.

## Target Customer
RV F&I managers who present 6-10 products per deal and currently achieve 1.5-2.5 products per deal (PPD) when industry best practice is 3.0-4.0 PPD.

## Impact If Built
Increases products-per-deal from 1.5-2.5 to 2.5-3.5, adding $800-$1,500 per deal in F&I revenue. For a dealer closing 20 deals per month, this translates to $16K-$30K in additional monthly F&I profit — often the difference between a profitable and unprofitable month.
