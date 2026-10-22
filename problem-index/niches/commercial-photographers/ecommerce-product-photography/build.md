# A Per-SKU Ledger of Image Cost and Outcome

**Niche:** [[niches/commercial-photographers/ecommerce-product-photography/profile|Ecommerce Product Photography]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Brands pay per image without knowing which images, angles and treatments earn their cost on the listing, and studios price per SKU without knowing which SKUs lose them money.
**Tags:** #gradient-boosting #causal-inference #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to deliver more usable images per SKU per dollar, but packshot production and on-model or lifestyle content are won by different studios on different measures: right first time against retailer specifications and the sample's true colour on one side, one consistent brand look across talent, sets and seasons on the other. Decomposed into contested sub-niches below.

## The Problem
A brand orders six images per SKU across a 2,000-SKU season. The studio quotes a flat per-SKU price. Neither side measures what each SKU actually cost to produce (set time, retouch minutes, reshoots) or what its images did on the listing (click-through, conversion, image-related returns). Price negotiations happen every season on averages.

## Why Nobody Has Built This
The data sits in four systems owned by three parties: the studio's capture and retouch logs, the brand's product information system, and the retailer's or marketplace's listing analytics. Each studio sees only its own costs and each brand only its own outcomes, so no one is positioned to join them.

## What to Build
A ledger keyed by SKU and colourway that records image count, shot types, set minutes, retouch minutes, reshoots and rejections from the studio side, and listing metrics and image-related return reasons from the brand side, shared under the brand's control. Models then estimate production cost by product attributes before the season is quoted, and estimate which shot types move conversion by category, adjusted for price, rank and season.

## Target Customer
Ecommerce content directors at brands with seasonal ranges, and the studio directors who quote them.

## Impact If Built
Seasons are quoted on predicted cost rather than averages, unprofitable SKU types are visible before the contract, and brands can stop paying for images that do nothing, a likely 10–20% of shot lists (estimate).
