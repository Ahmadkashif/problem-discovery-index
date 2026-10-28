# Collision Estimating Adapted to Wholesale Arbitration

**Niche:** [[niches/wholesale-auto-auctions/arbitration-post-sale-claims/profile|Arbitration & Post-Sale Claims]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Insurers estimate repair cost from photos at scale; wholesale arbitration still takes the buyer's shop estimate at face value.
**Tags:** #cnns #transfer-learning #object-detection #large-language-models #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to settle buyers' post-sale claims under the NAAA guidelines without taking the car back, and whoever settles the largest share of granted claims by price adjustment rather than unwinding the sale takes the account.

## The Problem
Whether a defect clears the NAAA threshold ($800, or 2% at $50,000 and up), and how much the adjustment should be, both turn on the repair cost. The desk sees a shop estimate and sometimes photos. It has no independent figure.

## What Already Exists
Collision estimating platforms used by insurers and body shops (CCC, Mitchell, and photo-based AI estimating such as Tractable, named from recall) produce line-item estimates from photos with labour times and parts prices. Total-loss and valuation analytics for insurers are mapped at [[niches/auto-body-shops/total-loss-valuation-providers/profile|Total Loss Valuation Providers]].

## The Customization Gap
Arbitration needs what collision tools leave out:
- mechanical and electrical defects (engines, transmissions, modules) priced from parts and labour guides rather than panels;
- ADAS calibration costs, now arbitrable;
- the per-defect threshold test, with each defect priced separately as the guidelines require;
- wholesale labour rates rather than insurer-negotiated retail ones;
- an output that states which Appendix I category each line falls under, so the desk can cite it.

## Target Customer
Arbitration and assurance teams at the national auctions; assurance underwriters pricing seller protection.

## Impact If Solved
An independent estimate settles the "does it clear $800?" argument on the first call. If a fifth of claims are disputed on cost and each dispute adds three days and two calls (estimates), an auction with 10,000 claims a year saves ~4,000 admin calls and ~6,000 days of cases left open.
