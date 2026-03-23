# Product Inventory System Adapted for Shade-Level Color Tracking

**Niche:** [[niches/hair-salons-independent/color-specialized/profile|Color-Specialized Salons]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Salon inventory systems track product by SKU but not by shade — a salon knows it has "14 tubes of Wella Koleston" but not which of the 120 available shades are in stock, low, or overstocked.
**Tags:** #time-series-forecasting #linear-regression #tabular-ml #automation #data-integration

## The Problem
A color salon stocks 80-200 individual shade tubes across 2-3 color lines. Inventory management at the shade level is a nightmare: some shades (blonde tones) turn over weekly, others (specialty reds) sit for months. Reordering is manual — the salon owner walks the color bar weekly, noting what's low. This "walking inventory" takes 30-60 minutes and misses shades that have just run out but haven't been pulled from the shelf. Standard inventory tools track "Wella Koleston" as a single SKU, not the 120 individual shades within that line.

## What Already Exists
Square for Retail, Lightspeed, and Vagaro include basic inventory management. SalonScale weighs color product to track per-service cost. Beauty distributor ordering platforms (SalonCentric, CosmoProf) handle purchasing. None track inventory at the individual shade level within a color line, forecast shade-level demand based on upcoming appointments, or suggest reorder quantities based on usage patterns.

## The Customization Gap
The inventory system needs shade-level granularity: each shade tube is an individual inventory item with its own usage rate, reorder point, and demand forecast. The system should link shade consumption to booked appointments (if 5 clients are booked for blonde services next week, predict blonde shade consumption), flag overstocked shades for promotional use, and optimize reorder quantities to minimize both stockouts and dead inventory. Integration with distributor ordering APIs for one-click reordering at the shade level.

## Target Customer
Salon owners spending $3,000-10,000/month on color products who currently do manual shelf-walk inventory and experience 5-10 shade stockouts per month.

## Impact If Solved
Reduces color product stockouts by 70-80%, cuts overstock waste by 20-30%, and saves 2-4 hours/week of manual inventory management time.
