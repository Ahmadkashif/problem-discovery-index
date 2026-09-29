# Lineage: Public Adjusters

**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**The tool:** Xactimate — the property-repair estimating program first written in 1986, and the regional unit-cost price list it prices every line item against
**Builder:** Xactware
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A property claim is settled on a repair estimate, and before the PC every estimate was a private document.

A contractor or adjuster walked the loss, listed the work room by room and priced it from his own experience of local labour and materials. The carrier's adjuster did the same and reached a different number. **There was no shared price for "remove and replace drywall"**, so every disagreement was an argument about whose memory of the market was right — and the policyholder had no way to judge either.

The public adjuster exists to fight that argument on the policyholder's side, for a contingency fee. What the fight lacked was a common unit.

## What Got Built

A program and, more importantly, a price book.

Xactimate breaks a repair into unit-cost line items. For each one it supplies labour cost, material cost, labour productivity, equipment, labour burden and overhead, and contents replacement value. A 2018 trainer's white paper counts **more than 19,500 line items** and pricing for **468 markets** in the US and Canada. It says a new price list is generated monthly in most regions.

The price list is the artefact that matters. From 1989, the same paper says, Xactware built its figures from market surveys — nearly 20,000 a month of randomly selected contractors, suppliers and service providers — plus completed estimates returned to it through its claims system. **An estimate became a list of standard line items multiplied by a published regional price**, and two estimates of the same loss became directly comparable, item by item.

## Who Built It, And Why Them

Xactware — founded by a restoration contractor, not by an insurer or an adjuster.

By the company's own account, as given in search summaries of its "About us" page, **James Loveland**, who ran one of Utah's largest building-restoration firms, began writing the software in the basement of his home in Orem in **May 1986**, for his own restoration crews.

**That is why it came from the repair side.** A restoration contractor doing insurance work is paid only when a carrier accepts his estimate. He is the party who most needs his number in a form the adjuster will not dispute, and the one who already knows repair as a list of priced tasks. Building the tool served both his estimating speed and his collections — an inference from his trade, not a documented statement of his motive.

Carriers then adopted it. The white paper says insurers took up both program and price list "as a means to show their settlements are being made in accordance with an 'industry standard'", and that 23 of the top 25 US property insurers use Xactware's claims tools. **ISO**, the insurer-backed rating organisation, acquired Xactware in 2006; it now sits under Verisk. Loveland died in 2005.

The public adjuster was the third party to arrive. The vault's own note says a PA "must write in it to negotiate with a carrier adjuster at all."

## What It Cost

**The public adjuster argues in the other side's language.** The price book is owned by a company under the carriers' rating organisation, and the white paper describes carriers applying custom price lists with "suppressed pricing and a limited number of line items" — a restoration-side claim, attributed here rather than adopted.

The standard fixed the prices, not the scope. Which items, what waste factor, whether overhead and profit are included — all of that stays a judgement. So the dispute moved from "what does this cost?" to "which line items does this loss need?" And the white paper says line items are added on nearly every update but never removed.

## What You Still Touch

Every PA supplement is a diff between two Xactimate files:

- [[problems/public-adjusters/high-impact|🔴 Damage Documentation Thoroughness and Claim Maximization]] — the hidden damage that has to become a line item to get paid
- [[niches/public-adjusters/supplement-tracking/build|Estimate Comparison and Dispute Resolution Engine]] — comparing "100-300 line items each" in "proprietary ESX format"
- [[niches/public-adjusters/xactimate-automation/fix|Estimate Inconsistency Across Adjusters]] — two PAs, same property, 15–30% apart
- [[niches/public-adjusters/property-repair-estimating-crossref/profile|Property Repair Estimating Data]] — the layer that publishes the unit costs

**Sources:** Mark Whatley, *Xactimate: The History & The Future*, Actionable Insights research white paper (April 2018), hosted by United Policyholders, PDF read directly, for 1986, the line-item fields, 19,500 line items, 468 markets, monthly price lists, the 1989 survey method and 20,000 monthly surveys, 23 of the top 25 insurers, the "industry standard" and "suppressed pricing" quotations, the never-removed line items, ISO's 1971 formation, the 2006 acquisition and Verisk. The author is an Xactimate affiliate trainer writing for the restoration side; his carrier-practice claims are attributed, not adopted. Deseret News, "Xactware's success not just estimated" (June 22 2008), fetched, for the 1986 founding and the 2006 ISO merger. Search summaries of xactware.com's "About us" page for James Loveland, May 1986, the Orem basement, his restoration firm, his own crews and his 2005 death; the page itself returned 403, so these are **not read at source**. This vault's public-adjusters hub, niche and problem notes (vault material). ⚠️ **Not established:** what machine or operating system the first Xactimate ran on — one search summary says early Macintosh, unconfirmed and omitted; the price or terms of the 2006 acquisition (the Verisk press release returned 404 and the Insurance Journal report timed out); when public adjusters as a group adopted Xactimate. The Daily Herald's 2013 profile returned no article text.
