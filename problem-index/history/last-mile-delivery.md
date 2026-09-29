# History: Last-Mile Delivery

**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Primary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** [[origins/package-carriers/profile|Package Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** A parent industry can solve a problem completely, at scale, for its own employees, and that solution can still fail to reach the atomised, small-operator layer of the same trade decades later — because the constraint on the smaller layer was never the algorithm, it was who could afford to build one.

## Before

Overnight and ground parcel delivery, before this industry existed as a distinct layer, was the direct province of FedEx, UPS and the US Postal Service — national networks running their own hub-and-spoke systems, their own tracking (COSMOS, live 1979), and their own drivers. There was no independent "last-mile" trade because there was no reason for one: the same company that sorted a package also delivered it.

This vault's hub note for the industry puts a number on why the final leg is worth unbundling at all: last-mile delivery represents an estimated **50–60% of total supply-chain cost**, despite covering the shortest physical distance in the chain, because it is the one leg that cannot be consolidated into a full truckload — it is, by definition, one stop at a time, in whatever order the address book requires. A failed first attempt — the hub note cites **5–10% of residential deliveries** — is re-driven at full per-stop cost with no additional revenue, which is exactly the kind of cost that scales with volume and did not exist as a distinct line item before e-commerce made volume itself the story.

E-commerce changed the volume, not the geography. As online retail grew from the mid-1990s onward, the national carriers' own networks became a capacity constraint during peak season, and a new question appeared that had not needed asking before: could the final leg — the actual stop-by-stop delivery to a residential address — be unbundled from the network that moved a package between cities, and run by someone smaller?

## The Origin Event

**Amazon Flex launched in 2015**, recruiting independent contractors to make on-demand deliveries from their own vehicles for Prime Now, at an advertised $18–25 an hour. It answered Amazon's first version of this question: rather than depend entirely on UPS, FedEx and USPS capacity, build a contractor-driven delivery layer of its own, priced by the task, matched by an app — the exact Wave 8 mechanism this file's neighbours in this batch use for a rider or a meal.

**The Delivery Service Partner (DSP) programme followed in 2018**, and it is the more consequential of the two. Rather than contracting directly with individual drivers, Amazon licenses small business owners to start their own delivery companies — using Amazon-branded vans, Amazon's own routing and dispatch technology, and Amazon-set delivery quotas, while the DSP owner hires and employs the actual drivers. **By the mid-2020s Amazon reported roughly 4,500 DSPs operating under this model**, and in 2024 announced a $1.9 billion investment aimed at lifting DSP driver pay toward a reported national average of nearly $23 an hour.

This is the origin event properly stated: **not a new algorithm, but a new organisational shape** — a franchise-like layer of small, Amazon-dependent businesses, built to extend a package carrier's network without the package carrier employing the drivers directly.

## What Became Cheap

Two different things, and it matters which one you mean. For Amazon, what became cheap was **capacity without headcount** — a delivery network that scales by licensing new small businesses rather than hiring and training employees at Amazon's own cost and liability. For everyone smaller than Amazon — the independent courier, the regional DSP not tied to a single retailer, the local delivery company — what became cheap was **buying the optimisation UPS spent a decade building**. Route4Me, OptimoRoute and Circuit sell a packaged, much smaller-scale version of exactly the sequencing-and-reoptimisation logic UPS's ORION runs internally, and the tracking number COSMOS turned into a customer-facing product in 1979 is now the baseline a customer expects from any DSP or independent courier, not a UPS exclusive.

## How It Was Actually Solved

Route optimisation for a small operator is a **smaller instance of the same vehicle-routing problem** ORION solves for UPS — minimise distance and time across a driver's stops, subject to delivery windows, with re-optimisation as the day changes. What differs is scale and the buyer: ORION was built once, by UPS, for UPS's own ~55,000 routes. Route4Me, OptimoRoute and Circuit build the same class of solver once and sell it, as software, to operators who could never have justified the decade of R&D UPS put into ORION (2003–2013, full deployment by 2016–17) for their own fleet of a dozen vans.

Proof-of-delivery followed the same pattern one layer down: a required photograph at every stop is the direct descendant of SuperTracker's 1986 handheld scan-at-every-handoff logic, repackaged as a phone camera rather than a barcode reader, feeding a much smaller company's records instead of COSMOS.

## The Trade-Off

The DSP structure moves capital cost and legal liability onto the DSP owner — vehicle leases, insurance, workers' compensation, driver hiring and firing — while Amazon retains the two things that actually determine the DSP's economics: the routing technology, which sets how many stops a route contains and how tightly it is timed, and the customer relationship, which sets the volume. A DSP owner is a business owner in name and a route operator in practice, running a plan they did not design against a quota they did not set.

This is a variant of the wave-08 asymmetric hold, one organisational layer removed from where the vault usually finds it. It is not the platform holding data back from an individual gig worker — it is the platform holding the routing and volume decisions away from a nominally independent business owner who employs the actual drivers. The surveillance the driver experiences (route adherence, delivery-time tracking, customer feedback tied back to a specific stop) is real, but it is mediated through an employer — the DSP owner — who is themselves dependent on Amazon for the plan.

## What's Still Open

- [[problems/last-mile-delivery/high-impact|🔴 Per-Stop Delivery Success Prediction]]
- [[problems/last-mile-delivery/low-impact-1|🟡 Real-Time Route Reoptimisation]]
- [[niches/last-mile-delivery/ecommerce-parcel-dsps/profile|E-Commerce Parcel DSPs]]
- [[niches/last-mile-delivery/route-optimization-vendors/profile|Route Optimization Vendors]]
- [[niches/last-mile-delivery/proof-of-delivery-documentation/profile|Proof-of-Delivery Documentation]]
- [[niches/last-mile-delivery/returns-reverse-logistics/profile|Returns & Reverse Logistics]]
- [[niches/last-mile-delivery/dsp-fleet-insurance-underwriting/profile|DSP Fleet Insurance Underwriting]]
- [[niches/last-mile-delivery/rural-route-delivery/profile|Rural Route Delivery]]

## The Transferable Pattern

> **When a large parent company unbundles a capability into a network of small licensed operators, ask which half of the arrangement it kept. It almost always keeps the software that sets the workload and gives away the balance sheet that bears the risk of that workload.**

`origins/package-carriers/legacy.md` already names the general shape: ORION's optimisation, proven at national scale for UPS's own employees, "has never reached the atomised, single-truck segment of the same industry" for owner-operators. Last-mile delivery is the partial counter-case — the optimisation *did* reach the small operator here, packaged as SaaS rather than built in-house — but it reached them as a rented tool inside someone else's franchise structure, not as an owned capability. An FDE should treat "does this business have access to the technology" and "does this business control the technology's parameters" as two separate questions; DSPs answer the first one yes and the second one no.

**Sources:** aboutamazon.com, *Amazon invests $1.9B in the Delivery Service Partner program* (DSP programme launched 2018, ~4,500 DSPs, 2024 investment); Wikipedia, *Prime Now* (Amazon Flex, launched 2015, $18–25/hour, 2015 and 2016 misclassification lawsuits); `origins/package-carriers/legacy.md`, `origins/package-carriers/the-mechanism.md`, `origins/package-carriers/origin-story.md` (COSMOS 1979, SuperTracker 1986, ORION 2003–2016/17); this vault's `industries/last-mile-delivery.md`.
