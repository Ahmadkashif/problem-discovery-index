# Lineage: Restaurant Suppliers

**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the distributor order guide — a per-account list of the items a restaurant habitually buys, keyed to the distributor's own item numbers, from which the sales rep takes the weekly order
**Builder:** no single builder
**Builder in vault:** n/a
**Verification:** partial — see Sources

## The Problem That Came First

A restaurant does not shop. It reorders.

A kitchen buys the same few hundred items week after week — the same fryer oil, the same portioned 8-oz chicken breast — and changes a handful of them when the menu changes. The distributor's cost is not in finding customers for those items. It is in **capturing the repeat order, correctly, from a chef who has twenty minutes between lunch and prep**, across 80–150 accounts per rep.

So the job was built around a person: a rep stood in the kitchen and walked the list, and the order was only as accurate as the rep's memory of "the usual".

## What Got Built

No single tool, no founding moment: a **list** — the order guide — and devices built for other industries, bent to carry it.

| Tool | Builder | Place | Year | What it was for |
|---|---|---|---|---|
| Sysco, a nine-company roll-up | John Baugh and eight distributor owners | Houston | **1969** | Scale in broadline foodservice distribution — the buyer of everything below |
| Portable handheld order-entry terminal | Telxon (then Electronic Laboratories) | Texas, later Akron | **early 1970s** | Built for grocery, drug and hardware ordering and inventory — not foodservice |
| Telxon handheld + payphone upload | Sysco sales consultants, as users | field | **1980s–1990s** | Rep keys the order guide into the handheld, dials a 1-800 number from a payphone |
| Foodservice GS1 US Standards Initiative | GS1 US with 55 manufacturers, distributors and operators | US | **Oct 5 2009** | GTINs and GLNs, with manufacturers asked to put GTINs *on order guides* by Q3 2010 |
| FSMA 204 Food Traceability Rule | FDA | US | **Nov 21 2022** | Lot-level traceability records for listed foods; compliance now **July 20 2028** |

The telling row is 2009: forty years after Sysco, the standards body was still asking manufacturers to print a globally unique product number on the order guide — because until then, the guide spoke only in each distributor's private item code.

## Who Built It, And Why Them

**Nobody built the order guide as a product.** It is an output of whatever system a house runs, and no source checked dates its origin.

The devices that carried it were built for grocery. Telxon's own SEC filings describe its handhelds as sold, from the early 1970s, to "retailers and wholesalers in the grocery, drug and hardware industries" for order entry and inventory. Foodservice inherited a store-shelf reorder tool; it fitted because the shape was the same — a known list, a quantity column, a transmit button.

The reason no foodservice-specific builder emerged is commercial rather than technical. Broadline distributors compete on the relationship and on the private item number itself. **A proprietary code makes a restaurant's guide expensive to move to a competitor.** Nobody in the chain had a reason to fund an open artefact until manufacturers wanted clean product data across all distributors — which is what the 2009 GS1 initiative was.

## What It Cost

The guide optimises the reorder and punishes everything else. It records what an account bought, not what it stopped buying or started buying elsewhere; a line that quietly goes to zero looks identical to a slow week. And because the rep owns the walk-through, **the customer knowledge lives in a person**, and leaves when the person does.

Private item codes cost a second thing: finding anything *not* on the guide means translating a chef's words into one house's SKU vocabulary.

## What You Still Touch

Every ordering app — BlueCart, Cut+Dry, Pepper, a broadliner's portal — opens on the order guide. New screen, same list.

- [[problems/restaurant-suppliers/high-impact|🔴 Sales Rep Account Churn Prevention]] — the guide records purchases, not drift
- [[problems/restaurant-suppliers/low-impact-2|🟡 Restaurant-Specific Catalog Search for Smallwares and Equipment]] — the cost of private item vocabularies
- [[problems/restaurant-suppliers/worker-life-1|🟢 Sales Rep Route Planning and Visit Prioritization]] — the rep-carried walk-through, still the unit of work
- [[niches/restaurant-suppliers/order-intake-automation/profile|Order Intake Automation]]
- [[niches/restaurant-suppliers/deviated-pricing-rebate-administration/profile|Deviated Pricing & Rebate Administration]]

**Sources:** company-histories.com, *SYSCO Corporation* (1969 merger of nine companies led by John Baugh, $115M combined sales); Sysco LABS, *A History of Ordering at Sysco — From Payphones to Ecommerce* (Telxon handhelds, binder catalogue, payphone 1-800 upload, later laptop over phone jack — oral recollections, decades given only as "1980s & 1990s" and "2000s"); Telxon Corp. Form 10-K filings on SEC EDGAR, FY1994–FY1998 (incorporated 1969 as Electronic Laboratories, successor to a 1967 Texas business, renamed 1974, Akron HQ 1978, handhelds to grocery/drug/hardware from the early 1970s); GS1 US announcement via Restaurant Business and GS1 US *Foodservice Standards Initiative* pages (Oct 5 2009, 55 companies, GTINs on order guides by Q3 2010); FDA, *FSMA Final Rule on Requirements for Additional Traceability Records*, and Federal Register compliance-date extension of Aug 7 2025 (July 20 2028). ⚠️ **Not established:** when or by whom the printed foodservice order guide originated — searched, no source found; the builder of the 2000s laptop order-entry programme (omitted from the table for that reason); any claim that Telxon built a foodservice-specific product. The vault hub's mention of Rutherford & Associates and Encompass route-accounting systems was not independently checked and is not used here.
