# B2B Commerce Platforms

## Profile
**Category:** Digital Commerce
**Market Size:** ~$14B US business-to-business ecommerce platform and enablement software
**Tech Maturity:** Consumer patterns applied to a different problem — SAP Commerce, Adobe Commerce B2B, BigCommerce B2B, Oracle, Salesforce and the industrial marketplaces have built B2B storefronts on architecture designed for consumer retail. The defining requirements of business purchasing — customer-specific pricing, entitlements, approvals and procurement integration — sit awkwardly on top of it.
**Workforce:** Implementation consultants, catalogue and product data specialists, pricing and contract administrators, integration engineers, inside sales support, customer success managers

## Key Pain Themes
Every business customer has their own prices. Contract pricing, volume tiers, customer-specific catalogues, entitlements that vary by contracting entity and location, and a distributor's negotiated terms produce a pricing surface that is customer times product times quantity times date, and it must be resolved in milliseconds at page load. Systems built for a single list price with promotions handle this by extension rather than by design, which is why customer-specific pricing performance is the most common reason a B2B storefront feels slow and why quotes still route to inside sales. Around it sit two burdens: procurement integration, where a large customer buys through their own purchasing system and expects punchout and electronic ordering that differs by their platform; and product data, where industrial catalogues run to hundreds of thousands of items with technical attributes that determine whether the right part is findable at all. Inside sales reps quote from spreadsheets, and catalogue managers maintain data that never becomes complete.

## Current Tech Landscape
Enterprise suites dominate large deployments with long implementations. Mid-market platforms have added B2B capability to consumer foundations with varying success. Punchout and electronic data interchange integration is handled by specialists like TradeCentric and remains a per-customer project. Product information management is a mature adjacent category and is unevenly adopted, which is why catalogue quality varies so widely. Search in industrial catalogues is a known weak point where part numbers, cross-references and technical specifications matter more than relevance ranking. Quote-to-cash workflow is frequently outside the commerce platform entirely, sitting in the ERP or in email.

## Problems
- [[problems/b2b-commerce-platforms/high-impact|🔴 High Impact: Customer-Specific Pricing and Entitlements at Scale]]
- [[problems/b2b-commerce-platforms/low-impact-1|🟡 Low Impact: Procurement System Integration]]
- [[problems/b2b-commerce-platforms/low-impact-2|🟡 Low Impact: Industrial Catalogue Data Quality]]
- [[problems/b2b-commerce-platforms/worker-life-1|🟢 Worker Life: Inside Sales Rep Quoting from a Spreadsheet]]
- [[problems/b2b-commerce-platforms/worker-life-2|🟢 Worker Life: Catalogue Manager Maintaining Product Data]]
- [[problems/b2b-commerce-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/b2b-commerce-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
B2B commerce differs from consumer commerce in a way the platforms have never fully internalised: the buyer is a repeat purchaser with a known entitlement, buying known parts on a predictable cycle, under a negotiated agreement. Almost nothing about consumer discovery and merchandising applies. What matters is reorder accuracy, part findability, price correctness and procurement fit — and those are the areas where the platforms are weakest, because they inherited an architecture built to help a stranger discover a product.
