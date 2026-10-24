# Pilot Measurement Kits From A/B Testing Platforms

**Niche:** [[niches/grocery-stores/fresh-department-ordering/profile|Fresh Department Ordering]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Experimentation platforms already measure treatment effects with matched controls; a chain's fresh-ordering pilot needs the same discipline with shrink and in-stock measured together.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to set each fresh item's store order before the truck is cut, and whoever cuts the most shrink at an unchanged in-stock rate takes the account.

## The Problem
Every fresh-ordering sale is decided by a store pilot, and every vendor measures its own pilot. Chains compare decks built on different control stores, different shrink definitions and different in-stock measures.

## What Already Exists
Experimentation and test-and-learn platforms (Mastercard's Test & Learn, Optimizely-style A/B tooling, in-house causal inference teams at the largest chains) that match test and control stores and estimate lift with confidence intervals.

## The Customization Gap
The fresh version needs matched controls on fresh mix, volume and supplier, not just region. It needs a shrink definition built from receiving, sales and cull records that the chain controls rather than the vendor. It needs in-stock measured from shelf scans or zero-sales runs, so a shrink cut bought with empty shelves shows up. And it needs a pre-registered decision rule, so the pilot ends with a number both sides accept.

## Target Customer
Chain replenishment and finance teams evaluating two or more fresh-ordering vendors.

## Impact If Solved
A standard pilot readout could shorten vendor selection from ~9 months to ~4 (estimate), and stop a chain from paying for a shrink cut that was really ~2 points of lost in-stock.
