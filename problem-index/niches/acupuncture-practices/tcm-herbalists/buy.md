# Inventory Management Adapted for Bulk Herb Dispensaries

**Niche:** [[niches/acupuncture-practices/tcm-herbalists/profile|Traditional Chinese Medicine Herbalists]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard inventory tools track SKUs and quantities but cannot handle bulk herb dispensaries where products are measured by weight, have variable shelf lives, and require lot-level sourcing traceability.
**Tags:** #time-series-forecasting #linear-regression #tabular-ml #automation

## The Problem
A TCM herb dispensary stocks 150-300 individual herbs as dried bulk material, granules, or tinctures. Inventory is tracked by weight (grams), not units. Shelf life varies by herb and storage conditions. Each batch may come from different farms or regions with varying potency. Practitioners need to track lot numbers for quality and recall purposes, reorder at weight-based thresholds, and cost formulas based on current per-gram pricing. Generic inventory management tools model discrete units, not bulk weight-based materials.

## What Already Exists
Square for Retail, Lightspeed, and inFlow Inventory handle general retail and restaurant inventory. Some have bulk/weight-based features for food service. QuickBooks Commerce handles basic inventory tracking. None understand TCM-specific requirements: herb-specific expiration tracking, potency grading by source region, lot-level traceability for FDA-regulated dietary supplements, or formula-based consumption forecasting.

## The Customization Gap
The inventory system needs: weight-based tracking with automatic deduction when formulas are compounded, herb-specific shelf life alerts (not generic "90 days"), lot tracking linked to supplier COAs (Certificates of Analysis), reorder forecasting based on formula compounding patterns (not just depletion rate), and per-gram cost tracking that updates formula pricing in real time. This is a vertical adaptation of food-service bulk inventory logic combined with pharmaceutical lot-tracking requirements.

## Target Customer
TCM practitioners running in-house dispensaries with $30,000-100,000 in annual herb inventory, currently tracking stock on spreadsheets or notebooks.

## Impact If Solved
Reduces herb waste from expiration by 20-30%, prevents stockouts that force formula substitutions, and provides per-formula cost visibility that enables accurate pricing — most practitioners underprice herbal formulas by 15-25%.
