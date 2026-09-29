# Lineage: E-Commerce Sellers

**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Amazon Marketplace's single detail page — one product page per item, on which third-party sellers' offers sit beside Amazon's own ("SDP" internally, launched November 2000)
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Amazon wanted other people's inventory without other people's storefronts.

By 1999 it had a catalogue, a checkout and a large audience, but its selection was limited to what it stocked. Used, rare and out-of-print books, and the long tail of goods it would never buy, sat with small sellers who had no way to reach its customers.

The first two answers failed. In Jeff Bezos's own account, Amazon launched **Auctions**, and "not many customers came." Auctions became **zShops** in September 1999, "basically a fixed price version of Auctions." Both put sellers in a separate area of the site with their own listings. A customer on the page for a book did not see them. Discovery happened on the product page, and the sellers were somewhere else.

## What Got Built

The seller was moved onto the product page.

Amazon Marketplace opened in **November 2000**. Internally, Bezos wrote, it was called **SDP, for Single Detail Page**: "the idea was to take our most valuable retail real estate — our product detail pages — and let third-party sellers compete against our own retail category managers."

The mechanic is that there is **one page per product, not one per seller**. A third party did not create a listing; it attached an offer to the page Amazon already had. Amazon's March 2001 press release describes used and collectible items appearing on the same detail pages where Amazon sold them new, with a seller able to list a single item in under a minute from a "Sell yours here" button on that page. In the first four months, the release says, monthly gross merchandise sales more than tripled; Bezos later wrote that sellers accounted for 5% of units within the first year.

## Who Built It, And Why Them

**Amazon**, and the reason is that it owned the page.

A standalone marketplace — eBay being the obvious one — could offer a seller a storefront and buyers who came to browse it. Only a retailer that had already built millions of product pages, and drew customers to them, could offer a seller a place *on the page the customer had already chosen*. The design is shaped by that asset. Amazon kept the page, the product description, the reviews and the checkout, and rented sellers a slot in them.

It also explains the risk Amazon accepted. SDP set outside sellers against Amazon's own category managers on Amazon's own pages. Auctions and zShops had protected the retail business by keeping sellers elsewhere, and failed for that reason. The single detail page gave up the protection to get the traffic.

## What It Cost

**The seller does not own the page.** Content on a shared product page is merged from many contributors, so a seller's title, images or bullet points can be overruled by someone else's. Selling the same item on several channels means maintaining separate listings under separate rules, because only one of those channels has a single page per product.

**Several sellers on one page means one of them is shown first.** Customers see a default offer, and sellers compete to be it on price, fulfilment and performance metrics. That contest is decided by Amazon and cannot be inspected by the seller. The metrics that decide it are the same ones that decide whether an account stays open.

**And the costs arrive in Amazon's categories, not the seller's.** Referral fees, fulfilment fees, storage and advertising are each charged by the platform in its own report. None of them is a per-SKU profit.

## What You Still Touch

Every "Other sellers on Amazon" box, every lost Buy Box and every suppressed listing is the single detail page doing what it was designed to do.

- [[problems/ecommerce-sellers/low-impact-1|🟡 Multi-Channel Listing Synchronization and Optimization]] — one channel with a shared page, the rest without
- [[problems/ecommerce-sellers/worker-life-1|🟢 Seller Account Health Anxiety and Suspension Risk]] — the metrics that decide who is shown
- [[problems/ecommerce-sellers/high-impact|🔴 True Profitability Tracking per SKU Across Channels]] — fees itemised by the page's owner
- [[niches/ecommerce-sellers/marketplace-trust-safety/profile|Marketplace Trust & Safety Analytics]]
- [[niches/ecommerce-sellers/repricing-software-analytics/profile|Repricing & Advertising Software Analytics]] — software built to win the default offer

**Sources:** Jeff Bezos, 2014 letter to Amazon shareholders, as republished on aboutamazon.eu, *Amazon Marketplace* (Auctions → zShops → Marketplace; "Internally, Marketplace was known as SDP for Single Detail Page" quote; 5% of units in the first year); Amazon press release, March 2001, *Amazon Marketplace a Winner for Customers, Sellers and Industry* (launch November 2000; used and collectible items on the same detail pages; "Sell yours here"; listing in under 60 seconds; sales more than tripled in four months); Wikipedia, *Amazon Marketplace* (launch date given as 6 November 2000; referral-fee structure); DM News, *Amazon.com opens zShops* (September 1999 zShops launch; segregated structure); this vault's `history/ecommerce-sellers.md` (cited as vault material, not independent corroboration). ⚠️ **Not established:** the launch month of Amazon Auctions (commonly given as March 1999, not checked against a primary source); the date the "Buy Box" name and its default-offer algorithm first appeared, and whether multi-seller default selection existed at the 2000 launch; the names of the Amazon staff who designed SDP. The claim that shared-page content is merged across contributors reflects current Amazon practice, not a dated 2000 design document.
