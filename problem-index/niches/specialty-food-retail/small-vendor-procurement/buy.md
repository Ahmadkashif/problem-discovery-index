# Automated Reorder Calculation from POS Data

**Niche:** [[niches/specialty-food-retail/small-vendor-procurement/profile|Small-Vendor Procurement Operations]]
**Industry:** [[industries/specialty-food-retail|Specialty Food Retail]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** POS systems track what sold, but none automatically calculate how much to reorder from each vendor — accounting for shelf life, vendor lead times, and minimum order quantities.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #data-integration #revenue-impact

## The Problem
The store buyer walks the shelves daily, eyeballing what's low and estimating how much to reorder. POS data shows exactly what sold in the last week, last month, and same period last year — but the buyer never looks at it for reorder decisions because there's no tool that converts sales velocity into a reorder recommendation adjusted for: shelf life (order 3 days of supply for bread, 14 days for canned goods), vendor lead time (2-day lead for the local baker, 7-day lead for the olive oil importer), minimum order quantity (the cheese creamery has a $150 minimum), and delivery schedule (vendor delivers Tuesday and Friday only). The buyer re-invents this calculation mentally for each of 50 orders per week.

## What Already Exists
POS systems (Square, Lightspeed, Revel) provide sales reporting. Enterprise grocery demand planning (Blue Yonder, Oracle) generates automated reorder recommendations but costs $100K+ and requires dedicated data teams. Some POS systems offer basic low-stock alerts but don't account for shelf life, lead time, or vendor minimums.

## The Customization Gap
The missing layer is a lightweight reorder engine that sits on top of POS data and vendor metadata: for each product, it knows the sales velocity (from POS), the shelf life (entered once at setup), the vendor lead time, and the vendor minimum. Each morning, it generates: "Order from Baker Joe: 20 sourdough, 10 rye, 15 baguette (delivery Thursday, covers through Saturday). Order from Cheese Creamery: 5 Brie wheels, 3 Manchego (delivery Friday, covers through Wednesday)." The buyer reviews and approves rather than calculating from scratch. Must handle the specialty food store's uniquely volatile SKU mix — seasonal items, new product trials, and vendor supply variability.

## Target Customer
Specialty food store buyers who make 50+ reorder decisions per week based on visual shelf checks rather than sales data, losing 5-8% of potential sales to stockouts on fast-moving items.

## Impact If Solved
Reduces stockout-related lost sales by 30-50% on fast-moving items (worth $20K-60K annually on a $1M store). Cuts spoilage by 15-25% through right-sized ordering based on actual velocity rather than gut estimates. Saves 3-5 hours/week of manual reorder calculation and shelf-walking time.
