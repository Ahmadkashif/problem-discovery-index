# Grocery & Same-Day Delivery

**Parent Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Category:** High Market Share

## Profile
**Market Size:** $15-20B
**Share of Parent Industry:** ~18%
**Digital Adoption:** Medium — large grocery chains use Instacart or proprietary platforms, but independent grocers and regional chains rely on basic dispatch tools or manual coordination
**Target Buyer:** Grocery delivery operations manager or dark store fulfillment lead
**Automation Potential:** High — order batching, driver routing, substitution logic, and delivery window management are all optimization-ready workflows

## What Makes This a Distinct Niche
Grocery delivery operates under constraints that parcel delivery doesn't face: temperature-sensitive products requiring cold chain from store to door (frozen, refrigerated, ambient separation), time-critical delivery windows (2-hour or same-day), high product substitution rates (15-25% of items are out of stock and require real-time substitution decisions), and order composition complexity (a single order may span produce, frozen, bakery, and household — requiring intelligent vehicle loading). The unit economics are challenging: average grocery delivery order value is $80-120, and delivery cost is $8-15, leaving thin margin for the delivery operation. Batching multiple orders per driver per trip is essential to profitability.

## Current Tools & Gaps
Instacart provides an end-to-end platform for grocers who outsource delivery. DoorDash DashPass and Uber Eats provide marketplace-based grocery delivery. For grocers operating their own delivery: Onfleet and Tookan provide basic delivery dispatch. None of these tools optimize for grocery-specific constraints: temperature zone vehicle loading, substitution communication during picking, or multi-order batching that respects cold chain timing (frozen items can't sit in a van for 90 minutes while other orders are delivered).

## Problems
- [[niches/last-mile-delivery/grocery-same-day/build|🔨 Build: Temperature-Aware Multi-Order Batching Engine]]
- [[niches/last-mile-delivery/grocery-same-day/buy|🛒 Buy: Grocery-Specific Route Optimization with Cold Chain Constraints]]
- [[niches/last-mile-delivery/grocery-same-day/fix|🔧 Fix: Real-Time Substitution Communication During Picking]]
