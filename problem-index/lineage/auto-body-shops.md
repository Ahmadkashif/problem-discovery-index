# Lineage: Auto Body Shops

**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the CIECA Estimate Management Standard (EMS) — the file set that carries a collision estimate out of the estimating system and into the shop's management system
**Builder:** CIECA
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A collision repair is written twice.

The estimate — every panel, part, labour operation and paint hour — was produced in an estimating system priced from the vendor's database, descended from the printed "P-page" crash guides. The insurer wanted it there because that was where it priced claims.

But the shop ran on a management system that ordered parts, scheduled technicians and produced the invoice. **Nothing moved between the two.** CIECA's own member recollection names the problem in two words — "double keying." A clerk printed the estimate and typed it again, line by line, into the shop's system. Every supplement meant doing it again, and every re-keyed line was a chance for the parts order, the invoice and the insurer's copy to disagree.

## What Got Built

A neutral file layout for an estimate.

EMS defined a fixed set of files that any estimating system could export and any shop management system could import: administrative data about the claim, vehicle and parties, and the estimate lines themselves, each carrying operation, part, labour and paint values in agreed positions. According to CIECA's account, the first releases were **ASCII comma-separated files**, a choice forced by the limits of the dBase tools shop software then used; version 2.0 split the administrative file in two to get round those limits.

**The estimate stopped being a printout and became a record.** The line the insurer approved could arrive in the shop's parts and production modules without being retyped.

## Who Built It, And Why Them

The Collision Industry Electronic Commerce Association — a non-profit standards body, not any of the software companies.

By CIECA's own account, the push came from a shop. Eric Bickett of Auto Center Auto Body started a Collision Industry Conference subcommittee on electronic data interchange, CIEDIS, in **1991**. Search summaries of CIECA's pages give the association's incorporation as **20 January 1994**. The EMS work began in **late 1993** and was completed around **mid-1994**; the board approved it in San Antonio in **1995**, and implementation ran through 1996–2000.

The people are the commercial explanation. The EMS committee was chaired by **Mike Hastings of Akzo Systems** — software from the paint side of the industry, which needed estimate data flowing into shop systems — and co-chaired by **Margaret Ho of CCC**, with **Fred Albert of Mitchell** writing the specification. CCC, Mitchell and ADP Claims Services led the early releases.

**That is why it had to be a consortium.** The three estimating vendors competed for insurer contracts and each owned its own format. None would publish an export designed for a rival's customers, and no shop-management vendor had the standing to dictate one to them. Only a body with all of them in the room — shops, insurers, estimating and management vendors — could write a format that made the estimate portable without making any one vendor's database the standard. That is an inference from who sat on the committee; CIECA does not state it as a motive.

## What It Cost

**EMS moved the estimate; it did not open it.** The labour times and prices inside each line still came from the estimating vendor's proprietary database. The standard made the output interchangeable while the pricing logic stayed where it was — so the argument about whether a line belongs on the estimate still happens inside systems the shop does not control.

It also fixed the format of a finished estimate, not of the negotiation around it. A supplement travels as a revised estimate, not as the evidence for why the hidden damage was there. And a flat-file layout designed around dBase limits aged quickly: CIECA dates its XML successor, the Business Message Suite, to **2004**, and describes EMS as still in use but superseded.

## What You Still Touch

Every supplement is a new estimate that flows through EMS or its successor, carrying the numbers but not the argument:

- [[problems/auto-body-shops/high-impact|🔴 Hidden Damage Prediction from Visible Impact]] — the damage no initial estimate line records
- [[problems/auto-body-shops/worker-life-2|🟢 Estimator Supplement Battle Fatigue]]
- [[niches/auto-body-shops/supplement-negotiation/profile|Supplement Negotiation Workflow]]
- [[niches/auto-body-shops/estimating-data-providers/profile|Collision Estimating Data Providers]] — the owners of the numbers inside each line

**Sources:** CIECA blog, "The Creation of the EMS: Recollections from Members" (fetched), for double keying, P-page systems, Eric Bickett and CIEDIS in 1991, late 1993 to mid-1994, 1995 board approval in San Antonio, 1996–2000 implementation, the committee members and their companies, ASCII CSV files and dBase limits, v2.0's split file, CCC, Mitchell and ADP Claims Services, and BMS (XML) in 2004 — members' recollections published by the standards body itself, not independent corroboration. Search summaries of cieca.com for incorporation on 20 January 1994, CIC origins and supersession by BMS; the FAQ page timed out and the About page did not carry these facts, so the incorporation date is **not read at source**. BodyShop Business, "Forget the Decoder Ring: CIECA's EMS System," returned 403. ⚠️ **Not established:** which shop management system first imported EMS; adoption counts; whether insurer direct-repair programmes required EMS output — searched, not found. A search summary says thirteen companies seeded CIECA for a year; the CIECA article fetched does not say so, and they are not named here.
