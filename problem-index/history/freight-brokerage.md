# History: Freight Brokerage

**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** [[origins/ocean-shipping-ports/profile|Ocean Shipping & Ports]] · [[origins/package-carriers/profile|Package Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** Capital can buy scale, an algorithm and a brand. It cannot buy a business model that never had operating leverage — and a matching market with no switching cost has none.

> **Wave-assignment note.** The spine assigns this industry to Wave 4, which is where its *computerisation* happened. But the events that **created** the industry are a statute (1980) and a corkboard (1978), both outside the wave. Recorded as a template break — see `series/_bookmark.md`.

## Before

Two facts made the industry impossible before 1980.

**Legally**, the Interstate Commerce Commission controlled who could carry freight, on what routes, at what rates. There was little to broker, because there was little to negotiate.

**Practically**, a shipper with a load and a carrier with an empty truck had no way to find each other except by knowing each other. Matching ran on CB radio, word of mouth, and a broker's personal rolodex — and the rolodex *was* the business.

## The Origin Event — two of them, neither a computer

**April 3 1978.** At the Jubitz Truck Stop in Portland, Oregon, Al Jubitz launched **"Dial-A-Truck."** Available loads were posted on a television monitor in the truck stop; a driver paid a fee for the phone number and called to claim one.

The monitor replaced something even simpler: **handwritten cards pinned to an actual corkboard.** That corkboard is where the term *load board* comes from — the name outlived the object by nearly fifty years. By 1985 the system ran on 200+ monitors across 42 states, having started with nine stops along I-5. It was renamed **DAT Services** in 1989.

**July 1 1980.** President Carter signed the **Motor Carrier Act**, deregulating interstate trucking — easing entry, and allowing rate flexibility within a ±15% band without challenge. Licensed carriers roughly doubled to over 40,000 by 1990.

Deregulation created something to broker. The load board created a way to find it. **Neither was a computer**, and the industry that resulted has spent forty-five years computerising a matching problem that was defined before it had any computing at all.

## What Became Cheap

**Discovery.** A broker could now see loads and capacity beyond their own rolodex.

Note what did *not* become cheap, because it is the whole story: **the relationship.** Knowing which carrier actually runs Chicago–Atlanta reliably, who has capacity Monday morning, who is negotiable and who is firm — none of that appeared on the monitor. The board told you a load existed. It did not tell you who would take it and actually show up.

This vault's hub note records the surviving gap: *"Senior brokers can cover a load in 30 minutes by calling 3 carriers they know; junior brokers post to load boards and wait."*

## How It Was Actually Solved

Three layers, laid down over three decades, each solving a different part.

**The load board (1978 → web).** Truckstop.com, founded by Scott Moscrip in **1995**, was the first internet-native board. DAT moved online later in the decade. Matching became searchable rather than phoned.

**The TMS (1980s).** **TMW Systems** (1983, acquired by Trimble in 2012) and **McLeod Software** (1985) gave brokerages a system of record: loads, carriers, rates, margins, settlements, in one schema. This is Wave 4 arriving on schedule — one company, one version of its own numbers.

**EDI (1990s onward).** Large shippers began requiring electronic tender rather than a phone call. The message set is still the industry's plumbing: **204** load tender, **990** accept or decline, **214** in-transit status, **210** invoice. *(ANSI X12 dates to the 1980s–90s; I could not verify a specific first-mandate date — treat the adoption curve as unverified.)*

**What none of it solved: pricing.** A broker quotes a shipper and buys capacity from a carrier, and the spread is the business. The vault's own high-impact note is precisely this — and it is a [[origins/airlines/the-mechanism|yield-management problem]] that does not know its own ancestry. Perishable capacity, heterogeneous buyers, a margin that depends on what you withhold.

## The Trade-Off

**Transparency was traded for volume, and the brokers made the trade themselves.**

Before the board, a broker's margin was protected by the shipper not knowing the market rate. Publishing rates created liquidity — and destroyed the information asymmetry the margin rested on. The vault records the result as the industry's first listed pressure: *"as the market has digitized, shippers have more visibility into market rates; fat margins on opaque pricing are harder to sustain."*

This is worth pausing on, because it is the rarer of the two patterns in this vault. Adtech **declined** to close a join that would shrink its invoice. Freight brokerage **closed** one and shrank its own invoice, because the volume was worth more than the margin. Both are rational. Only one is usually told as a morality tale.

## The Graveyard

**Convoy** was founded in **2015** in Seattle by Dan Lewis and Grant Goodale, both from Amazon. The thesis was explicit: apply Amazon-style logistics algorithms to trucking — algorithmic load-carrier matching, automated pricing, network effects that would drive down empty miles.

The backing was as good as it gets: Jeff Bezos, Bill Gates, CapitalG, Al Gore's Generation Investment Management, Reid Hoffman on the board. Roughly **$837M–$920M in equity** *(sources genuinely disagree; a separate $100M debt tranche came in March 2022 — do not quote a single clean figure)*. **Peak valuation $3.8B** at a Series E in **April 2022**, led by T. Rowe Price and Baillie Gifford.

Then the freight market turned. **Dry van spot rates fell 24.1% between January 13 and April 13 2022** — inside a month of that Series E.

**On October 19 2023, Convoy announced it was shutting down.** Four months of searching for a buyer had failed and cash was weeks from running out. Lewis's memo called it "the perfect storm": an unprecedented freight market collapse plus dramatic monetary tightening.

### Why it died — four accounts, and you should not flatten them

1. **Macro and timing** *(Lewis's own account)*: the freight recession and the VC funding contraction arrived simultaneously. Outside management control.
2. **Blitzscaling mismatch** *(FreightWaves)*: growth-at-all-costs requires network effects, switching costs and scale economies. Brokerage has **none of them** — commodity matching, near-zero carrier switching cost. Scaling the capital just scaled the losses.
3. **Tech over operations**: Convoy underweighted the relationship layer that incumbents use to secure capacity when it is tight. Strong in short-haul regional freight; never built depth with large carriers.
4. **Death from overfunding**: $900M+ let it avoid unit-economics discipline for years. When sentiment flipped from growth to profitability in 2022, the economics were exposed as never having worked.

These are complementary, not competing. An episode that picks one is editorialising.

### The ending nobody could have written

**Flexport bought Convoy's technology stack around November 1 2023** — a reported, and never confirmed by either party, **$16M**, plus roughly 50 employees including Lewis. Not the company; not the liabilities. The technology.

**In July 2025, Flexport sold that same stack to DAT Freight & Analytics for about $250M.**

DAT. The corkboard at the Jubitz Truck Stop. **The load board that digital freight brokerage was built to make obsolete ended up owning its technology** — and the asset round-tripped from a $3.8B equity valuation, to $16M, to $250M, across three owners in under two years.

## What Actually Failed — the distinction that matters

**"Digital freight brokerage failed" is wrong, and an episode must not say it.**

Only Convoy fully shut down. **Transfix** sold its brokerage business to NFI and pivoted to selling its TMS as software. **Loadsmart** retreated toward dock scheduling and TMS tooling. **Next Trucking** was acquired by another broker in a distress sale. **Uber Freight is still operating** *(no verified public standalone profitability figure — do not assert one)*.

Meanwhile the incumbents are shipping exactly the automation the startups promised. **C.H. Robinson** reports LLM-driven automation at scale — reading inbound email to auto-quote with an average response of 2 minutes 13 seconds, auto-tendering across modes, 10,000+ routine transactions a day. *(Company-reported, not independently audited.)*

So the defensible claim is narrow: **venture-scale, growth-at-all-costs, digital-only brokerage failed as a standalone business in this cycle.** Technology layered onto incumbent brokerage is proceeding fine. Those are completely different findings, and conflating them is how a plausible episode becomes a wrong one.

## What's Still Open

- [[problems/freight-brokerage/high-impact|🔴 Dynamic lane pricing and margin optimisation]] — yield management, unrecognised as such
- [[problems/freight-brokerage/worker-life-1|🟢 Automated load tendering and carrier outreach]] — the 80–100 calls a day
- [[niches/freight-brokerage/broker-pricing-science/profile|Broker Pricing Science]]
- [[niches/freight-brokerage/load-matching-dispatch/profile|Load Matching & Dispatch Automation]]
- [[niches/freight-brokerage/carrier-vetting-fraud-prevention/profile|Carrier Vetting & Freight Fraud Prevention]] — double-brokering, the fraud the load board enabled
- [[niches/freight-brokerage/load-board-market-data/profile|Load Board & Freight Rate Market Data]] — DAT's actual business, and now Convoy's tech

## The Transferable Pattern

> **Before believing a market can be disrupted by software, ask what the incumbent's advantage actually is. If it is an information asymmetry, software dissolves it. If it is a relationship that produces capacity under stress, software does not — and capital spent as though it does is capital lost.**

For an FDE the operational version is a single question: **what happens to this business in its worst quarter?** Convoy's model worked when capacity was loose and matching was the binding constraint. In a tight market the binding constraint is *who will actually take your load at 4pm on a Friday*, and that is answered by a relationship, not a ranking.

The vault said this before Convoy died. `industries/freight-brokerage.md` describes carrier relationship depth as *"the primary competitive advantage of a senior broker over a junior one."* An algorithm is a junior broker with excellent recall and no phone.

**Sources:** dat.com company history and blog (Dial-A-Truck, April 3 1978); truckstop.com (Scott Moscrip, 1995); Wikipedia, *DAT Solutions*, *TMW Systems*, *Convoy (company)*; Wikipedia and The Regulatory Review (Motor Carrier Act of 1980); CNBC (Convoy funding rounds 2019, 2022); GeekWire (shutdown memo, Flexport acquisition); FreightWaves (*Death from overfunding*, *Convoy's tech focus may have obscured the human element*, *Convoy autopsy*, Flexport–DAT sale); Supply Chain Dive; DAT news release (DAT–Flexport transaction, July 2025); C.H. Robinson press releases 2024–25 (company-reported automation figures); this vault's `industries/freight-brokerage.md`.
