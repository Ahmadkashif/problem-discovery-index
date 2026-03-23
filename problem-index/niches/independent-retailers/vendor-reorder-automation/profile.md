# Vendor Reorder Automation

**Parent Industry:** [[industries/independent-retailers|Independent Retailers]]
**Category:** Highly Automatable

## Profile
**Market Size:** $10-15B (embedded in inventory management costs — represents the labor, cash flow, and opportunity costs of manual reordering)
**Share of Parent Industry:** ~3% (as a cost center)
**Digital Adoption:** Low — most independent retailers manage vendor relationships and reorder decisions entirely through email, phone calls, and trade show visits, with no systematic reorder point monitoring
**Target Buyer:** Store owner or buyer responsible for maintaining stock levels across 20-100 vendor relationships
**Automation Potential:** High — reorder decisions follow deterministic rules (when inventory drops to X, order Y units from vendor Z) that are executed manually because POS reorder point features are unused or unavailable

## What Makes This a Distinct Niche
An independent retailer maintains relationships with 20-100 wholesale vendors, each with different minimum order quantities, lead times, payment terms, and ordering methods (some take orders via Faire, some via email, some only via phone, some through sales reps who visit monthly). The owner makes reorder decisions by walking the store, noticing empty spots on shelves, and mentally comparing what's low against vendor minimums and delivery schedules. This visual-reorder-by-walking approach misses items in back stock (the shelf looks full but the stockroom is empty), fails to anticipate upcoming demand (holiday items need to be ordered 6 weeks ahead), and doesn't optimize order timing (combining items to meet vendor minimums reduces shipping costs). The reorder process consumes 4-8 hours per week of the owner's time and is the single largest source of both overstock and stockouts.

## Current Tools & Gaps
POS platforms offer reorder point functionality (set a minimum quantity, get an alert when stock drops below it), but independent retailers rarely configure it — setting reorder points for 2,000-5,000 SKUs is a daunting initial setup task. Faire provides reorder suggestions for products originally purchased on their platform but doesn't cover the 50-70% of inventory sourced through other channels. No tool aggregates reorder needs across all vendors, optimizes order timing against vendor minimums and lead times, and generates purchase orders in vendor-specific formats.

## Problems
- [[niches/independent-retailers/vendor-reorder-automation/build|🔨 Build: Intelligent Reorder Engine Across All Vendor Channels]]
- [[niches/independent-retailers/vendor-reorder-automation/buy|🛒 Buy: Faire-Style Reorder Suggestions Extended to Non-Faire Vendors]]
- [[niches/independent-retailers/vendor-reorder-automation/fix|🔧 Fix: Vendor Minimum Order Aggregation and Timing Optimization]]
