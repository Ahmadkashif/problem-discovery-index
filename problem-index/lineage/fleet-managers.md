# Lineage: Fleet Managers

**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** OmniTRACS — Qualcomm's in-cab satellite terminal for two-way text messaging and automatic position reports between a truck and its dispatcher, first introduced in the US in 1988
**Builder:** Qualcomm
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Once a truck left the yard, the fleet lost it.

A long-haul dispatcher's only link to a moving vehicle was the driver's scheduled phone call from a truck stop. Between calls the office did not know where the truck was or whether it could take a load that had just come up nearby.

**The cost was empty miles and idle equipment.** A truck that finished early sat until its driver called in. A new load went to whichever truck reported next, not the closest one. The fleet's biggest asset spent much of its day invisible to the people planning its work.

## What Got Built

A box in the cab, a dish on the roof, and a keyboard and screen for the driver.

**OmniTRACS sent short text messages and position reports both ways between truck and dispatcher over leased Ku-band transponders on geostationary satellites.** Qualcomm's own filing describes it as a "satellite-based OmniTRACS mobile communications system … first introduced in the United States in 1988", with features listed as "status updates, load and pick-up reports, position reports at regular intervals, and vehicle and driving performance information."

Satellite meant coverage where no cellular network reached; text meant a dispatcher could handle dozens of trucks at once. The terminal became so common that drivers called the in-cab screen "the Qualcomm."

By September 2004 Qualcomm reported more than 520,000 satellite terminals shipped (OmniTRACS plus its sister product TruckMAIL), operating in over 39 countries.

## Who Built It, And Why Them

Qualcomm — but the trucking idea came from outside it.

Qualcomm was founded on July 1 1985 by seven former Linkabit engineers led by Irwin Jacobs and Andrew Viterbi, and began as a contract R&D shop for government and defence satellite work. Around the same time **Omninet Corp.**, a satellite-communications venture co-founded in 1984 by Neil Kadisha and relatives, hired the new Qualcomm to develop a two-way mobile satellite messaging system for trucking. The two combined in 1988, and Qualcomm raised $3.5 million to produce it.

**That is why Qualcomm and not a truck maker or a phone company.** The hard part was sending data from a small, cheap, moving antenna through a satellite channel shared with thousands of others. That was spread-spectrum signal processing, which was exactly what the Linkabit team knew from its military work. The trucking market supplied the demand and paying customers; Qualcomm supplied the modem.

The customer shaped the company. By 1989 Qualcomm had $32 million in revenue, **half of it from a single OmniTRACS contract with Schneider National**, the Green Bay truckload carrier. Headcount went from eight in 1986 to 620 in 1991 on OmniTRACS demand, and those profits helped pay for Qualcomm's CDMA research, the technology the company is now known for.

## What It Cost

**The fleet paid per message and bought the hardware.** Satellite airtime was expensive, so messages stayed short and formatted, and position reports came at set intervals, not continuously. That is the shape of what the dispatcher got: a regular ping and a canned status code, not a live feed.

The second cost was one-sided visibility. The terminal was built to tell the office about the driver, and "vehicle and driving performance information" came along with location from the start. Monitoring the driver was part of the product's value, and that is where today's arguments over driver scoring started.

## What You Still Touch

Samsara, Geotab and Motive sell the same deal on cellular networks and GPS: a device in every vehicle reporting where it is and how it is being driven, with the office on the other end. The regular position ping and the driver-behaviour record both go back to a system built for a dispatcher who could not see his trucks.

- [[problems/fleet-managers/low-impact-1|🟡 Driver Behavior Monitoring and Coaching]] — the part of the terminal's job that was about watching the driver
- [[problems/fleet-managers/high-impact|🔴 Predictive Maintenance Optimization]] — engine data flowing from the cab and still not used to predict failures
- [[niches/fleet-managers/fleet-safety-consultancies/profile|Fleet Safety Consultancies]]
- [[niches/fleet-managers/last-mile-delivery-fleets/profile|Last-Mile Delivery Fleets]]

**Sources:** Qualcomm Inc., Form 10-K filed 2004-11-03 (SEC EDGAR, CIK 804328), business section on QUALCOMM Wireless Business Solutions: 1988 US introduction, 520,000+ satellite units through September 2004, Ku-band/C-band transponders, feature list (quoted). Wikipedia, *Qualcomm* (founding July 1 1985; 1988 Omninet merger and $3.5M; 8→620 employees 1986–1991; 1989 revenue $32M, 50% from Schneider National contract; OmniTRACS profits funding CDMA), *Neil Kadisha* (Omninet founded 1984, commissioned Qualcomm, joined forces 1988), *Irwin M. Jacobs*, *Truck driver* (in-cab screen called "a Qualcomm"), *Solera Holdings* (2021 Omnitracs acquisition). ⚠️ WebSearch was unavailable this session (session cap reached); research used direct fetches of Wikipedia and SEC EDGAR only. **Not established:** the date and terms of the first Schneider order, how many trucks it covered, and whether Schneider was the first customer; Qualcomm's sale of the Omnitracs unit (commonly given as 2013 to Vista Equity Partners) could not be confirmed against a primary source and is left undated. Omninet's role is from a Wikipedia biography of its co-founder, not independently corroborated.
