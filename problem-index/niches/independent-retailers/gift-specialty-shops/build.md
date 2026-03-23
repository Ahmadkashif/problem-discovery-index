# Trade Show Buying Advisor Based on Store Sales Patterns

**Niche:** [[niches/independent-retailers/gift-specialty-shops/profile|Gift & Specialty Shops]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mobile app the gift shop owner opens at a trade show booth that instantly answers: "Based on what sells in my store, how likely is this product to move? What price point and quantity should I order?" — turning a gut-feel buying decision into a data-informed one.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Gift shop owners make their biggest financial decisions at trade shows — placing $10,000-50,000 in orders across 50-100 vendors over 3-4 days. These decisions are based on the owner's intuition about what their customers will buy, informed by years of watching products succeed or fail on their shelves. Experienced owners develop a sense for which products fit their store's aesthetic, price point, and customer base — but this intuition is inconsistent under trade show pressure (hundreds of products, limited time, vendor sales pitches). New owners lack this intuition entirely and over-buy products that look appealing but don't match their customer base. Neither experienced nor new owners have access to their sales data at the trade show — it's locked in their POS system back at the store.

## Why Nobody Has Built This
Building a trade show buying advisor requires: (1) historical POS data showing which products succeeded and failed at the specific store, (2) product attribute extraction from wholesale catalogs (category, price point, material, style, color palette), (3) a model that maps product attributes to store-specific sales success, and (4) a mobile interface usable at a trade show with poor wifi. The product attribute challenge is the hardest: wholesale product descriptions are unstructured text that must be normalized into features. The market is fragmented — each store has its own success patterns that don't generalize cleanly to other stores.

## What to Build
A mobile app that connects to the store's POS (Square, Shopify, Lightspeed via API) and maintains a profile of what sells: top categories, price point distribution, successful brands, seasonal patterns, and attribute-level preferences (the store sells well in earth tones but not neons; ceramic items outperform plastic). At the trade show, the owner scans a product barcode or enters basic attributes (category, price, material), and the app scores the product's predicted success at their specific store. High-confidence recommendations include suggested order quantity based on the store's historical sales velocity for similar products. The model trains on the store's own buying history — what was bought, what sold through, what was marked down.

## Target Customer
Gift shop owners who attend 2-4 trade shows per year and place $20,000-100,000 in annual wholesale orders based on intuition, currently with no access to their sales data during buying decisions.

## Impact If Built
Reduces dead stock by 20-30% by preventing poor buying decisions at trade shows. For a store with $150,000 in annual inventory purchases, avoiding 20% dead stock recovers $30,000 in working capital. Enables new store owners to make buying decisions with experienced-owner-level intuition within their first year.
