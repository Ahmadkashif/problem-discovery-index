# Phase 3 — The History Layer

Single source of truth for this workstream. A fresh session should be able to read only this file and continue correctly.

**To launch a session:** tell a fresh agent `Read series/_plan.md and execute it.` — scope comes from the CURSOR below.

---

## CURSOR

**Status:** H5 complete — spine, 18 origins, 66 history files, 40 failure cases. **H6 (episode assembly) is all that remains.**
**Research:** ✅ **approved and required** — this phase asserts historical fact
**Origins:** ✅ approved — **all 18** (Tier A + Tier B merged 2026-09-18 at user instruction)
**Myths killed to date:** 90

| Stage | Work | Sessions | Status |
|---|---|---|---|
| **H1** | Era spine — `series/_eras.md` + `series/eras/<wave>.md` ×12 + wave assignment for all 250 | 1 | ✅ **complete** 2026-09-18 |
| **H2** | `origins/` — **18** parent industries, 5 files each (91 files) | 1 | ✅ **complete** 2026-09-18 |
| **H3** | Pilot — 3 `history/<slug>.md`, break and rebuild the template | 1 | ✅ **complete** 2026-09-19 |
| **H4** | History sweep — Tier 1 children (66) | 1 | ✅ **complete** 2026-09-19 |
| **H5** | Graveyard — `series/failures/` (40 cases) | 1 | ✅ **complete** 2026-09-19 |
| **H6** | Episode assembly | ongoing | ⬜ not started |

**To resume:** read this file → read `series/_bookmark.md` → run the verification block (§10) → continue at the next uncompleted stage.

---

## 1. What we are building

A web series for **aspiring forward deployed engineers** — people new to industry with no exposure to how businesses actually work.

Each episode takes one industry and answers, in order:

1. What does this business do, and who pays it?
2. What was the fight it had to win?
3. How did it model that problem?
4. How was technology actually used to solve it — mechanically?
5. What was traded away, and who ate the cost?

**The premise being taught:** almost every tool we have was built to win a specific commercial fight in a competitor-heavy market. Tools are not neutral artefacts — they are frozen arguments about what mattered to someone.

**The skill being taught:** trade-off analysis. A grad who finishes a season should be able to walk into an unfamiliar business, find the contested decision, and reason about what a solution costs.

## 2. Why this phase exists

The vault was built as a **prospecting index**. `_direction.md` §1 says so: *"We are scouting the next vertical to sell into."* Every existing layer answers **"where is there an unsolved problem worth money?"**

FDE training needs the inverse: **"here is a problem that *was* solved, here is exactly how, and here is what they gave up."**

The vault maps open problems. A curriculum needs closed ones. This is a second axis, not a patch.

### The gap, measured (audit 2026-09-18, 13,320 content files)

**The present incumbent is documented exhaustively:**

| Term | Files | | Term | Files |
|---|---|---|---|---|
| spreadsheet | **1,405** | | fax | 100 |
| Excel | 480 | | barcode | 68 |
| QuickBooks | 192 | | Epic (the EHR) | 92 |

**The arrival of any technology, essentially never:**

| Term | Files | | Term | Files |
|---|---|---|---|---|
| "in the 1990s" | 2 | | SABRE | 1 |
| "replaced the" | 8 | | containerization | **0** |
| "originally" | 8 | | Toyota Production System | **0** |
| "first built" | **0** | | HITECH | **0** |
| "went bankrupt" | **0** | | | |

Only **15 of 250** industry hub notes contain any year at all.

### The diagnostic example

**Epic** appears in **92** files — always as a system you must integrate against. **HITECH**, the 2009 statute that forced EHR adoption and thereby manufactured the entire healthcare-software market the vault describes, appears in **0**.

The vault has every scar and no wounds.

> **The rule this phase exists to enforce: never describe a constraint without naming the decision that created it.**

## 3. The era spine

Twelve waves, scoped from **when computers arrived**. Pre-computer origins (licensed trades, deregulation) appear only as "what was true the day before."

The unifying mechanism and the series' through-line:

> **Each wave drove the cost of exactly one thing to near zero, and an industry crystallised around the newly cheap thing.**
> Coordination → items → modelling → integration → distribution → compute → memory → location → attention → audience → presence → inference.

All dates below are research-verified (2026-09-18). Detail and sourcing expand into `series/eras/<wave>.md` at H1.

| # | Wave | Span | Verified trigger | What went to ~zero | Vault children |
|---|---|---|---|---|---|
| 1 | **Mainframe & batch** | 1955–75 | ERMA unveiled Sept 1955, production Sept 14 1959 (BofA); MICR adopted by ABA 1956; SABRE built 1957–60, live 1960, nationwide 1964 | arithmetic over a whole customer file | payment-processors, credit-unions, insurance-tpa, medical-billing, collections-agencies, payroll-platforms |
| 2 | **Departmental & item-level** | 1964–80 | Orlicky formulates MRP at IBM c.1964, book 1975; **UPC first scan June 26 1974, 8:01am**, Marsh Supermarket, Troy OH; ACH live 1972, NACHA June 20 1974 | tracking physical things one at a time | contract-manufacturing, metal-fabrication, auto-dealers-independent, printing-shops, food-distributors, restaurant-suppliers |
| 3 | **PC & the spreadsheet** | 1979–92 | VisiCalc Oct 17 1979; Lotus 1-2-3 Jan 26 1983; Excel Mac Sept 30 1985, Windows Nov 19 1987 | **modelling** — anyone could build one without a programmer | *no industry of its own — the largest footprint in the vault* |
| 4 | **Client–server & ERP** | 1992–2000 | SAP R/3 July 6 1992 (after R/2 1979, R/1 1972) | one company having one version of its own numbers | warehouse-3pl, food-distributors, freight-brokerage, contract-manufacturing |
| 5 | **The commercial web** | 1993–2004 | Mosaic 1.0 April 22 1993; Netscape 1.0 Dec 1994; first SSL card purchase Aug 11 1994 | distribution and discovery | online-marketplaces, ecommerce-sellers, affiliate-networks, seo-tooling-vendors, email-sms-marketing-platforms |
| 6 | **Cloud & SaaS** | 1999–2015 | Salesforce March 8 1999; **AWS S3 March 14 2006, EC2 Aug 25 2006** | the *fixed* cost of compute — capex became opex | all 22 vertical + horizontal SaaS, developer-tools-vendors, observability-vendors, ci-cd-platforms |
| 7 | **Big data** | 2006–15 | Hadoop split from Nutch Jan 28 2006, v0.1 April 2006; Spark top-level 2014 | keeping everything | bi-analytics-platforms, customer-data-platforms, data-platform-integrators |
| 8 | **Mobile & GPS** | 2007–16 | iPhone on sale June 29 2007; Uber (as UberCab) March 2009; DoorDash 2013 | knowing where the workforce is | gig-delivery-platforms, rideshare-fleet-operators, last-mile-delivery, field-service-software |
| 9 | **Programmatic** | 2005–21 | Right Media live April 1 2005; AdECN Oct 2005; DoubleClick Ad Exchange 2009 (scale); OpenRTB 2010 → IAB 2.1 Jan 2012. **Ended by ATT, iOS 14.5, April 26 2021** | pricing attention per impression | programmatic-ad-platforms, retail-media-networks, marketing-attribution-vendors, audio-adtech-networks |
| 10 | **The creator platform** | 2012–20 | algorithmic feeds + direct payout rails | reaching an audience | creator-businesses, newsletter-media, podcasting-networks, ugc-video-platforms, influencer-marketing-platforms |
| 11 | **The COVID dislocation** | 2020 | emergency licensure waivers + reimbursement parity, March 2020 | the requirement of physical co-presence | telehealth-platforms, remote-work-infrastructure, online-tutoring-platforms, virtual-assistant-services, digital-bpo-operations |
| 12 | **Transformers** | 2017– | *Attention Is All You Need*, arXiv June 12 2017; ChatGPT Nov 30 2022 | inference over unstructured text | the 11 Data & AI Economy industries, llm-application-tooling, ai-inference-providers, synthetic-data-providers |

**Wave 3 is the sleeper.** It created no industry and is the live incumbent in 1,405 files of this vault. For an FDE it is the most important wave on the list: you are almost always replacing a spreadsheet, and the spreadsheet won for reasons that still hold.

**Regulatory triggers cut across waves.** HITECH (Feb 2009), HIPAA (1996), SOX (2002), Dodd-Frank (2010), GDPR (2018), the ELD mandate (2017) and the Motor Carrier Act (July 1 1980) create or reshape industries without inventing anything. Assign such an industry to the wave matching the *date*, and say in the file that the trigger was statutory.

### The chronology of failure

Phase 2 identified three recurring failure classes. They are not a taxonomy — **they are a chronology**, and this is the series' central argument.

| Class | Era | What happens |
|---|---|---|
| **The missing join** | integration (W1–W5) | Two systems never spoke. Nobody's fault. |
| **The declined join** | platform (W6–W9) | One party now owns both sides and *chooses* not to measure, because the honest number is smaller. |
| **The asymmetric hold** | gig (W8, W10–11) | The platform measures the worker exhaustively and itself not at all. |

The failure mode did not change because engineers got worse. It changed because **as technology consolidated, the party able to measure became the party who benefited from not measuring.**

## 4. Vault safety — non-negotiable

### PROTECTED — never edit, never delete, append nothing

| Layer | Files |
|---|---|
| `industries/*.md` | 250 |
| `problems/**` | 1,750 |
| `niches/**` | 11,320 |
| `metadata/**` | 3 |
| `plans/**` | 12 |
| **content-layer subtotal** | **13,335** |
| root trackers `_*.md` | 7 |
| `CLAUDE.md` | 1 |
| `_state/*.md` | 3 |
| **Total protected** | **13,346** |

Phase 3 is **purely additive**. If a session finds an error in a protected file, it records it in `series/_bookmark.md` under `## Flagged` and **does not fix it**.

### WRITABLE — new in Phase 3

```
series/_plan.md            this file
series/_eras.md            the twelve-wave spine (canonical)
series/_bookmark.md        build log, flagged items, myths killed
series/_state/             durable helpers — wave-assignment.txt, kids.sh
series/eras/<wave>.md      one per wave
series/failures/<case>.md  the graveyard, cross-cutting
origins/_index.md          the ten parents
origins/<slug>/*.md        5 files each
history/<slug>.md          one per child industry
```

**Nothing this phase produces may live outside the vault.** Scratch directories are deleted with the session. If a stage generates data a later stage needs — an assignment table, a helper script — it goes in `series/_state/` before the session ends. `series/_state/README.md` documents what is there.

`history/` is a **fourth slug-keyed layer** beside `industries/` `problems/` `niches/`. Existing parity checks compare `industries↔problems` and `industries↔niches` only, so a fourth key trips nothing.

**Do not add origins to `industries/`.** They are teaching cases, not prospects, and folding them in would break 1:1:1 parity.

### Tag discipline

Unchanged. `metadata/tags.md` remains the sole registry — **190 canonical tags**, verified against `_state/safe-tags.txt`. Phase 3 files MAY carry canonical tags where they describe a modelling approach. They MUST NOT invent tags. Never reintroduce a deprecated tag.

## 5. Research and citation discipline

Research is **approved and required**. A wrong date in a published episode is an unrecoverable credibility loss.

1. **No unsourced date.** Every file ends with `**Sources:**`.
2. **Flag the contested.** Where accounts conflict, say so in the file rather than picking. Contested history teaches better than clean history.
3. **Kill the myths.** Where a famous anecdote does not survive checking, the file says so explicitly. This is among the most valuable output of the phase — log every kill in `series/_bookmark.md`.
4. **Approximate honestly.** `~1987` is fine. A confident wrong date is not.
5. **Mechanism over anecdote.** "What the system actually computed" outranks "who said what in the boardroom."
6. **Separate authorized from disbursed.** Programme dollar figures are routinely inflated by conflating the two. Say which you mean.

### Myths already killed during spine research — do not reintroduce

| Myth | Correction |
|---|---|
| "T+2 settlement explains the payment-processor batch lag" | **Wrong.** T+2 is *securities* settlement (US equities → T+1, May 2024). Card/ACH batch cycles are a different mechanism: overnight windows inherited from paper check clearing. Also note the "why batch was chosen" rationale is a well-supported inference, **not** a documented decision. |
| "RTB was invented in 2009" | Right Media went live **April 1 2005**; AdECN Oct 2005. 2009 (DoubleClick Ad Exchange) was *scaling*, not origin. |
| "NASDAQ was the first electronic stock exchange (1971)" | In 1971 it was a **quotation system**, not a trading venue or a legal exchange — execution still happened by phone. It became a registered exchange only in **2006**. |
| "Yield management killed People Express" | Strong simplification. Co-causes: overexpansion, the debt-heavy 1985 Frontier acquisition, service collapse. Burr's own quotes are real and citable; the monocausal claim is not. |
| "HITECH spent $36B" | **No single authoritative figure exists.** $19.2B / $27B / $30B / $35B all circulate depending on authorized vs obligated vs disbursed, and on whether the whole HITECH title or only the CMS incentive programmes is counted. Always caveat. |
| "SABRE launched in 1964" | Built 1957–60, first live **1960** at one site, nationwide **1964**. Qualify which milestone is meant. |
| "Telecom churn prediction dates to early-1990s AT&T" | Unverified, likely myth. Earliest solid documented production case is **Mozer et al., NeurIPS 1999 / IEEE 2000** on a US wireless carrier. |
| "MRP and Toyota's JIT are the same lineage" | **Opposed.** MRP is US/IBM computerised *push* scheduling; TPS/JIT is Japanese *pull*-based, computer-independent shop-floor discipline that predates it. Conflated constantly in pop-business retellings. |
| "Containerization instantly crashed shipping costs" | The unit-cost drop is real (~$5.86/ton hand-loaded → ~$0.16/ton containerized, per Levinson). The *trade-growth* effect was **delayed** — NY/NJ real labour cost per ton fell only ~7% from 1970–75 despite productivity doubling, because unions extracted fringe-benefit concessions. |
| "ISO sets insurance rates" | Advisory **loss costs** only, since 1989. Insurers set their own rates. |
| "Insurers digitised late" | Backwards. Insurers were **1950s** commercial computing pioneers. |
| "Salesforce coined SaaS" | The term is in print by **Feb 2001** (SIIA), popularised as an acronym 2005 — after Salesforce's 1999 founding. |
| "Semiconductor yield analytics has a founding case" | It does not. Gradual, SEMATECH-consortium-driven; earliest datable milestone is early-1990s run-to-run CMP control. Distrust any single-company origin claim. |

### Killed during H1 (era spine research)

| Myth | Correction |
|---|---|
| **"COVID permanently moved the telehealth regulatory boundary"** | **Largely false — this was this project's own working thesis and it did not survive.** HIPAA enforcement discretion **expired** Aug 9 2023. Interstate licensure waivers mostly expired (only NY and TX by May 2023). Medicare parity survives only on repeated short-term congressional patches — currently through Dec 31 2027. Utilisation settled at 13–17% of visits, ~55% below peak. Correct framing: *settled above baseline, well below peak, on borrowed regulatory time.* |
| "COVID created the EOR industry" | Deel and Remote were both founded **2019**, Papaya Global 2016. A demand shock, not an origin story. |
| "85% of big data projects fail" | No traceable primary study. An analyst soundbite (Gartner's Nick Heudecker) layered on an earlier, also-uncited 60% figure. Cite as a widely repeated industry claim or not at all. |
| "25% of Apple II buyers bought it for VisiCalc" | Unsourced press retelling, not a study. The killer-app *effect* is real (35k→78k units 1979–80); the *number* is spurious precision. |
| "94% of spreadsheets contain errors" | Misquote. The 94% is from Panko's **13 field audits of real operational spreadsheets** (1995–2004), not all spreadsheets everywhere. Lab studies show ~3.9% cell error rate; field ~5.2%. Keep the distinction. |
| "The London Whale was one Excel error" | Oversimplified. Regulatory post-mortems attribute the $6.2B loss to a chain of modelling, risk-limit and oversight failures. The copy-paste error was one link. |
| "Google decided last-click attribution" | No. **DoubleClick's cookie tooling (Feb 1996) could only reliably capture the last touch**, so last-click became the path of least resistance; agency practice entrenched it; Google popularised it; the IAB codified it (2004, 2009). Nobody chose it. Former IAB president Greg Stuart calls it "a big mistake." |
| "Amazon invented affiliate marketing" | PC Flowers & Gifts predates Amazon Associates (July 1996). Amazon scaled the model. |
| "Google invented link-based ranking" | Kleinberg's HITS and related link-analysis research were contemporaneous. Google's edge was execution and scale, not sole invention. |
| "Hadoop derived from Google's code" | Architectural inspiration from the GFS (2003) and MapReduce (2004) papers only. No code reuse, no Google involvement or collaboration. |
| "Vine's shutdown shows platforms killing creators" | Primarily Twitter's monetisation and strategic failure, not an algorithmic distribution change. Do not conflate with the adpocalypse or Facebook's pivot-to-video, both of which have hard documentary evidence. |
| Creator power-law point figures | Vary widely by source, year and platform definition (top 1% capturing 15%→21% of payment volume, 2023→2025). Use ranges. Treat the *shape* as the finding, not any single number. |


### Killed during H2 (origins research)

| Myth | Correction |
|---|---|
| "Reg NMS Rule 611 caused HFT and fragmentation" | Rule 611 bars executing at a price *worse* than a protected quote. **It does not mandate routing to the best-priced venue.** It created an incentive to *see and react to* every protected quote fast — that incentive, not a routing mandate, made speed valuable. |
| "UPS saves money by not turning left" | Myth with a kernel. UPS never *bans* left turns; NPR reported the heuristic in **2007, pre-ORION**. ORION is full route/sequence optimisation; left-turn avoidance is one minor input, popular because it is telegenic. |
| "ORION saves 100M miles / $300–400M a year" | Those are **full-deployment projections**, routinely quoted as achieved. Actual banked saving by Dec 2015 (partial deployment): **$320M+ cumulative**. Measured per-driver effect: 6–8 fewer miles/day. |
| "Amadeus dates to the 1960s" | **Founded 1987.** Conflated with Sabre's 1960 origin. |
| "OTAs killed travel agents" | Oversimplified. Commissions went to zero by 2002 and ARC locations fell ~36,000 → ~13,000, but agents largely **re-intermediated on a fee-for-service model** rather than disappearing. |
| "Priceline's Name Your Own Price was a reverse auction" | It was not. Sellers pre-set a **hidden floor**; the buyer bid blind to brand; the trade cleared automatically if it beat the floor. A price-discrimination fence, not an auction. |
| "EDC replaced paper CRFs in [year]" | **No credible date exists.** Real trial groups were still converting from paper as late as **2012**. Treat any specific year as unsupported. A negative finding, recorded as one. |
| "AI is revolutionising drug discovery" | >$100B invested; gains sit almost entirely in **preclinical**. **~90% of candidates entering clinical trials still fail — unchanged**, because the bottleneck is human biology and trial endpoints. No FDA approval clearly attributable to an AI-discovered molecule as of sources checked. |
| "Fee-based compensation replaced the 15% commission" | It did not. The commission eroded gradually from the 1980s with **no clean end date**, and the ANA has documented **commission-equivalent economics resurfacing in programmatic** as undisclosed markups and rebates. Same structure, less visible layer. |
| "Programmatic destroyed agency margins" | Oversimplified — margins are **expanding** for surviving majors via consolidation and cost cuts. The squeeze hit mid-tier and independent shops. |
| "82% of advertisers have in-housed" | ANA-member **self-report**, a more sophisticated cohort than the average advertiser. Treat as an upper bound, not a market-wide figure. |
| "ARRA mandated smart meters" | ARRA **funded** rollout through $3.4B in competitive grants. It mandated nothing; utilities and state regulators drove adoption. |
| "The 2003 Northeast blackout was a grid overload" | The proximate cause was a **race-condition software bug in GE's XA/21 EMS** at FirstEnergy, which silently disabled the alarm system. Tree contact on a sagging line was the trigger; it should have stayed local. **The failure was that nobody knew.** |
| "PTC and PSR are the same story" | Unrelated. **PTC** is a federally mandated collision-avoidance system (RSIA 2008, complete Dec 29 2020, ~$15B). **PSR** is a private cost-cutting operating model. Constantly conflated. |
| "PSR was a computational breakthrough" | It is a **management heuristic** — scheduling discipline plus asset reduction — not an optimisation advance. Genuine network-flow optimisation for blocking and yard operations remains an open OR problem. |
| "PSR began in 1993" | Contested. 1993 (Harrison at Illinois Central) is standard, but Harrison traced his thinking to the early 1980s at Burlington Northern, and some credit Ed Moyers with the original IC operating plan. |
| "Stuxnet hacked a nuclear plant" | It targeted **uranium enrichment centrifuges at Natanz**, not a power reactor. ~1,000 IR-1 centrifuges damaged while operators were fed falsified HMI readings. |
| "Stuxnet proved air gaps don't work" | The precise lesson is that air gaps fail at the **human and removable-media layer** — it propagated by USB — not that network isolation is worthless. |
| "Shell and Cutler invented model predictive control" | They get primacy for the dominant commercially propagated version (DMC). **Concurrent independent MPC-family work** (model algorithmic control, IDCOM) was underway elsewhere in the same period. |
| "The Anderson Bombshell caused Intel's DRAM exit" | Causation is **multi-factor and not traceable to one event.** The 1980 HP finding (Japanese 16K RAMs beating US parts ~6:1 on defect rate) is real and is what produced SEMATECH in Aug 1987. |
| "McLean invented the container" | Matson Navigation containerised independently in **1958** (SS *Hawaiian Merchant*). Two origin lines, not one inventor. |
| **"Orlicky formulated MRP by studying the Toyota Production System"** | **Chronologically impossible — and this error was introduced by *this project's own* research brief, then caught by the agent writing the file.** TPS was undocumented outside Toyota until Ohno's 1978 Japanese-language book, **14 years after** Orlicky's 1964 work at IBM. Widely repeated; apocryphal. |
| "GM bought its way to Toyota-level quality" | The opposite. GM's 1980s automation programme (widely cited at ~$90B — an order of magnitude, not an audited figure) failed, while **NUMMI (1984)** succeeded using the same unionised workforce with far less capital and real kanban/andon discipline. Capital could not buy the discipline. |
| "Toyota's pull model won" | Neither lineage won. Modern manufacturing runs a **hybrid** — MRP/ERP for planning, kanban for floor execution. |
| "ORION proves UPS out-optimised FedEx" | FedEx runs comparable internal route and network optimisation. ORION is simply the system UPS chose to submit through INFORMS's public Edelman process. **Do not mistake a published case study for competitive superiority.** |
| "Every origin fight produces a corpse" | Package carriers produced a **duopoly**. Network topology can be replicated with capital; an algorithmic capability gap (airline yield management) could not. Different class of outcome — worth teaching as the contrast. |
| "FICO scoring began in 1989" | Two distinct founding dates, 15 years apart and routinely conflated: **Fair Isaac's first lender scorecards 1956–58**, and the **bureau-wide consumer FICO score 1989–91**. |
| "The big three bureaus were always national" | **TransUnion did not reach full US coverage until 1988.** |

| "Digital EMS replaced analog control in [year]" | A **decade-plus, vendor-by-vendor migration** (late 1960s–80s). No single date is defensible. |
| DMC's industry-wide ROI figure | **Unsourceable at rigorous precision.** Qualitative consensus that constraint-pushing paid for itself is strong; no audited industry-wide number exists. Do not invent one. |
| *(negative)* "Every origin has a competitive duel" | **Telecom and pharma CROs do not.** Telecom's fight was regulatory (1984 AT&T divestiture, cellular duopoly licensing) manufacturing competition industry-wide. CRO formation was gradual and multi-company. Distrust any source naming a single founding battle. |


### Structural finding from H2 — carry into H3 and H6

**Six of the eighteen origins have no competitive duel**, and the files say so rather than manufacturing one:

| Origin | What stood in for the fight |
|---|---|
| Telecom carriers | Regulatory — the 1984 AT&T divestiture and cellular duopoly licensing manufactured competition industry-wide |
| Pharma R&D & CROs | Gradual, multi-company industry formation; no founding battle |
| Semiconductor fabs | No founding case for yield analytics; the March 1980 "Anderson Bombshell" and SEMATECH (Aug 1987) supplied the opening instead |
| Electric utilities | A systems-failure case — the 2003 Northeast blackout |
| Railroads | An internal operating-model argument (PSR), with the credit dispute and the safety argument both left unresolved |
| Process manufacturing | A genuine adversarial attack — Stuxnet |

**The episode format cannot assume a duel.** A third of the parent industries have no People Express. `the-fight.md` must be understood as *"the contest the technology was built to win"* — which may be against a rival, a regulator, a physical limit, an adversary, or the industry's own operating assumptions.

H3 must test whether `history/<slug>.md` survives this. A child industry with no named competitor is the likelier case, not the exception.

**Two inheritance links were flagged in-file as weak** rather than stretched: electric-utilities → agtech-platforms, and process-manufacturing → metal-fabrication. Both are adjacency, not transplant. H4 should expect more of these and should keep flagging them.

## 6. The eighteen origins

These sit **above** the 250, not beside them. Each owns a founding computing story the existing industries inherited.

| # | Origin | Wave | Verified founding event | Children in the vault |
|---|---|---|---|---|
| 1 | **Airlines** | 1 | SABRE live 1960 / nationwide 1964; Crandall's Super Saver 1975; **DINAMO + Ultimate Super Saver 1985** | hotels-boutique, short-term-rentals, charter-bus-operators, every dynamic-pricing note |
| 2 | **Supermarket chains** | 2 | UPC first scan **June 26 1974, 8:01am**, Troy OH — Wrigley's Juicy Fruit, 67¢. IRI founded 1979 | retail-pos-platforms, retail-media-networks, independent-retailers, subscription-commerce, specialty-food-retail |
| 3 | **Retail banking** | 1 | ERMA Sept 1955 → production Sept 14 1959; MICR/E-13B adopted 1956; SCOPE 1968 → first ACH 1972 → NACHA 1974 | payment-processors, neobanks, bnpl-providers, lending-marketplaces, credit-unions |
| 4 | **Hospital systems** | 7 *(statutory trigger)* | HITECH enacted **Feb 2009** under ARRA; Meaningful Use Stages 1–3; penalties from 2015. Basic EHR 9% (2008) → 84% (2015) | healthcare-practice-software, medical-billing, telehealth-platforms, urgent-care, home-health-agencies |
| 5 | **Insurance carriers** | 1 | IBM 650-era actuarial computing ~1956; ISO formed **April 1 1971**; advisory loss costs 1989; FICO insurance score 1993 | independent-insurance-agents, insurtech-platforms, insurance-tpa, public-adjusters, insurance-restoration |
| 6 | **Exchanges & market makers** | 1 → 9 | Instinet 1969; NASDAQ quotation system **Feb 8 1971**; Island ECN 1996/97; Reg NMS adopted June 9 2005, Rule 611 compliance **Feb 5 2007**; Spread Networks Aug 2010 → microwave 2012 | crypto-exchanges, robo-advisors, wealth-management-rias |
| 7 | **Telecom carriers** | 4 → 7 | OSS/BSS billing at scale; **Mozer et al. 1999/2000** churn modelling on ~47,000 subscribers — logistic regression, trees, nets, boosting, framed on ROI | every subscription business in the vault |
| 8 | **Ocean shipping & ports** | 2 *(pre-computer trigger)* | **SS Ideal-X, April 26 1956**, Port Newark → Houston, 58 containers. ISO/TC 104 formed 1961; ISO/R 668 published Feb 1968 | freight-brokerage, warehouse-3pl, customs-brokers, cold-chain-logistics |
| 9 | **Semiconductor fabs** | 4 | SPC doctrine by 1991; SEMATECH run-to-run CMP control early 1990s → APC (FDC + R2R) mid-1990s. No single founding case | electronics-contract-mfg, medical-device-mfg — and all compute downstream |
| 10 | **Auto OEMs** | 2 | Orlicky formulates MRP c.1964, book 1975; Black & Decker first production user; Wight's MRP II 1983. **Separately:** Ohno's kanban from 1953, TPS book 1978, NUMMI 1984 | contract-manufacturing, metal-fabrication, auto-dealers-independent, auto-repair-shops |

Two deliberate irregularities, both kept because they teach:

- **Ocean shipping's founding event is not a computer.** The container is physical standardisation that made the later data layer possible. Standardisation precedes digitisation — that is the lesson.
- **Hospital systems' trigger is a statute, not an invention.** The best predictor of a software market is sometimes a law.

### Tier B — approved and merged into H2 (2026-09-18)

Originally deferred pending the H3 pilot; the user elected to build all eighteen at once.

| # | Origin | Wave | Founding event | Why it earns a slot |
|---|---|---|---|---|
| 11 | **Package carriers** | 2 → 8 | package-level tracking; UPS ORION | the tracking number as a product; route optimisation at national scale |
| 12 | **Credit bureaus** | 1 | FCRA 1970; FICO bureau scores 1989 | the first consumer scoring at population scale — parent of all underwriting in the vault |
| 13 | **Online travel agencies** | 5 | GDS disintermediation; Expedia, Priceline | the clearest distribution-layer fight; child of Airlines |
| 14 | **Pharma R&D & CROs** | 4 | EDC replacing paper CRFs; FDA 21 CFR Part 11 | regulated computing where the validation cost exceeds the software cost |
| 15 | **Ad holding companies** | 9 | the 15% commission, and its death | the incumbent programmatic disintermediated; ANA 2016 transparency report |
| 16 | **Electric utilities** | 4 → 8 | SCADA, economic dispatch; AMI rollout | optimisation under physical constraint; the 2003 blackout as a systems-failure case |
| 17 | **Railroads** | 2 → 4 | computerised car scheduling; PSR; PTC mandate | the oldest large-scale scheduling problem still imperfectly solved |
| 18 | **Process manufacturing** | 4 | Honeywell TDC 2000 (1975); model predictive control | where control theory actually shipped; the OT/IT divide |

**Rejected:** universities, defense primes, federal government — hard to source, weak transferable pattern, thin FDE relevance.

## 7. Tiering the 250

Deep history for all 250 is the wrong spend; a first season is ~12 episodes.

| Tier | Count | Treatment |
|---|---|---|
| **1** | ~60 | Full `history/<slug>.md`. Every industry that will carry an episode. |
| **2** | ~90 | Origin event + wave + transferable pattern only. ~400 words. |
| **3** | ~100 | Wave assignment in `series/_eras.md`. Nothing more. |

Tier 1 criterion is **narrative strength, not market size**: a dated origin, a named competitive fight, a mechanism worth explaining, and ideally a corpse.

## 8. Templates

### `series/eras/<wave>.md`

```markdown
# Wave N — <Name> (<span>)

**Trigger:** <specific event + verified date>
**What went to ~zero:** <the one cost>
**Industries created:** <slugs>
**Industries transformed:** <slugs>
**Failure class produced:** missing join | declined join | asymmetric hold

## What Was True The Day Before
## The Trigger
## What Became Possible
## The Competitive Fight
## What It Broke
## Children in This Vault

**Sources:**
```

### `origins/<slug>/` — five files

| File | Contains |
|---|---|
| `profile.md` | What the industry is, who pays, the economics. Mirrors an `industries/` hub. |
| `origin-story.md` | The founding computing event, in narrative depth. |
| `the-fight.md` | The competitive contest the tech was built to win. Winners and casualties, named. |
| `the-mechanism.md` | How the system actually worked — data model, the loop, the algorithm class, the trade-offs taken. |
| `legacy.md` | What it bequeathed. Links **down** to children in `industries/`. |

### `history/<slug>.md` — **revised at H3**

The H3 pilot wrote three files and got **three different section sets**. The template is therefore a **required spine plus a conditional set**, not a fixed list.

```markdown
# History: <Industry Name>

**Industry:** [[industries/<slug>|<Name>]]
**Primary Wave:** <N — Name>
**Secondary Wave:** <N — Name>
**Origin Parent:** <one or more — dental has two, freight has two>
**Episode Tier:** 1 | 2 | 3
**Transferable Pattern:** <one line — the shape an FDE will meet again>

## Before                          REQUIRED — what the work was and what bounded it
## The Origin Event                REQUIRED — a moment, or an explicit "there isn't one"
## What Became Cheap               REQUIRED — the one cost that fell
## How It Was Actually Solved      if there is a mechanism worth explaining
## The Contest                     if there was one — who fought, who won, who died
## The Trade-Off                   if a real trade was made
## The Binding Constraint          if the real limit is a rule, number or policy
## The Graveyard                   if something died — a company OR a thesis
## What's Still Open               REQUIRED — links INTO problems/ and niches/
## The Transferable Pattern        REQUIRED — the FDE payload

**Sources:**                       REQUIRED
```

**Five required sections. The rest are conditional, and the conditionality is the point.**

> **The absence rule.** When a conditional section does not apply, **say so under a heading that names the absence** — "Why There Is No Fight", "The Origin Event — there isn't one" — and explain why. **Never pad an empty section, and never manufacture a fight or a corpse to fill one.** An industry with no competitive contest is a finding about that industry, and frequently the most useful thing in the file.

**Headings may be renamed to name their subject.** "Before" became "Before the Auction" for a Wave 9 child that has no pre-computer era. The heading should describe what actually changed rather than assume a pre-digital past.

**Industry-specific sections are allowed and expected.** Dental needed "The Exclusion That Explains the Rest" (HITECH) and "What Is Actually Happening Now" (the DSO rollup and payer-side AI). Freight needed "What Actually Failed — the distinction that matters," to stop the file claiming more than the evidence supports.

**Length:** the pilot came in at **1,500–1,950 words**. The working assumption of 1,200–2,000 is confirmed. **One file, not a directory** — also confirmed.

### `series/failures/<case>.md` — **revised at H5**

```markdown
# Failure: <Name> (<years>)

**Lesson class:** <one of the eight below>
**Wave:** [[series/eras/wave-NN-name|N — Name]]
**Industries touched:** <2+ links into industries/ or origins/ — a failure that touches one industry belongs in that industry's history file, not here>
**What was claimed:** <one line — the thesis, stated as its believers stated it>
**Capital at risk:** <figure, or omit entirely if not a funded venture>

## Why It Was Plausible          REQUIRED — and the hardest section to write honestly
## What Actually Killed It       REQUIRED — competing accounts left unflattened where they compete
## What It Was Not               REQUIRED — the tidy wrong story, killed
## The Lesson That Transfers     REQUIRED — must generalise beyond the industry it happened in

**Sources:**                     REQUIRED
```

**Why "Why It Was Plausible" comes first.** Hindsight makes every failure look stupid, and a file that treats it as stupid teaches nothing — a fresh graduate learns only that other people are fools. The useful version reconstructs why intelligent, well-informed people with money believed this. If you cannot make the case sound reasonable, you have not understood it yet.

**Why "What It Was Not" is required.** Every famous failure has a tidy explanation attached that does not survive checking — *"yield management killed People Express," "digital freight brokerage failed," "Vine died to the algorithm."* Killing that story is frequently the most valuable output in the file.

**Cross-cutting is the entry requirement.** A failure file must touch **two or more** industries. One corpse should teach several industries at once; if it only teaches one, it belongs in that industry's `history/<slug>.md` instead.

**The eight lesson classes** (see `series/_state/failures.txt`):
`capital-cannot-buy-it` · `the-measurement-was-wrong` · `concentration-became-systemic` · `thesis-died-company-lived` · `the-regulator-arrived` · `the-platform-changed-the-rules` · `software-failure-physical-harm` · `the-whole-market-repriced`

## 9. Session protocol

1. Read this file in full. Read `series/_bookmark.md` for position.
2. Take the next uncompleted stage from the CURSOR. **Do not skip ahead.**
3. Research before writing. Every factual claim sourced.
4. Write files. Match the templates exactly.
5. Run the verification block (§10).
6. Update `series/_bookmark.md` — files written, flagged items, myths killed.
7. Update the CURSOR in this file.

### Operational rules learned in H4 (2026-09-19)

**1. Agents must not sub-delegate file writes.** Two H4 batches spawned their own research forks; in at least two cases a fork wrote the batch's files despite research-only instructions, and forks then raced each other on the same paths. Sub-agents may research. **Only the agent holding the assignment writes the file.**

**2. Agent reports are NOT evidence of file state.** A batch-G agent reported writing a Graveyard section citing a specific recent acquisition with a dollar figure and a date. **A content-level check found none of it on disk** — its own fork had overwritten the file with a different, more conservative version. Always verify from disk with `grep`/`wc`, never from the hand-back report. The surviving file was the better one, which is luck, not process.

**3. The "concurrent overwrite" reports are real, not misreads.** Two agents reported overwrites on slug-disjoint assignments. The content check above confirms files genuinely changed after being written. Cause is nested delegation (rule 1), not cross-batch collision — the batch assignments themselves never overlapped.

**4. Citation provenance must be explicit.** A Phase 3 file citing another Phase 3 file **must say so** and must not present it as independent corroboration. See the integrity flag in `series/_bookmark.md` — a single unverified trade-press claim reached four files by being cited from the vault's own earlier files.

**5. The word ceiling is soft.** Files ran 1,200–2,387. Do not cut sourced, load-bearing material to hit 2,000. Do not pad to reach 1,200.

**6. Research budget is shared and finite.** WebSearch hit its session-wide cap early in H4; later batches fell back to WebFetch against known URLs. Coverage is consequently thinner in later files, and they say so in-file. **A top-up research pass is required before any file becomes a script.**

**Parallelisation:** per-slug work in H4 is parallel-safe. **H1, H2, and any stage writing `series/_eras.md`, `series/_bookmark.md`, `origins/_index.md` or this file is NOT** — those are shared files and must be written by a single thread at close-out. Same rule as Phase 2 Stage B.

## 10. Verification

```bash
# Phase 3 canonical files exist
ls series/_eras.md series/_plan.md series/_bookmark.md

# every history file carries its required metadata
for f in history/*.md; do
  for k in 'Primary Wave' 'Origin Parent' 'Episode Tier' 'Transferable Pattern'; do
    grep -q "^\*\*$k:\*\*" "$f" || echo "MISSING $k -> $f"
  done
done

# every Phase 3 file cites sources
grep -L '^\*\*Sources:\*\*' history/*.md series/eras/*.md series/failures/*.md 2>/dev/null

# every Tier 1 history file links back into the existing vault
grep -l 'Episode Tier:\*\* 1' history/*.md 2>/dev/null | while read f; do
  grep -qE '\[\[(problems|niches)/' "$f" || echo "NO VAULT LINK -> $f"
done

# origins complete at 5 files each
for d in origins/*/; do
  [ "$(ls "$d" | wc -l)" -eq 5 ] || echo "INCOMPLETE -> $d"
done

# tags still canonical across Phase 3 only
grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' series origins history --include='*.md' 2>/dev/null \
  | tr -d ' ' | sort -u | comm -23 - <(sort -u _state/safe-tags.txt)

# PROTECTED CONTENT LAYERS UNTOUCHED — must print 13335
find industries problems niches metadata plans -name '*.md' | wc -l

# WHOLE PROTECTED SURFACE — must print 13346
find . -name '*.md' -not -path './.obsidian/*' -not -path './series/*' \
  -not -path './origins/*' -not -path './history/*' | wc -l
```

## 11. Pilot questions — answered at H3

1. **One file or a directory?** → **One file.** 1,500–1,950 words held comfortably.
2. **Does `## The Graveyard` belong per-industry?** → **Yes, when there is one, and it may be a *thesis* rather than a company.** Programmatic's corpse is the assumption that identity would stay stable and cheap; freight's is Convoy; dental has none and says so.
3. **How long?** → **1,200–2,000 confirmed.**
4. **Do episodes map 1:1 to industries?** → **Not settled, and now leaning no.** Dental's episode is really *the annual maximum*; freight's is *what capital cannot buy*. Both would work better grouped by failure shape than by industry. Defer to H6.
5. **Do all twelve waves survive?** → **Yes, but wave assignment is not always the origin.** Freight's creating events (a corkboard in 1978, a statute in 1980) sit outside its assigned Wave 4. Where this happens, say so in the file rather than forcing the assignment.

### New questions raised by H3, for H4

6. How many Tier 1 industries have **no contest and no graveyard**? Dental suggests this is the common case, not the exception. If it exceeds half, the series' framing has to change.
7. Does **"The Binding Constraint"** recur? Dental's annual maximum is a rule nobody has revisited. If that pattern is widespread it may deserve promotion to a required section.
8. Should the **chronology of failure** be softened? Supermarkets show a **declined join in 1985** (promotional-lift accounting), two decades before the platform era the spine assigns it to.

---

**Trackers:** `series/_bookmark.md` (build log) · CURSOR above (stage position)
**Protected:** `industries/ problems/ niches/ metadata/ plans/ _*.md` — 13,346 files
**Created:** 2026-09-18 · **Spine verified:** 2026-09-18
