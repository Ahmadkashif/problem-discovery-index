# Lineage: Warehouse & 3PL

**Industry:** [[industries/warehouse-3pl|Warehouse & 3PL]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the X12 940 Warehouse Shipping Order, and its reply the 945 Warehouse Shipping Advice
**Builder:** ASC X12
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A public warehouse ships goods it does not own, to customers it has never met, on the say-so of someone who is not in the building.

That is the whole 3PL business in one sentence, and it is an information problem before it is a logistics one. The **depositor** — a manufacturer or wholesaler — takes the order, holds the customer relationship and sends the invoice. The **warehouse** holds the pallets. Every shipment therefore begins as an instruction crossing a company boundary: ship these items, in these quantities, to this address, by this carrier.

Before a standard message existed, that instruction arrived however the depositor chose to send it — paper, phone, telex, a proprietary file. Each new client meant a new intake format, re-keyed by hand. And the reply mattered as much as the request: the depositor could not invoice its own customer until the warehouse said what actually left the dock.

## What Got Built

Two transaction sets, one in each direction.

**The 940** is the depositor's instruction. Its published purpose is to notify a *public warehouse* of an order to be shipped, carrying everything the warehouse needs to cut a pick ticket and a bill of lading. **The 945** is the answer: what was actually picked, packed and shipped, so the seller can reconcile shipped against ordered, raise its invoice, and send its own 856 advance ship notice onward.

Read the pair together and the business model is legible in the schema. **The warehouse never originates a sale and never invoices the end customer.** The 945 exists because the party with the invoice is not the party with the goods.

## Who Built It, And Why Them

**ASC X12**, the ANSI-chartered committee (1979) that grew out of the transportation sector's Transportation Data Coordinating Committee. Under the vault's keying precedent, an interoperable standard is keyed to its owner, not to the first user.

But the owner is not the whole story, and the part before it is the part not established. Secondary sources describe a warehouse-specific EDI subset, **WINS — Warehouse Information Network Standards**, established around **1982** and later folded into X12. One glossary credits WINS to the Warehousing Education and Research Council; no primary source checked confirms that, and the obvious alternative — the public-warehousing trade body, the American Warehouse Association (merged into IWLA in 1997) — also went unconfirmed.

Why a standards committee rather than a vendor is clearer. A 3PL has dozens of clients, each running a different ERP; a client may use several warehouses. **Neither side can impose its own format on the other without losing the other's other partners.** Only a neutral, many-to-many message could make taking on the next client cheap — and cheap onboarding is what lets a public warehouse sell capacity at all.

## What It Cost

The pair is a **batch conversation between two systems that each believe they are the truth**. The 940 says what the client *thinks* should ship; the 945 says what the warehouse *thinks* did. Nothing in either message makes the two inventories the same thing, and the reconciliation between them runs on transmission schedules, not on a shared ledger.

The standard also bakes in who is subordinate. The warehouse executes; the client decides. Slotting, labour and pick routing — the things that actually determine a 3PL's margin — are invisible to the message that drives the work.

## What You Still Touch

Every 3PL onboarding still begins with "send us a 940 and we'll return a 945." The mapping project is the first invoice a new client receives.

- [[problems/warehouse-3pl/low-impact-1|🟡 Inventory Discrepancy Detection and Cycle Count Targeting]] — the two beliefs, drifting between transmissions
- [[problems/warehouse-3pl/high-impact|🔴 Dynamic SKU Slotting Optimization]] — the margin decision the order message never sees
- [[niches/warehouse-3pl/billing-reconciliation-3pl/profile|Client Billing & Reconciliation]]
- [[niches/warehouse-3pl/ecommerce-dtc-fulfillment/profile|E-Commerce DTC Fulfillment]]

**Sources:** 1 EDI Source, *EDI 940: Warehouse Shipping Order* and *EDI 945: Warehouse Shipping Advice* (purpose statement naming the public warehouse; 945 used to reconcile, invoice and generate the 856); Zenbridge, *EDI 940 and EDI 945 for 3PL*; alsharqi.co glossary and William Zavorskas, *A History of EDI* (LinkedIn) — WINS established 1982 as an X12 subset, WERC attribution from the glossary only; IWLA public profile (1997 merger of the American Warehouse Association with CAWDS); this vault's `history/warehouse-3pl.md` for X12's 1979 ANSI charter and TDCC lineage (cited as vault material, not independent corroboration). ⚠️ **Not established:** the sponsoring body of WINS (WERC vs the American Warehouse Association vs another — searched, not confirmed in any primary source); the year the 940 and 945 first appeared in a published X12 version; the year WINS was absorbed into X12.
