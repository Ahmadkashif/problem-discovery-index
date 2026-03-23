# Size-Curve Optimizer for Small-Batch Apparel Buying

**Niche:** [[niches/independent-retailers/clothing-boutiques/profile|Independent Clothing Boutiques]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tool that recommends the optimal size distribution for each style order based on the boutique's own sales data — so the owner stops guessing "how many smalls vs. mediums vs. larges" and stops losing $3,000-8,000 per season on wrong-size dead stock.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
When a boutique owner orders a new style, they must specify quantities per size (typically XS-XL or 0-14, 5-8 sizes). Standard wholesale minimums require ordering a pre-set size curve (e.g., 1-2-2-2-1 across S-M-L-XL-XXL) that may not match the boutique's actual customer size distribution. A boutique whose customers skew toward M-L ends up with unsold XS and XXL units. An experienced buyer develops intuition for their store's size curve, adjusted by garment fit (oversized styles sell larger, fitted styles sell smaller, stretchy fabrics are more forgiving) — but this intuition is never formalized. A new buyer uses vendor-recommended curves and sits on wrong-size inventory that cannot be sold even at markdown.

## Why Nobody Has Built This
Enterprise apparel retail (Nordstrom, Zara) runs sophisticated size-curve optimization models, but these require millions of transactions across thousands of SKUs. A boutique with 2,000 SKUs selling 5-30 units per style doesn't generate enough data per style for traditional size-curve analysis. The model must learn the store's customer size distribution and combine it with garment-level fit characteristics (gleaned from return reasons, customer feedback, and vendor fit notes) to recommend per-style size curves. This requires pooling data across similar boutiques — a network effect that no platform currently enables.

## What to Build
A size-curve recommendation engine that: (1) analyzes the boutique's POS data to determine the store's base size distribution (what percentage of total sales are S/M/L/XL), (2) adjusts the base curve per style based on garment attributes (fit type, fabric stretch, brand sizing tendency), (3) recommends quantities per size for each new order, (4) tracks post-purchase outcomes (which sizes sold through, which remained) to continuously refine the model, and (5) for boutiques with insufficient individual data, pools anonymized size distribution data from similar boutiques (same customer demographic, same apparel category). Integrated with Faire and other wholesale platforms so the recommendation appears at the point of order.

## Target Customer
Clothing boutique owners ordering 100-500 styles per year who currently guess at size distributions and lose 15-25% of margin to wrong-size dead stock.

## Impact If Built
Reduces size-related dead stock by 30-50%. For a boutique purchasing $100,000 in annual wholesale, with 20% current dead stock from size mismatches, this recovers $6,000-10,000 in working capital and preserved margin per year.
