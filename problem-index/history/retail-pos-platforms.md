# History: Retail POS Platforms

**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Primary Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** [[origins/supermarket-chains/profile|Supermarket Chains]]
**Episode Tier:** 1
**Transferable Pattern:** A platform can hold the exact data a hard capability requires and still not build it, because the business model that funds the platform is not paid for building it.

> **Wave-assignment note.** The category's ancestry is Wave 2 — it exists to produce the row the 1974 scan made possible. But the category as it is sold today, to the merchants this vault studies, was built in Wave 6. Two origin events, thirty-five years apart, and this file treats both.

## Before

A cash register before the scanner was a mechanical or early-electronic adding machine with a locked drawer. A cashier read a price stamped or ink-jetted onto each item and keyed it in by hand. Every keystroke was a chance to undercharge, overcharge, or key the wrong department code. Checkout speed was bounded by typing, and a price change meant physically re-stamping stock on the shelf.

Behind the register, the store had no item-level view of itself at all — see [[origins/supermarket-chains/origin-story|the origin story]] for the full account of what that fog cost.

## The Origin Event — two of them, thirty-five years apart

**June 26 1974, 8:01am.** The category's founding fact belongs to its parent, not to it: an NCR scanner and register read a 10-pack of Wrigley's Juicy Fruit at a Marsh Supermarket in Troy, Ohio, and a store learned for the first time what it had actually sold. **Retail POS Platforms is the category that exists to keep producing that row, for everyone who is not a supermarket chain.** NCR was the scanner vendor at Troy and remained a dominant proprietary POS hardware vendor for the next three decades, later acquiring Radiant Systems in 2011 for $1.2 billion to extend that position into hospitality and specialty retail.

**April 2012 → 2013.** The category's *modern* founding event is a cluster, not a moment, and it is worth being precise about what each piece actually did:

| Year | What arrived | What it solved |
|---|---|---|
| **Feb 2009** | Square founded by Jack Dorsey and Jim McKelvey, after McKelvey lost a $2,000 sale for want of a way to take a card | Card acceptance for a merchant too small to get a traditional merchant account |
| **2010** | Square's card reader ships | The same, made physical and free |
| **Oct 2010** | Clover Network incorporated (Beatty, Speiser, Schulze, Zheng); launches April 2012 as a cloud-based Android POS | A general-purpose cloud register, sold through a payments processor's sales channel rather than a software company's |
| **Dec 2012** | Clover agrees to be acquired by First Data | The payments industry buys its way into the software layer, rather than a software company building the payments stack |
| **Aug 2013** | Shopify — e-commerce only since its 2006 launch as the Snowdevil snowboard store's own platform — ships Shopify POS | The online store's inventory and catalogue extended into a physical till |

Lightspeed (founded 2005, Montreal, under Dax Dasilva) is the odd one out and belongs in the same cluster for a different reason: it targeted specialty retail and hospitality specifically, where Square's generic register was a poorer fit, and grew by acquisition — MerchantOS (2013), the Belgian POSIOS (2014), Amsterdam's SEOShop (2015) — into a multi-channel platform before going public in 2019.

## What Became Cheap

**Twice, and not the same thing each time.**

In 1974, what became cheap was *identifying* an item — turning it into a database row. In the 2010s, what became cheap was *becoming a merchant who could accept a card at all*. Before Square, a card-present merchant account required an underwriting relationship, a monthly minimum, often a multi-year contract and a physical terminal lease. Square's 2.75%-per-swipe model, confirmed in the press by late 2011, collapsed that into a free reader and a flat percentage with no signup.

**Note what stayed expensive across both events: making a decision from the data.** The row existed in 1974. The subscription exists now. The capability to act on either — what to reorder, what to mark down — did not travel with the price drop.

## How It Was Actually Solved — and what it actually is

The mechanism the category runs on is not a software mechanism. It is a **payments mechanism wearing a software front end.**

Square, Clover and their peers give away or steeply discount the point-of-sale software because the software's job is to be the on-ramp to a card-processing relationship, where the real margin sits. This is why Clover was bought by a card processor (First Data, later folded into Fiserv in 2019) rather than the other way around, and why the category's cheapest tier is consistently the free or near-free one: the till is the distribution channel for the payment rail, not a product sold on its own economics.

**That inversion explains the vault's own diagnosis of the category, stated in its hub note without knowing the ancestry:** *"Merchandising decisions, which are what actually determine whether an independent retailer survives, are made in spreadsheets alongside the software."* A payments-funded product is built to be adopted by the widest possible number of merchants at the lowest possible friction. Open-to-buy planning and markdown optimisation are the opposite of that — narrow, analytically heavy, valuable only to a merchant who already has volume worth optimising. Nothing in the payments-first business model rewards building it.

## The Trade-Off

**Distribution was traded for depth, and the trade was structural, not a choice any one vendor made.**

Enterprise retailers have run markdown optimisation and demand-planning software for roughly two decades — the vault's own analysis records the capability as mature and unpackaged for anyone below enterprise scale. *(I could not independently verify a clean founding date for that enterprise category in this session — trade press commonly cites vendors including ProfitLogic and later Oracle Retail Demand Chain products from the early-to-mid 2000s. Treat the company-level history as unverified and the qualitative claim — mature, enterprise-only, never repackaged down-market — as the vault's own established finding, not new research.)*

The reason it never moved down-market is not secrecy. It is that the vendors who reach the hundreds of thousands of independent merchants are payments companies, and a payments company is paid on transaction volume, not on the sophistication of the decision that produced the transaction.

## Why There Is No Fight Worth Naming — and the one exception

Square, Clover, Shopify POS and Lightspeed did displace an incumbent generation of proprietary terminal vendors, and the clearest evidence is defensive: **NCR itself split in 2023** into NCR Voyix (software and digital commerce, including the POS business) and NCR Atleos (ATM and self-service hardware), completed October 16 2023 — effectively conceding that the hardware-terminal business and the software business no longer belonged in the same company. That is a real contest, but it was fought and settled on **distribution cost**, not on capability: cloud-and-tablet POS won because it was cheaper to sell and install, not because it computed anything the proprietary terminals could not.

**No comparable contest exists over the harder capability — merchandising intelligence.** Nobody is fighting to own markdown optimisation for independents, because nobody has found a way to charge for it that survives contact with a merchant whose whole software budget is the payments fee they already resent paying.

## What's Still Open

- [[problems/retail-pos-platforms/high-impact|🔴 Markdown Timing and Depth]] — the enterprise-grade capability that never came down-market
- [[problems/retail-pos-platforms/low-impact-1|🟡 Specialty Product Catalogue Enrichment]]
- [[problems/retail-pos-platforms/low-impact-2|🟡 Multi-Channel Inventory Reconciliation]]
- [[niches/retail-pos-platforms/pos-payments-merchant-services/profile|POS & Payments Merchant Services]] — the business model this whole file is about
- [[niches/retail-pos-platforms/specialty-retail-merchandising/profile|Specialty Retail Merchandising]]
- [[niches/retail-pos-platforms/multichannel-inventory-accuracy/profile|Multi-Channel Inventory Accuracy]]
- [[niches/retail-pos-platforms/merchant-underwriting-risk/profile|Merchant Underwriting & Risk]]

## The Transferable Pattern

> **Before assuming a data-rich platform will eventually build the intelligent feature on top of its own data, find out what the platform is actually paid for. If it is paid for something else — a payment rail, a subscription seat, a marketplace take rate — the intelligent feature is a cost centre to that business, not a roadmap item, no matter how obviously valuable it looks from outside.**

Retail POS platforms are the cleanest case in this vault of a capability sitting *directly on top of* the data that would enable it, unbuilt, for over a decade, for a reason that has nothing to do with technical difficulty. An FDE evaluating "why hasn't the incumbent built this yet" should always ask what the incumbent's actual revenue line is before assuming the answer is neglect.

**Sources:** Smithsonian Institution and Wikipedia, *Universal Product Code* (June 26 1974 scan); NCR Corporation and Wikipedia, *NCR Voyix* (Radiant Systems acquisition 2011; 2023 split, completed Oct 16 2023); Wikipedia, *Block, Inc.* (Square founding Feb 14 2009, McKelvey's $2,000 sale, 2.75%-per-swipe fee reported Oct 2011); Wikipedia, *Clover Network* (incorporated Oct 15 2010, launched April 2012, First Data merger agreement Dec 28 2012, Fiserv acquisition of First Data July 2019); Wikipedia, *Shopify* (founded 2006 as Snowdevil, POS announced Aug 2013); Wikipedia, *Lightspeed Commerce* (founded 2005, acquisitions 2013–2018, IPO March 2019); this vault's `industries/retail-pos-platforms.md` and `origins/supermarket-chains/the-mechanism.md`.
