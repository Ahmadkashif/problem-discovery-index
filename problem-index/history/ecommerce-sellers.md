# History: E-Commerce Sellers

**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Primary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Secondary Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**Origin Parent:** [[origins/package-carriers/profile|Package Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** Free distribution and cheap fulfilment do not add up to a knowable cost of doing business — they add up to five separate invoices that nobody has ever reconciled into one number, and the seller is the only party positioned to want that number to exist.

## Before the Seller Account

Running a retail business that reached customers outside your own city required capital most people did not have: a merchant account, a payment gateway, warehouse space, a relationship with a shipping carrier, and — until [[series/eras/wave-06-cloud-saas|Wave 6]] made compute a meter rather than a purchase — a server. **E-commerce existed before 2000**, but it was a business for companies large enough to build all of that themselves. There was no equivalent of "becoming a seller" the way there is today; there was building a company.

## The Origin Event — two, in the same year, eleven years apart in consequence

**November 6 2000.** **Amazon Marketplace** opens, letting anyone list a product against Amazon's own catalogue pages and compete for the **Buy Box** — the default seller Amazon shows a buyer. This is the moment "seller" becomes an occupation rather than a business someone built from nothing: the storefront, the traffic, and the payment infrastructure were now rented, not owned.

**September 19 2006.** **Fulfillment by Amazon (FBA)** launches. A seller could now ship inventory to an Amazon warehouse and let Amazon pick, pack, ship, handle returns and staff customer service — the entire physical half of retail, outsourced for a per-unit fee. By 2020, sellers had used FBA to complete more than **5.5 billion orders in the US** alone.

**2006, the same year.** **Shopify** launches publicly (Tobias Lütke, Daniel Weinand, Scott Lake), built out of the team's own frustration running **Snowdevil**, a snowboard e-commerce store, on the software available in 2004. Where Amazon Marketplace rented a seller Amazon's traffic, Shopify rented a seller their own storefront software, and nothing else — no built-in demand, no fulfilment network, no customer base to compete inside.

**These are not the same origin event wearing two names.** They are two different bets about which piece of retail infrastructure was worth renting, made in the same twelve months, and this industry has run on both lineages simultaneously ever since — a seller is now either renting an audience (marketplace) or renting a storefront (Shopify/DTC), and the niches in this vault (`amazon-fba-aggregators`, `marketplace-ppc-management` against `shopify-dtc-brands`) split cleanly along that line.

## What Became Cheap

**The capital that used to gate entry to retail.** A marketplace seller needed no warehouse, no fulfilment staff, no payment integration, no server. A Shopify seller needed no development team to build a shopping cart, no systems administrator, no PCI-compliance project. Both routes removed a distinct fixed cost that had previously required a real company to absorb before the first sale.

**What did not become cheap: knowing what any of it actually cost.** [[origins/package-carriers/profile|Package Carriers]]' own legacy note states this almost as a prediction of what would happen downstream: **COSMOS solved "where is it" in 1979; nobody in this chain has solved "what did it actually cost to get there."** Forty-one years later, this vault's hub note for the industry describes exactly that unsolved problem at the level of the individual seller — true per-SKU profitability is "nearly impossible to calculate because costs are fragmented across ad spend, marketplace fees (which change quarterly), return shipping, FBA storage fees, and COGS that fluctuate with supplier pricing and freight rates." The tracking number became a customer expectation nobody questions. What it actually cost to earn that tracking number was never joined back to the sale that paid for it.

## How It Was Actually Solved — partially

A layer of point-solution tooling grew up around each piece of the fragmentation separately — inventory-sync tools, keyword-research tools, repricing engines, review-monitoring dashboards — because each of those problems has a clean, bounded input and output. None of them integrate into a single ledger, because the inputs live in different companies' systems (Amazon's fee schedule, the seller's supplier invoices, the carrier's freight bill, the ad platform's spend report) and none of those companies is incentivised to make its slice legible against the others. This vault's own note for the industry names the workaround directly: sellers "stitch together 5–10 SaaS tools and spreadsheets to approximate what should be a single dashboard." Nobody has built the dashboard because nobody owns all five data sources at once — the seller is the only party who needs the joined number, and the seller is the smallest, least resourced party in the chain.

## The Trade-Off

**Where a seller chooses to sell determines whether "the cost of being found" shows up as a fee or as an ad budget — not whether that cost exists.** A marketplace seller pays Amazon a referral fee and, increasingly, an advertising spend, in exchange for demand Amazon already generated. A Shopify seller pays nothing to a platform for distribution, and instead must manufacture all of it — which by [[series/eras/wave-09-programmatic|Wave 9]] meant buying it back from Meta, Google Shopping and TikTok, the same discovery-is-the-scarce-asset problem this vault's wider Wave 5 thesis identifies, now paid per click rather than per sale. Both routes converge on the same fact from opposite directions: **distribution was never free, it only became free to list.** The invoice for actually being found never disappeared; it moved.

## The Contest, and the Graveyard It Produced

Cheap capital in the 2020–2021 period produced a real, dated contest with a real, dated casualty: the **Amazon FBA aggregator**. The thesis, funded at enormous scale, was that a portfolio of small owner-operated Amazon brands, bought up and run through shared software, supply-chain and advertising infrastructure, would outperform any single founder-run brand — arbitrage between the multiple a small brand sold at and the multiple a diversified portfolio could command. **Thrasio**, founded 2018, became one of the fastest-growing US companies by this measure, and the model spawned a wave of imitators (Perch, Elevate Brands, Berlin Brands Group and others), collectively raising billions in acquisition capital through 2021.

**The thesis did not survive rising ad costs, rising capital costs, and Amazon's own unchanged referral-fee and account-health rules — the same fragmentation problem described above, at portfolio scale rather than single-SKU scale.** Public reporting through early 2024 described Thrasio filing for Chapter 11 bankruptcy protection to restructure its debt. *(I could not independently re-verify the exact filing date, debt figure, or current post-restructuring status this session against a primary source — treat the Thrasio bankruptcy as reported rather than confirmed here, and check before it goes in a script.)*

What died was not the marketplace-seller model itself — sellers on Amazon and Shopify alike continue to operate, and FBA order volume kept growing through the period. What died was the **specific thesis that capital and shared software could substitute for the operator-level knowledge of a single brand's unit economics** — the same missing join this file has described throughout, just discovered the hard way, at roll-up scale, by parties who had assumed a spreadsheet could stand in for it.

## What's Still Open

- [[problems/ecommerce-sellers/high-impact|🔴 True Profitability Tracking per SKU Across Channels]] — the missing join, stated as this vault's own top problem for the industry
- [[problems/ecommerce-sellers/low-impact-2|🟡 Amazon PPC Campaign Management at Scale]] — Wave 9's programmatic bidding logic, run by an operator with no bidding desk
- [[problems/ecommerce-sellers/worker-life-1|🟢 Seller Account Health Anxiety and Suspension Risk]] — a platform rule enforced with no visible mechanism and no appeal path a seller can inspect
- [[niches/ecommerce-sellers/amazon-fba-aggregators/profile|Amazon FBA Aggregators]] and [[niches/ecommerce-sellers/amazon-aggregator-diligence/profile|Amazon Aggregator Diligence]] — the roll-up thesis, and what due diligence on it now has to check for
- [[niches/ecommerce-sellers/marketplace-intelligence-platforms/profile|Marketplace Intelligence Platforms]] and [[niches/ecommerce-sellers/repricing-software-analytics/profile|Repricing Software Analytics]] — the point solutions that exist instead of the joined ledger
- [[niches/ecommerce-sellers/3pl-fulfillment-analytics/profile|3PL & Fulfillment Analytics]] — the freight-cost side of the same unsolved join

## The Transferable Pattern

> **When a business rents its distribution from one company and its fulfilment from another and its advertising from a third, ask who is supposed to add those three invoices into one number. If the answer is "the seller, by hand, in a spreadsheet," that is not an oversight — it is the natural consequence of a value chain where every party can see its own slice and no party is paid to reconcile the whole.**

The FBA aggregator boom is the cautionary case: capital assumed the reconciliation problem was already solved because the individual sellers seemed to be managing. It was not solved, it was merely being absorbed, invisibly, by founders working the spreadsheet themselves — and a portfolio model removed exactly the person who had been doing that work by hand.

**Sources:** Wikipedia, *Amazon Marketplace*, *Fulfillment by Amazon*, *Shopify* (via direct article retrieval, Sept 2026); this vault's `industries/ecommerce-sellers.md` and `origins/package-carriers/legacy.md`; public reporting on Thrasio and the Amazon FBA aggregator sector circa 2021–2024, flagged above as unverified in this session and requiring confirmation before use in a script.
