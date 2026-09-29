# Lineage: Field Service Software

**Industry:** [[industries/field-service-software|Field Service Software]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** ServiceTitan — a cloud platform, launched 2012, that puts the call, the dispatch board, the technician's job on a phone, the flat-rate pricebook estimate and the invoice in one record per job
**Builder:** ServiceTitan
**Builder in vault:** [[industries/field-service-software|Field Service Software]]
**Verification:** partial — see Sources

## The Problem That Came First

A trades business does its work in someone else's house and its paperwork at its own kitchen table.

A plumbing or HVAC contractor's day has two shifts. The first is in the field: take the call, send a truck, diagnose, quote, fix. The second starts after dinner: type the invoices, reconcile receipts, work out timesheets to pay the technicians, schedule tomorrow. ServiceTitan's own prospectus describes exactly this — owners "processing shoeboxes full of receipts and calculating timesheets" at night.

The expensive part is that the two shifts do not share a record. What the technician found, quoted and did lives on paper in a truck. What the office needs to bill it lives somewhere else. Every job is written up twice, and whatever does not survive the trip back is lost revenue.

## What Got Built

One system in which a job is a single record from the phone call to the payment.

ServiceTitan's S-1 lists the core product's workflows: call tracking, scheduling, dispatching, customer communications, estimating, job costing, sales, inventory and payroll integration. Add-ons sit on top — Dispatch Pro, Scheduling Pro, Pricebook Pro — and a payments and consumer-financing layer from which the company takes a fee.

The shape is the point. Dispatch, the technician's mobile app, the pricebook and the invoice are one database, so a price chosen in a customer's kitchen is the line on the invoice and the figure in the owner's revenue report without anyone re-typing it. By fiscal 2024 the company reported about 8,000 active customers, roughly 109 million jobs completed through the platform, and $55.7 billion invoiced by its customers.

## Who Built It, And Why Them

Ara Mahdessian and Vahe Kuzoyan, in Glendale, California.

Both are sons of immigrant trades-business owners; their fathers started as technicians and then ran their own firms. They met on an Armenian Student Association ski trip, studied engineering, and — in their own words — came home to find their parents' businesses "frozen in time", served by "legacy desktop applications" and "fragmented point solutions." The company was incorporated in 2007 as LinxLogic, Inc.; the platform launched in 2012; the company took the name ServiceTitan in 2014. It listed on Nasdaq as TTAN in December 2024.

**Why them:** the category already had software. What it lacked was software written by people who had watched the second shift. The founders' first customers were their own families, so the product was built against the owner's night at the kitchen table — which is why it is organised around the *job* and the *invoice* rather than around a scheduling engine. That also explains the money: the core bet is that a contractor will pay for a system that raises the ticket, which is why pricebook, sales and financing tools sit so close to the centre.

## What It Cost

One record per job means one vendor for everything. The more of the business runs through a single database — pricing, payroll, payments, financing — the harder it is to leave, and the vendor's revenue grows with the contractor's volume rather than with seats alone.

It also moved cost upward. A platform built as an end-to-end operating system suits a shop with an office, a dispatcher and a sales process; the smallest operators are served by lighter tools. And a record that sees every job also records every technician's day.

## What You Still Touch

The flat-rate price a technician shows you on a tablet, instead of an hourly estimate, is the pricebook sitting inside the same record as the invoice — the owner's back-office problem solved by moving it into the customer's kitchen.

- [[problems/field-service-software/low-impact-1|🟡 Flat-Rate Price Book Maintenance]] — the pricebook as a maintained asset
- [[problems/field-service-software/worker-life-2|🟢 Technician Administration at the Truck]] — the second shift, relocated to the driveway
- [[problems/field-service-software/high-impact|🔴 First-Time Fix and the Dispatch Match]]
- [[niches/field-service-software/residential-trades-platforms/profile|Residential Trades Platforms]]
- [[niches/field-service-software/flat-rate-price-book-content/profile|Flat-Rate Price Book Content]]

**Sources:** ServiceTitan, Inc., Form S-1, SEC EDGAR, filed 18 November 2024 (CIK 1638826, accession 0001193125-24-260611) — founders' letter, business description, product list, fiscal 2024 metrics, and "Corporate Information" (incorporated 2007 as LinxLogic, Inc.; renamed ServiceTitan, Inc. in 2014; platform first launched 2012); Wikipedia, *ServiceTitan* (Nasdaq listing 12 December 2024 under TTAN); this vault's `history/field-service-software.md` and `industries/field-service-software.md` (cited as vault material, not independent corroboration). WebSearch was unavailable this session (session cap reached). ⚠️ **Keying note:** the build-time legal entity was LinxLogic, Inc.; whether the 2012 product already carried the ServiceTitan name was not established, so the key uses the product and company name. **Not established:** which trade each founder's father worked in, and an older ancestor first considered for this note — IBM's radio data network for its own field engineers, built with Motorola and later sold as ARDIS — which Wikipedia (*DataTAC*, *Mobile data terminal*) mentions only without dates, so it is not asserted here.
