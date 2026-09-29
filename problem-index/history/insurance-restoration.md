# History: Insurance Restoration

**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Secondary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — The PC & the Spreadsheet]]
**Origin Parent:** [[origins/insurance-carriers/profile|Insurance Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** When two parties must agree on a number to conclude a transaction, whoever owns the shared reference database that the agreement rests on has effectively set the price — check whose revenue that owner actually depends on before you call the number neutral.

## Before

A water-damage or fire-damage repair is, mechanically, a negotiation between two parties who do not trust each other's arithmetic: the contractor who has to be paid for real labour and materials, and the carrier who has to verify the bill matches the policy's covered scope and no more. Before a shared estimating standard existed, that negotiation happened line by line, on paper, per job — a contractor's handwritten scope against an adjuster's own judgement of what the trade should cost in that market, resolved by argument, by whichever side had better local information, or, at the limit, by the policy's appraisal clause. There was no common unit of account both sides had already agreed to before the argument started.

This is the same shape as the paper ledger in [[history/dental-practices|dental practices]] — money and record kept as separate objects a human reconciled by hand — except here the reconciliation is adversarial by design: the two parties are independently pricing the same repair and comparing answers, not cooperating on a shared record.

## The Origin Event

**Xactware was founded in 1986** (company-stated founding year, per Xactware/Verisk's own corporate records). This session could not independently verify founders' names, an exact date within 1986, or a first-release date for Xactimate distinct from the company's founding — the closer detail available for [[history/dental-practices|Dentrix and Eaglesoft]] does not appear to exist in comparably citable form here. **That gap is recorded rather than papered over.**

What is well documented is the corporate lineage that follows:

| Date | Event |
|---|---|
| **1986** | Xactware founded (company-stated) |
| **Aug. 2006** | **ISO acquires Xactware** — "a provider of estimation software and services for the property insurance, remodeling and restoration industries" |
| **2008 / 2009** | Verisk Analytics formed as ISO's holding company; Verisk IPOs |
| **Dec. 2018** | CoreLogic acquires **Symbility Solutions** (Calgary) — Xactimate's most credible rival platform |
| **June 18, 2020** | RIA's Advocacy & Government Affairs Committee briefs Xactware CEO Mike Fulton on whether Xactimate "accurately reflects current pricing in your market" |
| **2021 / 2025** | CoreLogic taken private (Stone Point Capital, Insight Partners); rebrands as **Cotality** |
| **Apr. 2026** | Trade press reports a new "large loss efficiency" labour-time designation, cutting several allowances industry-wide |

The load-bearing fact in that table is the 2006 line: **the company that makes the pricing tool contractors use to bill carriers has been owned, since 2006, by the same organisation — ISO, later Verisk — that invented pooled, credibility-weighted loss-cost data for the insurers on the other side of the table.**

## What Became Cheap

**Agreement.** Specifically, the cost of getting two parties who don't trust each other's numbers to a settled figure on a routine claim, without a bespoke negotiation each time.

Xactimate's real product is not a price list — it is a shared vocabulary. Over 27,000 line-item codes cover almost every repair task a residential or light-commercial loss can require, each carrying a labour-and-materials price already agreed before the job starts, because both the contractor's estimate and the carrier's audit read off the same database. New codes and price adjustments are issued roughly monthly (Xactware's eService Center and bulletins document additions such as dry-ice-blasting codes added in 2020), and prices publish as named regional lists — the one trade-press example found this session cites "the Atlanta, Ga., price list," confirming geographic differentiation, though the specific claim that granularity runs to three-digit ZIP prefixes could not be independently confirmed and should be treated as unverified.

What that machinery replaced was the cost of *arguing*, line by line, job by job, over what a covered repair should cost. What it did not replace is the argument over *quantity* — how many square feet of drywall were actually affected, how far moisture actually migrated. That argument still happens on every job. The vocabulary is shared; the facts about a specific structure are not.

## How It Was Actually Solved

Mechanically: the contractor scopes the loss and selects codes and quantities in Xactimate; the software applies the *database's* price for each code, not the contractor's own rate. A contractor can override a price, but doing so invites the exact carrier scrutiny the shared code exists to avoid — that friction is the enforcement mechanism. The carrier's own claims system typically runs the same platform or a compatible audit tool, so an estimate can be machine-checked against the identical list rather than re-priced by an adjuster's private judgement. This is the same functional move as CDT coding in [[history/dental-practices|dental]] — a standard that makes a claim machine-legible to the payer — except here the code also carries a price, not just a billing category.

**This is not merely analogous to the credibility-weighting mechanism at [[origins/insurance-carriers/the-mechanism|the origin of this whole tree]] — it is the same company doing a structurally identical thing one layer further down the supply chain.** ISO's function since 1971 has been pooling claims experience across insurers into a class's pure premium — a shared, credible number no single insurer computes alone, which each insurer then prices around with its own private scoring. Since 2006, ISO/Verisk has owned a company doing exactly this for property-repair costs: a shared price list neither contractor nor adjuster sets alone, which each side negotiates around at the margins (quantity, condition, code selection) rather than on the price itself. The pooled floor moved from *premiums* to *repair costs*, and the same owner ended up underneath both.

## The Contest — real, but not where you'd expect it

There was a genuine rival platform: **Symbility Solutions**, out of Calgary, used by a real slice of the market including some Canadian and US carriers and TPAs. This session could not establish how close Symbility ever came to Xactimate's share, or find a documented account of *why* contractors and carriers chose one over the other — that comparative history does not appear to exist in easily citable form, and inventing a market-share narrative to fill the gap would be dishonest.

What is verifiable is how the contest ended: not with Symbility's product losing and the company folding, but with **CoreLogic acquiring Symbility Solutions in December 2018** — CoreLogic being a separate, and by some measures larger, property-data conglomerate, later taken private in 2021 and rebranded Cotality in 2025. The two viable claims-estimating platforms in this industry did not resolve into one winner and one corpse. They resolved into two platforms, each now owned by a large third-party data company whose core commercial relationships run to insurers and data buyers, not to the contractors keying in line items. **If there was a fight, both sides of it are now on the same side of the table** — a stranger and more useful finding for an FDE than a clean displacement story would have been.

## The Trade-Off

What was traded away: the contractor's ability to individually negotiate a labour rate, or a material markup, per job. What was gained: speed and certainty of payment on routine claims, because both parties price off the same instrument instead of starting from zero every time.

**Who eats the cost when the trade goes wrong:** the contractor, specifically in the gap between when real costs move and when the shared list catches up. The database updates on its own monthly cadence, set by its owner; a contractor's actual labour and material costs move on the market's schedule, which does not wait for Xactware's release notes — most visibly after a storm floods a regional labour market with restoration demand, or during a supply-chain shock. When the two diverge, there is no renegotiation of the underlying price, only a formal supplement request the carrier can accept, question, or decline (the vault's [[niches/insurance-restoration/supplement-negotiation/profile|Supplement Negotiation]] niche, in miniature).

## The Binding Constraint

**This is the strongest single fact in this file: the contractor does not set the price for a covered repair. A licensed, monthly-updated, regionally-priced database does — owned by Xactware, a subsidiary of ISO/Verisk since August 2006 — and the carrier on the other side of every negotiation requires or strongly incentivises its use.**

This is not a hidden arrangement; the industry's own trade association has organised around it in public, more than once, over six years:

- **June 18, 2020** — the Restoration Industry Association's Advocacy & Government Affairs Committee briefed Xactware CEO Mike Fulton directly, asking whether Xactimate "accurately reflect[s] current pricing in your market" and pressing for transparency in how the database is compiled. Xactware committed to work on regional accuracy; this session could not verify what concrete changes, if any, followed.
- **April 2026** — trade press documented a new "large loss efficiency" labour-time designation, cutting several time allowances — drive time eliminated, setup/cleanup time reduced, a restoration-environment productivity-loss factor removed entirely — averaging an estimated 4–5% reduction across affected estimates, applied globally across trades with no settled industry definition of what counts as a "large loss." The RIA was again preparing position statements.

Read together, this is a **recurring structural fight the industry keeps having to have, because there is no negotiating table.** There is a vendor release email, and a trade association that can ask questions but cannot vote on the price list. Xactware's position isn't obviously adversarial — its tool only has value if both sides trust it — but the asymmetry is real: the database's owner has always been an insurer-side data company (ISO, then Verisk), its largest commercial relationships run to carriers buying enterprise licensing at scale, and neutrality here is a design choice that must be actively maintained, not a default property of the tool.

**Flagged, not asserted:** a rigorous, independent, quantified study of how far Xactimate's price list lags real-world material and labour inflation (the 2020–2023 shock most relevant here) could not be found this session. What exists instead is qualitative trade-press evidence of an ongoing, organised dispute, plus one specific quantified vendor-side change — the 4–5% "large loss" reduction — moving in the direction contractors complain about. Real and useful. Not the same thing as a documented lag study.

## The Graveyard — mostly absent, and the one candidate isn't a corpse

There is no clean graveyard of dead estimating platforms here. Symbility Solutions, the one credible rival this session could verify, did not lose a market fight and die — it was acquired into a different data conglomerate in 2018 and appears to still exist as a product line. No other rival platform, and no specific named contractor casualty of the preferred-vendor system, turned up in sources reachable this session. Rather than manufacture a corpse to fit the template: **the casualties this industry produces aren't companies named in trade press. They're individual restoration firms who lose preferred-vendor status over a slipped response-time SLA or two bad quarters of customer-satisfaction score** (see [[niches/insurance-restoration/managed-repair-program-administrators/profile|Managed Repair Program Administrators]]) — real, per the vault's own problem notes, but not documentable as named events at this remove.

## What's Still Open

- [[problems/insurance-restoration/high-impact|🔴 Moisture migration and scope-of-loss prediction]] — $5K–$15K per job lost to underscoped water damage; unsolved because no platform connects field moisture readings to drying predictions
- [[problems/insurance-restoration/worker-life-1|🟢 The project manager on 24/7/365 call]] — no intelligent after-hours triage
- [[niches/insurance-restoration/property-repair-estimating-data/profile|Property Repair Estimating Data]] — directly on top of this file's central finding
- [[niches/insurance-restoration/supplement-negotiation/profile|Supplement Negotiation]] — disputing the price-list number after the fact
- [[niches/insurance-restoration/managed-repair-program-administrators/profile|Managed Repair Program Administrators]] — preferred-vendor status, up to 60–80% of a restoration company's revenue
- [[niches/insurance-restoration/moisture-documentation/profile|Moisture Documentation]] — the handheld-meter, grid-paper layer this file's mechanism section doesn't reach
- [[niches/insurance-restoration/restoration-industry-benchmarking/profile|Restoration Industry Benchmarking]] — an industry without pricing leverage building leverage from its own data instead
- [[niches/insurance-restoration/job-management-platform-data/profile|Job Management Platform Data]] — PSA, DASH, MICA, Next Gear: this industry's real Wave-4 artefact, sitting atop a pricing layer that isn't

## The Transferable Pattern

> **Before building a tool for two parties who must agree on a number to close a transaction, find out who owns the shared reference database that agreement will rest on, and whose revenue that owner actually depends on. A standard both sides use is not neutral by construction — it is neutral only for as long as its owner chooses to keep it that way, and that choice cannot be audited from the outside.**

This is the same lesson as dental's annual maximum, in a different shape. Dental's constraint was an inert number nobody had revisited — a policy artefact with no active owner. This one has an owner, and the owner is not neutral by accident: a subsidiary of the same company that invented pooled, carrier-side statistical credibility in 1971, now selling a structurally identical product one rung down the value chain, to the same carriers, about the contractors' own costs.

For an FDE, the move is the ISO/Xactware genealogy in this file, generalised: **trace who currently owns the "shared" number before building on top of it, and ask which counterparty that owner is actually paid by.** The workflow layer above that number — job management, moisture documentation, supplement tracking, benchmarking — is real, buildable, and exactly where this industry's vault niches point. The number itself isn't yours to move, and a better dashboard won't move it — the same mistake as expecting a faster verification tool to raise a dental insurance cap.

**Sources:** Wikipedia, *Verisk Analytics* (Xactware/ISO acquisition, Aug. 2006); Wikipedia, *Insurance Services Office* (founding 1971; Verisk holding co. 2008; IPO 2009); Wikipedia, *CoreLogic*/*Cotality* (Symbility acquisition, Dec. 2018; 2021 take-private; 2025 rebrand); LinkedIn company page, Xactware (1986 founding, company-stated); Cleanfax — "A Quiet Change in Xactimate Could Cost You on Every Job" (Jeff Cross, Apr. 10 2026), "AGA to Host Restoration Industry Briefing with Xactware" (June 17 2020), "Missing Line Items" (Nick Sharp); this vault's `industries/insurance-restoration.md`, `problems/insurance-restoration/*.md`, `origins/insurance-carriers/legacy.md` and `the-mechanism.md`. Founders' names, an exact 1986 date, and an independent quantified price-lag study could not be verified and are flagged above, not asserted.
