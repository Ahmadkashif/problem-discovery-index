# Failure: Convoy (2015–2023)

**Lesson class:** capital-cannot-buy-it
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Industries touched:** [[industries/freight-brokerage|Freight Brokerage]] · [[industries/last-mile-delivery|Last-Mile Delivery]] · [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**What was claimed:** Amazon-grade logistics algorithms — automated load–carrier matching, dynamic pricing, network effects that would compound and drive down empty miles — could be applied to freight brokerage and would out-compete relationship-based incumbents at scale.
**Capital at risk:** $837M–$920M in equity (sources genuinely disagree) plus a separate $100M debt tranche raised March 2022; peak valuation $3.8B at a Series E in April 2022.

This file draws heavily on this vault's own `history/freight-brokerage.md`, which conducted the primary post-mortem research on Convoy's funding, timeline and the four competing accounts of its failure. Where this file repeats a fact from that one, it is citing it, not independently re-verifying it.

## Why It Was Plausible

Every element of the thesis was individually reasonable, and several were things sophisticated people had already seen work elsewhere.

The founders, Dan Lewis and Grant Goodale, came from Amazon — a company that had, within living memory, solved matching and logistics problems of comparable or greater complexity at planetary scale. If anyone had the pattern-matched right to believe "this fragmented, phone-driven market is a software problem," it was two engineers who had watched Amazon solve an adjacent one.

The backers were not naive money. Jeff Bezos, Bill Gates, CapitalG, Al Gore's Generation Investment Management, and Reid Hoffman on the board represent some of the most experienced capital allocators in technology. And this was not a single leap of faith: Convoy raised repeatedly over seven years, at rising valuations, with each round independently re-underwritten by new institutional investors — a $2.75B valuation in November 2019, then $3.8B at the April 2022 Series E, led by T. Rowe Price and Baillie Gifford. The market kept checking the thesis and kept saying yes.

The underlying market was genuinely inefficient in a way that looks addressable by software: freight brokerage is an ~$80B US segment (per this vault's `industries/freight-brokerage.md`) built on opaque pricing, phone-based matching, and a broker's personal rolodex. "Large, fragmented, analogue market meets algorithmic matching and a trusted brand" had already worked in adjacent categories — Amazon in retail, Uber in ride-hailing — and 2020–2021's real freight-capacity crunch gave Convoy's model a live, favourable environment in which algorithmic matching plausibly did add measurable value. A five-year run of validating data, not a single pitch deck, sat behind the April 2022 valuation.

## What Actually Killed It

`history/freight-brokerage.md` records four accounts, deliberately left unflattened because they are complementary rather than competing:

1. **Macro and timing** (Lewis's own shutdown memo): the freight recession and a simultaneous VC funding contraction arrived together, outside management's control.
2. **Blitzscaling mismatch** (FreightWaves): growth-at-all-costs strategy requires network effects, switching costs, or scale economies. Freight brokerage has essentially none of these — carrier switching cost is near zero, and matching is a commodity function. Scaling the capital scaled the losses.
3. **Tech over operations**: Convoy underweighted the relationship layer incumbents use to secure capacity when markets tighten. It was strong in short-haul regional freight and never built the deep carrier relationships that hold up in a hard market.
4. **Death from overfunding**: $900M-plus let Convoy avoid unit-economics discipline for years. When investor sentiment flipped from growth to profitability in 2022, the underlying economics were exposed as never having worked on their own.

The trigger that made the exposure sudden rather than gradual is dated precisely: dry van spot rates fell **24.1% between January 13 and April 13 2022** — inside a month of the Series E that valued the company at $3.8B. On October 19 2023, Convoy announced it was shutting down after four months of failing to find a buyer, with cash weeks from running out.

## What It Was Not

**"Digital freight brokerage failed" is wrong, and this is not a new finding — it is the established correction in `history/freight-brokerage.md` and this file repeats it deliberately rather than re-deriving it.** Only Convoy fully shut down. Transfix sold its brokerage business to NFI and pivoted to selling its TMS as software. Loadsmart retreated toward dock-scheduling and TMS tooling. Next Trucking was acquired by another broker in a distress sale. Uber Freight is still operating. Meanwhile the incumbents are shipping exactly the automation the startups promised: C.H. Robinson reports (company-figures, not independently audited) LLM-driven email-to-quote automation averaging a 2-minute-13-second response across 10,000-plus routine transactions daily.

There is a second myth worth killing specifically here, distinct from the freight-brokerage-wide one: **the matching technology itself was not the failure.** Flexport paid a reported (never confirmed by either party) $16M for Convoy's tech stack in November 2023, and in July 2025 sold that same stack to DAT Freight & Analytics for approximately $250M — DAT being the direct descendant of the handwritten load board at the Jubitz Truck Stop that digital freight brokerage was founded to make obsolete. A market that thought the technology was worthless would not have bid it from $16M to $250M in twenty months. What failed was the belief that owning that technology, financed by venture-scale capital chasing growth, constituted a defensible standalone company in a market with no moat. The defensible claim is narrow: venture-scale, growth-at-all-costs, digital-only brokerage failed as a standalone business in this cycle. Software layered onto incumbent brokerage relationships is proceeding fine.

## The Lesson That Transfers

Capital can buy an algorithm, a brand, and years of runway. It cannot buy a business model that never had operating leverage, in a market with no switching cost — because more capital deployed into a structurally thin-margin, commodity-matching business does not change the structure; it only changes how long the structure's absence can be hidden. The operational question an FDE should ask before proposing to disrupt an incumbent market is not "can this be automated" but "what happens to this business in its worst quarter" — Convoy's model worked when capacity was loose and matching was the binding constraint; in a tight market the binding constraint became *who will actually take your load at 4pm on a Friday*, and that question is answered by a relationship, not a ranking.

This generalises past freight. Two other files in this same batch — People Express and GM's 1980s automation programme — describe the identical shape in different industries: real capital, a real capability gap the loser could see, and a purchase of the *visible proxy* for that capability (a robot, a website, a bidding platform) rather than the underlying, non-purchasable thing (shop-floor discipline, a data flywheel, a carrier relationship). Convoy is the freight instance of a pattern that recurs across this entire lesson class.

**Sources:** this vault's `history/freight-brokerage.md`, which itself cites dat.com company history and blog; Wikipedia, *DAT Solutions*, *Convoy (company)*; CNBC (Convoy funding rounds, 2019 and 2022); GeekWire (shutdown memo, Flexport acquisition); FreightWaves (*Death from overfunding*, *Convoy's tech focus may have obscured the human element*, *Convoy autopsy*, Flexport–DAT sale); DAT news release (DAT–Flexport transaction, July 2025); C.H. Robinson press releases 2024–25 (company-reported automation figures, not independently audited); this vault's `industries/freight-brokerage.md`.
