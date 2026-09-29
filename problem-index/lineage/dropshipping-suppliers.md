# Lineage: Dropshipping Suppliers

**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Oberlo, first shipped as "Ali Importer" — a Shopify app that copied AliExpress listings into a store and kept their stock and prices updated
**Builder:** Oberlo
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Drop shipping is older than the web: a retailer takes the order and a supplier ships it. What the web changed was the distance. A merchant in one country could sell, from a hosted storefront, goods listed by a supplier in another, and never see them.

AliExpress, launched by the Alibaba Group in 2010, made that practical at small scale. It gathered small Chinese sellers offering goods to international buyers one unit at a time, with a listing page for each. A merchant could take an item from that page, put it on their own store at a markup, and buy it from the supplier only when a customer had paid.

The listing page was the only interface. Every product was copied into the store by hand. Every order was typed back into AliExpress by hand. And the supplier's stock and price moved without notice, so the store went on selling things that were out of stock or had just become unprofitable.

## What Got Built

A Shopify app that treated a supplier's listing as a live source rather than something to copy once.

Tomas Šlimas, who co-founded Oberlo, described the manual loop the team ran on their own store: every morning, exporting the day's orders from Shopify as a CSV, sending the file to suppliers, and waiting for tracking codes to come back. Products sourced from AliExpress kept running out of stock and changing price. The team built a tool, first called **Ali Importer**, that imported AliExpress products into a Shopify store and **updated stock levels and prices automatically**.

It launched on the Shopify App Store with only those two things — import, and inventory-and-price sync. Order fulfilment automation came later. The product was renamed Oberlo.

## Who Built It, And Why Them

**Oberlo**, a Vilnius, Lithuania company; secondary profiles give the founding year as 2015 and list five co-founders, among them Tomas and Andrius Šlimas. Šlimas has said he started his first dropshipping store in 2014 and that it later reached $3 million in annual revenue before he sold it.

That is the reason it was them. **AliExpress sold to buyers; Shopify sold storefronts; neither was paid to join the two.** The only people who felt the whole gap every morning were merchants running both at once, and this team was one of those merchants. The app's first feature set is exactly the list of things that had cost them money: re-keying products, and selling items that no longer existed at a price that no longer held.

Shopify completed its purchase of Oberlo UAB on **28 April 2017**, for $17.2 million in cash according to its own quarterly filing. It shut the app down in June 2022.

## What It Cost

Oberlo synchronised **what the supplier said**, not **what the supplier did**.

Stock and price are the fields on a listing page, so those were what a merchant-built tool could track. Whether an order shipped on time, arrived intact or matched its photographs was not on the page, and was never part of the first design. The integration layer that platforms like AutoDS, Spocket and CJ Dropshipping sell today descends from that shape: catalogue import and stock sync as the baseline feature, with supplier performance summarised as a rating.

Synchronisation against a listing is also only as fresh as the last check of it. A supplier who stops carrying a product does not announce it; the listing simply changes, and the merchant learns on the next update, or from an unfulfillable order.

## What You Still Touch

Every "import product" button in a dropshipping app is Ali Importer's first feature, and every oversold item is the gap between a listing and a warehouse.

- [[problems/dropshipping-suppliers/low-impact-1|🟡 Catalogue and Stock Synchronisation]] — the problem Ali Importer was built for, still unsolved at the latency it chose
- [[problems/dropshipping-suppliers/high-impact|🔴 Supplier Reliability Is Unmeasured]] — the field that was never on the listing page
- [[niches/dropshipping-suppliers/catalogue-and-stock-sync/profile|Catalogue & Stock Synchronisation]]
- [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/profile|Stock Accuracy & Oversell Prevention]]
- [[niches/dropshipping-suppliers/supplier-selection-and-reliability/profile|Supplier Selection & Reliability Signals]]

**Sources:** Oberlo podcast, *Oberlo Dropshipping: How Repeat Failure Inspired the Oberlo App* (Šlimas on the CSV order loop, stock-outs and price changes, "Ali Importer", launch with import and inventory/price sync only, first store 2014, $3M-revenue store) — this is the company's own account, not independent corroboration; SEC EDGAR, Shopify Q2 2017 financial statements exhibit (acquisition of Oberlo UAB completed 28 April 2017, $17.2 million cash); SaleHoo and Tracxn company profiles (Vilnius, founded 2015, five named co-founders; June 2022 shutdown) — secondary; Wikipedia, *AliExpress* (launched 2010, Alibaba Group; small sellers offering to international buyers). ⚠️ **Not established:** the exact date Ali Importer first appeared on the Shopify App Store and the date of the rename to Oberlo; the "founded 2015" year rests on secondary profiles only. A widely repeated $15 million acquisition price conflicts with Shopify's filing and is not used. The stated reason for the 2022 shutdown (Shopify's fulfilment-network focus) is speculation in secondary blogs and is omitted. How Oberlo technically read AliExpress stock and prices was not established.
