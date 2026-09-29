# Catalogue & Stock Synchronisation

**Parent Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Category:** High Market Share
**Contested on:** This niche is not terminal — knowing whether the item still exists and making the listing worth buying are different contests with different winners, and they are stated separately in the sub-niches below.

## Profile
**Market Size:** ~$2.4B US
**Share of Parent Industry:** ~20% of category revenue
**Digital Adoption:** High — universal feature, poor outcomes
**Target Buyer:** Platform integration engineering
**Automation Potential:** High — both halves are mechanisable

## What Makes This a Distinct Niche
Catalogue import and stock sync are the baseline feature of every platform in the category, and merchants still oversell items their supplier stopped carrying weeks ago. The connection between a supplier's catalogue and a merchant's storefront is the platform's core mechanism — everything a merchant sells passes through it — which makes it the second-largest concentration of contested value in the category.

It is also **not terminal**. Writing the contested statement for this niche produces two sentences rather than one, and they describe different companies winning. One fight is over whether the merchant's storefront reflects what the supplier actually has, which is a latency and reconciliation problem: detect the change fast, reconcile two systems that disagree, and never take an order for something that is gone. The other is over whether the listing is worth buying at all, which is a content and differentiation problem: ten thousand merchants receive the identical supplier photograph and description, and the contest is who can turn a shared source into a page that converts. A competitor can lead decisively on either while being ordinary at the other. The two contests are stated in the sub-niches.

## Current Tools & Gaps
Scheduled polling of supplier feeds, catalogue import with mapping, storefront connectors, and bulk listing tools. The gaps: polling latency that is adequate for slow goods and useless for volatile ones; no reconciliation when the supplier and the platform disagree; identical content across every merchant selling the item; no enrichment path; and no handling of variants, discontinuations and substitutions.

### Contested sub-niches
- [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/profile|🎯 Stock Accuracy & Oversell Prevention]]
- [[niches/dropshipping-suppliers/listing-content-differentiation/profile|🎯 Listing Content Differentiation]]

## Problems
- [[niches/dropshipping-suppliers/catalogue-and-stock-sync/build|🔨 Build: The Baseline Feature That Does Not Work]]
- [[niches/dropshipping-suppliers/catalogue-and-stock-sync/buy|🛒 Buy: Data Integration Practice]]
- [[niches/dropshipping-suppliers/catalogue-and-stock-sync/fix|🔧 Fix: The Feed That Went Quiet]]
