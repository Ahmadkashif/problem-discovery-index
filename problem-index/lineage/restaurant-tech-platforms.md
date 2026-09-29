# Lineage: Restaurant Tech Platforms

**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the OpenTable Electronic Reservation Book (ERB) — software at the host stand that replaced the paper reservation book, so the restaurant's own table inventory could be sold to diners online in real time
**Builder:** OpenTable
**Builder in vault:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A restaurant's capacity lived in a paper book, and the only way to query it was to phone the person holding the pencil.

The reservation book at the host stand was the single authoritative record of which tables were promised at which times. It was accurate precisely because only one person wrote in it, in front of the room. That made it impossible to consult from anywhere else. A diner could not see availability; they could only ask, one restaurant and one call at a time, during hours when someone would pick up.

For the diner the cost was time. For the restaurant it was a host on the phone during service, and a cover history that existed only as handwriting.

## What Got Built

Two halves, and the unglamorous one mattered more.

The visible half was a website where diners booked tables. The load-bearing half was the **Electronic Reservation Book**, which "computerizes restaurant host-stand operations" and "replaces existing paper reservation systems," handling reservations, table management and guest recognition. From 1998, restaurants in San Francisco used this back-end software to process the reservations made on the website, "resulting in a real-time reservation system for both diners and restaurants."

The shape follows from the problem. A website cannot sell a table it cannot see, and it cannot see a table while the truth is in pencil. So the product had to *become* the book — the restaurant's own system of record — not sit beside it. Only then does an online booking land in the same place the host is seating walk-ins, and only then is availability real rather than a quota the restaurant set aside and forgot.

The pricing followed the same logic: free to diners, with restaurants paying "flat monthly and per-reservation fees."

## Who Built It, And Why Them

OpenTable — founded on **2 July 1998** by Chuck Templeton, Sid Gorham and Eric Moe, and first incorporated in California as **easyeats.com, Inc.**

The origin is a diner's complaint rather than a restaurateur's. In 1998, when Templeton's in-laws visited, his wife spent three and a half hours on the phone trying to secure reservations — notable because his father-in-law was a founding partner of Lettuce Entertain You Enterprises, the Chicago restaurant group. If a restaurant insider's family could not get a table without an afternoon of calls, the problem was the channel, not access.

**Why a start-up and not the POS vendors or the restaurants:** the value only exists as a network. One restaurant's electronic book is a nicer pencil; a thousand of them behind one search box is a marketplace. A single restaurant had no reason to build it, and a point-of-sale vendor sold to the kitchen and the till, not to the diner. The party that could charge diners nothing and charge restaurants per seated cover had to be a third party sitting between both.

## What It Cost

The restaurant handed its most valuable operational record to a vendor that also owned the diner relationship.

And the data it created stayed specific: the ERB knew reservations and covers booked through it, not the walk-ins, the no-shows booked elsewhere, or what anyone ordered. It gave restaurants their first machine-readable cover history — and a partial one.

OpenTable went public on NASDAQ on **21 May 2009** and in 2014 agreed to a takeover by the Priceline Group at $103 a share, about **$2.6 billion**.

## What You Still Touch

Every restaurant that forecasts tonight's covers from a booking count, and every manager who schedules staff against "reservations plus a guess at walk-ins," is working from the record the electronic book started — a digital cover history that is only as complete as the channels that write to it.

- [[problems/restaurant-tech-platforms/high-impact|🔴 Store-Level Demand Forecasting for Labour and Prep]] — forecasting on a cover history the book only half-records
- [[problems/restaurant-tech-platforms/worker-life-1|🟢 Manager Schedule Rebuild Cycle]]
- [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|Full-Service Restaurant POS & Operations]]
- [[niches/restaurant-tech-platforms/independent-fsr-forecasting/profile|Independent Restaurant — Forecasting on a Thin History]]

**Sources:** Wikipedia, *OpenTable* (founding 2 July 1998 by Templeton, Gorham and Moe; easyeats.com, Inc.; San Francisco 1998 operations; Electronic Reservation Book description; fee model; IPO 21 May 2009; Priceline offer $103/share, ~$2.6bn in 2014); Wikipedia, *Chuck Templeton* (three-and-a-half-hour phone story, father-in-law's partnership in Lettuce Entertain You Enterprises). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs only. ⚠️ **Not established:** the ERB's original platform and hardware, and its first installation date as distinct from the 1998 start of operations; whether the ERB was a separate product name from launch; the claim that POS vendors did not attempt online reservations first is this note's argument, not a sourced finding.
