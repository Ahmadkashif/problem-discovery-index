# Lineage: Ecommerce Aggregators

**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Fulfillment by Amazon (FBA) — web-service calls that let a third-party seller stow inventory in Amazon's fulfilment centres and have Amazon pick, pack and ship it, launched September 19 2006
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A small online seller's business used to be a room full of boxes.

Before 2006 a third-party merchant owned the listing and also the work behind it: receiving stock, picking, packing, labelling, taking returns — done in a garage or small unit by the person who knew where everything was.

That made it hard to sell. **A buyer of such a business was buying a lease, a routine and usually the founder's labour** — none of which moves cleanly to a new owner. Small ecommerce businesses changed hands, but they did not do so as a standardised asset class, because the thing being sold was mostly an operation.

## What Got Built

Fulfillment by Amazon, launched on September 19 2006 alongside WebStore by Amazon.

Jeff Bezos described it in the 2006 letter to shareholders in terms that are worth quoting exactly: **"a set of web services API's that turns our 12 million square foot fulfillment center network into a gigantic and sophisticated computer peripheral."** The seller paid 45 cents per cubic foot per month for space. They made web-service calls to tell Amazon that inventory was arriving, to pick and pack items, and where to ship them.

Mechanically, a seller shipped cartons to Amazon once and from then on the orders ran without them. The business shrank to three things that could be written on a page: a product with a supplier behind it, a listing on Amazon's detail page with its reviews and rank, and inventory already sitting in Amazon's network.

## Who Built It, And Why Them

Amazon, because it already had both halves that nobody else combined.

It had the physical network — the 12 million square feet Bezos cited — and it had the marketplace demand that network would serve. It also, by 2006, framed its own infrastructure as something outsiders could call through APIs; the shareholder letter presents FBA in exactly that vocabulary. A third-party logistics firm could offer warehousing, but not the placement on Amazon's own product page. Only Amazon could sell both at once.

Bezos's stated test in the letter was commercial: FBA was "differentiated, can be large, and passes our returns bar."

What Amazon did not set out to build was an acquisition market. That arrived later, as a side effect. **Once fulfilment was Amazon's job, a seller's business became portable** — inventory, listing, trademark and supplier contract. Thrasio, Perch, Branded, SellerX and their peers raised capital to buy those portable businesses by the hundred and run them as portfolios. I could not confirm founding dates for any of them this session and do not give them here.

## What It Cost

**The seller handed Amazon the operation and kept only the claim on the listing.** FBA fees, storage rules, inventory limits and policy changes all sit with the platform, and a business built on FBA has no fallback channel that runs at the same cost.

For the aggregators that cost multiplied. What they paid for — ranking, review velocity, Buy Box share — lived on Amazon's detail page and could be moved by Amazon's decisions rather than the owner's. The industry's underwriting failure is the bill: a multiple of trailing earnings for revenue that depended on things that did not change hands at closing, the founder's supplier relationships and responsiveness among them. Even diligence runs through Seller Central, reporting built for running an account rather than valuing one.

## What You Still Touch

Any listing marked as fulfilled by Amazon is this design, and a large share of the brands behind such listings changed owners without the buyer ever seeing a warehouse. The single detail page the seller competes on is traced in [[lineage/ecommerce-sellers|Lineage: E-Commerce Sellers]].

- [[problems/ecommerce-aggregators/high-impact|🔴 Underwriting Revenue Persistence]] — the price of buying a business whose operation Amazon runs
- [[problems/ecommerce-aggregators/low-impact-1|🟡 Post-Acquisition Migration Without Ranking Loss]]
- [[problems/ecommerce-aggregators/worker-life-2|🟢 Diligence Analyst in Seller Central]]
- [[niches/ecommerce-aggregators/marketplace-policy-risk/profile|Marketplace Policy Risk]] — the dependency FBA created, priced as risk
- [[niches/ecommerce-aggregators/acquisition-underwriting/profile|Acquisition Underwriting]]

**Sources:** Wikipedia, *Fulfillment by Amazon* (launch date September 19 2006, alongside WebStore; no named executive given); Amazon.com 2006 Letter to Shareholders, filed with the SEC as Exhibit 99.1 (sec.gov EDGAR, CIK 1018724) — source of the "computer peripheral" quotation, the 12 million square foot figure, the 45-cent pricing and the "returns bar" test. The aggregator names and the sector's underwriting failure are taken from this vault's `industries/ecommerce-aggregators.md` (vault material, not independent corroboration). ⚠️ **Not established:** WebSearch hit its session cap before this note was researched, so all checks were WebFetch against known URLs. No Wikipedia article for Thrasio exists; thrasio.com gives no founding history; TechCrunch URLs tried returned 404. Founding years, founders and the bankruptcy date of Thrasio and its peers are therefore deliberately omitted. I could not confirm the internal team or executive who designed FBA, nor whether FBA inventory was Prime-eligible at launch — neither is claimed. Nothing here relies on the false "spare capacity" account of AWS.
