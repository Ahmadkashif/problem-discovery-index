# Inventory Management Adapted for Salon Back-Bar & Retail Split

**Niche:** [[niches/hair-salons-independent/retail-product-sales/profile|Retail Product Sales & Inventory]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard inventory systems track products as a single pool but salons split the same products between back-bar (used during services) and retail (sold to clients) — and can't track depletion from both channels.
**Tags:** #time-series-forecasting #linear-regression #tabular-ml #automation #data-integration

## The Problem
A salon stocks a professional shampoo in two locations: a liter on the back-bar for stylists to use during services, and retail bottles on the shelf for clients to purchase. The same product depletes through two channels at different rates. Inventory systems see "shampoo: 15 units in stock" but don't distinguish between back-bar and retail inventory. The salon can't track how much product stylists are using per service (is the new hire using twice as much shampoo as the senior stylist?), can't forecast when to reorder based on combined depletion rates, and can't calculate the true product cost per service.

## What Already Exists
Square for Retail, Lightspeed, and Vagaro track product inventory by SKU with sales-based depletion. Some salon-specific tools (SalonScale, Vish) track back-bar color product usage by weight. None handle the dual-channel problem: tracking both retail sales depletion AND back-bar usage depletion for the same SKU, with different reorder triggers for each channel.

## The Customization Gap
The inventory system needs dual-channel product tracking: (1) separate back-bar and retail inventory counts for shared products, (2) back-bar depletion tracking based on service volume (auto-deducting estimated product usage per service type), (3) retail depletion from POS sales data, (4) combined reorder forecasting that accounts for both channels, (5) per-stylist back-bar usage analytics (identifying over-users), and (6) product cost-per-service calculations using actual back-bar consumption data.

## Target Customer
Salon owners spending $2,000-8,000/month on professional products who cannot distinguish between back-bar usage and retail shrinkage in their current inventory system.

## Impact If Solved
Identifies 15-20% in back-bar product waste from over-usage, provides accurate per-service product costs for pricing decisions, and prevents retail stockouts that lose $500-2,000/month in potential sales.
