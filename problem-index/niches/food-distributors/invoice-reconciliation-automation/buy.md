# AP Automation Adapted for Catch-Weight and Promotional Pricing

**Niche:** [[niches/food-distributors/invoice-reconciliation-automation/profile|Invoice Reconciliation Automation]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AP automation platforms (Bill.com, AvidXchange, Stampli) handle invoice capture and approval workflows but cannot perform three-way matching on catch-weight line items where the PO, receiving, and invoice all show different weights — the most common discrepancy type in food distribution.
**Tags:** #data-integration #automation #compliance #quick-win

## The Problem
In catch-weight food distribution, a single line item on a PO might say "50 cases of beef strip loins at $8.50/lb" — but the actual weight of 50 cases varies from 2,800 to 3,200 lbs. The receiving dock weighs the delivery and records 3,050 lbs. The supplier's invoice shows 3,080 lbs (their warehouse weight). Now three-way matching must reconcile three different weights: PO estimated weight, receiving actual weight, and invoice weight. Standard AP automation performs exact three-way matching (PO = receiving = invoice) and flags everything that does not match exactly. In food distribution, nothing matches exactly on catch-weight items, so 100% of catch-weight line items are flagged as discrepancies — drowning the real discrepancies in noise.

## What Already Exists
Bill.com and AvidXchange provide invoice capture, approval routing, and basic three-way matching. Stampli adds AI-powered coding and GL line allocation. SAP Business One and NetSuite provide ERP-integrated three-way matching. None support tolerance-based catch-weight matching (accept the invoice weight if it is within 2% of receiving weight), catch-weight price recalculation (the PO price was $8.50/lb — does the invoice calculate correctly at invoice weight x unit price?), or the concept of promotional allowance offsets (the invoice includes a $0.50/lb credit line that offsets the base price).

## The Customization Gap
A food distribution AP adaptation needs: (1) tolerance-based catch-weight matching with configurable thresholds by product category (beef: 2% weight tolerance, produce: 5% count tolerance), (2) catch-weight price verification (does invoice total = invoice weight x agreed unit price, within rounding tolerance?), (3) promotional allowance tracking as a separate ledger item that cross-references against supplier promotional calendars, (4) short-ship credit auto-detection (PO said 50 cases, receiving recorded 47, did the invoice charge for 47 or 50?), and (5) exception-only workflow where clean matches are auto-approved and only genuine discrepancies route to the AP clerk.

## Target Customer
AP managers at food distributors processing 200+ catch-weight invoices/week. Approximately 1,500-2,500 US distributors in this category. Price point: $500-$1,500/month.

## Impact If Solved
False discrepancy alerts from catch-weight matching eliminated (currently 80-90% of all "discrepancies" are within normal weight tolerance). AP clerk time reduced by 50-60% as they focus on genuine discrepancies rather than noise. Invoice processing speed improves from 3-5 days to 1-2 days, allowing the distributor to capture early-payment discounts worth 1-2% on $50M+ in annual purchases.
