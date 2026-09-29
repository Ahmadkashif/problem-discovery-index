# Phase 3 Bookmark — The History Layer

Build log for Phase 3. Paired with `series/_plan.md` (the spec and the CURSOR).

**Last updated:** 2026-09-18

---

## Status

| Stage | Work | Status |
|---|---|---|
| **H0** | Plan + spine research | ✅ complete |
| **H1** | Era spine — `series/_eras.md` + `series/eras/<wave>.md` ×12 + wave assignment ×250 | ✅ complete |
| **H2** | `origins/` — **18** parents, 5 files each | ✅ complete |
| **H3** | Pilot — 3 `history/<slug>.md`, template rebuilt | ✅ complete |
| **H4** | History sweep — Tier 1 (66) | ✅ complete |
| **H5** | Graveyard — `series/failures/` (40 cases) | ✅ complete |
| **H6** | Episode assembly | ⬜ not started |

---

## H0 — Plan and spine research ✅

**Completed 2026-09-18.**

Files written: `series/_plan.md`, `series/_bookmark.md`. Scaffold created: `series/eras/`, `series/failures/`, `origins/`, `history/`.

**Gap audit across 13,320 content files.** The vault documents the present incumbent exhaustively (spreadsheet 1,405 files · Excel 480 · QuickBooks 192 · Epic 92) and the arrival of any technology essentially never ("first built" 0 · "went bankrupt" 0 · containerization 0 · Toyota Production System 0 · HITECH 0 · SABRE 1 · "in the 1990s" 2). Only **15 of 250** industry hubs contain any year.

**Twelve-wave spine researched and verified** across three independent research threads. All dates in `series/_plan.md` §3 and §6 are source-backed. Detail expands into `series/eras/<wave>.md` at H1.

**13 myths killed.** Recorded in `series/_plan.md` §5 — do not reintroduce. The most consequential correction was to this project's own working assumption:

> **T+2 does not explain the payment-processor batch lag.** T+2 is *securities* settlement (US equities moved to T+1 in May 2024). Card/ACH batch cycles are a separate mechanism — overnight windows inherited from paper check clearing. The underlying insight survives; the label was wrong. Additionally, the "why batch was chosen" rationale is a well-supported *inference*, not a documented decision, and must be presented as such.

Also corrected: RTB origin (2005, not 2009) · NASDAQ 1971 was a quotation system, not an exchange · "yield management killed People Express" is monocausal and unsupported · HITECH has no single authoritative dollar figure · SABRE 1960 vs 1964 · telecom churn ML dates to 1999/2000 not early-1990s AT&T · MRP and Toyota JIT are opposed lineages, not one · containerization's trade effect was delayed, not instant · ISO publishes advisory loss costs, not rates · insurers were 1950s computing pioneers · Salesforce did not coin "SaaS" · semiconductor yield analytics has no founding case.

---

## H1 — Era spine ✅

**Completed 2026-09-18.** 14 files, ~16,800 words.

`series/_eras.md` (the canonical spine + full assignment) and twelve `series/eras/wave-NN-*.md` files. Four research threads verified the trigger dates, competitive mechanics and breakage for every wave; all twelve files cite sources.

**All 250 industries assigned** a primary and secondary wave — 250 rows, zero strays, zero unassigned, verified against `ls industries/`.

| Wave | Primary | | Wave | Primary |
|---|---|---|---|---|
| 1 Mainframe & batch | 10 | | 7 Big data | 14 |
| 2 Departmental & item-level | 16 | | 8 Mobile & GPS | 16 |
| 3 PC & the spreadsheet | 16 | | 9 Programmatic | 6 |
| 4 Client–server & ERP | 18 | | 10 The creator platform | 14 |
| 5 The commercial web | 45 | | 11 The COVID dislocation | 4 |
| 6 Cloud & SaaS | **83** | | 12 Transformers | 8 |

**Three findings worth carrying into H2 and H3:**

1. **Wave 6 owns a third of the vault (83/250).** Cloud was a *pricing* change — capex to opex — and that change alone made a 12-person business an addressable software customer. Nearly all Vertical SaaS descends from it.
2. **Wave 3 created nothing and is everywhere.** 16 industries whose core artefact is a spreadsheet model; the word appears in 1,405 files. This is the incumbent an FDE actually competes with, and the vault has never asked why it never loses.
3. **Wave 9 is the only wave with a death date** — ATT, April 26 2021. Cleanest three-act structure available for a pilot episode.

**12 further myths killed** (running total 25), logged in `series/_plan.md` §5. The most consequential overturned this project's own thesis:

> **"COVID permanently moved the telehealth regulatory boundary" is largely false.** HIPAA enforcement discretion expired Aug 9 2023; interstate licensure waivers mostly expired; Medicare parity survives only on annual congressional patches, currently through Dec 31 2027. Utilisation settled at 13–17% of visits, ~55% below peak. The clean permanent shift is **remote work** (~5.7% of workers in 2019 → a stable 20–25% of paid workdays), not telehealth. `series/eras/wave-11-covid-dislocation.md` is written to the corrected account.

**Verification at H1 close-out:** all 12 era files carry the five required sections and a `**Sources:**` line · every `[[industries/…]]` and `[[series/eras/…]]` wikilink resolves · 250/250 assignment rows · content layers 13,335 and protected surface 13,346, both unchanged · 1:1:1 parity clean · zero non-canonical tags.

---

## H2 — Origins ✅

**Completed 2026-09-18.** 91 files, ~55,000 words. **All 18 origins** (Tier A + Tier B merged at user instruction), 5 files each, plus `origins/_index.md`.

Written: airlines, supermarket-chains, retail-banking (by the lead thread, as the reference implementation) · hospital-systems, insurance-carriers, exchanges-market-makers, telecom-carriers, ocean-shipping-ports, semiconductor-fabs, auto-oems, package-carriers, credit-bureaus, online-travel-agencies, pharma-rd-cros, ad-holding-companies, electric-utilities, railroads, process-manufacturing (five parallel threads, per-slug disjoint — parallel-safe under §9).

**29 further myths killed** (running total **54**), logged in `series/_plan.md` §5. Three of consequence:

> **This project introduced an error and the delegation caught it.** The H2 brief stated that Orlicky formulated MRP "studying the Toyota Production System." That is chronologically impossible — TPS was undocumented outside Toyota until Ohno's 1978 book, 14 years after Orlicky's 1964 work. Flagged in-file rather than propagated.

> **"Reg NMS caused HFT" is an overstatement.** Rule 611 bars trading through a better displayed price; it does **not** mandate routing to the best venue. The incentive it created was to *see and react* fast — which is not the same claim.

> **The 2003 Northeast blackout was not a capacity failure.** A race-condition bug in GE's XA/21 EMS silently disabled FirstEnergy's alarms. Operators did not redistribute load because they did not know they needed to. The failure was that nobody knew.

**Six of eighteen origins had no competitive duel and the files say so** rather than manufacturing one — telecom carriers (regulatory: the 1984 AT&T divestiture), pharma CROs (gradual multi-company formation), semiconductor fabs (the March 1980 "Anderson Bombshell" and SEMATECH Aug 1987 stood in), electric utilities (the 2003 blackout as a systems-failure case), railroads (an internal operating-model argument, PSR), and process manufacturing (an adversarial attack, Stuxnet).

**This is the stage's most consequential finding for the series.** A third of the parent industries have no People Express, so the episode format cannot assume a duel. `the-fight` means *the contest the technology was built to win* — against a rival, a regulator, a physical limit, an adversary, or the industry's own assumptions. Recorded in `series/_plan.md` §6 as a constraint on H3.

**Two inheritance links flagged as weak** rather than stretched: electric-utilities → agtech-platforms, process-manufacturing → metal-fabrication. Adjacency, not transplant. H4 should expect more.

**Index reconciled.** `origins/_index.md` contested-decision one-liners were rewritten to match the fuller framings in each `profile.md`, after a subagent flagged the divergence.

**Verification at H2 close-out** (`series/_state/verify-phase3.sh`): `PHASE3-VERIFY-CLEAN`. 18 origins at exactly 5 files · every file cites sources · all wikilinks resolve · tags canonical · content layers 13,335 and protected surface 13,346, both unchanged · 1:1:1 parity clean.

---

## H3 — Pilot ✅

**Completed 2026-09-19.** 3 files, 5,171 words. Written by the lead thread — this was design work, not production.

Pilots chosen to stress different cases: **programmatic-ad-platforms** (a wave with a death date), **freight-brokerage** (a real corpse), **dental-practices** (neither — the control case).

### The template broke, as intended

Three files produced **three different section sets**. Only five sections appeared in all three. `series/_plan.md` §8 now specifies a **required spine of five plus a conditional set**, governed by an **absence rule**: when a conditional section does not apply, say so under a heading that names the absence and explain why — never pad, never manufacture a fight or a corpse.

| Break | Fix |
|---|---|
| "Before the Computer" fails for a Wave 9 child born inside computing | Heading renamed to name its subject — "Before the Auction" |
| "The Origin Event" assumes a moment; dental has none | Explicit "there isn't one" is a valid and valuable answer |
| "The Fight" does not exist in dental | Made conditional; absence stated and explained |
| "The Graveyard" — programmatic's corpse is a *thesis*, not a company | Graveyard may hold a thesis |
| Origin Parent assumed singular | Freight has two, dental has two |
| Wave assignment ≠ origin for freight (1978 corkboard, 1980 statute, assigned W4) | Say so in-file rather than forcing it |
| No home for dental's real story | New conditional section: **The Binding Constraint** |

**Answered:** one file not a directory · 1,200–2,000 words confirmed (came in 1,500–1,950) · graveyard belongs per-industry when it exists.

### The finding that matters

**Dental has no competitive fight and no corpse, and that is the common case, not the exception.**

Its binding constraint is **a number nobody has revisited**: the dental insurance annual maximum, $1,000–$1,500, set somewhere between the 1950s and 1970s and still the modal figure — ~32.8% of in-network PPO plans sat in that band in 2025/2026. **$1,500 in the early 1970s is roughly $9,000–$10,000 today.**

Every pain the vault records for this industry descends from it: the 10–15 minutes per patient verifying benefits, the ~50% treatment-plan acceptance, the financial-presentation problem. **No software moves it.** Dentistry was also substantially **excluded from HITECH** — only the Medicaid track, largely paediatric — which is why its clinical record layer is underdeveloped where hospitals' is not.

This confirms at child level what H2 found at parent level (6 of 18 origins had no duel). **The series cannot be built on rival-versus-rival narratives.** Most businesses are not fighting a competitor with an algorithm; they are coping with a rule.

### Six more myths killed (running total 62)

> **"Digital freight brokerage failed" is wrong.** Only Convoy fully shut down. Transfix sold its brokerage to NFI and pivoted to software; Loadsmart retreated to dock scheduling; Next Trucking was a distress sale; Uber Freight still operates. Incumbents are shipping the automation the startups promised — C.H. Robinson reports LLM auto-quoting at a 2min 13sec average response (company-reported, unaudited). The defensible claim is narrow: **venture-scale, growth-at-all-costs, digital-only brokerage failed as a standalone business in this cycle.**

Also: "RTB was invented in 2009" (it was April 2005 — 2009 is Google's scaling) · Convoy's funding total is genuinely disputed ($837M–$920M equity, plus $100M debt; do not quote one figure) · Flexport's $16M purchase price is reported but never confirmed by either party · "Sirona invented CEREC" (Mörmann and Brandestini at Zurich, Sept 1985; Sirona did not exist until 1997) · Open Dental's "open source" framing is source-available, not OSI-approved.

### The ending that could not have been invented

Convoy peaked at a **$3.8B valuation in April 2022**, shut down **October 19 2023**, and its technology stack sold to Flexport for a reported **$16M** — then to **DAT Freight & Analytics for ~$250M in July 2025**.

DAT began as **handwritten cards on a corkboard at the Jubitz Truck Stop, Portland, on April 3 1978**. The load board that digital freight brokerage existed to make obsolete now owns its technology.

### Flagged for follow-up

- **Payer-side dental AI could not be verified** — the claim that Overjet and peers are being adopted faster by insurers for claims review than by dentists for care is the most interesting thread in the dental file and is marked unverified in-file. **Research before it reaches a script.**
- Freight EDI mandate adoption curve and MercuryGate's founding date: unverified, flagged in-file.
- DSO penetration has **two incompatible figures** in circulation (8.8%→16.1% vs 16%→30%+). Unresolved.

**Verification at H3 close-out:** `PHASE3-VERIFY-CLEAN`. All three carry the four required metadata fields, all cite sources, all Tier 1 files link into `problems/` or `niches/`, all wikilinks resolve, tags canonical, protected layers unchanged.

---

## H4 — History sweep ✅

**Completed 2026-09-19.** 66 files, **102,468 words**. Tier 1 defined in `series/_state/tier1.txt` (grew from 64 to 66 during the run). Three written by the lead thread at H3; 63 across thirteen parallel batches, slug-disjoint.

### The statistics settle the series' central question

| Section | Files | Share |
|---|---|---|
| **`## The Binding Constraint`** | **40 / 66** | **61%** |
| `## The Contest` | 29 / 66 | 44% |
| `## The Graveyard` | 27 / 66 | 41% |
| Explicitly **names an absence** | 35 / 66 | 53% |
| **No origin parent** | 16 / 66 | 24% |

**The binding constraint is more common than the competitive fight — 61% against 44%.** The section was invented at H3 as a one-off fix for dentistry. It turned out to be the dominant shape of the corpus.

**56% of Tier 1 industries have no competitive contest. 59% have no corpse.** The rival-versus-rival episode is the exception, not the template. This answers H3's open question 6 (*"if it exceeds half, the framing has to change"*) — it exceeds half. **The series cannot be built on duels.**

The FDE skill this teaches is therefore not "spot the algorithm." It is **tell a rule apart from a rival before you build**, because the software each implies is completely different.

### Binding constraints found

Durbin/Reg II (payment processors) · field-of-membership rules from the 1934 Act (credit unions) · DRG-fixed reimbursement (medical billing) · ERISA §514 + 50 state regimes (insurance TPA) · OTA commission set two layers up (boutique hotels) · floor-plan financing (independent auto dealers — **not** franchise law, a correction to the brief) · PBM/DIR fees, partly fixed by CMS effective 1 Jan 2024 (independent pharmacy) · UPC "Number System 2" variable-weight carve-out (specialty food retail) · AICPA peer review (SMB accounting) · GSE appraisal-waiver threshold (appraisers) · the billable hour (small law) · ACE's release schedule (customs brokers) · SAFE Act/Dodd-Frank/TRID (mortgage brokers) · **Xactimate, owned by Verisk** (insurance restoration) · ONC certification (healthcare practice software) · card-network chargeback rules (payment fraud) · Prop 22 "engaged time" (gig delivery) · the ELD mandate (owner-operator trucking) · inbox deliverability (newsletter media) · reimbursement on annual congressional patches (telehealth).

### Structural findings worth carrying to H5 and H6

1. **Verisk owns both sides of the restoration negotiation.** Xactware (acquired by ISO Aug 2006; Verisk formed 2008) owns Xactimate, the price list contractors must quote against — and ISO has pooled insurer loss-cost data since 1971. The party advising insurers what claims should cost owns the price list for fixing them.
2. **Amazon broke Turkopticon.** Mechanical Turk workers built their own reputation tooling (Irani & Silberman, 2008) as browser extensions; Amazon broke them. This removes the engineering excuse from the asymmetric hold entirely.
3. **The ELD mandate removed a workaround, it did not fix the economics.** ~80% of drivers are unpaid for dock detention and logged it off-duty to protect HOS hours. Electronic logging ended that. Unpaid detention was untouched.
4. **Classification: a natural experiment.** Gig platforms bought a carve-out by ballot (Prop 22, $205M+, upheld unanimously 25 Jul 2024). Truckers went to court and lost (CTA, Ninth Circuit 2021, cert denied 2022). Same question, two routes, opposite outcomes.
5. **Owning the list is not owning delivery.** Newsletters escaped algorithmic platforms into Apple Mail Privacy Protection (Sept 2021) and Gmail/Yahoo bulk-sender rules (Feb 2024).
6. **Podcasting's failure is a *missing* join, not a declined one** — download ≠ listen, and nobody is withholding it. Correct class discrimination, preserved.
7. **The tooling preceded the demand event.** LangChain (Oct 2022) and LlamaIndex (Nov 2022) both predate ChatGPT's 30 Nov 2022 launch by ~6 weeks.

### Late findings from the final two batches

8. **"Telehealth was technologically immature before COVID" is false.** Teladoc had 15M members and ~75% US market share by **Nov 2016**, four years before the pandemic. The unlock was legal, not technical — which sharpens Wave 11's whole argument.
9. **Telehealth has a real corpse, and it is caused by the wave's own mechanism.** Done Global (founded 2019): its CEO and Clinical President were **convicted 18 Nov 2025** of illegally distributing 40M+ Adderall pills, $100M+ revenue, by exploiting the DEA's suspended in-person-exam requirement. Distinct from, and more concrete than, Cerebral's $3.65M Nov 2024 settlement.
10. **Two dislocations, two waves, one industry — do not conflate them.** Online tutoring was hit by COVID (2020) and then, unrelatedly, by generative AI (2023). Chegg fell 38% in a day in May 2023, posted an $873M net loss in 2024, and cut ~67% of staff by Oct 2025. Meanwhile Preply (founded 2012, nothing to do with COVID) reached a $1.2B valuation in Jan 2026. **Human-relationship tutoring survived what killed answer-lookup tutoring.** New transferable pattern.
11. **A live, unresolved contest.** Rippling sued Deel March 2025; Deel countersued June 2025 alleging a planted spy; DOJ opened a criminal investigation into Deel in **Jan 2026**. Ongoing — flagged as unresolved, not narrated as settled.
12. **"Thesis died, company survived" is its own graveyard class.** Klarna $46B (June 2021) → $6.7B (July 2022), −85%. Grubhub: bought for $7.3B (2021), sold to Wonder for $650M (Jan 2025) — a **>$6.5B loss** on a still-operating business. Neither is a bankruptcy.
13. **The billable hour has quantified evidence.** ABA Journal: expected annual hours rose from 1,750–1,800 in 1986 to 2,000–2,200 by 2007. Efficiency is a revenue loss under hourly billing, and the number moved the wrong way.
14. **NAEP caveat, added honestly.** NAEP's own reporting frames 2015–2025 as a longer decline "not only during the pandemic" — used to avoid over-attributing the score drop to school closures.

### Verification at H4 close-out

`PHASE3-VERIFY-CLEAN`. All 66 carry required metadata · 66/66 cite sources · 66/66 link into `problems/` or `niches/` · all wikilinks resolve · tags canonical · protected layers 13,335 / 13,346 unchanged · 1:1:1 parity clean.

---

## H5 — The graveyard ✅

**Completed 2026-09-19.** 40 files, **47,384 words**, in `series/failures/`. Case list and lesson classes in `series/_state/failures.txt`. Seven parallel batches, grouped **by lesson class, not by industry** — a corpse that teaches only one industry belongs in that industry's history file.

**Template revised before starting** (`series/_plan.md` §8). Two additions, both earned at H3/H4:
- **`## Why It Was Plausible` is first and required.** Hindsight makes every failure look stupid, and a file that treats it as stupid teaches a graduate only that other people are fools. If you cannot make the thesis sound reasonable, you have not understood it.
- **`## What It Was Not` is required.** Every famous failure carries a tidy explanation that does not survive checking. Killing it is usually the file's most valuable output.
- **Cross-cutting is the entry requirement** — 2+ industries per file. All 40 pass.

### ⚠️ The taxonomy was wrong, and the files said so

I named a lesson class **`the-regulator-arrived`**. In two of its six cases **no regulator arrived at all**, and the agent refused to paper over it:

- **ANA rebate report (2016):** no evidence any regulator — FTC, SEC, state AG — ever acted. A **trade association performed a regulator's investigative function in a jurisdictional vacuum.**
- **NASDAQ odd-eighths (1994):** **one public academic finding did the whole job overnight** — spreads halved the day after the newspapers ran it, before DOJ or the SEC did anything.

And in a third, the regulator was on the **wrong side**: **BaFin banned short-selling of Wirecard (Feb–Apr 2019) and made criminal referrals against the FT journalist Dan McCrum and short-sellers** — i.e. it acted to suppress the people who were right.

**The class should be `the-reckoning-arrived`**, with the *source* of the reckoning as the variable: a regulator, a journalist (Small Smiles was triggered by Roberta Baskin's 2007–08 WJLA hidden-camera exposé, not an agency), an academic, an auditor, or a commercial counterparty. On **Done Global**, pharmacies (CVS/Walmart, early 2022) and ad platforms (Google/TikTok, mid-2024) acted **before DOJ's case reached a jury**. Commercial counterparties are frequently faster than regulators, and that is a better lesson than the one I set out to teach.

**Recorded, not renamed** — the class label stays for continuity; H6 should use the corrected framing.

### Findings worth carrying to H6

1. **Turkopticon is the best file in Phase 3**, and because of what it refuses to claim. It separates the documented (Amazon's site changes broke worker-built reputation extensions; Dynamo enrolment closed) from the unevidenced (any stated intent), then makes the structural argument that needs no intent: Amazon holds every requester's full rejection history and could have built this since 2005. Its diagnostic generalises — **"has a third party already built a substitute out of scraps, and did the platform help it, ignore it, or actively degrade it?"** Ignoring is a backlog item; degrading is evidence the withholding is maintained.
2. **The DOJ was worried about the wrong risk.** It sued to block UnitedHealth/Change Healthcare in Feb 2022 on *data-competition* grounds. The concentration then failed as **ransomware through a Citrix portal with no MFA**. Same concentration, different failure mode, and the antitrust theory pointed elsewhere.
3. **"Thesis died, company lived" has two distinct flavours.** Klarna ($46B → $6.7B) and Grubhub ($7.3B → $650M) destroyed value. **CrowdFlower was a positive-return exit** — $58M raised, sold to Appen for $300M — and the *thesis* still lost to narrower competitors. The profitable failure is harder to see and more common.
4. **Cloudera was relegated, not destroyed** — taken private by KKR/CD&R in Oct 2021 for ~$5.3B, *larger* than the entire 2019 merger valuation, while Snowflake's Sept 2020 IPO took the category's upside.
5. **Kaseya was not "1,500 businesses hacked"** — ~60 MSPs were compromised directly; the 800–1,500 downstream cascaded through trusted RMM access and were never individually breached.
6. **CrowdStrike was not an ordinary bug.** The failure sat in the rapid-content-delivery path **deliberately exempted from staged rollout** — the thing built for speed had no brake.
7. **NEW MYTH, via NTSB Chair Homendy's June 2024 testimony:** East Palestine's **vent-and-burn was not chemically necessary.** NTSB found polymerisation was not occurring and the cars could have cooled safely.
8. **The spine has no aerospace era.** Boeing MCAS has no fitting wave, and its industry linkage is flagged in-file as *thematic adjacency, not lineage*. Stuxnet and East Palestine also sit outside their origins' assigned waves. **The spine describes industry formation, not the date of every event inside an industry** — state this in H6 rather than forcing assignments.

### Corrections to this vault's own files, found by the H5 batches

9. **`bn.com` launched May 1997, not "1999–2000."** `series/eras/wave-05-commercial-web.md` — a file written by the lead thread — had this wrong. Barnes & Noble was ~2 years behind Amazon, not 4–5. **Corrected.**
10. **And the B&N lesson does not survive a second case.** **Borders outsourced its entire e-commerce operation to Amazon from 2001 to 2007** — the opposite choice — and **went bankrupt in Feb 2011 anyway.** Owning the online channel was not the determining variable. Added to the era file; "they were slow to go online" is an inadequate explanation of what happened to bookselling.
11. **People Express's $301M reconciles.** Texas Air's figure decomposes into ~**$125M for People Express itself** plus **$176M for Frontier assets sold separately** — resolving what looked like conflicting numbers across sources.
12. **Convoy's technology was never the failure.** Flexport paid a reported $16M for the stack and DAT paid ~$250M for it 18 months later. **The matching technology worked; the venture-scale financing model did not.** That is a sharper statement of the lesson than the vault previously carried.
13. **Yellow Corporation's Aug 6 2023 bankruptcy** (30,000 jobs, a $700M CARES loan, a Teamsters dispute) is a **multi-year structural failure**, explicitly separated from the cyclical 2022–24 freight repricing — and separated again from Convoy's venture-capital failure. Three different deaths in one industry, three different causes.
14. **SEO tooling is a downstream *consequence* of the dot-com crash, not a casualty of it** — the term was coined in 1997, PageRank arrived in 1998, and the tooling industry professionalised roughly a decade behind.

### Verification at H5 close-out

`PHASE3-VERIFY-CLEAN`. All 40 carry the four required sections · 40/40 cite sources · 40/40 link 2+ industries · all wikilinks resolve · tags canonical · protected layers 13,335 / 13,346 unchanged.

**Verifier bug fixed during close-out:** the era-link check matched `[[series/eras/wave-NN-name|…]]` — the *template placeholder in `series/_plan.md` §8* — and reported it as a broken link across ~140 files. The check now requires a real `wave-NN-` slug. The verifier was flagging its own specification.

---

## Flagged — errors found in protected files

Phase 3 is additive. Errors found in `industries/`, `problems/`, `niches/`, `metadata/` or `plans/` are recorded here and **not fixed**.

### Tag audit of protected layers (H4, 2026-09-19)

Surfaced by a subagent, then audited properly. **33 non-canonical tag types are in use across `problems/`, `niches/` and `industries/`.** Breakdown:

| Category | Count | Status |
|---|---|---|
| **Deprecated tags still in use** (`#cnn`, `#llm`, `#nlp`, `#lstm`, `#random-forest`, …) | **31** | **Known, previously flagged, unapproved for fixing.** These are listed in `metadata/tags.md`'s own "Deprecated (do not use)" section. |
| `#iot` | 1 occurrence, 1 file | **Genuinely unknown** — not canonical, not deprecated. The only real new finding. |
| `#foodtruckfriday` | 1 occurrence, 1 file | **False positive.** It is an Instagram hashtag quoted inside prose in `problems/food-trucks/ai-agents-platforms.md`, describing social-media inputs — not a vault tag. |

**Method note for whoever audits next.** Compare against **`_state/safe-tags.txt` (138)**, not `metadata/tags.md` (190). The latter includes the deprecated section, so auditing against it silently passes every deprecated tag. This caught out the first pass of this very audit.

**Not fixed, per the additive rule.** Phase 3's own layers (`series/`, `origins/`, `history/`) are clean against `safe-tags.txt`.

---

## ⚠️ Flagged — unverified claims propagating inside Phase 3

**Found during H4, 2026-09-19. This is the failure mode the research discipline exists to prevent, and it happened anyway.**

### 1. The Greg Stuart "big mistake" quote — 4 files

Attributed to a former IAB president, used as the human authority for the series' **central thesis** that last-click attribution was nobody's decision.

**Its entire provenance is one trade-press page (mi-3.com.au) surfaced in a single H0 research pass. That URL now returns 403.** The H4 agent writing `marketing-attribution-vendors.md` tried to re-verify it and could not.

Appears in: `history/programmatic-ad-platforms.md` · `history/marketing-attribution-vendors.md` · `series/eras/wave-05-commercial-web.md` · `series/_plan.md` §5.

### 2. The IAB codification dates (impressions 2004, clicks 2009) — 7 files

Same provenance. Appears additionally in `origins/ad-holding-companies/profile.md`, `origins/ad-holding-companies/origin-story.md`, and (incidentally) two `origins/semiconductor-fabs/` files.

### Why this matters more than the individual facts

**Each new file cited the vault's own earlier files rather than the original source.** A single unverified trade-press claim acquired the appearance of corroboration by being repeated inside the corpus that first recorded it. That is laundering, and no individual agent did anything wrong — each one cited what the vault said.

**The mechanism failed, not the people.** Nothing in the template or §5 required a writer to distinguish *"verified from a primary source"* from *"carried from another Phase 3 file."*

### ✅ RESOLVED AT H5 — searched, not corroborated, removed

An H5 verification pass attempted verification and **documented the full trail**: mi-3.com.au returns **403**; there is **no Wikipedia article** for Greg Stuart; Wikipedia's *Interactive Advertising Bureau* article **does not mention** the quote or the 2004/2009 dates; **iab.com**'s insights listing and **IAB Europe**'s site search returned **no match**.

**Status is now "searched and not corroborated," which is stronger than "unverified."**

- `series/failures/last-click-attribution.md` is written **entirely without** the quote or the dates, carries an explicit `**Provenance status:**` line, and builds the argument on the independently-documented mechanism instead (DoubleClick Feb 1996; a cookie could only capture last-touch; **Amazon Associates hit the identical constraint independently in July 1996**).
- It also pre-empts a softened re-import: even if the 2004/2009 dates are later confirmed, they would describe the IAB **documenting pre-existing agency practice, not originating it.**
- The other four files (`history/programmatic-ad-platforms.md`, `history/marketing-attribution-vendors.md`, `series/eras/wave-05-commercial-web.md`, `series/_plan.md` §5) now carry an inline warning with the search trail. **Nothing was deleted from them** — unverified is not wrong — but nothing may go to script.

### Also corrected at H5

**Reinhart-Rogoff was three errors, not one.** A coding error, selective country exclusion, and an unconventional weighting scheme — and **the spreadsheet error was not necessarily the largest contributor.** The single-formula telling is a simplification this vault itself repeated in `series/eras/wave-03-pc-spreadsheet.md`; now corrected there.

**Facebook's "pivot to video" is two distinct failures, routinely conflated:** the 2015–16 metric overstatement, and the unrelated **2018 "Meaningful Social Interactions" reach cut**. Unsealed filings allege Facebook knew from 2015 and include an internal line about obfuscating "the fact that we screwed up the math"; plaintiffs allege 150–900% overstatement against Facebook's disclosed 60–80%. **Left unflattened as competing accounts.**

**Public Health England:** the **15,841 dropped cases** is solid (a direct count). The University of Warwick estimate of ~125,000 additional infections and ~1,500 deaths is **PHE-disputed modelling, not fact** — flagged as such.

### Original required actions (now addressed)

1. **Verify the Stuart quote against a primary source** — an interview, a recorded talk, an IAB publication. If it cannot be verified, **remove it from all four files** and rewrite the argument without it. *The underlying claim survives without the quote*: last-click's origin in DoubleClick's 1996 cookie tooling is independently documented and does not depend on anyone calling it a mistake.
2. **Verify the IAB guideline dates** against IAB's own publication record.
3. **Add to §5 a citation-provenance rule** — a Phase 3 file citing another Phase 3 file must say so explicitly and must not present it as independent corroboration.

**Do not delete anything yet.** The claims are plausible and may well be correct. They are *unverified*, which is a different status from *wrong*, and the files should say which.

---

## Myths killed

Running log across all stages. Full detail in `series/_plan.md` §5.

| Stage | Count | Cumulative |
|---|---|---|
| H0 | 13 | 13 |
| H1 | 12 | 25 |
| H2 | 31 | 56 |
| H3 | 6 | 62 |
| H4 | 14 | 76 |
| H5 | 14 | **90** |

---

## Invariants held

- Protected content layers untouched: **13,335 files** (`industries/ problems/ niches/ metadata/ plans/`)
- Whole protected surface: **13,346 files** (adds 7 root trackers, `CLAUDE.md`, 3 `_state/*.md`)
- 1:1:1 parity `industries↔problems↔niches` verified clean after Phase 3 scaffold
- Pass 1's 944 niches, the 250 industry hubs and all of `problems/` unedited
- Tag registry unchanged — 190 canonical tags
- No new tags introduced
