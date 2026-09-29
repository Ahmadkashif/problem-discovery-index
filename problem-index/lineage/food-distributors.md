# Lineage: Food Distributors

**Industry:** [[industries/food-distributors|Food Distributors]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the GS1-128 case label — a Code 128 barcode carrying GS1 Application Identifiers for GTIN (01), dates (13, 16), lot (10) and net weight (310n / 320n)
**Builder:** Uniform Code Council
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A case of chicken thighs is not a can of soup.

The UPC solved retail identification by assuming every unit of a product is identical: one number, one price, scanned at a till. A foodservice distributor moves cases that break that assumption on three counts. The weight varies case to case and the price follows it. The case has a pack date and a sell-by date that matter more than its brand. And when something goes wrong — a recall, a temperature exception — the question is not *which product* but *which lot*.

A 12-digit number could say none of that. So the variable facts travelled on paper: a handwritten weight, a printed date nobody scanned, a lot code a receiver copied into a ledger if they copied it at all.

## What Got Built

A barcode that labels its own fields.

**GS1-128** — formerly UCC/EAN-128 — sits on **Code 128**, a symbology Computer Identics developed in **1981**. What the numbering bodies added was the **Application Identifier**: a short numeric prefix declaring what the digits after it mean. `(01)` is a GTIN. `(13)` is a pack date, `(16)` a sell-by date. `(10)` is a batch or lot. `(310n)` is net weight in kilograms and `(320n)` net weight in pounds, where the fourth digit *n* says where the decimal point goes. One symbol can string several together, separated by a function character.

For foodservice, the specific artefact is the **Foodservice GS1 US Standards Initiative's Voluntary GS1-128 Barcode Guideline for Cases and Cartons**. Its recommendation is concrete: every case label should carry "the GTIN, the appropriate product date(s), and batch/lot or serial number."

## Who Built It, And Why Them

The **Uniform Code Council**, jointly with its European counterpart EAN, and the reason is that they already owned the number the label had to carry.

A case label is only useful if every trading partner reads it the same way, which rules out any single manufacturer or distributor as author. The UCC had administered the UPC since 1974 and the grocery EDI standard since 1983; extending its numbering system to cases, dates, lots and weights was an extension of a registry it already ran. The value was in the dictionary of identifiers, not the bars, which is why the bars were borrowed from an existing symbology.

Foodservice did not ask for it first. The **Foodservice GS1 US Standards Initiative** began only in **2009**, announced by GS1 US — the UCC's continuation — with the International Foodservice Distributors Association and the National Restaurant Association, and it is explicitly voluntary. The tool was built for general distribution; foodservice adopted it decades later.

## What It Cost

**Voluntary adoption meant the label arrived partially, and the variable fields are fragile.**

A guideline cannot compel a supplier to print a lot code, so a distributor's receiving dock sees a mix of full labels, bare GTINs and none. Every case without the data falls back to a person.

And the weight field carries a trap GS1 US's own guidance spells out: the same six digits `000400` mean **400 lb under AI (3200) and 4 lb under AI (3202)**. The implied-decimal design saves label space and hands every scanner, ERP and invoice a place to be wrong by a factor of a hundred — in the one field that sets the price of a catch-weight case.

## What You Still Touch

Scan a case at a broadline distributor's dock today and a GS1-128 label is what the gun is reading, when it is there. Where it is not — no lot, no weight, a mis-set decimal — the discrepancy reaches the invoice.

- [[problems/food-distributors/low-impact-2|🟡 Supplier Invoice Reconciliation Against PO and Receiving]] — catch-weight and short-ship mismatches, where the label's weight field either works or does not
- [[problems/food-distributors/high-impact|🔴 Perishable Demand Forecasting and Inventory Optimization]] — dates that exist on the case and rarely reach the inventory system
- [[niches/food-distributors/invoice-reconciliation-automation/profile|Invoice Reconciliation Automation]]
- [[niches/food-distributors/food-traceability-compliance-services/profile|Food Traceability Compliance Services]] — the lot field, as a compliance obligation

**Sources:** GS1 US, *Getting Started with GS1-128 Barcodes in Foodservice* (2017, read in full) — the recommended data elements, the AI examples (01, 13, 16, 10, 21) and the 3200/3202 net-weight example are quoted from it; IFDA, *GS1 US Standards Initiative* ("since 2009"); eTundra and BHS blog pages (announcement by the National Restaurant Association, GS1 US and IFDA); Wikipedia, *Code 128* (Computer Identics, 1981), *Uniform Communication Standard* (UCC administering UCS from 1983), *GS1*; activebarcode.com and Honeywell support pages on UCC/EAN-128 and AI 310n. This vault's `history/food-distributors.md` (UCC founded April 1974), cited as vault material. ⚠️ **Not established:** the release year of UCC/EAN-128 and its Application Identifier system — secondary sources give "early 1991" and elsewhere 1989, and no primary UCC/EAN document was found, so no year is asserted above. **Not established:** which individuals at UCC or EAN designed the AI scheme, or that it was designed with foodservice catch-weight in mind. **Keying note:** the standard was co-issued by the UCC and EAN; it is keyed to the Uniform Code Council as the US standards owner at build time, per the "key the standard's owner" precedent. No foodservice-wide GS1-128 adoption figure was found.
