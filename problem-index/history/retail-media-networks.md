# History: Retail Media Networks

**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Primary Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**Secondary Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**Origin Parent:** [[origins/supermarket-chains/profile|Supermarket Chains]] *(the data lineage)* · [[origins/ad-holding-companies/profile|Ad Holding Companies]] *(the auction mechanism)*
**Episode Tier:** 1
**Transferable Pattern:** A measurement asymmetry can compound for fifty years through a sequence of individually reasonable decisions, arriving at a market where the party selling the product also grades whether the product worked.

## Before the Shelf Was a Ledger

A supermarket in 1973 knew what it had ordered and, once a week or so, what a cashier had rung up by category — groceries, produce, meat — because that was as fine a grain as a mechanical register could report. It did not know, item by item, what had actually sold. A manufacturer paying for a shelf-end display had no way to learn whether the display had moved product, only whether the retailer said it had been installed. The two parties who needed to trust each other's numbers — retailer and brand — each held a different, partial, unauditable account of the same shelf.

## The Origin Event

**8:01am, June 26 1974, Marsh Supermarket, Troy, Ohio.** A ten-pack of Wrigley's Juicy Fruit gum, 67 cents, became the first item sold anywhere via a Universal Product Code scan. The scanner did not know it was creating an advertising business. It was installed to speed up the checkout line and reduce pricing errors — a labour and accuracy problem, not a marketing one.

What it produced as a byproduct was the first machine-readable, item-level record of what actually sold, by store, by hour. Nobody at Marsh's or NCR or the UPC standards committee was building a data business in June 1974. The data business arrived five years later, uninvited by anyone who had touched the checkout project.

**1979.** **John Malec and Gerald Eskin** founded **Information Resources, Inc. (IRI)** in Chicago. IRI's model was to place scanning equipment in grocery stores and sell the resulting purchase data back to the consumer packaged goods manufacturers whose products the scanners had just rung up. By 1993, slightly more than half of IRI's revenue came from its Infoscan syndicated data service. The shopper had generated the data by shopping. The retailer had captured it as a side effect of computerising the checkout line. IRI's contribution was the idea that the manufacturer would pay to see it — and would pay well, because until 1979 a brand's only view of its own sell-through was whatever the retailer chose to report.

That is the first step in the chain this file is about, and it is worth being precise about its shape: **each actor did something locally sensible.** The retailer wanted a faster checkout. IRI wanted to sell a data product nobody else could supply. The manufacturer wanted to know, finally, whether its trade spend was working. None of them was assembling a measurement asymmetry on purpose.

## What Became Cheap

**Knowing what sold, item by item, without asking anyone.** Before the scanner, that fact lived in a cash drawer and a stack of register tapes. After it, it lived in a queryable table, and — because IRI existed — it could be sold to the one party who had always wanted it and never had it: the brand.

## How the Chain Closed — the mechanism worth stating precisely

The scanner (1974) supplied the *what*: an item-level record of sale. It did not supply the *who*. A shopper who bought the gum was, to the register, identical to every other shopper who bought the gum. That gap — sale without identity — is [[series/eras/wave-02-departmental-item-level|Wave 2]]'s own recorded blind spot, and it stayed open for roughly twenty years.

**Loyalty cards, through the 1990s**, closed it. A card number let a retailer join a purchase record to a specific, repeat, identifiable shopper across visits. Kroger's loyalty programme and its data-science subsidiary (later 84.51°, formed from Kroger's 2003 dunnhumby-style analytics ambitions) is the clearest example of a retailer treating loyalty data as an asset in its own right rather than a discount mechanism. The card was pitched to shoppers as a way to save money. Its actual function, from the retailer's side, was attaching identity to the table the scanner had already built.

**Retail media, from the 2010s and at scale through the 2020s**, is the fourth step, and it is the one this file exists to name precisely: **the retailer sells the brand the ability to target the shopper whose data the scanner captured and the loyalty card identified — and the retailer also measures, reports and is paid on whether that targeting worked.** Amazon's advertising business is the reference implementation; Walmart Connect, Kroger Precision Marketing, Roundel and Instacart Ads are the fast-following peer set; retail media's share of global digital ad spend reached roughly a fifth of the total by 2024, and this vault's own industry note records margins of 70–90% on it — a profit rate that is itself a clue about who is grading the exam.

Trace the four steps in sequence and each is a small, defensible extension of the one before it:

1. **1974 — the scan.** Speed up the checkout. Byproduct: item-level sale data.
2. **1979 — IRI.** Sell that byproduct back to the manufacturer who generated the demand for it.
3. **1990s — the loyalty card.** Attach identity to the byproduct, sold to the shopper as a discount.
4. **2010s–20s — retail media.** Sell the brand access to the now-identified shopper, and report the result inside the same system that sold the ad and rang the sale.

**No single step looks like misconduct.** A faster checkout, a data product, a loyalty discount, a targeted ad — each was a reasonable business decision made by a different set of people, often decades apart, none of whom was designing the endpoint. The endpoint is nonetheless a market structure in which the party being measured is the only party positioned to run the measurement, and — as this vault's own niche research on the industry documents — routinely chooses not to run it in the way that would produce a smaller number.

## The Trade-Off

This vault's `problems/retail-media-networks/high-impact.md` states the resulting number without softening it: a retailer "shows the ad and rings the sale in the same system, and still reports a ROAS that counts shoppers who searched the brand by name and subtracts nothing for the organic sale the ad displaced." That is last-click measurement — the same convention this vault's programmatic and affiliate-network history traces to DoubleClick's 1996 cookie tooling — but applied inside a closed loop where, unlike open-web programmatic, **every fact needed to compute the honest number is already sitting in one company's own database.**

This is the detail that separates retail media from the rest of the vault's adtech history. Programmatic's declined join is expensive to close because identity is fragmented across companies that do not trust each other with it. Retail media's is not expensive to close. The retailer already has the purchase record, the ad-exposure record and a shopper identity that persists across visits, all under one roof. **Computing organic-versus-incremental sales and reporting it honestly requires no new technology.** It requires a public company to publish a number that shrinks the profit pool its own retail media division reports to Wall Street.

The vault's industry note names the second, quieter cost of the same trade: every sponsored placement occupies a shelf slot that might otherwise have shown a better-matched or higher-margin product, and that cost lands in basket size and repeat-visit behaviour over months — a horizon no campaign report covers, while the ad revenue lands the same week it is booked. The category merchant, accountable for category profit, absorbs a cost nobody has attached a number to.

## What's Still Open

- [[problems/retail-media-networks/high-impact|🔴 The Only Closed Loop in Advertising, Spent Counting Sales That Were Already Happening]] — this file's endpoint, stated as the vault's own top problem
- [[niches/retail-media-networks/incrementality-and-cannibalisation/profile|Incrementality & Cannibalisation]] — the honest number, and why nobody with the data has published it
- [[niches/retail-media-networks/the-platform-layer/profile|The Platform Layer]] — most networks license the same auction technology and differentiate only on data
- [[niches/retail-media-networks/trade-spend-and-supplier-funding/profile|Trade Spend & Supplier Funding]] — the pre-digital funding relationship retail media descended from
- [[niches/retail-media-networks/the-category-merchant/profile|The Category Merchant]] — the person absorbing the cost this file's chain never priced
- [[niches/retail-media-networks/ad-load-economics/profile|Ad Load Economics]] — what a quarter-advertising search page costs in basket size, over a horizon no campaign report covers

## The Transferable Pattern

> **When a business appears to be grading its own homework, look for the chain of prior, individually reasonable decisions that put the answer key in its hands. Rarely was any single step in that chain a bad-faith move — the asymmetry accretes, one locally sensible extension at a time, and by the time it is visible as a business model, undoing any one step would require unwinding revenue nobody who benefits from it has an incentive to give back.**

An FDE evaluating a company that both delivers a service and measures whether the service worked should ask, before anything else: **who else could plausibly compute this number, and could they get the data if they wanted to?** If the answer is "no one else has the data," the honest measurement is a genuine, buildable product — a clean room, a mandated third-party audit, an incrementality-testing layer sold *to the brand* rather than to the retailer. If the answer is "someone else could get the data but has no reason to want the smaller number," you are not looking at an engineering gap. You are looking at retail media's fifty-year chain, one industry later.

**Sources:** Smithsonian Institution object record and History.com, *This Day in History — June 26* (UPC first scan, Marsh Supermarket, Troy OH, June 26 1974); Wikipedia, *Information Resources, Inc.* (IRI founding 1979, John Malec and Gerald Eskin, Infoscan revenue share by 1993); Wikipedia, *Retail media* (retail media at ~21% of global digital ad spend, 2024; offsite retail media emergence, early 2020s); this vault's `industries/retail-media-networks.md`, `origins/supermarket-chains/legacy.md` and `series/eras/wave-02-departmental-item-level.md` (loyalty-card identity join, 1990s); ANA 2023 Programmatic Media Supply Chain Transparency Study and ANA/K2 Intelligence 2016 transparency report (via this vault's `origins/ad-holding-companies/` files) for the broader measurement-asymmetry pattern this file traces into retail media specifically. *(Kroger/84.51° founding detail and precise Amazon Advertising launch date could not be independently re-verified this session — a direct Wikipedia article for Amazon Advertising returned no result, and the aboutamazon.com history page was unreachable. Treat both as approximate pending re-verification.)*
