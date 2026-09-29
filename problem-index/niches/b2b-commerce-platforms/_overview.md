# Niche Analysis — B2B Commerce Platforms

**Parent Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Entitlement & Price Resolution | 🔵 High Market Share | $3.2B | Low — handled by extension, not by design | Every distributor and manufacturer selling B2B |
| 2 | B2B Storefront Experience | 🔵 High Market Share | $3.6B | High | Repeat account buyers; separately, part searchers |
| 3 | Procurement Integration | 🟠 Low Digitized | $1.6B | Low — standards exist, connection is a project | Integration teams on both sides |
| 4 | Quote to Cash | 🟠 Low Digitized | $1.4B | Very Low — outside the platform entirely | Sales operations and finance |
| 5 | The Inside Sales Rep | 🟣 Underserved Audience | $1.0B | None — quoting from spreadsheets and memory | Sales organisations |
| 6 | The Catalogue Manager | 🟣 Underserved Audience | $800M | None — prioritising by intuition | Catalogue and product data functions |
| 7 | Attribute Extraction | ⚡ Highly Automatable | $1.3B | Low — keyed from manufacturer documents | Product data operations |
| 8 | Purchasing Pattern Intelligence | ⚡ Highly Automatable | $1.1B | None — the most predictable buyer in commerce, unmodelled | The platforms and their customers |

## Why These Niches

Every business customer has their own price for every product at every quantity on every date. Contract pricing, volume tiers, customer-specific catalogues, entitlements varying by contracting entity and location, and negotiated distributor terms produce a pricing surface of customer times product times quantity times date, which must resolve in milliseconds at page load. Systems built for a single list price with promotions handle this by extension rather than by design, which is why customer-specific pricing performance is the most common reason a B2B storefront feels slow and why quotes still route to inside sales. That resolution problem is the largest contested surface in the category.

The storefront **failed the filter as one niche**. The account buyer is a repeat purchaser with a known entitlement reordering known parts on a predictable cycle: the contest is speed and accuracy of reorder, and the competitor is that buyer phoning their rep or ordering through their own procurement system. The part searcher is looking for a specific item in a catalogue of hundreds of thousands, identified by part number, cross-reference or technical specification: the contest is findability against technical data, and the competitor is picking up the phone to ask. One is a workflow problem with almost no discovery in it; the other is a retrieval problem where relevance ranking matters far less than exact identification. Decomposed below.

The two underdigitised areas are both places where a standard exists and the work does not scale. Punchout and electronic ordering have existed for decades and are supported by every platform, and connecting to each large customer's procurement system remains a per-customer project measured in weeks. And quote-to-cash workflow sits outside the commerce platform entirely, in the resource planning system or in email, which is why the highest-value orders never touch the storefront.

The two underserved constituencies are the inside sales rep assembling quotes by hand from a resource planning system, a spreadsheet and their memory of what this customer usually pays, and the catalogue manager keying technical attributes from manufacturer documents into a system that will never be complete, prioritising by intuition.

The automation niches are attribute extraction from manufacturer documentation, which is now straightforward and is still done by keying, and the purchasing pattern corpus — the most predictable buyer in commerce, observed repeatedly under a known agreement, and unmodelled.

## Niches
- [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/profile|🔵 Entitlement & Price Resolution]]
- [[niches/b2b-commerce-platforms/b2b-storefront-experience/profile|🔵 B2B Storefront Experience]]
  - [[niches/b2b-commerce-platforms/reorder-and-account-purchasing/profile|🎯 Reorder & Account Purchasing]]
  - [[niches/b2b-commerce-platforms/part-search-and-selection/profile|🎯 Part Search & Selection]]
- [[niches/b2b-commerce-platforms/procurement-integration/profile|🟠 Procurement Integration]]
- [[niches/b2b-commerce-platforms/quote-to-cash/profile|🟠 Quote to Cash]]
- [[niches/b2b-commerce-platforms/the-inside-sales-rep/profile|🟣 The Inside Sales Rep]]
- [[niches/b2b-commerce-platforms/the-catalogue-manager/profile|🟣 The Catalogue Manager]]
- [[niches/b2b-commerce-platforms/attribute-extraction/profile|⚡ Attribute Extraction]]
- [[niches/b2b-commerce-platforms/purchasing-pattern-intelligence/profile|⚡ Purchasing Pattern Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **B2B Storefront Experience** is not: it names the buying surface rather than a contest, and the two buyers using it have opposite problems. The account buyer knows exactly what they want, has bought it fifty times, and needs it reordered correctly at their negotiated price against their approval rules — a workflow contest with no discovery in it, lost to a phone call or a procurement system. The part searcher does not know what they want in the platform's terms, has a part number from a competitor, a specification from a drawing or a photograph of a broken component, and needs to be told which item in three hundred thousand is the right one — a retrieval and technical-data contest, lost to a phone call to a specialist. The data, the techniques and the definition of success share nothing. Decomposed into two contested sub-niches.

Two candidates were rejected. *Resource planning and order management systems* were rejected because they are a separate enterprise software industry that the commerce platform integrates with rather than competes against. *Two-sided B2B marketplaces* were rejected because their contest is liquidity between many buyers and many sellers, which is covered under the online marketplace industry in this vault.
