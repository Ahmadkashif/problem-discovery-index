# The Lineage Sweep — Build Log

Append-only build log. Paired with `_lineage.md` (the spec and the CURSOR) and `_builder-index.md` (the rollup).

**Framework:** one tool-first note per industry — which specific artefact exists because of this industry's problem, who built it, and why them.
**Per industry:** 1 file, 450–750 body words (excluding Sources), five required headings, no tags.
**Order:** by wave (W1→W12), alphabetical within wave. **Batch:** 5 industries. **Never parallel.**
**Per-batch check:** `bash _state/verify-lineage.sh` · **Per-stage check:** `bash series/_state/verify-phase3.sh`

**Last updated:** 2026-09-21

---

## Status

| Stage | Wave | Industries | Status |
|---|---|---|---|
| 1 | W1 Mainframe & Batch | 10 | ✅ complete — gate closed 2026-09-21 |
| 2 | W2 Departmental & Item-Level | 16 | ✅ complete — gate closed 2026-09-22 |
| 3 | W3 PC & the Spreadsheet | 16 | ✅ complete — **at gate** |
| 4 | W4 Client–Server & ERP | 18 | ⬜ not started |
| 5 | W5 The Commercial Web | 45 | ⬜ not started |
| 6 | W6 Cloud & SaaS | 83 | ⬜ not started |
| 7 | W7 Big Data | 14 | ⬜ not started |
| 8 | W8 Mobile & GPS | 16 | ⬜ not started |
| 9 | W9 Programmatic | 6 | ⬜ not started |
| 10 | W10 The Creator Platform | 14 | ⬜ not started |
| 11 | W11 The COVID Dislocation | 4 | ⬜ not started |
| 12 | W12 Transformers | 8 | ⬜ not started |

---

## Stage 1 — Wave 1, Mainframe & Batch

Ten industries. Chosen as the pilot because it splits 5 with an existing `history/` note
(payment-processors, credit-unions, medical-billing, insurance-tpa, hotels-boutique) and 5 without
(collections-agencies, independent-insurance-agents, municipal-services, payroll-platforms,
wealth-management-rias) — so it tests both the write-cold case and the add-a-lens-to-existing case.

### Conventions established on industry 1 (2026-09-21)

Frozen after the reference implementation, before any delegation. Batch agents inherit these.

- **`**Builder:**` is an aggregation key, not a sentence.** Short canonical name, ≤60 chars, no dates or founder names. The first draft wrote `IBM — invented by Forrest Parry (1960), industrialised by…`, which would have made every builder unique and silently destroyed the nomination gate. Caught before batch 1. Verifier now enforces it.
- **The word band is measured on the body, excluding `**Sources:**`.** Counting Sources penalises honest citation — the reference note's 100-word Sources block exists because it records two things it could *not* establish. Band is 450–750 body words.
- **Expect to cut.** The reference came in at 923 and trimmed to 733 without losing a claim. Write long, then cut; do not write to length.
- **The `## What You Still Touch` bullets carry an em-dash gloss** tying each link back to this note's argument, not just a bare link list.

### Rate calibration

`payment-processors`: 2 web searches, 1 vault read for link targets, 1 draft + 3 trims. Research was the cheap part; **finding the builder was the whole job**, which matches the finding that 46 of 66 history notes name no builder at all.

### Completed

- **payment-processors** — tool: the magnetic stripe and its ABA Track 2 record · builder: **IBM** (ABSENT) · 733 body words · 2 dated claims recorded as *not established* (ABA Track 2 adoption year; NBI electronic authorisation date)

**Batch 1 (2026-09-21) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK`.

- **collections-agencies** — tool: the predictive dialer, US Patent 4,858,120 · builder: **International Telesystems Corp** (ABSENT) · 748 words · flags that the patent *never mentions collections*, and leaves DSI's competing commercial-primacy claim unresolved
- **credit-unions** — tool: the share draft, payable-through a commercial bank · builder: **Credit Union National Association** (ABSENT) · 745 words
- **hotels-boutique** — tool: the Uniform System of Accounts for the Lodging Industry · builder: **Hotel Association of New York City** (ABSENT) · 749 words · only `verified` note in the batch
- **independent-insurance-agents** — tool: the ACORD form library (125, 25) · builder: **ACORD** (ABSENT) · 749 words
- **insurance-tpa** — tool: IAIABC EDI Claims FROI/SROI · builder: **IAIABC** (ABSENT) · 750 words

**Batch theme — the finding, not the status.** Five of five builders are **ABSENT from the vault, and four of the five are not vendors at all** — they are trade associations and standards bodies (CUNA, HANYC, ACORD, IAIABC). `_assessment.md` predicted the vault was missing *sellers of computing*. Wave 1 suggests the missing layer is broader and stranger than that: **the industry consortium that agreed a format none of its members owned.** That rhymes with the vault's own existing observation that three of the first four waves turn on competitors agreeing a standard — MICR's E-13B (1956), the ISO container (1968), the UPC (1973). Carry this into Stage 2 and test whether it holds outside Wave 1; if it does, the nomination gate may be selecting for the wrong kind of entity.

**Calibration flag.** Body words came in at 748 / 745 / 749 / 749 / 750 — every note overran and was trimmed to just under the ceiling. The agent reports trimming, not padding, and a full read of `collections-agencies` confirms dense, unpadded prose. But **a band that every note hits exactly is a band that is binding, not describing.** Raise at the Stage 1 gate: 450–750 may be too tight for the material this question produces.

**Rail 3 watch.** 0 of 5 `unknown` builders, which the agent itself flagged as unusual. Mitigating: all five are documented standards bodies or patent assignees, and each note carries explicit negative findings in Sources rather than asserting through the gaps. Not a fabrication signal on inspection, but the `unknown` rate stays under watch — if it is still zero at the end of Stage 2, the rail is not being exercised.

**Batch 2 (2026-09-21) — 4 industries, 4 files.** Verified from disk, `LINEAGE-OK`.

- **medical-billing** — tool: Current Procedural Terminology, the copyrighted five-digit code set · builder: **American Medical Association** (ABSENT) · 745 words · primary source read (9th Cir. 1997 copyright-misuse ruling); deliberately avoids the history note's DRG/clearinghouse framing
- **municipal-services** — tool: the governmental fund and the GAAFR "Blue Book" · builder: **Government Finance Officers Association** (ABSENT) · 747 words
- **payroll-platforms** — tool: the 94-character ACH file and its PPD credit entry · builder: **Nacha** (ABSENT) · 750 words
- **wealth-management-rias** — tool: the IARD Form ADV filing system and its public IAPD record · builder: **FINRA** (ABSENT) · 744 words

---

## Stage 1 gate — Wave 1 complete, 10 of 250

`LINEAGE-OK (10 notes)` · `content layers (13335) OK` · protected surface unchanged.

### Finding 1 — the builders are not vendors, they are consortia

**10 of 10 builders are ABSENT from the vault. 8 of the 10 are not companies at all:**

| Kind | Builders |
|---|---|
| Trade association / standards body / SRO | ACORD · CUNA · Hotel Association of New York City · IAIABC · American Medical Association · GFOA · Nacha · FINRA |
| Company | IBM · International Telesystems Corp |

`_assessment.md` argued the vault was missing **sellers of computing** and named six vendor-shaped `origins/` candidates — AWS, packaged software, platform gatekeepers, Nvidia, and so on. **Wave 1 does not support that framing.** What it supports is broader and stranger: the entity that dictated the artefact's shape is most often **the consortium that got a format agreed among competitors who each had to give something up to accept it.**

This rhymes with something the vault already noticed and never followed: `origins/_index.md` observes that three of the first four waves turn on competitors agreeing a standard none of them owned — MICR's E-13B (1956), the ISO container (1968), the UPC (1973). It called that "standardisation precedes digitisation" and then built no origin around it.

**This is exactly what the sweep was for.** The guess is already being corrected by the count at 4% coverage. **Carry into Stage 2 and test whether it survives outside Wave 1** — W1 is the regulated-and-clearinghouse-heavy wave and may be unrepresentative.

### Finding 2 — the word band is binding, not describing

| | Body words |
|---|---|
| Written by hand (orchestrator) | 717 |
| Written by agents (9 notes) | 744, 745, 745, 747, 748, 749, 749, 750, 750 |

Every agent note landed within six words of the 750 ceiling. Batch 2 was **explicitly instructed** not to treat 750 as a target and it changed nothing.

Inspection says these are trimmed, not padded — `collections-agencies` and `medical-billing` were both read in full and are dense, primary-sourced and free of filler. So the band is not producing bad notes; it is producing *uniformly maximal* ones, which means it is setting the length rather than describing it. **Decision needed at this gate**, options in the report to the owner.

### Finding 3 — Rail 3 is satisfied, but not where it was aimed

**0 of 10 `Builder: unknown`.** On inspection this is legitimate rather than lazy: every builder is a named patent assignee or a documented standards body, and **every note carries explicit negative findings in its Sources block** — CPT's second-edition date, the AMA royalty line being combined rather than CPT-only, the dialer patent never mentioning collections, DSI's contested commercial primacy, GFOA Blue Book dates behind a 403, the ACORD founding roster, IAIABC Release 1's year.

So the uncertainty is real and recorded — it just lands at **claim level rather than builder level**. The rail is working; it is simply aimed at the field where doubt turned out *not* to concentrate. Keep it unchanged and keep watching: if `unknown` is still zero at the end of Stage 2, that is worth re-examining.

### Finding 4 — the nomination gate has not fired, and may be mis-shaped

0 of 10 builders nominated, because each appears exactly once. That is expected at 4% coverage and not yet a problem.

But the shape of Finding 1 raises a real question: **if most industries have their own dedicated standards body, no builder will ever reach ≥5 industries**, and the gate will nominate only the recurring horizontal players (IBM, Nacha, and later presumably Microsoft, AWS, Visa). That may be correct — a single-industry standards body should *not* become an `origins/` entry. But it means the per-builder gate will never surface the consortium pattern itself, which is currently the single most interesting finding of the sweep. **Consider whether the category deserves a separate treatment from the per-builder count.**

### Calibration

Batch of 5: ~10 searches, 4 fetches, 2 blocked (403/DNS). Batch of 4: ~131 tool calls. Research is cheap; **establishing the builder is the whole job**, and trimming to the band is the second-biggest cost. At this rate the remaining 240 industries are ~48 batches.

---

## Stage 2 — Wave 2, Departmental & Item-Level

**Stage 1 gate closed 2026-09-21.** Owner approved Wave 2; word band (450–750) and nomination gate (≥5 industries, ≥2 waves) kept unchanged. Recorded in the GATE block of `_lineage.md`.

**Batch 1 (2026-09-21) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (15 notes)`. Two notes read in full (`coffee-shops-independent`, `contract-manufacturing`); no stray writes outside `lineage/`.

- **auto-dealers-independent** — tool: the CARFAX vehicle history report, VIN-keyed and first delivered by fax · builder: **Carfax** (ABSENT) · 739 words · not established: contents of the 1986 report, the Missouri dealers' association's actual role
- **coffee-shops-independent** — tool: no single tool; Rail 2 dated table led by the Faema E61 and its portafilter · builder: **no single builder** (n/a) · 744 words · first Rail 2 note of the sweep; punch-card builder not established
- **contract-manufacturing** — tool: BS 5750 → ISO 9001 and the third-party registration certificate · builder: **British Standards Institution** (ABSENT) · 726 words · convening story rests on a single avowed critic (Seddon), flagged in-file; first BSI certificate not established
- **dental-practices** — tool: the CDT Code, first published 1969 · builder: **American Dental Association** (ABSENT) · 739 words · authoring ADA body and date of the D-prefix not established (key source 403)
- **electronics-contract-mfg** — tool: IPC-A-610, first issued August 1983 · builder: **IPC** (ABSENT) · 742 words · IPC founders and 1983 drafters not established

**Batch theme.** The consortium pattern holds outside Wave 1: three of five builders are standards bodies or professional associations (BSI, ADA, IPC), one is a company (Carfax), and one industry built nothing and borrowed everything. Still 0 `unknown` builders across 15 notes — uncertainty continues to land at claim level, every note carrying explicit negative findings in Sources.

**Batch 2 (2026-09-21) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (20 notes)`. Two notes read in full (`food-manufacturing`, `independent-restaurants`); no stray writes outside `lineage/`.

- **food-manufacturing** — tool: HACCP and the written plan with a log at every critical control point · builder: **Pillsbury** (ABSENT) · 748 words · year of the farina-glass incident and a 1959 start date not established; FMEA-via-Natick claim not asserted (403)
- **greenhouse-horticulture** — tool: the greenhouse climate computer (Hoogendoorn TUCO 1974, Priva 1977) · builder: **no single builder** (n/a) · 734 words · Hoogendoorn and Priva both claim primacy; unresolved in-file
- **independent-restaurants** — tool: ViewTouch, the graphical touchscreen POS shown at Fall COMDEX 1986 · builder: **ViewTouch** (ABSENT) · 689 words · every builder-side fact is Mosher's own account, said so in-file; 1978 vs 1979 start, the restaurants themselves, and primacy not established; one "why them" paragraph explicitly marked as inference
- **independent-retailers** — tool: the cash register, Ritty patent 221,360 (1879), remade for shops by NCR · builder: **NCR** (ABSENT) · 739 words · Rittys invented it for a saloon, NCR keyed as builder because it made the shop version; first locking drawer not established
- **livestock-operations** — tool: no single tool; electronic animal ID and today's USDA "840" ear tag, dated table · builder: **no single builder** (n/a) · 739 words · no 1970s tag established as a direct ancestor

**Batch theme.** The consortium pattern weakens here: three companies (Pillsbury, ViewTouch, NCR) and two no-single-builder industries, no standards body. Wave 2's item-level industries look vendor- and operator-built where Wave 1's clearinghouse industries were consortium-built. `unknown` still 0 across 20; `no single builder` now 3.

**Batch 3 (2026-09-21) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (25 notes)`. Two notes read in full (`medical-device-mfg`, `retail-pos-platforms`); no stray writes outside `lineage/`.

- **medical-device-mfg** — tool: the 510(k) premarket notification and its "substantially equivalent" predicate test (Medical Device Amendments, May 28 1976) · builder: **US Congress** (ABSENT) · 735 words · keyed to Congress because the artefact is a statutory section; FDA chief counsel co-drafted it, said in-file. Cooper Committee injury counts deliberately not repeated
- **metal-fabrication** — tool: AWS D1.1 Structural Welding Code — Steel (1972, from a 1928 code) · builder: **American Welding Society** (ABSENT) · 741 words · "why them" labelled as inference; date prequalified procedures entered not established
- **pharmacy-independents** — tool: NCPDP Telecommunication Standard v1.0, the real-time pharmacy claim (September 1988) · builder: **NCPDP** (ABSENT) · 742 words · Universal Claim Form year (1978) secondary-only; vault history note's 1968 PBM-card date conflicts with JAMA's 1969 founding date, flagged
- **retail-pos-platforms** — tool: the Square Reader, headphone-jack stripe reader (2010) · builder: **Square** (in vault as `industries/retail-pos-platforms` — first builder the vault already owns) · 699 words · hardware designer contested (Morley dispute settled for $50.0M, never adjudicated)
- **rv-dealerships** — tool: the N.A.D.A. Recreation Vehicle Appraisal Guide · builder: **National Automobile Dealers Association** (ABSENT) · 709 words · first RV edition (possibly 1980, library record only) and NADA's reason for extending to RVs not established

**Key convention.** Square is keyed `Square`, not `Block`, because the artefact predates the 2021 rename. Future notes naming the company use `Square` so the rollup does not split.

**Batch theme.** Consortium/standards pattern returns: AWS, NCPDP and NADA are trade or standards bodies, plus a legislature (US Congress). First builder already in the vault (Square). `unknown` still 0 across 25 — every doubt again recorded at claim level.

**Batch 4 (2026-09-21) — 1 industry, 1 file** (last in the wave). Verified from disk, `LINEAGE-OK (26 notes)`. Note read in full; no stray writes outside `lineage/`.

- **specialty-food-retail** — tool: the price-computing scale, Pitrat's US Patent 314,717 (March 31 1885), and the prefix-2 random-weight UPC label its descendants print · builder: **Computing Scale Company** (ABSENT) · 749 words · deliberately **not** keyed to IBM, which inherited the scale by merger (1911) and sold it to Hobart (1934); prefix-2 designer, weigh-wrap-label date, Canby and Ozias's motive and the Pitrat/Pitrap spelling all recorded as not established

---

## Stage 2 gate — Wave 2 complete, 26 of 250

`LINEAGE-OK (26 notes)` · `PHASE3-VERIFY-CLEAN` · `content layers (13335) OK` · protected surface unchanged.

### Finding 1 — the consortium pattern survives, but it is a Wave 1 majority, not a law

| Kind | W1 (10) | W2 (16) | Total (26) |
|---|---|---|---|
| Trade association / standards body / SRO | 8 | 6 — BSI · ADA · IPC · American Welding Society · NCPDP · NADA | 14 |
| Legislature | 0 | 1 — US Congress | 1 |
| Company | 2 | 6 — Carfax · Pillsbury · ViewTouch · NCR · Square · Computing Scale Company | 8 |
| No single builder | 0 | 3 — coffee shops · greenhouses · livestock | 3 |

Consortia still lead overall, but Wave 2's item-level industries (counters, shops, dealerships, kitchens) were built for by **vendors and operators** where Wave 1's clearinghouse industries were built for by **agreements**. The split tracks the kind of problem: a format shared between rivals needs a convenor; a machine on one counter needs a manufacturer. `_assessment.md`'s vendor-shaped guess is still wrong about the majority, but not about all of it.

### Finding 2 — Rail 3 is still at zero `unknown` after 26 notes

The handover set this as the re-examination trigger. On inspection, the same reading as Stage 1 holds: every builder is a documented institution, patent assignee or statute, and every note carries explicit claim-level negatives in Sources — contested inventors (Square/Morley, Hoogendoorn/Priva), self-reported founders (ViewTouch), a single hostile source (BSI via Seddon), inference paragraphs labelled as inference. The genuinely unattributable cases are landing in `no single builder` (3), not `unknown`. **Not a fabrication signal; the rail is being exercised at claim level.** Whether to add a builder-level spot audit is an owner decision.

### Finding 3 — the nomination gate has still not fired, and no builder has repeated

22 distinct absent builders across 26 industries, **every one named exactly once**. Not even IBM has repeated — and one reason is a keying choice made this stage (below). At this rate the ≥5 gate will not fire until the horizontal waves (W5–W6), if then.

### Finding 4 — three keying precedents were set this stage

- **Inheritor vs originator:** `specialty-food-retail` keyed the scale to **Computing Scale Company**, not IBM, which acquired it by merger in 1911 and sold it in 1934. Right by the spec's "who built it" question, but it suppresses horizontal-player counts.
- **Statutes:** `medical-device-mfg` keyed the 510(k) to **US Congress** — the first non-industry builder.
- **Renames:** Square is keyed **`Square`**, not `Block`.

Future batches should follow these unless the owner changes them.

### Finding 5 — the word band loosened on its own

Wave 2 body words ran **689–749** (six notes under 740, three under 710) against Wave 1's 744–750. The band is no longer uniformly binding. Kept unchanged per the owner's Stage 1 decision.

### Calibration

Four agents, ~345 tool calls, ~60 minutes of agent time for 16 notes. Blocked pages (403/429) logged in-file in most batches. Research budget did not run out in any batch.

---

## Stage 3 — Wave 3, PC & the Spreadsheet

**Stage 2 gate closed 2026-09-22.** Owner approved Wave 3. Rail 3 and the Stage 2 keying precedents (originator over inheritor; statutes → `US Congress`; `Square` not `Block`) left unchanged. Recorded in the GATE block of `_lineage.md`.

**Batch 1 (2026-09-22) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (31 notes)`. Two notes read in full (`commercial-real-estate`, `energy-auditors`); no stray writes outside `lineage/`.

- **accounting-firms-smb** — tool: the SSARS No. 1 compilation report (December 1978) · builder: **AICPA** (ABSENT) · 744 words · whether the planned peer-review exclusion for preparation work was adopted not established
- **commercial-real-estate** — tool: the CoStar database, broker-sourced and first shipped on floppy disk · builder: **CoStar Group** (ABSENT) · 734 words · founding year (1986 Princeton dorm vs 1987 Washington) unresolved; "why them" labelled inference; ARGUS dropped because its founder could not be trusted
- **energy-auditors** — tool: the blower door and its CFM50 reading · builder: **no single builder** (n/a) · 746 words · Rail 2 dated table (Sweden, Saskatchewan, Princeton, Gadsco, Harmax, The Energy Conservatory); Home Energy's 1995 history not read directly
- **engineering-consultants** — tool: Brooks Act qualifications-based selection (PL 92-582, 1972) and the SF 254/255 → SF 330 forms · builder: **US Congress** (ABSENT) · 738 words · first issue date of SF 254/255 and the Act's lobbyists not established
- **environmental-consultants** — tool: ASTM E1527 (1993) and its search-distance table · builder: **ASTM International** (ABSENT) · 748 words · formation of Committee E50 and who drove the standard not established; "why them" labelled inference

**First repeat builder.** `US Congress` now appears twice (W2 `medical-device-mfg`, W3 `engineering-consultants`) — the statute-keying precedent from Stage 2 is what made the count join. `unknown` still 0 across 31; `no single builder` now 4.

**Batch 2 (2026-09-22) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (36 notes)`. Two notes read in full (`independent-publishers`, `estate-planning`); no stray writes outside `lineage/` (`history/general-contractors.md` was corrected *in the lineage note only*, not edited).

- **estate-planning** — tool: NumberCruncher, the 1984 estate-tax and split-interest calculator · builder: **Leimberg & LeClair** (ABSENT) · 741 words · VisiCalc-template origin not established (vendor page 403); unnamed "colleague" not assumed to be LeClair
- **event-planning** — tool: the APEX Event Specifications Guide (approved September 30 2004) · builder: **Convention Industry Council** (ABSENT) · 743 words · keyed to the name at build time, now Events Industry Council; Banquet Event Order's origin not established
- **general-contractors** — tool: AIA G702/G703, the monthly pay application · builder: **American Institute of Architects** (ABSENT) · 749 words · form copyright lines date G702 to 1953 and G703 to 1963, which `history/general-contractors.md` had left unverified; G702's drafter not established
- **grant-writers** — tool: *The Foundation Directory* · builder: **Foundation Center** (ABSENT) · 684 words · keyed to the build-time name, not Candid (2019); first edition 1960 vs 1967 unresolved
- **independent-publishers** — tool: the ISBN, from WHSmith's 1965 Standard Book Number to ISO 2108 (1970) · builder: **WHSmith** (ABSENT) · 720 words · 1970 vs 1974 conflict flagged; Bowker prices from search summary only; warehouse-as-cause offered as context, not asserted

**Keying notes.** Two more build-time-name keys (`Convention Industry Council`, `Foundation Center`), consistent with the Stage 2 `Square`-not-`Block` precedent. `Leimberg & LeClair` is the first key naming individuals rather than an organisation — used because the 1984 build predates any firm the sources establish; the later company name (Leimberg, LeClair & Lackner) contains commas and was not asserted for 1984. Every "why them" in this batch is labelled inference. `unknown` still 0 across 36.

**Batch 3 (2026-09-22) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (41 notes)`. Two notes read in full (`public-adjusters`, `real-estate-appraisers`); no stray writes outside `lineage/`.

- **printing-shops** — tool: the Pantone Matching System, 1963 Printers' Edition · builder: **Pantone** (ABSENT) · 738 words · colour count of the 1963 guide and the Levine brothers' first names conflict across sources
- **public-adjusters** — tool: Xactimate and its regional unit-cost price list (1986) · builder: **Xactware** (ABSENT) · 743 words · founding year confirmed (Deseret News); founder, Orem basement and 2005 death from search summaries of a 403 vendor page, flagged "not read at source"; 2006 ISO deal terms not found
- **real-estate-appraisers** — tool: the URAR (Fannie Mae 1004 / Freddie Mac 70) and its three-comparable adjustment grid · builder: **Fannie Mae & Freddie Mac** (ABSENT) · 750 words · origin year and designing GSE not established, so no origin year appears in the body
- **small-law-firms** — tool: the daily Time Record in the ABA's 1958 pamphlet *The 1958 Lawyer and His 1938 Dollar* · builder: **American Bar Association** (ABSENT) · 744 words · committee's 1957 founding and a solo-practice percentage illegible in the OCR scan
- **tax-prep-firms** — tool: IRS e-file, the 1986 Electronic Filing System pilot · builder: **Internal Revenue Service** (ABSENT) · 737 words · inventor of the refund anticipation loan contested, left unresolved

**Keying note — first joint key.** `Fannie Mae & Freddie Mac` is used because the form is jointly issued and which GSE designed it is not established. It will **not** merge with a later note keyed to either GSE alone — raise at the Stage 3 gate. Government builders now at three (US Congress ×2, Internal Revenue Service). `unknown` still 0 across 41.

**Batch 4 (2026-09-22) — 1 industry, 1 file** (last in the wave). Verified from disk, `LINEAGE-OK (42 notes)`. Note read in full; no stray writes outside `lineage/`.

- **video-production-smb** — tool: SMPTE timecode, the HH:MM:SS:FF frame address (ST 12; proposed 1970, approved 1975) · builder: **SMPTE** (ABSENT) · 737 words · keyed to the standard's owner, not EECO, whose 1967 proprietary code preceded it — consistent with the named artefact being the interoperable standard (as BSI over MIL-Q in Stage 2); adopted-version inventor contested (O'Donnell/NFB rests on Wikipedia only)

---

## Stage 3 gate — Wave 3 complete, 42 of 250

`LINEAGE-OK (42 notes)` · `PHASE3-VERIFY-CLEAN` · `content layers (13335) OK` · protected surface unchanged.

### Finding 1 — the PC wave's tools are mostly forms the PC later filled in

Wave 3 is "PC & the Spreadsheet", but only **2 of its 16 tools are PC software** (NumberCruncher, Xactimate), plus one data product first shipped on floppy (CoStar). **Eleven are forms, standards or code sets**: the SSARS compilation report, SF 254/255, ASTM E1527, the APEX guide, AIA G702/G703, the ISBN, the Pantone guide, the URAR, the ABA Time Record, SMPTE timecode, and the Foundation Directory as a printed reference. The appraiser note states the pattern outright: *the software filled in the GSEs' grid faster; it did not change the grid.* For professional services, the artefact that dictates the work's shape predates the PC and was set by the profession or its biggest buyer.

### Finding 2 — the builder mix, three waves in

| Kind | W1 (10) | W2 (16) | W3 (16) | Total (42) |
|---|---|---|---|---|
| Trade association / standards body / SRO | 8 | 6 | 6 — AICPA · ASTM International · Convention Industry Council · American Institute of Architects · American Bar Association · SMPTE | 20 |
| User-funded nonprofit | 0 | 0 | 1 — Foundation Center | 1 |
| Government / legislature / GSE | 0 | 1 | 3 — US Congress · Internal Revenue Service · Fannie Mae & Freddie Mac | 4 |
| Company | 2 | 6 | 4 — CoStar Group · Pantone · Xactware · WHSmith | 12 |
| Named individuals | 0 | 0 | 1 — Leimberg & LeClair | 1 |
| No single builder | 0 | 3 | 1 — energy auditors | 4 |

Consortia hold at roughly half the sweep. **Government as builder is new and rising** — where the state is the biggest buyer or the regulator (federal procurement, the IRS, the GSEs), it wrote the form.

### Finding 3 — the first repeat builder

**`US Congress` is named by 2 industries across 2 waves** (`medical-device-mfg` W2, `engineering-consultants` W3) — the only builder of 36 to repeat. It joined only because of the Stage 2 statute-keying precedent. The ≥5 gate has not fired.

### Finding 4 — Rail 3 is at zero `unknown` for the third gate running

0 of 42. Same reading as before: builders are documented institutions, and doubt is recorded at claim level in every note. **One new texture worth naming:** several builder-side facts now rest on search summaries of pages that returned 403 (Xactware's founder, the VisiCalc origin of NumberCruncher), and the agents consistently flag these "not read at source" and keep them out of the `**Builder:**` key, which is independently established each time. Still not a fabrication signal. Nearly every "why them" this stage is explicitly labelled inference.

### Finding 5 — four more keying precedents

- **Build-time name:** `Convention Industry Council` (now Events Industry Council), `Foundation Center` (now Candid) — consistent with `Square` not `Block`.
- **Named individuals:** `Leimberg & LeClair`, because no 1984 firm is established; the later company name contains commas.
- **Joint key:** `Fannie Mae & Freddie Mac`, because the URAR is jointly issued and the designing GSE is not established. **Will not merge** with a later note keyed to either GSE alone.
- **Standard owner over first vendor:** `SMPTE`, not EECO, because the artefact named is the interoperable standard, not EECO's proprietary code.

### Finding 6 — the word band is binding again

Wave 3 body words ran 684–750, with **13 of 16 at 734 or above**. Wave 2's loosening did not persist. Band unchanged per owner.

### Calibration

Four agents, ~386 tool calls, ~80 minutes of agent time for 16 notes. 403s on vendor pages were the most common blocker; research budget did not run out.


---

## Stage 4 — Wave 4, Client–Server & ERP

**Stage 3 gate closed 2026-09-25.** Owner approved Wave 4 end to end ("go, run wave 4 end to end"). Joint key and Rail 3 left unchanged. Recorded in the GATE block of `_lineage.md`.

**Batch 1 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (47 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`auto-repair-shops`, `charter-bus-operators`); no stray writes outside `lineage/`.

- **ap-automation-vendors** — tool: the ANSI ASC X12 810 Invoice, matched against the 850 purchase order · builder: **ASC X12** (ABSENT) · year X12 first published the 810 not established
- **auto-body-shops** — tool: the CIECA Estimate Management Standard (EMS) file set · builder: **CIECA** (ABSENT) · 20 Jan 1994 incorporation from search summary only; consortium-neutrality argument labelled inference
- **auto-repair-shops** — tool: the OBD-II port, SAE J1962 connector and J2012 trouble codes · builder: **Society of Automotive Engineers** (ABSENT) · keyed by standard-owner precedent, CARB's 12 Sep 1989 mandate in body; J1962/J2012 publication years not established
- **charter-bus-operators** — tool: the CDL with P endorsement, plus CDLIS · builder: **US Congress** (ABSENT) · statute precedent; AAMVA/AAMVAnet in body, 1988 charter and 3 Jan 1989 go-live not read at source; Act's signing date omitted
- **compliance-consulting** — tool: SAS 70, *Service Organizations* (1992), ancestor of SOC 1/SOC 2 · builder: **AICPA** (ABSENT) · SAS 44 year and who pressed for SAS 70 not established

**Batch 2 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (52 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`digital-forensics-firms`, `freight-brokerage`); no stray writes outside `lineage/`.

- **customs-brokers** — tool: the Automated Broker Interface (ABI) · builder: **US Customs Service** (ABSENT) · 740 words · 1984 start from secondary glossaries only
- **database-platform-vendors** — tool: System R's cost-based query optimizer (Selinger et al., SIGMOD 1979) · builder: **IBM** (ABSENT; existing key, now 2 industries W1+W4) · 720 words · IBM's installed-base motive labelled inference
- **digital-forensics-firms** — tool: EnCase and its E01 evidence file · builder: **Guidance Software** (ABSENT) · 737 words · **open originator question:** E01 v1 "reportedly" based on ASR Data's Expert Witness format; LoC page 403; key may move to ASR Data if confirmed
- **food-distributors** — tool: the GS1-128 (UCC/EAN-128) case label and Application Identifiers · builder: **Uniform Code Council** (ABSENT) · 723 words · jointly issued with EAN, keyed to the US owner at build time; 1989 vs 1991 release unresolved, no year given
- **freight-brokerage** — tool: the Dial-A-Truck load board, launched 3 April 1978 · builder: **Jubitz Corporation** (ABSENT) · 717 words · subsidiary's legal name and driver fee not found

**Batch 3 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (57 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`insurance-restoration`, `procurement-spend-platforms`); no stray writes outside `lineage/`.

- **insurance-restoration** — tool: IICRC S500 water-damage standard (1st ed. 1994), Categories and Classes of water · builder: **IICRC** (ABSENT) · 741 words · keyed to today's name because the IICUC→IICRC rename date is not established (possible build-time-name exception); 1994 drafters and origin of the Category/Class scheme not established
- **medical-supply-retail** — tool: HCPCS Level II (the E-codes for equipment) · builder: **Health Care Financing Administration** (ABSENT) · 735 words · build-time name, now CMS; 1983 date from search summary only
- **mortgage-brokers** — tool: Desktop Underwriter (production June 1995) plus Desktop Originator · builder: **Fannie Mae** (ABSENT) · 726 words · single key justified by a 1997 AAAI paper by Fannie Mae staff; **does not merge with `Fannie Mae & Freddie Mac` (W3)** — the split open decision 2 predicted
- **oil-gas-field-services** — tool: PIDX Field Ticket and Invoice standards · builder: **American Petroleum Institute** (ABSENT) · 738 words · API ran PIDX 1987–2010; first EDI transaction date and the XML-in-the-1990s vs 2002 v1.0 tension not resolved
- **procurement-spend-platforms** — tool: UNSPSC (MoU signed Sep/Nov 1998) · builder: **United Nations Development Programme & Dun & Bradstreet** (ABSENT) · 705 words · second joint key; which party designed v1 not established

**Batch 4 (2026-09-25) — 3 industries, 3 files.** Verified from disk, `LINEAGE-OK (60 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`restaurant-suppliers`, `utility-contractors`); no stray writes outside `lineage/`.

- **restaurant-suppliers** — tool: the distributor order guide · builder: **no single builder** (n/a) · 737 words · Rail 2 table (Sysco 1969, Telxon handhelds, GS1 US Foodservice Initiative 2009, FSMA 204 2022); origin of the printed order guide not established
- **utility-contractors** — tool: the APWA Uniform Color Code for underground marks · builder: **American Public Works Association** (ABSENT) · 721 words · adoption year not established ("1970s"/"1960s" only); pre/post 1976 Culver City strike unresolved; why-them labelled inference
- **warehouse-3pl** — tool: X12 940 Warehouse Shipping Order and 945 reply · builder: **ASC X12** (ABSENT; existing key, now 2 industries) · 678 words · WINS sponsor and 940/945 first-publication year not established

---

## Stage 4 gate — Wave 4 complete, 60 of 250

**Set 2026-09-25.** Wave 4 ran end to end as 4 sequential agents (5·5·5·3), ~183 tool calls, ~30 minutes of agent time. Every batch verified from disk; two notes read in full per batch; no stray writes; `PHASE3-VERIFY-CLEAN` throughout.

### Finding 1 — the client–server wave's tools are mostly standards and mandates again

Of 18 tools, only 4 are software products (Desktop Underwriter, EnCase, System R's optimizer, Dial-A-Truck). The rest are EDI transaction sets (X12 810, 940/945), file and code standards (CIECA EMS, OBD-II, GS1-128, HCPCS, UNSPSC, PIDX), practice standards (SAS 70, IICRC S500), a licence (CDL) and a paint colour code. Wave 3's reading holds: the era's software carried formats someone else convened.

### Finding 2 — the builder mix, four waves in

| Kind | W1 | W2 | W3 | W4 | Total |
|---|---|---|---|---|---|
| Trade association / standards body / SRO | 8 | 6 | 6 | 9 | 29 |
| User-funded nonprofit | 0 | 0 | 1 | 0 | 1 |
| Government / legislature / GSE | 0 | 1 | 3 | 4 | 8 |
| Company | 2 | 6 | 4 | 3 | 15 |
| Named individuals | 0 | 0 | 1 | 0 | 1 |
| Joint public–private | 0 | 0 | 0 | 1 | 1 |
| No single builder | 0 | 3 | 1 | 1 | 5 |

Consortia at half of Wave 4; government keeps rising (Congress, US Customs Service, HCFA, Fannie Mae).

### Finding 3 — repeats are appearing, still far from the gate

`US Congress` 3 industries (W2–W4); `AICPA` 2 (W3–W4); `IBM` 2 (W1, W4); `ASC X12` 2 (W4 only). The ≥5 / ≥2-wave gate has not fired.

### Finding 4 — the joint-key split has now happened

`mortgage-brokers` is keyed `Fannie Mae` (designer established by a 1997 AAAI paper by Fannie Mae staff); `real-estate-appraisers` (W3) stays `Fannie Mae & Freddie Mac`. They do not merge. A second joint key appeared: `United Nations Development Programme & Dun & Bradstreet` (UNSPSC).

### Finding 5 — two keys may need to move

- `digital-forensics-firms` — E01 v1 "reportedly" based on ASR Data's Expert Witness format; if confirmed, originator-over-inheritor moves the key to ASR Data.
- `insurance-restoration` — keyed `IICRC` (today's name); the IICUC→IICRC rename date is not established, so the build-time name may be IICUC.

### Finding 6 — Rail 3 at zero `unknown` for the fourth gate running

0 of 60. Same texture as before: doubt lands at claim level, every note carries explicit negative findings, and search-summary-only facts are flagged "not read at source" and kept out of the key.

### Calibration

Word counts 678–748. Four agents, ~183 tool calls, ~30 minutes — faster than Wave 3.

**Stage 4 gate closed 2026-09-25.** Owner gave standing approval for all remaining waves (W5–W12), sequential, one agent at a time, a one-line update per wave, no stopping at boundaries. Stage-gate findings are still written here at each boundary. Non-blocking items (Fannie Mae split, joint keys, E01/IICUC key moves, Rail 3) left unchanged.

---

## Stage 5 — Wave 5, The Commercial Web

**Batch 1 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (65 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`bug-bounty-platforms`, `b2b-commerce-platforms`); no stray writes outside `lineage/`.

- **affiliate-networks** — tool: the Amazon Associates referral link (US Patent 6,029,141) · builder: **Amazon** (ABSENT) · 734 words · date of move from item-level credit to cookie-window attribution not established
- **b2b-commerce-platforms** — tool: cXML 1.0 PunchOut (spec dated 16 Aug 1999) · builder: **Ariba** (in vault via `industries/procurement-spend-platforms`) · 731 words · SAP OCI year not established
- **brand-protection-firms** — tool: eBay's VeRO programme and NOCI form · builder: **eBay** (in vault via `industries/online-marketplaces`) · 734 words · 1998 start from secondary sources only
- **bug-bounty-platforms** — tool: Netscape's "Bugs Bounty" for the Navigator 2.0 beta · builder: **Netscape** (ABSENT) · 688 words · Oct 1995 vs early 1996 launch unresolved; press release unreachable
- **content-moderation-services** — tool: PhotoDNA · builder: **Microsoft** (ABSENT) · 737 words · Microsoft vs joint Microsoft–Farid key arguable; Facebook adoption 2010 vs 2011; NCMEC donation undated

**Batch 2 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (70 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`digital-audio-platforms`, `digital-bpo-operations`); no stray writes outside `lineage/` (`.obsidian/` changes are the owner's Obsidian app, not the agent).

- **conversion-optimization-firms** — tool: the Optimizely JavaScript snippet and visual editor (private beta July 2010) · builder: **Optimizely** (ABSENT) · 727 words · Google Website Optimizer launch year not established
- **crowdsourcing-platforms** — tool: Amazon Mechanical Turk and the HIT (US 7,197,459; launched 2 Nov 2005) · builder: **Amazon** (ABSENT; existing key) · 721 words · Junglee lineage of inventors labelled inference
- **digital-accessibility-firms** — tool: WCAG 1.0 and its A/AA/AAA conformance levels (5 May 1999) · builder: **W3C** (ABSENT) · 698 words · editor list and Watchfire–Bobby acquisition date (2002 vs 2004) not established
- **digital-audio-platforms** — tool: the pro-rata ("streamshare") royalty pool · builder: **unknown — searched, not established** (n/a) · 735 words · **first `unknown` of the sweep (1 of 70)**; Rhapsody Dec 2001 pool claim search-summary only and contradicted by Quirk's penny-per-play recollection
- **digital-bpo-operations** — tool: the Galaxy automatic call distributor, sold to Continental Airlines 1973 · builder: **Collins Radio** (ABSENT) · 722 words · build-time name; Rockwell controlled Collins from 1971 — judgment call; patent number not found

**Batch 3 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (75 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`dropshipping-suppliers`, `digital-goods-marketplaces`); no stray writes outside `lineage/`.

- **digital-goods-marketplaces** — tool: the DMCA takedown notice, 17 U.S.C. § 512(c)(3) (signed 28 Oct 1998) · builder: **US Congress** (ABSENT; existing key, now 4 industries) · 740 words · negotiating parties and session dates not established; no primary legislative history reached
- **digital-native-publishers** — tool: the HotWired banner ad (AT&T "You Will", 27 Oct 1994) with pageviews from server logs · builder: **HotWired** (ABSENT) · 740 words · first CPM pricing not established; $30k vs $10k/month conflict
- **dropshipping-suppliers** — tool: Oberlo, first shipped as "Ali Importer" · builder: **Oberlo** (ABSENT) · 724 words · App Store launch and rename dates not established; 2015 founding secondary only; Shopify's filed $17.2M used over reported $15M
- **ecommerce-sellers** — tool: Amazon Marketplace's single detail page (Nov 2000) · builder: **Amazon** (ABSENT; existing key, now 3 industries) · 740 words · Amazon Auctions launch month and Buy Box origin not established
- **edge-cdn-providers** — tool: Akamai FreeFlow · builder: **Akamai** (ABSENT) · 734 words · ARL freshness/invalidation handling not established

**Batch 4 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (80 notes)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`email-sms-marketing-platforms`, `identity-verification-vendors`); no stray writes outside `lineage/`.

- **email-sms-marketing-platforms** — tool: the open-tracking pixel · builder: **unknown — searched, not established** (n/a) · 742 words · Web Bug FAQ (11 Nov 1999) documents the practice; no first sender, ESP or originating patent found
- **esignature-document-workflow** — tool: the DocuSign envelope and Certificate of Completion · builder: **DocuSign** (in vault via its own industry, Square precedent) · 743 words · first use of "envelope" and 2005 per-envelope pricing not established
- **freelance-marketplaces** — tool: the oDesk Work Diary backing the hourly Payment Guarantee · builder: **oDesk** (in vault via its own industry) · 745 words · Work Diary ship date not established; founding 2003 vs 2005
- **game-asset-marketplaces** — tool: the Unity Asset Store (10 Nov 2010, Unity 3.1) · builder: **Unity Technologies** (ABSENT) · 741 words · 70/30 split from launch not established
- **identity-verification-vendors** — tool: no single tool (Rail 2 table: ICAO 9303 MRZ, PDF417, AAMVA DL/ID-2000, PATRIOT Act §326, CIP rule, Jumio, NISTIR 8280) · builder: **no single builder** (n/a) · 745 words · first selfie-to-ID product and Netverify launch year not established


**Temporary parallelism (2026-09-25, from 16:58 for ~50 min).** Owner authorised 2 extra concurrent agents (3 at once) to use spare quota before the window resets, then back to 1 (max 2). Each agent still writes only its own `lineage/<slug>.md`; the orchestrator alone merges shared files, one batch at a time.

**Batch 5 (2026-09-25) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (87 notes, incl. in-flight parallel files)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`language-schools`, `localization-services`); no stray writes outside `lineage/`.

- **indie-game-studios** — tool: Steam Greenlight (30 Aug 2012) and its 2017 replacement, the Steam Direct fee · builder: **Valve** (ABSENT) · 718 words · no figures for pre-Greenlight manual curation
- **it-staffing-firms** — tool: DICE, the Data Processing Independent Consultants Exchange BBS (1990) · builder: **Dice** (ABSENT) · 721 words · Iowa move 1994 vs 1995, web launch, direct-employer entry 1998 vs 1999, original pricing unresolved
- **language-schools** — tool: SEVIS and the Form I-20 (mandatory 1 Aug 2003) · builder: **Immigration and Naturalization Service** (ABSENT) · 725 words · no outside contractor found; 1993 WTC link omitted as unchecked
- **lending-marketplaces** — tool: the LendingTree qualification form and Lend-X exchange · builder: **LendingTree** (in vault via its own industry) · 709 words · fees and four-lender limit from the 2002 annual report only; patent date unknown
- **localization-services** — tool: Trados Translator's Workbench and the "Trados grid" · builder: **Trados** (in vault via `industries/localization-services`, founded as a translation agency) · 685 words · MultiTerm 1990 vs 1992 and Workbench 1992 vs 1994 unresolved; first fuzzy-match discounting undated

**Batch 7 (2026-09-25, parallel) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (92 notes, incl. in-flight parallel files)`, `PHASE3-VERIFY-CLEAN`. Two notes read in full (`personal-injury-law`, `penetration-testing-firms`); no stray writes outside `lineage/`.

- **penetration-testing-firms** — tool: SATAN network vulnerability scanner (5 Apr 1995) · builder: **Dan Farmer & Wietse Venema** (ABSENT) · 726 words · named-individuals precedent, no firm at build time; SGI's reason for firing Farmer not established
- **performance-marketing-agencies** — tool: GoTo.com's pay-per-click keyword bid auction (1998) · builder: **GoTo.com** (ABSENT) · 688 words · build-time name, not Overture; launch day and original auction rules not established
- **personal-injury-law** — tool: Colossus bodily-injury evaluation system · builder: **Computations Pty Ltd** (ABSENT) · 676 words · originator over CSC; GIO vs Computations design split ("jointly"); ALJ 1992 details search-summary only; Allstate 1995 go-live unconfirmed
- **print-on-demand-platforms** — tool: the CafePress shop, base price plus seller markup (1999) · builder: **CafePress** (ABSENT) · 657 words · founders' motive, printing method, San Mateo vs San Leandro not established
- **recommerce-platforms** — **deleted and respawned 2026-09-25:** duplicated `online-marketplaces`'s tool (eBay Feedback Forum) — a race between two parallel agents. Rewritten by a fresh agent; see its line below.

**Batch 6 (2026-09-25, parallel) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (98 notes, incl. in-flight parallel files)`, `PHASE3-VERIFY-CLEAN`. Notes read in full: `moving-companies`; `online-marketplaces` checked against `recommerce-platforms` (duplicate tool found — see batch 7); no stray writes outside `lineage/`.

- **marketing-agencies-smb** — tool: UTM campaign parameters from Urchin · builder: **Urchin Software Corporation** (ABSENT) · 741 words · UTM introduction date unresolved (one site says 1996, before Urchin's 1998 release); web-shop origin from one self-disclaiming source
- **moving-companies** — tool: HGCB Tariff 400N, the collective weight-and-distance tariff · builder: **Household Goods Carriers' Bureau** (ABSENT) · 730 words · founding date (1937?) not established; Ex Parte 656 vs separate proceeding unresolved
- **music-distribution-platforms** — tool: DDEX Electronic Release Notification (ERN) · builder: **DDEX** (ABSENT) · 739 words
- **news-media-local** — tool: Press+ metered paywall · builder: **Journalism Online** (ABSENT) · 734 words · revenue share and local-vs-national customer mix not established
- **online-marketplaces** — tool: the eBay Feedback Forum (26 Feb 1996) · builder: **eBay** (in vault via its own industry) · 727 words · kept `eBay` over build-time `AuctionWeb` (same operation, existing key); 1996 scoring rules and 2008 change date not established

**Parallelism raised (2026-09-25 17:12).** Owner authorised 3 more agents (6 at once) inside the same window. Conflict control: batches grouped by theme so adjacent industries share one agent; every agent checks all existing `**The tool:**` lines and a scratchpad claims directory (one file per slug, written by its own agent) before choosing, and must not duplicate an artefact already used. Wave 6 started in parallel while Wave 5 finishes; Stage 5 gate findings to be written when W5 closes.

**Batch 8 (2026-09-25, parallel) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (100 notes)`, `PHASE3-VERIFY-CLEAN`. Read in full: `software-dev-agencies` builder section; no duplicate tools across `lineage/`; no stray writes.

- **recruiting-tech-vendors** — tool: Resumix resume scanner (first deployed at Sun, Jan 1989) · builder: **Resumix** (ABSENT) · 739 words · Leung's background and HotJobs price not established
- **seo-tooling-vendors** — tool: WebPosition Gold's Reporter rank checker · builder: **FirstPlace Software** (ABSENT) · 719 words · first release year and location not established
- **short-term-rentals** — tool: the VRBO flat-fee classified listing (1995) · builder: **VRBO** (ABSENT) · 735 words · originator over acquirer; launch month not established; $72 (founder) used over $67
- **software-dev-agencies** — tool: the function point (Albrecht, 1979) · builder: **IBM** (ABSENT; existing key, now 3 industries) · 687 words · DP Services customer-contract work secondary only; IFPUG 1986 vs 1987
- **staffing-agencies** — tool: the Bullhorn hosted ATS · builder: **Bullhorn** (ABSENT) · 686 words · pivot trigger disputed; first ATS release date not found

**Recommerce rewrite (2026-09-25).** `recommerce-platforms` — tool: the StockX green authentication hangtag ("Verified Authentic", renamed "StockX Verified" 2022) · builder: **StockX** (ABSENT) · 746 words · first use of the green tag undated; 100-point checklist is StockX's own claim. Duplicate resolved.

**Batch 9 (2026-09-25, parallel) — 5 industries, 5 files.** Verified from disk, `LINEAGE-OK (109 notes, incl. in-flight W6 files)`, `PHASE3-VERIFY-CLEAN`. Builder sections read for `web-data-extraction-firms` and `vocational-schools`; no duplicate tools; no stray writes.

- **stock-media-marketplaces** — tool: the royalty-free stock licence on PhotoDisc's CD-ROM packs (1991) · builder: **PhotoDisc** (ABSENT) · 744 words · "first" and founders' motive not established; founder list disputed
- **trade-associations** — tool: iMIS association management system · builder: **Advanced Solutions International** (ABSENT) · 678 words · 1996 WaPo and ASI history pages not fetched — search summaries only
- **ux-research-agencies** — tool: the "test with five users" rule (Alertbox, 18 Mar 2000) · builder: **Nielsen Norman Group** (ABSENT) · 718 words · keyed to the 2000 rule, curve has several earlier originators
- **vocational-schools** — tool: ACCSC Graduation and Employment Chart and 70% benchmark · builder: **ACCSC** (ABSENT) · 711 words · chart/benchmark introduction date not established, so keyed to today's name (was ACCSCT 1993–2009)
- **web-data-extraction-firms** — tool: robots.txt (Feb 1994) · builder: **Martijn Koster** (ABSENT) · 730 words · named individual; no evidence Nexor sponsored it

---

## Stage 5 gate — Wave 5 complete, 105 of 250

**Set 2026-09-25; record-and-continue under standing approval.** Nine batches plus one respawn; ran sequentially for batches 1–4, then 3 and later 6 agents in parallel under the owner's temporary authorisation.

### Finding 1 — the commercial web flips the builder mix to companies

| Kind | W1 | W2 | W3 | W4 | W5 | Total |
|---|---|---|---|---|---|---|
| Trade association / standards body / SRO | 8 | 6 | 6 | 9 | 4 | 33 |
| User-funded nonprofit | 0 | 0 | 1 | 0 | 0 | 1 |
| Government / legislature / GSE | 0 | 1 | 3 | 4 | 2 | 10 |
| Company | 2 | 6 | 4 | 3 | 34 | 49 |
| Named individuals | 0 | 0 | 1 | 0 | 2 | 3 |
| Joint public–private | 0 | 0 | 0 | 1 | 0 | 1 |
| No single builder | 0 | 3 | 1 | 1 | 1 | 6 |
| Unknown | 0 | 0 | 0 | 0 | 2 | 2 |

34 of 45 Wave 5 builders are companies — Amazon, eBay, Netscape, Akamai, Optimizely, Valve, StockX. The consortium finding of Waves 1–4 was a finding about the *pre-web* era, not about the vault as a whole. On the web, the convenor role mostly disappears: the platform itself sets the format (the Feedback Forum, the Associates link, PunchOut, Greenlight).

### Finding 2 — the first `unknown` builders are honest ones

`digital-audio-platforms` (the pro-rata streamshare pool) and `email-sms-marketing-platforms` (the open-tracking pixel) — both are conventions that emerged across many firms with no documented originator. Rail 3 is no longer at zero; the rate (2 of 105) is still low.

### Finding 3 — repeats are forming

`US Congress` 4 industries (W2–W5); `Amazon` 3 (W5); `IBM` 3 (W1, W4, W5); `eBay` 2 but in vault. No builder is at the ≥5 / ≥2-wave gate yet; `US Congress` is closest.

### Finding 4 — parallel runs need conflict control

Two parallel agents both chose the eBay Feedback Forum (`online-marketplaces`, `recommerce-platforms`). Resolved by delete-and-respawn (StockX hangtag). From Wave 6, batches are grouped by theme and every agent checks existing tools plus a scratchpad claims directory before choosing.

### Finding 5 — self-referential "in vault"

Several platform builders (DocuSign, oDesk, LendingTree, Trados, eBay) point `**Builder in vault:**` at their own industry, following the `Square` precedent. They therefore drop out of the ABSENT rollup — correct by spec, but the rollup undercounts platform companies as a class.

---

## Stage 6 — Wave 6, Cloud & SaaS

**Batch D (2026-09-25, parallel; themed: appointment-driven local services).** Verified from disk, `LINEAGE-OK (123 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder sections read for `med-spas`, `gyms-independent`; no duplicate tools; claims honoured.

- **fitness-wellness-software** — tool: the MINDBODY class schedule (1998 Pilates origin, online 2005) · builder: **Mindbody** (ABSENT) · 700 words · garage start 2000 vs 2001
- **gyms-independent** — tool: American Billing Company's third-party dues-billing account (1981) · builder: **American Billing Company** (ABSENT) · 675 words · build-time name, now ABC Financial; 1981 payment method not established
- **hair-salons-independent** — tool: the StyleSeat per-stylist booking profile (2011) · builder: **StyleSeat** (ABSENT) · 679 words · booth-renter targeting at launch not established
- **med-spas** — tool: BOTOX Cosmetic (FDA approval April 2002, glabellar lines) · builder: **Allergan** (ABSENT) · 653 words · Carruthers origin anecdote omitted as unverified
- **scheduling-booking-platforms** — tool: iCalendar, RFC 2445 (Nov 1998) and the `.ics` VEVENT · builder: **IETF** (ABSENT) · 645 words · standard-owner precedent; authors from Lotus and Microsoft

**Batch C (2026-09-25, parallel; themed: security & compliance).** Verified from disk, `LINEAGE-OK (128 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder sections read for `software-supply-chain-security`, `grc-compliance-platforms`; no duplicate tools. Orchestrator fixed one metadata link format only (`cybersecurity-mssp` Builder in vault → wikilink).

- **cybersecurity-mssp** — tool: Counterpane's Sentry collection box and Socrates correlation system · builder: **Counterpane Internet Security** (in vault via its own industry) · 742 words · go-live date not established
- **grc-compliance-platforms** — tool: the Unified Compliance Framework (2005) · builder: **Network Frontiers** (ABSENT) · 694 words · Halpern's law firm conflicting
- **security-awareness-training** — tool: PhishGuru embedded-training phishing email · builder: **Carnegie Mellon University** (ABSENT) · 641 words · PhishMe founding not established
- **soc2-audit-firms** — tool: the CPA WebTrust seal and criteria (Sept 1997), ancestor of the Trust Services Criteria · builder: **AICPA** (ABSENT; existing key, now 3 industries) · 677 words · AICPA vs CICA origination and first SOC 2 guidance year not established
- **software-supply-chain-security** — tool: SPDX (2010 "Package Facts", v1.0 Aug 2011) · builder: **Linux Foundation** (ABSENT) · 664 words · **agent hit a 200-query WebSearch cap mid-note; note rests on direct fetches and says so**; 2010 convenor not established

**Batch A (2026-09-25, parallel; themed: specialty trades).** Verified from disk, `LINEAGE-OK (129 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `plumbing-contractors`; no duplicate tools.

- **electrical-contractors** — tool: NECA Manual of Labor Units (1923) · builder: **National Electrical Contractors Association** (ABSENT) · 729 words · compiler and derivation not established; NECA pages 403
- **hvac-contractors** — tool: ACCA Manual J, *Residential Load Calculation* · builder: **Air Conditioning Contractors of America** (ABSENT) · 713 words · first-edition year and pre-ACCA origin not established
- **painting-contractors** — tool: MPI Architectural Painting Specification Manual and Approved Products List · builder: **Master Painters and Decorators Association** (ABSENT) · 702 words · originator (BC association, mid-1960s) over MPI; 1967 vs late-1990s dating conflict flagged
- **plumbing-contractors** — tool: the fixture unit and Hunter's curve (NBS BMS 65, 1940) · builder: **National Bureau of Standards** (ABSENT) · 736 words · first code adoption of Hunter's tables not established
- **roofing-contractors** — tool: the EagleView roof measurement report (2008) · builder: **EagleView Technologies** (ABSENT) · 722 words · founding anecdote second-hand; patent and verdict appeal not checked

**Batch B (2026-09-25, parallel; themed: developer infrastructure).** Verified from disk, same run. Builder section read for `ci-cd-platforms`; no duplicate tools.

- **api-infrastructure-providers** — tool: the Swagger specification (OpenAPI from 2016) · builder: **Wordnik** (ABSENT) · 736 words · Wordnik's motive inferred
- **ci-cd-platforms** — tool: CruiseControl (30 Mar 2001) · builder: **ThoughtWorks** (in vault via `industries/software-dev-agencies`) · 741 words · Atlas origin and Foemmel authorship secondary only; AnthillPro 2001 from Wikipedia only
- **developer-tools-vendors** — tool: the Language Server Protocol (27 Jun 2016) · builder: **Microsoft** (ABSENT; existing key) · 722 words · TypeScript/OmniSharp predecessors secondary only
- **internal-developer-platforms** — tool: the Backstage software catalog and `catalog-info.yaml` · builder: **Spotify** (ABSENT) · 723 words · System Z's builder and YAML use not established
- **observability-vendors** — tool: the Dapper trace (Google TR dapper-2010-1, Apr 2010) · builder: **Google** (ABSENT) · 736 words · Dapper start year (~2008) and Zipkin June 2012 secondary only

**Batch E (2026-09-25, parallel; themed: property & real estate).** Verified from disk, `LINEAGE-OK (130 notes)`, `PHASE3-VERIFY-CLEAN`. Builder sections read for `proptech-platforms`, `hoa-management`; no duplicate tools; earlier over-band soft warnings fixed by the agent.

- **construction-tech-platforms** — tool: PlanGrid iPad sheet-set app · builder: **PlanGrid** (ABSENT) · 734 words · first ship date and first-release features not established
- **hoa-management** — tool: *The Homes Association Handbook*, ULI Technical Bulletin 50 (1964) · builder: **Urban Land Institute** (ABSENT) · 720 words · FHA's Byron Hanke principal author in body; 1963 FHA rule document not identified
- **home-inspection** — tool: the ASHI Standard of Practice (1977) · builder: **American Society of Home Inspectors** (ABSENT) · 734 words · 1977 wording not seen; Texas 1985 licensing secondary only
- **property-management** — tool: the Uniform Residential Landlord and Tenant Act (1972) · builder: **National Conference of Commissioners on Uniform State Laws** (ABSENT) · 718 words · build-time name; act text described via state enactments; WebSearch cap hit mid-note
- **proptech-platforms** — tool: RealPage's YieldStar rent-pricing engine · builder: **RealPage** (ABSENT) · 735 words · Camden origin software unnamed and undated, so key stays on RealPage

**Batch F (2026-09-25, parallel; themed: health & animal practices).** Verified from disk, `LINEAGE-OK (141 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `pet-services`; no duplicate tools. **Whole batch researched by direct page fetch only — the session's 200-query WebSearch cap was already exhausted; every note says so.**

- **acupuncture-practices** — tool: Medicare NCD 30.3.3, *Acupuncture for Chronic Low Back Pain* (21 Jan 2020) · builder: **Centers for Medicare & Medicaid Services** (ABSENT; new key, kept separate from build-time-era `Health Care Financing Administration`) · 745 words · CPT 97810–97814 creation year not established
- **chiropractic-practices** — tool: Medicare's subluxation-only chiropractic benefit (1972), P.A.R.T. and AT modifier · builder: **US Congress** (ABSENT; existing key) · 712 words · public-law number and X-ray-rule repeal statute not established
- **physical-therapy** — tool: the Medicare outpatient therapy cap (BBA 1997 §4541(c)) and KX modifier · builder: **US Congress** (ABSENT; existing key, now 6 industries) · 678 words · AT modifier and 8-minute rule dates not established
- **veterinary-practices** — tool: *Plumb's Veterinary Drug Handbook* (earliest found 1991) · builder: **Donald C. Plumb** (ABSENT) · 743 words · 1988 edition not found; PharmaVet ownership unknown
- **pet-services** — tool: the Dunbar Dog Bite Scale · builder: **Ian Dunbar** (ABSENT) · 745 words · publication date not established; Levels 4–6 from circulated text, not re-fetched

**Nomination gate fired (2026-09-25).** `US Congress` reached 6 industries across 5 waves (W2–W6) with `physical-therapy` — the first builder over the ≥5 / ≥2-wave gate. Logged only; no `origins/` entry is built without an owner decision.

**Batch I (2026-09-25, parallel; themed: games & media platforms).** Verified from disk, `LINEAGE-OK (150 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `game-porting-studios`; no duplicate tools. Researched by direct fetch only (WebSearch cap).

- **game-hosting-providers** — tool: Agones and its Allocated game-server state · builder: **Google** (ABSENT; existing key) · 728 words · why-them inferred
- **game-liveops-services** — tool: the battle pass, first shipped as the Dota 2 Compendium (May 2013) · builder: **Valve** (ABSENT; existing key) · 678 words · Compendium price and 2023 status not established
- **game-porting-studios** — tool: the 10NES lockout chip (US 4,799,635) and Nintendo pre-release approval · builder: **Nintendo** (ABSENT) · 665 words · Lotcheck/TRC/TCR dates not established (NDA)
- **no-code-app-builders** — tool: Microsoft Access 1.0 and the .mdb file (16 Nov 1992) · builder: **Microsoft** (ABSENT; existing key) · 657 words · price and early sales not established
- **streaming-video-platforms** — tool: HTTP Live Streaming and .m3u8 (Internet-Draft 1 May 2009) · builder: **Apple** (ABSENT) · 653 words · why-them inferred; App Store HLS rule not confirmed

**Batch G (2026-09-25, parallel; themed: fintech).** Verified from disk, `LINEAGE-OK (155 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `neobanks`; no duplicate tools. Researched by fetch of primary documents only (WebSearch cap).

- **bnpl-providers** — tool: Afterpay's "pay in 4" · builder: **Afterpay** (in vault via its own industry) · 738 words · "first" and Reg Z intent not established
- **crypto-exchanges** — tool: the Chainalysis address cluster (common-input heuristic, labelled and risk-scored) · builder: **Chainalysis** (ABSENT) · 732 words · Reactor/KYT launch dates not established
- **embedded-finance-platforms** — tool: Marqeta Just-in-Time Funding · builder: **Marqeta** (in vault via its own industry) · 739 words · JIT launch date not established
- **neobanks** — tool: the Durbin Amendment small-issuer exemption, 15 U.S.C. § 1693o-2 · builder: **US Congress** (ABSENT; existing key, now 7 industries) · 744 words · legislative intent behind the $10B line not established
- **robo-advisors** — tool: SEC Rule 3a-4 (1997) and its client profile · builder: **Securities and Exchange Commission** (ABSENT; new key) · 713 words · adopting release number not found

**Batch J (2026-09-25, parallel; themed: HR & workplace).** Verified from disk, `LINEAGE-OK (155 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `talent-assessment-platforms`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **corporate-training** — tool: the Kirkpatrick four levels · builder: **Donald Kirkpatrick** (ABSENT) · 710 words · 1959 article titles/journal and his employer not established
- **hr-consultants** — tool: the Hay Guide Chart-Profile Method · builder: **Hay Group** (ABSENT) · 745 words · firm's 1943–51 name not established (possible build-time-name exception); 1951 date single secondary source
- **hr-tech-platforms** — tool: the ASC X12 834 benefit enrollment transaction (HIPAA v4010, 2000) · builder: **ASC X12** (ABSENT; existing key, now 3 industries) · 694 words · first publication year and drafter not established
- **talent-assessment-platforms** — tool: the four-fifths rule, 29 CFR 1607.4(D) · builder: **California Fair Employment Practice Commission** (ABSENT) · 725 words · originator (1972 TACT guidelines) over the 1978 federal Uniform Guidelines; panel members not established; single Wikipedia account
- **work-collaboration-tools** — tool: Basecamp (5 Feb 2004) · builder: **37signals** (ABSENT) · 695 words · build-time name; launch price not established

**Batch H (2026-09-25, parallel; themed: commerce & fintech ops).** Verified from disk, `LINEAGE-OK (155 notes)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `insurtech-platforms`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **ecommerce-aggregators** — tool: Fulfillment by Amazon (19 Sep 2006) · builder: **Amazon** (ABSENT; existing key, now 4 industries in W5–W6) · 743 words · aggregator founders/dates not established
- **headless-commerce-vendors** — tool: the commercetools API-only commerce platform (2013) · builder: **commercetools** (in vault via its own industry) · 726 words · founding 2006 vs 2010
- **insurtech-platforms** — tool: SERFF rate-and-form filing system · builder: **National Association of Insurance Commissioners** (ABSENT) · 712 words · conception date, first filing, internal lead not established
- **spend-management-platforms** — tool: the Brex corporate card · builder: **Brex** (in vault via its own industry) · 738 words · launch month not confirmed
- **subscription-commerce** — tool: the Recharge subscriptions app for Shopify · builder: **Recharge** (ABSENT) · 699 words · origin story and Shopify Subscription API date not established

**Batch L (2026-09-25, parallel; themed: cloud & IT services).** Verified from disk, `LINEAGE-OK (164 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `it-managed-services`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **cloud-cost-management** — tool: the AWS cost allocation tag · builder: **Amazon** (ABSENT; existing key) · launch date (likely 2012) not established
- **cloud-infrastructure-consultants** — tool: the AWS Well-Architected Framework (2 Oct 2015) and Tool (29 Nov 2018) · builder: **Amazon** (ABSENT; existing key) · 720 words · pillar-addition and partner-programme dates not established
- **it-managed-services** — tool: ConnectWise's PSA · builder: **ConnectWise** (ABSENT) · 735 words · own-shop origin story unconfirmed; first ship year not established
- **open-source-commercial-vendors** — tool: the Server Side Public License v1 (16 Oct 2018) · builder: **MongoDB** (in vault via its own industry) · 712 words · drafters not established
- **qa-test-automation-vendors** — tool: Selenium, first "JavaScriptTestRunner" (2004) · builder: **ThoughtWorks** (in vault via `industries/software-dev-agencies`; existing key) · 727 words · WebDriver start year not established

**Second nomination (2026-09-25).** `Amazon` reached 6 industries across W5–W6 with the two AWS notes above — over the ≥5 / ≥2-wave gate. Logged only.

**Batch K (2026-09-25, parallel; themed: SaaS go-to-market).** Verified from disk, `LINEAGE-OK (166 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. `contract-lifecycle-platforms` read through its builder section; no duplicate tools. Researched by fetch/EDGAR only (WebSearch cap).

- **contract-lifecycle-platforms** — tool: CUAD, the Contract Understanding Atticus Dataset (2021) · builder: **The Atticus Project** (ABSENT) · 707 words · **weakest tool choice of the wave** — a 2021 benchmark rather than an artefact the industry was built on; agent dropped CompareRite/DeltaView for lack of a builder or date. Atticus founders/date not established
- **crm-platforms** — tool: the ACT! contact manager (1 Apr 1987) · builder: **Conductor Software** (in vault via its own industry) · Conductor vs "Contact Software" naming conflict flagged
- **customer-support-platforms** — tool: the KCS article (Knowledge-Centered Support) · builder: **Customer Support Consortium** (ABSENT) · build-time name (Jan 1997 incorporation); rename date not established
- **revops-consultancies** — tool: the SiriusDecisions Demand Waterfall · builder: **SiriusDecisions** (ABSENT) · 2006 (firm) vs 2005 (Wikipedia)
- **saas-implementation-partners** — tool: the Salesforce Sandbox · builder: **salesforce.com** (in vault via `industries/crm-platforms`) · build-time name; earliest source a 10-K of 15 Mar 2006

**Batch M (2026-09-25, parallel; themed: tech-enabled services).** Verified from disk, `LINEAGE-OK (177 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `freight-tech-platforms`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **developer-relations-agencies** — tool: the Orbit Model (orbit levels and gravity) · builder: **Orbit** (ABSENT) · start 2014 vs 2016; Postman acquisition date self-reported
- **fractional-cto-services** — tool: the Joel Test (9 Aug 2000) · builder: **Joel Spolsky** (ABSENT) · named individual (own byline); Fog Creek founding month not established
- **freight-tech-platforms** — tool: MacroPoint's per-load tracking feed replacing the check call · builder: **MacroPoint** (in vault via its own industry) · founders, founding year, first product date not established
- **restaurant-tech-platforms** — tool: the OpenTable Electronic Reservation Book · builder: **OpenTable** (in vault via its own industry) · first installation date not established
- **technical-content-agencies** — tool: DITA · builder: **IBM** (ABSENT; existing key, now 4 industries) · paper date 2001 vs 2003

**Batch Q (2026-09-25, parallel; 3 remaining W6 industries).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `catering-companies`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **agtech-platforms** — tool: Ag Leader's on-the-go combine yield monitor (1992) · builder: **Ag Leader Technology** (ABSENT) · model name, sensor design, Al Myers' employer and "first" claim not established
- **alterations-tailoring** — tool: no single tool (Rail 2: NBS CS 215-58 standard sizes, 1958, on the O'Brien–Shelton survey) · builder: **no single builder** (n/a) · survey years and USDA publication number not established; dress form and price-list origins not traced
- **catering-companies** — tool: Sterno canned heat · builder: **S. Sternau & Co.** (ABSENT) · first sale year, Colgate-Palmolive acquisition, caterer adoption not established

**Parallel window closing (2026-09-25 17:42).** Last parallel launch was W7 health batch. From here: let running agents finish; launch new batches only while ≤1 other agent is running (owner: "revert to a single or max 2 agents").

**Batch P (2026-09-25, parallel; themed: legal & social services).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `public-defenders`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **funeral-homes** — tool: the FTC Funeral Rule General Price List (16 CFR 453, eff. 30 Apr 1984) · builder: **Federal Trade Commission** (ABSENT) · investigation start and original FR cite not established
- **immigration-law** — tool: the Visa Bulletin · builder: **US Department of State** (ABSENT) · first issue and Dates-for-Filing start not established
- **legal-practice-software** — tool: LEDES 1998B e-billing file with UTBMS codes · builder: **LEDES Oversight Committee** (ABSENT) · UTBMS first-publication year and Price Waterhouse leads not established
- **nonprofits-social-services** — tool: HUD's HMIS Data and Technical Standards (30 Jul 2004) · builder: **US Department of Housing and Urban Development** (ABSENT) · later revisions and VAWA restriction not traced
- **public-defenders** — tool: NAC Standard 13.12 caseload limits (1973) · builder: **Law Enforcement Assistance Administration** (ABSENT) · commission's name exceeds the 60-char key; keyed to its parent body; derivation of the numbers not established

**Batch O (2026-09-25, parallel; themed: community & education).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `k12-private-schools`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **childcare-centers** — tool: ECERS, Early Childhood Environment Rating Scale (Harms & Clifford, 1980) · builder: **Frank Porter Graham Child Development Institute** (ABSENT) · authors' 1980 affiliation not confirmed
- **faith-organizations** — tool: the CCLI Church Copyright License · builder: **Christian Copyright Licensing International** (ABSENT) · SESAC acquisition date not established
- **k12-private-schools** — tool: the SSS Parents' Financial Statement and shared need analysis · builder: **unknown — searched, not established** (n/a) · originator an unnamed mid-1950s boarding-school coalition; NAIS (1968) is the inheritor, not the key
- **tutoring-centers** — tool: the Kumon small-step worksheet · builder: **Toru Kumon** (ABSENT) · named individual; company dates (1955/1974) used over Wikipedia's (1958/1983)
- **youth-sports-orgs** — tool: the Volunteer Protection Act of 1997 (PL 105-19) · builder: **US Congress** (ABSENT; existing key, now 8 industries) · sponsorship from Wikipedia only

---

## Stage 7 — Wave 7, Big Data

**Batch A (2026-09-25, parallel; themed: data platforms).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `data-platform-integrators`; no duplicate tools. Researched by fetch, GitHub API and HN API only (WebSearch cap).

- **bi-analytics-platforms** — tool: the Business Objects universe semantic layer (US 5,555,403, filed 1991) · builder: **Business Objects** (in vault via its own industry) · first ship 1990 vs 1991
- **customer-data-platforms** — tool: analytics.js (HN launch 12 Dec 2012) · builder: **Segment.io** (in vault via its own industry) · build-time name; co-founders and rename date not established
- **data-analytics-consultants** — tool: CRISP-DM 1.0 (Aug 2000) · builder: **CRISP-DM consortium** (ABSENT)
- **data-marketplace-brokers** — tool: Snowflake Secure Data Sharing "share" object · builder: **Snowflake Computing** (in vault via `industries/database-platform-vendors`) · launch date and designer not established
- **data-platform-integrators** — tool: dbt and `ref()` (first commit 10 Mar 2016) · builder: **RJMetrics** (in vault via `industries/bi-analytics-platforms`) · originator over Fishtown Analytics; hand-off not established

**Batch N (2026-09-25, parallel; themed: home & site services).** Verified from disk, `LINEAGE-OK (196 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `security-guard-firms`; no duplicate tools. Researched by fetch, Federal Register API and Wayback only (WebSearch cap).

- **cleaning-companies** — tool: The Official ISSA Cleaning Times workloading table · builder: **ISSA** (ABSENT) · first edition and compiler not established
- **landscaping** — tool: the ChemLawn season-subscription lawn programme · builder: **ChemLawn** (in vault via its own industry) · original method, visit count, "first" not established; why-them labelled inference
- **pest-control** — tool: NPMA-33 Wood Destroying Insect Inspection Report · builder: **National Pest Management Association** (ABSENT) · first-issue year and NPCA→NPMA rename date not established — possible build-time-name exception
- **security-guard-firms** — tool: the Detex Newman watchman's clock and keyed stations · builder: **Detex** (ABSENT) · keyed to the product's maker; 1878 firm name and fire-insurer mandate not established
- **solar-installers** — tool: PVWATTS calculator · builder: **National Renewable Energy Laboratory** (ABSENT) · build-time name (renamed 1 Dec 2025 per Wikipedia); pre-2000 release date and developers not established

---

## Stage 6 gate — Wave 6 complete, 188 of 250

**Set 2026-09-25; record-and-continue under standing approval.** 83 industries in 17 themed batches, run up to 6 at a time under the owner's time-boxed authorisation. No duplicate tools after the claims directory was introduced.

### Finding 1 — Cloud & SaaS keeps the company majority, but the state is back

| Kind | W6 |
|---|---|
| Company | 45 |
| Trade association / standards body / SRO | 15 |
| Government / legislature / regulator | 13 |
| Named individuals | 5 |
| University / research nonprofit | 3 |
| No single builder | 1 |
| Unknown | 1 |

Half the SaaS-era tools are company products (Mindbody, Brex, Marqeta, RealPage, Basecamp). But the local-service and practice industries in this wave (chiropractic, PT, funeral homes, immigration law, public defenders, youth sports, solar) were shaped by a statute, rule or federal lab, not by software. The software came later and runs on the government's form.

### Finding 2 — nominations

`US Congress` 8 industries (W2–W6) and `Amazon` 6 (W5–W6) are over the ≥5 / ≥2-wave gate. `IBM` 4 across W1/W4/W5/W6 and `ASC X12`, `AICPA` 3 each are next. No `origins/` entry built — owner decision.

### Finding 3 — research quality dropped mid-wave

The session's 200-query WebSearch cap was exhausted during Wave 6 batch C. From then on every note was researched by direct fetch of known URLs (Wikipedia, eCFR/CMS manuals, EDGAR, GitHub/HN APIs, Wayback) and says so in Sources. The notes still meet the rails and carry explicit negative findings, but more of them rest on a single secondary source (often Wikipedia) and more dates are left open. **Recommend a spot re-check of W6–W7 notes with search restored.**

### Finding 4 — named individuals and precedents

Five individual keys this wave (Kumon, Spolsky, Dunbar, Kirkpatrick, Plumb). New build-time-name cases: `salesforce.com`, `Segment.io`, `37signals`, `American Billing Company`, `National Renewable Energy Laboratory`. Possible exceptions flagged in-file where the rename date was not found: `Hay Group`, `National Pest Management Association`.

### Finding 5 — weakest tool

`contract-lifecycle-platforms` (CUAD, a 2021 ML benchmark) is the one tool choice that does not read as an artefact the industry was built on. Candidate for re-do.

**Batch B (2026-09-25; themed: health delivery).** Verified from disk, `LINEAGE-OK (199 notes, incl. in-flight)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `behavioral-health-clinics`; no duplicate tools; earlier over-band soft warnings fixed by the agent. Researched by fetch only (WebSearch cap).

- **behavioral-health-clinics** — tool: the PHQ-9 depression scale · builder: **Pfizer** (ABSENT) · funder and copyright holder; Zoloft motive labelled inference
- **healthcare-practice-software** — tool: Medicare's NCCI code-pair edits (Jan 1996) · builder: **Health Care Financing Administration** (ABSENT; existing key) · building contractor not established
- **home-health-agencies** — tool: OASIS home health assessment (Univ. of Colorado under 1988 contract; mandatory 1999) · builder: **Health Care Financing Administration** (ABSENT; existing key, now 3 industries) · Colorado leads not confirmed
- **urgent-care** — tool: Place of Service code 20, "Urgent Care Facility" (1 Jan 2003) · builder: **Centers for Medicare & Medicaid Services** (ABSENT; existing key) · who requested the code and final payment rate not established

**Batch C (2026-09-25; themed: analytics, fraud & threat intel).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `payment-fraud-vendors`; no duplicate tools. Researched by fetch, Wayback, EDGAR and Crossref/OpenAlex only (WebSearch cap).

- **game-analytics-vendors** — tool: the GameAnalytics SDK and fixed event types · builder: **GameAnalytics** (in vault via its own industry) · event-type introduction dates not established
- **mlops-platforms** — tool: the Michelangelo feature store (Uber blog, 5 Sep 2017) · builder: **Uber** (ABSENT) · earlier use of "feature store" and Tecton link not established
- **payment-fraud-vendors** — tool: HNC Software's Falcon neural-network fraud system · builder: **HNC Software** (in vault via its own industry) · launch year 1992 vs 1993, first customer, issuer consortium not established
- **player-research-firms** — tool: Microsoft Game Studios' TRUE instrumentation (CHI 2008) · builder: **Microsoft** (ABSENT; existing key, now 4 industries) · paper paywalled; case-study games not confirmed
- **threat-intelligence-vendors** — tool: STIX with TAXII · builder: **MITRE** (ABSENT) · DHS sponsor case noted; STIX 1.0 date not established

---

## Stage 7 gate — Wave 7 complete, 202 of 250

**Set 2026-09-25; record-and-continue.** 14 industries in 3 batches, all researched without WebSearch. Builders: companies 9 (Business Objects, Segment.io, Snowflake, RJMetrics, Pfizer, GameAnalytics, Uber, HNC, Microsoft); government 3 (HCFA ×2, CMS); consortia/standards 2 (CRISP-DM consortium, MITRE). No `unknown`. The big-data wave's artefacts are schemas and semantic layers (universe, `ref()`, feature store, STIX) — each fixes a vocabulary so data from many sources can be joined. Health artefacts remain federal billing codes and assessments.

---

## Stage 8 — Wave 8, Mobile & GPS

**Batch 1 (2026-09-25; themed: vehicle operators).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `rideshare-fleet-operators`; no duplicate tools. Researched by fetch of Wikipedia, EDGAR, govinfo, LII, Google Patents, CourtListener (WebSearch cap).

- **fleet-managers** — tool: Qualcomm OmniTRACS in-cab satellite terminal (1988) · builder: **Qualcomm** (ABSENT) · first Schneider order and sale date not established
- **non-emergency-medical-transport** — tool: the Medicaid NEMT brokerage contract (SSA §1902(a)(70), DRA 2005 §6083) · builder: **US Congress** (ABSENT; existing key, now 9 industries) · first waiver broker state not established
- **owner-operator-trucking** — tool: the ELD rule, 49 CFR 395 Subpart B (Dec 2015) · builder: **Federal Motor Carrier Safety Administration** (ABSENT; new key — a regulation keyed to its agency, MAP-21 mandate in body) · first 1988 recorder's maker not established
- **rideshare-fleet-operators** — tool: Xchange Leasing, Uber's driver car-leasing subsidiary (2016–2018) · builder: **Uber** (ABSENT; existing key) · launch date and buyer not established; a programme more than an artefact — borderline Rail 1
- **towing-companies** — tool: the Holmes twin-boom wrecker (US 1,254,804, 1918) · builder: **Ernest Holmes** (ABSENT) · named individual on the patents; origin anecdote secondary only

**Batch 2 (2026-09-25; themed: delivery & logistics).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `cold-chain-logistics`; no duplicate tools. Researched by fetch, EDGAR and Internet Archive (WebSearch cap).

- **cold-chain-logistics** — tool: the engine-driven truck refrigeration unit (Numero & Jones, US 2,303,857) sold as the Thermo King · builder: **U.S. Thermo Control Company** (ABSENT) · build-time name; founding 1938 vs 1939; origin anecdote unverified
- **field-service-software** — tool: the ServiceTitan platform (2012) · builder: **ServiceTitan** (ABSENT) · incorporated 2007 as LinxLogic, renamed 2014 — possible build-time-name exception, flagged in-file
- **food-trucks** — tool: no single tool (Rail 2; Kogi BBQ's 2008 Twitter location posts lead the table) · builder: **no single builder** (n/a) · first location tweet date not established
- **gig-delivery-platforms** — tool: PaloAltoDelivery.com (12 Jan 2013) · builder: **Palo Alto Delivery** (ABSENT) · build-time name per DoorDash S-1
- **last-mile-delivery** — tool: UPS ORION route optimisation · builder: **UPS** (in vault via `origins/package-carriers`) · project leads not established

**Batch 4 (2026-09-25; themed: field & land).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `land-surveyors`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **crop-farming** — tool: John Deere StarFire satellite GPS correction (1998) · builder: **Deere & Company** (ABSENT) · AutoTrac date, Stanford lead, SA shut-off date not established
- **land-surveyors** — tool: the State Plane Coordinate System (Serial No. 562, 1933) · builder: **US Coast and Geodetic Survey** (ABSENT) · build-time name; NC requester and state adoption laws not established; OPUS dropped for lack of a launch date

**Batch 3 (2026-09-25; themed: mobile apps & brands).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `app-marketing-firms`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **app-marketing-firms** — tool: the Advertising Identifier (IDFA), iOS 6 (19 Sep 2012) · builder: **Apple** (ABSENT; existing key) · designers and SKAdNetwork first iOS version not established
- **d2c-brand-operators** — tool: Shopify and Liquid (opened to merchants June 2006) · builder: **Shopify** (ABSENT) · build-time name "Jaded Pixel" unconfirmed (uncited Wikipedia) so keyed `Shopify`; agent switched from Lookalike Audiences for lack of a primary source
- **mobile-game-publishers** — tool: StoreKit In App Purchase opened to free apps (15 Oct 2009) · builder: **Apple** (ABSENT; existing key, now 3 industries) · designers not established
- **product-design-studios** — tool: Sketch and the `.sketch` format (7 Sep 2010) · builder: **Bohemian Coding** (ABSENT) · founders and Symbols date not confirmed; business case inferred

---

## Stage 8 gate — Wave 8 complete, 218 of 250

**Set 2026-09-25; record-and-continue.** 16 industries in 4 batches, all fetch-only. Builders: companies 10 (Qualcomm, Uber, U.S. Thermo Control, ServiceTitan, Palo Alto Delivery, UPS, Deere, Apple ×2, Shopify, Bohemian Coding — 11 notes), government 3 (US Congress, FMCSA, US Coast and Geodetic Survey), named individual 1 (Ernest Holmes), no single builder 1 (food trucks). No `unknown`. The Mobile & GPS wave's artefacts split between **positioning** (OmniTRACS, StarFire, State Plane, ORION, ELD) and **platform gates** (IDFA, StoreKit IAP) — the phone platform owner, not the app industry, set the terms. `US Congress` now 9 industries; `Apple` 4.

---

## Stage 9 — Wave 9, Programmatic

**Batch A (2026-09-25; themed: ad measurement).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. No duplicate tools. Researched by fetch only (WebSearch cap). **Orchestrator re-keyed one note** (`marketing-attribution-vendors` `Meta` → `Facebook`, build-time name) with a keying note in its Sources.

- **audio-adtech-networks** — tool: the IAB podcast download-counting rule (Podcast Measurement Technical Guidelines v1.0, 6 Sep 2016) · builder: **IAB Tech Lab** (ABSENT) · first certification date not established
- **game-user-acquisition-firms** — tool: SKAdNetwork's signed install postback (iOS 11.3, 29 Mar 2018) and iOS 14 conversion value · builder: **Apple** (ABSENT; existing key, now 4 industries across W6–W9) · motive and designers not established
- **marketing-attribution-vendors** — tool: Robyn, open-source marketing-mix modelling (first commit 1 Oct 2020) · builder: **Facebook** (ABSENT) · launch and CRAN dates not established; ATT link inferred

**Batch B (2026-09-25; themed: programmatic & privacy).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. No duplicate tools. Researched by fetch only (WebSearch cap; Internet Archive offline).

- **privacy-tech-vendors** — tool: IAB Europe's TCF consent string (TC String) · builder: **IAB Europe** (ABSENT) · CJEU C-604/22 date and holding not established
- **programmatic-ad-platforms** — tool: the OpenRTB bid request/response · builder: **IAB Tech Lab** (ABSENT) · **open keying question:** started Nov 2010 by six companies, bid protocol proposed by Nexage, adopted by IAB Jan 2012 — standard-owner precedent gives the IAB, but IAB Tech Lab did not exist until later, so the build-time key may be `Interactive Advertising Bureau`. Drafters not established
- **retail-media-networks** — tool: Amazon Sponsored Products and ACoS · builder: **Amazon** (ABSENT; existing key) · launch year and designer not established

---

## Stage 9 gate — Wave 9 complete, 224 of 250

**Set 2026-09-25; record-and-continue.** 6 industries in 2 batches, fetch-only. Builders: standards bodies 3 (IAB Tech Lab ×2, IAB Europe), platforms 3 (Apple, Facebook, Amazon). The programmatic wave is the clearest split in the sweep: **the trade body writes the pipe (OpenRTB, TCF, podcast counting), the walled garden writes its own rules (SKAdNetwork, Sponsored Products, Robyn)**. Open question for the owner: `IAB Tech Lab` vs build-time `Interactive Advertising Bureau` for 2012 OpenRTB.

---

## Stage 10 — Wave 10, Creator Platform

**Batch A (2026-09-25; themed: creator media & representation).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `podcasting-networks`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **creator-businesses** — tool: the YouTube Partner Program (widened Dec 2007; 1,000 subs / 4,000 hours from Jan 2018) · builder: **YouTube** (ABSENT) · invite-only start and 55% share not confirmed
- **creator-talent-agencies** — tool: the California talent agency licence (Labor Code §§1700–1700.54) · builder: **California Legislature** (ABSENT) · pre-1959 statutes and *Marathon v. Blasi* holding not established
- **influencer-marketing-platforms** — tool: FTC Endorsement Guides disclosure rule, 16 CFR 255.5 (Oct 2009) · builder: **Federal Trade Commission** (ABSENT; existing key) · FR citations not established
- **newsletter-media** — tool: the Substack paid newsletter (18 Jul 2017) · builder: **Substack** (ABSENT) · launch fee, processor, export not established
- **podcasting-networks** — tool: the RSS `<enclosure>` element (RSS 0.92, Dec 2000) · builder: **UserLand Software** (ABSENT) · exact release day and Winer's motive not established

**Batch B (2026-09-25; themed: platforms for creators).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. `ugc-video-platforms` read through its builder section; no duplicate tools. Researched by fetch only (WebSearch cap; Internet Archive offline).

- **live-commerce-platforms** — tool: the Home Shopping Club live phone-order channel (1982 local, 1985 national) · builder: **Home Shopping Network** (ABSENT) · build-time name may be Home Shopping Club — possible exception; GTE suit years not established
- **membership-community-platforms** — tool: Discourse trust levels TL0–TL4 · builder: **Civilized Discourse Construction Kit** (in vault via its own industry) · first-ship date and Stack Exchange lineage not established
- **online-course-platforms** — tool: Coursera Signature Track (verified paid certificate) · builder: **Coursera** (in vault via its own industry) · Jan 2013 launch and ID-check method not confirmed (sources 404)
- **trust-safety-tooling-vendors** — tool: Perspective API TOXICITY score (June 2017) · builder: **Jigsaw** (ABSENT) · builders' names not established
- **ugc-video-platforms** — tool: YouTube Content ID · builder: **Google** (ABSENT; existing key) · launch June 2007 / Oct 2007 / early 2008 conflict. **Keying split flagged:** `creator-businesses` keys the 2007 Partner Program to `YouTube`, this note keys 2007 Content ID to `Google` (argued as the acquirer answering the Viacom suit). Same entity-era, two keys — owner ruling needed

**Batch C (2026-09-25; themed: performers, studios & game economies).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `tattoo-studios`; no duplicate tools. Researched by fetch only (WebSearch cap).

- **esports-organizations** — tool: the LCS franchise slot (June 2017, from 2018) · builder: **Riot Games** (ABSENT) · terms from Wikipedia only
- **personal-trainers** — tool: IHRSA's Jan 2006 NCCA-accredited-certification recommendation · builder: **IHRSA** (ABSENT) · Wikipedia only; founding dates not established
- **tattoo-studios** — tool: the electric tattooing machine, US 464,801 (1891) · builder: **Samuel O'Reilly** (ABSENT) · named individual on the patent; later coil-machine patents not traced
- **virtual-economy-operators** — tool: Steam Community Market (Dec 2012 beta) · builder: **Valve** (ABSENT; existing key, now 3 industries) · fee split unsourced; beta day not established

---

## Stage 10 gate — Wave 10 complete, 238 of 250

**Set 2026-09-25; record-and-continue.** 14 industries in 3 batches, fetch-only. Builders: platforms/companies 9 (YouTube, Substack, UserLand, Home Shopping Network, Civilized Discourse Construction Kit, Coursera, Jigsaw, Google, Riot, Valve — 10 notes), government 2 (California Legislature, FTC), trade body 1 (IHRSA), named individual 1 (Samuel O'Reilly). No `unknown`. The creator economy's artefacts are **platform rulebooks** — payout thresholds, trust levels, franchise slots, match-and-monetise — with the state appearing only as disclosure (FTC) and licensing (California). Open keying split: `YouTube` vs `Google` for 2007 YouTube products.

---

## Stage 11 — Wave 11, COVID Dislocation

**Batch 1 (2026-09-25).** Verified from disk, `LINEAGE-OK (242 notes)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `remote-work-infrastructure`; no duplicate tools; earlier over-band soft warnings fixed by the agent. Researched by fetch only (WebSearch cap; Wayback unreachable).

- **online-tutoring-platforms** — tool: Preply's tutor commission schedule (100% of trial, then 33%→18%) · builder: **Preply** (ABSENT) · introduction date not established
- **remote-work-infrastructure** — tool: the global employer-of-record arrangement · builder: **unknown — searched, not established** (n/a) · dated ancestor table; first cross-border EOR and Globalization Partners' founding not established
- **telehealth-platforms** — tool: OCR's telehealth Notification of Enforcement Discretion (eff. 17 Mar 2020) · builder: **HHS Office for Civil Rights** (ABSENT; new key)
- **virtual-assistant-services** — tool: no single tool (Rail 2; Gmail mail delegation as the chief borrowed artefact) · builder: **no single builder** (n/a) · delegation launch date and motive not established

## Stage 11 gate — Wave 11 complete, 242 of 250

**Set 2026-09-25; record-and-continue.** 4 industries. The COVID wave built almost nothing new: one enforcement-discretion notice (the state suspending its own rule), one commission schedule, and two industries whose core artefact is borrowed or unattributable (EOR `unknown`, VA `no single builder`). Dislocation moved existing tools into new hands rather than creating tools.

---

## Stage 12 — Wave 12, Transformers

**Batch B (2026-09-25; themed: evaluation, red-teaming & data).** Verified from disk, `LINEAGE-OK`, `PHASE3-VERIFY-CLEAN`. Builder section read for `data-labeling-services`; no duplicate tools. Researched by fetch only.

- **ai-model-evaluation-firms** — tool: Chatbot Arena pairwise-vote Elo leaderboard (3 May 2023) · builder: **LMSYS Org** (ABSENT) · Wikipedia's 24 Apr 2023 date and creator list conflict with the LMSYS post
- **ai-red-teaming-firms** — tool: MITRE ATLAS, formerly the Adversarial ML Threat Matrix (22 Oct 2020) · builder: **MITRE** (ABSENT; existing key, now 2 industries) · MITRE/Microsoft design split not established
- **data-labeling-services** — tool: the Dawid–Skene annotator-error model (JRSS C, 1979) · builder: **Dawid & Skene** (ABSENT) · named-individuals precedent; clinical study behind it not identified
- **synthetic-data-providers** — tool: the Synthetic Data Vault (IEEE DSAA, Oct 2016) · builder: **Massachusetts Institute of Technology** (ABSENT; new key) · paper not read (404/paywall); privacy claims and licence change not established

**Batch A (2026-09-25; themed: LLM stack).** Verified from disk, `LINEAGE-OK (250 notes)`, `PHASE3-VERIFY-CLEAN`. Builder section read for `llm-application-tooling`; no duplicate tools. Researched by fetch, GitHub API, PyPI and arXiv only.

- **ai-agent-platforms** — tool: OpenAI function calling (13 Jun 2023; `tools` from 6 Nov 2023) · builder: **OpenAI** (ABSENT) · designers and plugins alpha date not established; post read via reader proxy after 403
- **ai-inference-providers** — tool: vLLM / PagedAttention (20 Jun 2023) · builder: **University of California Berkeley** (ABSENT) · GPU funding not established
- **llm-application-tooling** — tool: LangChain's `Prompt` + `LLMChain` (first commit 24 Oct 2022) · builder: **Harrison Chase** (ABSENT) · named individual, no firm at build time
- **vector-search-vendors** — tool: FAISS `Index` (first commit 22 Feb 2017) · builder: **Facebook** (ABSENT; build-time name) · first production use not established

## Stage 12 gate — Wave 12 complete. SWEEP COMPLETE: 250 of 250

**Set 2026-09-25.** Wave 12's eight builders are almost all research labs and individuals (UC Berkeley, MIT, LMSYS, Dawid & Skene, Harrison Chase, MITRE) plus two model/platform companies (OpenAI, Facebook) — the transformer era's tools started as papers and first commits, not products.

### Final tally

- **250 notes**, `LINEAGE-OK (250 notes)`, `PHASE3-VERIFY-CLEAN`, no duplicate tools.
- **198 distinct builder keys.** 205 notes ABSENT from the vault; the rest point at an existing industry/origin or are `n/a`.
- **4 `unknown`** (streamshare pool, open pixel, SSS financial-aid form, global EOR) and **9 `no single builder`**.
- **Nominations fired (≥5 industries, ≥2 waves):** `US Congress` (9, W2–W8) and `Amazon` (7, W5–W9). Next tier at 4: `Apple`, `IBM`, `Microsoft`.

### The shape, end to end

Waves 1–4: consortia and standards bodies build the tools. Wave 5 onward: companies do, and the state returns wherever it is the payer or regulator (Medicare codes, FTC rules, statutes). No vendor class dominates; the only builders with enough reach to be nominated are **the legislature** and **one platform company**.

### Open items for the owner

1. Build `origins/` entries for `US Congress` and/or `Amazon`? (Nothing built without a decision.)
2. Keying rulings: `Fannie Mae` vs `Fannie Mae & Freddie Mac`; `YouTube` vs `Google` (2007); `IAB Tech Lab` vs `Interactive Advertising Bureau` (2012 OpenRTB); possible build-time exceptions flagged in-file (`IICRC`, `Hay Group`, `National Pest Management Association`, `ServiceTitan`, `Home Shopping Network`, `ACCSC`).
3. Possible key moves: `digital-forensics-firms` (ASR Data), `contract-lifecycle-platforms` (weak tool — CUAD).
4. **Research-quality re-check:** from W6 batch C onward (~120 notes) research was fetch-only after the session's 200-query WebSearch cap. A spot audit with search restored is recommended.
