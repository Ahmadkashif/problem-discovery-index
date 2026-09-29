# Lineage: Freight Tech Platforms

**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** MacroPoint load tracking — a per-load location feed that found a truck through whatever it already carried (the driver's mobile phone by network triangulation, a GPS smartphone app, or the carrier's on-board logging device) and posted its position to the broker in place of the check call
**Builder:** MacroPoint
**Builder in vault:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A broker who had sold a load did not own the truck carrying it.

That is the defining fact of truckload brokerage. The shipper's customer wants to know where the freight is; the broker has promised to know; and the truck belongs to a small carrier — often one driver with one tractor — who has no system connected to anyone's. Whatever telematics a fleet owned was the fleet's, not the broker's.

So visibility was manufactured by telephone. A track-and-trace rep called the driver every few hours — the **check call** — asked where they were, typed the answer into the load record, and repeated it for every load on the board. The data was as good as the driver's willingness to pick up, and the cost scaled linearly with loads.

## What Got Built

A tracking layer that belonged to the *load*, not to the truck.

MacroPoint's design choice was to locate a shipment through whatever device was already in the cab. At the time of its 2017 acquisition its network drew positions from four sources: **location-based mobile phone triangulation**, **GPS-enabled smartphone applications**, **on-board electronic logging devices**, and integrations with **transportation management systems**. The broker assigned tracking to a load; positions arrived against that load for its duration; the track stopped when the load delivered.

The phone-triangulation route is the load-bearing part. It needed no hardware, no app install and no integration with the carrier — only a working mobile number. That made it usable against small carriers who would never buy telematics for a broker's convenience.

The **ELD rule** then widened the supply. FMCSA's electronic logging device mandate took effect with a compliance date of **18 December 2017**, with fleets on older recorders given until December 2019 — putting a location-capable device in nearly every regulated truck, which tracking networks could read with the carrier's permission.

## Who Built It, And Why Them

MacroPoint, a Cleveland, Ohio company — and here the record runs out.

This note could not establish when MacroPoint was founded, by whom, or when it first tracked a load. What is documented is its end state: on **15 August 2017** Descartes Systems Group agreed to buy it for approximately **US$107 million** ($87 million cash plus $20 million in shares). Descartes described it as having annualised revenue of about $12.5 million, more than 8,000 transportation providers, brokers and shippers connected, and a network of over 2 million trucking assets. MacroPoint's CEO called it "the market leader for truckload shipment visibility."

**Why a third party rather than the carriers or the brokers:** the problem sat in the gap between them. A carrier had no reason to fund visibility it was not paid for; a broker could not install hardware in trucks it did not own. A neutral network that sold the location to the broker, and asked of the carrier only a phone number or a data permission, is the only party whose economics worked on both sides.

## What It Cost

Consent and coverage. Tracking a driver's phone means tracking a person, and a load whose driver declines — or whose phone is off — simply goes dark.

It also made location a claim about a device, not about a truck. A position proves where a phone or ELD is; it does not prove who is driving or that the carrier who accepted the load is the one hauling it — the gap double brokering now exploits.

## What You Still Touch

Every "tracking link" a broker sends a shipper, and every rep whose queue shows only the loads that *stopped* reporting, descends from replacing the check call with a per-load feed.

- [[problems/freight-tech-platforms/worker-life-2|🟢 Track and Trace Check Calls]] — the job the feed was built to remove
- [[problems/freight-tech-platforms/high-impact|🔴 Carrier Identity and Double Brokering Fraud]] — what a device location cannot prove
- [[niches/freight-tech-platforms/freight-visibility-platforms/profile|Freight Visibility Platforms]]
- [[niches/freight-tech-platforms/truckload-eta-accuracy/profile|Truckload — Coverage and ETA Accuracy]]

**Sources:** Descartes Systems Group, "Descartes Acquires MacroPoint" news release, 15 August 2017 (price and split, Cleveland location, revenue, network size, four tracking methods, CEO quotation — read directly); Wikipedia, *Descartes Systems Group* (August 2017 acquisition of "Ohio-based MacroPoint truck-tracking business"); Wikipedia, *Electronic logging device* (18 December 2017 compliance date; December 2019 deadline for fleets with earlier recorders). macropoint.com's about page was fetched and gave no founding history. FMCSA's own ELD timeline page (403) and the Federal Register final-rule page (redirected to a block page) could not be read. WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs only. ⚠️ **Not established:** MacroPoint's founding year, founders, and first product date; whether phone triangulation required driver opt-in and in what form; the CEO's name — the fetched release text attributes the quotation to "Bennett Adelson," which this note does not repeat as a person's name because it could not be confirmed.
