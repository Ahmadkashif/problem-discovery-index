# Service-to-Retail Product Recommendation Engine

**Niche:** [[niches/hair-salons-independent/retail-product-sales/profile|Retail Product Sales & Inventory]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system automatically generates personalized product recommendations for salon clients based on the services they received and products used during their appointment.
**Tags:** #recommendation #gradient-boosting #tabular-ml #revenue-impact #ai-agent

## The Problem
A stylist uses a volumizing mousse, heat protectant, and finishing spray during a blowout service. The client loves the result and asks "what did you use?" If the stylist remembers the exact products and recommends them, there's a 40-50% conversion rate. If the stylist is rushed and says "I'll tell you next time" or gives vague recommendations, the conversion drops to near zero and the client buys a competing product at Ulta. This happens 10-20 times per day per stylist. The information needed for the recommendation (which products were used on which client) exists in the stylist's hands but never enters any system.

## Why Nobody Has Built This
The service-to-retail connection requires capturing in-chair product usage data that stylists don't currently log. Building this requires either: (1) getting stylists to document every product used during a service (high friction), (2) inferring product usage from service type (lower accuracy), or (3) creating a frictionless logging mechanism (scan/tap system at the styling station). The salon retail market's fragmentation (thousands of independent salons buying from dozens of brands) makes it unattractive for either POS companies or product manufacturers to build this bridge.

## What to Build
A product recommendation system that: (1) pre-populates likely products used based on service type and stylist preferences, (2) allows one-tap confirmation/modification of products used per service, (3) generates a personalized product list sent to the client via text after their appointment ("here's what we used on your hair today — tap to purchase"), (4) integrates with the salon's POS for in-store purchase or links to online ordering, (5) tracks recommendation-to-purchase conversion by stylist, product, and service type, and (6) provides stylists with client-specific product history at the next visit ("last time you recommended Product X — ask how she liked it").

## Target Customer
Salon owners whose retail revenue is below 10% of total revenue and who employ 3+ stylists with inconsistent product recommendation habits.

## Impact If Built
Could increase salon retail revenue from 5-10% to 15-20% of total revenue, representing $30,000-80,000/year in additional high-margin revenue for a mid-size salon.
