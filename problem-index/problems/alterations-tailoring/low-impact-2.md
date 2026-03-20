# Pricing Estimation by Garment Complexity

**Industry:** [[alterations-tailoring|Alterations & Tailoring]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every alterations shop posts a price list on the wall, but the actual price for any specific garment depends on fabric type, construction quality, lining, number of layers, and alteration complexity — factors that only the master tailor can evaluate, making pricing inconsistent when anyone else handles intake.
**Tags:** #gradient-boosting #cnns #linear-regression #transfer-learning #feature-engineering #cross-validation #evaluation-metrics

## The Problem
Alterations pricing is supposed to be simple: "Hem pants: $15. Take in waist: $20." In reality, hemming unlined cotton chinos takes 10 minutes and hemming fully-lined wool trousers with a blind-stitched cuff takes 45 minutes — yet both are "hem pants." The price list on the wall represents minimums for the simplest version of each alteration. The actual price depends on: fabric type (silk requires hand-sewing; leather requires special equipment), garment construction (lined vs. unlined, number of seam layers at the alteration point), alteration complexity (simple hem vs. hem with taper, take in waist at the center back vs. reconstructing side seams), and number of alterations interacting (shortening a jacket requires adjusting every horizontal detail — pockets, buttons, darts). Master tailors assess these factors instantly at intake and quote accordingly. When front desk staff or less experienced workers handle intake, they default to the wall price, either undercharging for complex work or, knowing the wall price is wrong, making uncomfortable calls to the tailor mid-appointment.

## What Already Exists
Generic POS systems support item-based pricing. Some alterations-specific apps (iRoar) provide category-based pricing. No system evaluates the specific garment to adjust pricing based on construction, fabric, and complexity. The wedding dress market has attempted standardized pricing by alteration type, but even there, a "take in bodice" varies enormously by construction method.

## The Customisation Gap
A garment-aware pricing system needs to: (1) classify the garment from photos (garment type, fabric category, construction features — lined, boned, beaded, layered), (2) assess alteration complexity based on the specific garment's construction at the alteration points, (3) generate a price quote that reflects actual work time rather than category averages, (4) explain the price to the customer ("Your trousers have a cuffed, blind-stitched, lined hem — this requires hand-finishing that takes 3x longer than a standard machine hem"), (5) build a per-shop pricing model that reflects the shop's specific rate and typical completion times, and (6) track actual time vs. estimated time to refine future pricing accuracy.

## Impact If Solved
Eliminates pricing inconsistency — customers quoted the same price for the same work regardless of who handles intake. Increases revenue by 15-25% on complex garments that were previously underpriced at wall-chart rates. Reduces customer disputes over pricing by providing transparent, garment-specific justifications. Enables non-tailor intake staff to quote accurately, freeing the master tailor from interruptions during sewing.
