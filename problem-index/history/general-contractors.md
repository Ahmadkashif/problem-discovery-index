# History: General Contractors

**Industry:** [[industries/general-contractors|General Contractors]]
**Primary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** none — see note below
**Episode Tier:** 1
**Transferable Pattern:** A margin thin enough that one bad estimate erases the project teaches an industry to trust software for measurement long before it trusts software for judgment — and an FDE who conflates the two will be corrected by an estimator with twenty years of gut checks.

> **Origin Parent note.** No origin among the eighteen fits cleanly. Auto OEMs' MRP lineage is the closest in shape — a bill-of-materials explosion against a schedule — but MRP is push-based mass-production planning for a repeated product, and a construction bid is a one-off estimate for a never-repeated structure; the legacy file names no construction child. Treated as a direct Wave 3 child.

## Before

Estimating a job meant a person with a scale ruler and a highlighter walking a set of paper drawings, counting linear feet of wall, square feet of floor, and fixtures one takeoff at a time, then pricing each quantity from a cost book or from memory. Scheduling ran on the same paper logic that industrial planning did before computers: a hand-drawn bar chart, or — for the largest jobs — the critical path method, developed in the civil-engineering and defence-contracting world in the late 1950s, worked out with a pencil and a network diagram rather than software. **Payment itself was already standardised on paper before any of this computerised**: the American Institute of Architects' G702 (Application and Certificate for Payment) and G703 (Continuation Sheet) forms gave the industry a common schedule-of-values format — columns for scheduled value, previous billing, this period's work, stored materials, percent complete, balance to finish — that reads, and always read, exactly like a spreadsheet. *(Precise first-publication dates for G702/G703 could not be verified to a primary AIA source in this session.)*

## The Origin Event — a founder building his own house

**2002.** **Craig "Tooey" Courtemanche** founded **Procore** in Santa Barbara, California, after building his own home and discovering — as a technologist, not a contractor by trade — how much of the construction process still ran on paper, phone calls and fragmented email. Procore went public on the NYSE on **May 20 2021**, raising $634.5M.

This is one of the few genuinely dateable founder-moments in this vault's Wave 3 children, and it is worth naming precisely because it is rare in this file's neighbours: most of this industry's other software arrived the way dental's did, as slow accumulation rather than a single event. **Bluebeam**, the PDF markup tool that became a near-universal takeoff and drawing-review standard on construction sites, was also founded in **2002** — the same year, independently, solving an adjacent problem (marking up and measuring digital plan sets rather than managing the project around them).

Estimating-specific software followed a similarly gradual path: digital takeoff tools (PlanSwift, Sage Estimating, STACK) let an estimator measure quantities from a PDF instead of a paper set and a ruler, but — per this vault's own hub note — still "requires experienced estimators to apply the unit costs." The measurement got a computer. The pricing judgment did not.

## What Became Cheap

**Measuring a quantity from a drawing.** A digital takeoff tool turns hours of manual counting into minutes of clicking a polygon onto a PDF. This is the cheapest, least contested win in the whole file, and it is exactly wave-03's core effect: a repetitive arithmetic task that used to require a trained person's full attention now runs in the background of a tool anyone on the team can operate.

**What did not become cheap: the number itself.** This vault's hub note is explicit that experienced estimators develop, over a decade or more, "a mental model of cost per square foot by project type, structural system, and local market conditions that allows them to gut-check a takeoff before it's complete." No software product in this file's research automates that gut check — takeoff software counts; it does not price.

## The Trade-Off

**Margins of 3–7% net mean the cost of trusting the wrong number is existential, and that asymmetry is why the industry still keeps a human between the software and the bid.**

A takeoff error of a few percent is recoverable. An estimate that's wrong on unit pricing by the same few percent can consume the entire project's profit, because the margin *is* a few percent. That is the specific, quantifiable reason this industry's adoption of automation stops at measurement rather than extending to judgment: the downside of a bad number is asymmetric with the upside of a faster one. The bid — the actual number that goes out the door — still lives in a spreadsheet, because a spreadsheet is the one artefact an estimator can argue with, line by line, against a bid deadline, before signing their name to it.

## What Is Actually Happening Now — the SaaS rollup

Construction technology's last decade looks less like a competitive fight and more like **acquisition-led consolidation into two platform strategies**, worth recording as a finding rather than a contest with a winner:

- **Oracle** acquired **Textura** (construction payment-application and lien-waiver software) in **2016**, reportedly for approximately **$663M** *(figure commonly reported in trade press, not independently re-verified to a primary source this session)* — automating, not incidentally, the same G702/G703 schedule-of-values workflow described above — and **Aconex** (construction collaboration and document management, founded 2000 in Australia) for **US$1.19B**, completed **December 17 2017**.
- **Autodesk** acquired **PlanGrid** (field collaboration and blueprint markup, founded 2011) for **$875M**, closing **December 20 2018**.
- **Procore** stayed independent through IPO rather than being folded into a larger platform.

**There is no graveyard in the freight-brokerage or programmatic sense — no venture-scale failure.** What happened instead is that the specialised point tools construction actually needed (payment applications, document collaboration, field markup) proved valuable enough to be bought by the two enterprise-software giants already serving the industry's back office, rather than to displace them. Recorded as consolidation, not competition, because that is what the dated record shows.

## What's Still Open

- [[problems/general-contractors/high-impact|🔴 AI-Assisted Preliminary Cost Estimation from Architectural Drawings]] — the gut-check, not yet automated
- [[problems/general-contractors/worker-life-2|🟢 Schedule Delay Cascade Prediction]]
- [[problems/general-contractors/low-impact-2|🟡 Change Order Documentation from Field Observations]]
- [[niches/general-contractors/gc-preconstruction-estimating/profile|GC Preconstruction Estimating]]
- [[niches/general-contractors/estimating-bidding/profile|Estimating & Bidding]]
- [[niches/general-contractors/project-scheduling-management/profile|Project Scheduling & Management]]
- [[niches/general-contractors/construction-claims-forensics/profile|Construction Claims Forensics]]
- [[niches/general-contractors/subcontractor-prequalification-data/profile|Subcontractor Prequalification Data]]
- [[niches/general-contractors/reality-capture-progress-monitoring/profile|Reality Capture & Progress Monitoring]]

## The Transferable Pattern

> **Find the line between what the software measures and what the human still prices, and ask why that line sits where it does. In a thin-margin business, it sits exactly at the point where a wrong number stops being recoverable.**

An FDE pitching estimating automation to a GC should expect enthusiasm for anything that speeds up the takeoff, and real resistance to anything that proposes to finalise the number — not because the estimator distrusts computers in general, but because the margin structure of the business makes that specific trust extremely expensive to extend. The software that wins here augments the gut check. It does not replace the person whose name is on it.

**Sources:** Wikipedia, *Procore* (founding 2002, IPO May 20 2021), *Bluebeam* (founding 2002), *PlanGrid* (founding 2011, Autodesk acquisition Dec 2018), *Aconex* (founding 2000, Oracle acquisition Dec 17 2017, US$1.19B), *Building Information Modeling* (origins, Autodesk 2002 BIM white paper); trade-press reporting on Oracle's Textura acquisition (2016, ~$663M, not independently re-verified this session); AIA G702/G703 schedule-of-values format (precise first-publication date unverified this session); this vault's `industries/general-contractors.md` and `problems/general-contractors/*.md`.
