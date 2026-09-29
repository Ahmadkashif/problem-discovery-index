# Assessment — Is the Vault Rich Enough to Build the Series From?

**Date:** 2026-09-21
**Question asked:** *Will adding more industries and niches help build a more cohesive understanding and a smoother story? Does the story have unexplained gaps?*
**Answer in one line:** The vault has far more material than a season needs; the series' gap is **not** in industries or niches but in a layer that does not exist yet — every entity in the vault is a *buyer* of computing and nothing in it *sells* computing — and separately, the vault-as-prospecting-index has seven real industry holes that do not block a single episode.

---

## 1. The verdict, stated properly

The question has three parts and they do not get the same answer.

| Question | Answer |
|---|---|
| Is there enough material? | **Yes, comfortably.** 18 origins + 66 history notes + 12 era notes + 40 failures. A first season is ~12 episodes. **No expansion is justified on volume**, and none is proposed on those grounds. |
| Should more **industries** be added *for the series*? | **One, not seven.** The series' gap is not in `industries/`; putting it there costs ~24,000 words of prospecting material per entry for companies you will never sell to. The single exception is argued in §9. |
| Should more **niches** be added? | **No — none.** 3,794 niche directories exist and all 66 history notes already close on them (347 links). Nothing in the diagnostic points at niche coverage. This is the clearest negative in the assessment. |
| Is there a real gap for the series? | **Yes — one, with several faces.** It belongs in `origins/`, costs ~2,900 words per entry, and six entries close it. |
| Anything else? | **Yes, and it is a different project.** Seven genuine industry absences that serve the vault's *original prospecting purpose*, not the series. Recorded in §9 so they are not lost, and deliberately **not** folded into the series build. |

The honest shape of this is: **one real gap for the series, and the fix is smaller than you asked about — plus a separate finding you did not ask about, kept separate.**

---

## 2. Method — the chain test

Per the brief, a gap is a place where the chain breaks:

> *A mechanic exists → because a business needed it → that business existed because of an earlier mechanic → …*

I drafted candidate episodes as the owner specified them — **tech-first**, starting from an artefact the audience already touches — and tried to walk each chain backwards through the vault. Where I had to say *"and then somehow…"*, I recorded a break, then grepped all 13,346 files to confirm the break was real and not a naming miss.

**Calibration note:** raw mention counts are useless here. The vault's own audit found it well: *"every scar and no wounds."* "Prior authorization" appears in **65** files — all present-tense pain, none of it origin. So the test is **ownership**: is there a file whose *subject* is the mechanic, with a dated event, a named fight, and an explained mechanism?

---

## 3. What is already strong — and should not be touched

This matters because it bounds the recommendation.

- **`origins/airlines/the-mechanism.md` is the template and it is excellent.** It takes one commercial question, turns it into a modelling problem, gives Littlewood's actual decision rule, and states what was traded away (price fairness, deliberately). Its closing line — *"the algorithm was the cheap part, the data infrastructure was the moat"* — is the series' best sentence.
- **The history layer carries time properly.** 66 of 66 history notes contain a year; only 15 of 250 industry hubs do. The history layer is doing exactly the job it was built for.
- **The research discipline is genuinely high.** 90 myths killed, competing accounts left unflattened, and the Greg Stuart/IAB quote marked *"searched and not corroborated"* rather than quietly dropped. That standard is rarer than it sounds and this assessment tries to hold to it.
- **Honest negatives are already recorded.** `history/dental-practices.md` opens with *"There is no moment here. No SABRE, no 8:01am in Troy Ohio."* That is the right instinct and there are ~20 such notes.

---

## 4. Two claimed gaps that are **not** gaps

Reported because a diagnostic that only confirms its own hypothesis is not a diagnostic.

**Interchange fees — the handover's own worked example of a gap — is covered.** `history/payment-processors.md` runs BankAmericard (18 Sept 1958, Fresno, 65,000 unsolicited live cards) → the spin-out to NBI (June 1970) → Visa (16 Dec 1976) → the Durbin Amendment and Regulation II, including the consequence that actually matters architecturally: every debit transaction must route over at least two unaffiliated networks, so the *acquirer* picks the cheaper path. That is a complete chain. It needs nothing.

**Amazon's marketplace mechanics are better covered than expected.** `history/online-marketplaces.md` owns the Buy Box with a dated origin (6 Nov 2000), a named fight (eBay vs Amazon on *what a listing is*), and a real mechanism — ranking sellers "reduces to a small, well-behaved optimisation… because the catalogue page defines sameness for you." `series/failures/amazon-auctions.md` is a full post-mortem of the platform owner's own failed bet. What is missing there is only the *money* (referral rates, FBA schedule, ad revenue), not the mechanism.

---

## 5. The gap

### The finding

**Every entity in this vault is a buyer of computing. Nothing in it sells computing.**

- The **250 industries** bought software.
- The **18 origins** bought computers earlier and built with them. Check the list: airlines, supermarkets, retail banking, hospitals, insurers, exchanges, telecoms, shipping, fabs, auto OEMs, carriers, credit bureaus, OTAs, pharma, ad agencies, utilities, railroads, process manufacturing. Every one is a *user*. Not one is a vendor.
- The **era spine is scoped, by its own design, to "what went to ~zero for the buyer"** — coordination → items → modelling → integration → distribution → compute → memory → location → attention → audience → presence → inference. Because of that scoping, no wave *can* name a commercial invention by a vendor. This is architectural, not an oversight.

The consequence is that every episode the vault can currently support has the same direction of travel: *a business had a problem, technology arrived, here is what they did with it.*

**That is the direction the brief says to avoid.** The owner wants the artefact as the subject and the business case as the explanation. For most artefacts a fresh graduate actually touches every day — the spreadsheet, the cloud bill, the 30% cut, the annual licence renewal, the recommendation feed, the GPU — the business case belongs to **a vendor**, and the vault has no vendors.

### The evidence — hard zeros across all 13,346 files

| Mechanic | Files | Note |
|---|---|---|
| "Amazon Web Services" | **1** | Wave 6 is **83 of 250** industries — the vault's largest cohort — and its cause gets 4 sentences |
| IBM 1969 unbundling | **0** | 19 hits for "unbundl" are medical claims, airline fees, and Microsoft/Teams in the EU in 2023 |
| Codd / System R / Sybase | **0 / 0 / 0** | `industries/database-platform-vendors.md` is 466 words and contains **no year at all** |
| WordPerfect / "office suite" | **0 / 0** | |
| "Google Play" / "Play Store" | **0 / 0** | |
| App Store 30% | **2 mentions** | Both a subordinate clause about someone else's loss. No date, no derivation |
| Netflix Prize / "item-to-item" | **0 / 0** | "Collaborative filtering" appears ~17× — every one a technique on a "what already exists" shelf |
| Taylorism / scientific management / Hawthorne | **0 / 0 / 0** | |
| ARPANET / TCP-IP / NSFNET / net neutrality / tier-1 | **0** | The web wave arrives with no network under it, and the cloud wave with no data centre under that |
| TSMC / fabless / foundry / Morris Chang | **0** | |
| Kerberos / LDAP / SAML / SCIM / hypervisor | **0** | |
| Maintenance-and-support (the ~20%/yr annuity) | **0 words** | The only explanation anywhere is ~55 words inside a game-asset niche, used as an analogy |
| Moore's Law / scaling laws | **0 / 0** | |

And the structural tell: the five tech-vendor hub notes in `industries/` — database platforms, developer tools, commercial open source, API infrastructure, edge CDN — contain **zero years between them.** The layer that carries time (`history/`) skips the entire software-infrastructure category.

### The clincher — a chain that is already broken in a file you have written

`history/work-collaboration-tools.md` tells the Teams-vs-Slack bundling war at full strength: ~450 words, dated (Teams 2 Nov 2016, EU antitrust July 2023, charges June 2024), with the mechanism named exactly right — a company already paying for Microsoft 365 was choosing between *"a tool we already have"* and *"a new line item,"* which made it **"an accounting question rather than a user-experience question."**

That is the 1990s office-suite war, refought. The vault never names the original. The chain reads:

> Teams beat Slack by bundling ← because Microsoft knew bundling works ← because Microsoft used it to kill Lotus and WordPerfect ← **[nothing]**

This is not a theoretical hole. It is a live one, in a finished file, in the vault's best-argued paragraph.

**Second clincher:** `origins/_index.md` poses the gatekeeper question itself — the OTA entry's contested decision is *"What stops a cheap distribution layer becoming a worse gatekeeper than the one you removed?"* — and there is no platform-owner file anywhere that can answer it. The platform gatekeeper was **never considered and never rejected**; `origins/_index.md` rejects only universities, defence primes and federal government. This is an unexamined absence, not a deliberate one.

---

## 6. Two defects found in passing

1. **`origins/semiconductor-fabs/profile.md:5`** claims the children are the three manufacturing industries *"and all compute downstream."* That last clause is unearned — `legacy.md` cashes out only the three, and the foundry/fabless split that would actually connect fabs to computing (TSMC, 1987) appears nowhere in the vault. Either narrow the claim or build the file that backs it.
2. **`series/eras/wave-12-transformers.md`** instructs: *"Write this wave with dates and mechanisms and without predictions."* That discipline is correct about the future and has been over-applied to the past. CUDA's history is settled fact, not prediction, and it is absent.

---

## 7. What I recommend **not** doing

- **No new `industries/` entries for the vendor gap** — one qualified exception in §9. That layer is bound by 1:1:1 parity with `problems/` and `niches/`. One addition costs 7 problem files plus 8 niches × 4 files — roughly 24,000 words — of build/buy/fix opportunity notes for a company you will never sell to. `origins/` exists precisely to avoid this and says so: *"You are not selling an insight engine to Maersk."* You are not selling one to AWS either.
- **No new niches.** All 66 history notes already close on them (347 links). 3,794 exist. Nothing in the diagnostic points at niche coverage.
- **Nothing in `series/failures/`.** The handover already calls it tangential and I agree; it is not where the chain breaks.
- **No government or defence origins**, beyond what item 7 below covers incidentally. The existing rejection is well reasoned.

---

## 8. The build — staged, scoped to the gaps proved above

Everything below is a **`origins/<slug>/` entry: 5 files, ~2,900 words.** Nothing touches the protected layers.

### Stage 0 — one file, to test the thesis before committing to it

**`history/database-platform-vendors.md`** — ~1,600 words, the standard history template.

The hub note it serves is one of the few with no history file at all and contains no year in 466 words. The chain *Codd (June 1970) → System R → Oracle v2 (1979) → the per-processor licence → the 20% maintenance annuity → Oracle-as-acquirer* repairs, in a single file, five of the gaps in the table above.

**Why this first:** it is the cheapest possible test of the central claim — that a vendor-side note produces a better episode than the vault already produces. If it does not, stop here and build nothing else. This is the step the previous phase skipped.

### Stage 1 — the three the audience lives inside daily

| # | Add | Gap it closes | Episode it unlocks |
|---|---|---|---|
| 1 | **`origins/cloud-hyperscalers/`** | Wave 6 is 83/250 industries with no parent; "Amazon Web Services" = 1 file; `hypervisor` = 0, so the VMware step between *buy a server* and *rent a meter* is missing too | **"Why does it cost money to get your own data out?"** — egress pricing as a retention mechanism |
| 2 | **`origins/packaged-software-vendors/`** | The vault's single largest footprint (spreadsheet, 1,405 files) has no vendor; IBM 1969 = 0; the maintenance annuity = 0 words | **"Why is your company's real operating system a spreadsheet?"** and **"Why do you pay for software every year, forever?"** |
| 3 | **`origins/platform-gatekeepers/`** | Never considered, never rejected; Google Play = 0; the 30% appears twice, both as someone else's loss | **"Why does the same app cost more on your phone?"** |

### Stage 2 — the three that repair the series' own argument

| # | Add | Gap it closes | Episode it unlocks |
|---|---|---|---|
| 4 | **`origins/scientific-management/`** | Taylorism = 0, Hawthorne = 0. The series' central claim — the chronology of failure ending in *the asymmetric hold* — has a 1911 parent it never names | **"Why does the app count your seconds?"** — a straight line from a stopwatch at Bethlehem Steel to a delivery driver's rating screen |
| 5 | **`origins/recommender-platforms/`** | Netflix Prize = 0, item-to-item = 0 | **"Why does it recommend that?"** |
| 6 | **`origins/accelerated-compute/`** | Wave 12 is the audience's own era and has the thinnest spine: Nvidia 2 files, CUDA 2, scaling laws 0 | **"Why did a gaming card decide what AI exists?"** |

**Item 4 is the most important recommendation in this document**, and the only one that fixes the series' *thesis* rather than its coverage. The chronology of failure is the series' central argument; its opening act is missing.

**Item 5 is the best single episode available anywhere in this vault**, because of what the research already shows (§9): the $1M-winning algorithm was never deployed. That rhymes exactly with `origins/airlines/the-mechanism.md` — *the algorithm was the cheap part* — and two independent cases making the same point, forty years apart, is what cohesion actually looks like.

### Stage 3 — conditional, only if the season runs past ~12 episodes

| # | Add | Gap | Episode | Why ranked lower |
|---|---|---|---|---|
| 7 | `origins/internet-backbone/` | ARPANET/NSFNET/tier-1 all 0 | "Why is your video call free when your phone call wasn't?" | Substantially a government-handoff story, which the vault deliberately de-prioritised |
| 8 | `origins/foundry-fabless/` | TSMC/Morris Chang = 0; also repairs defect §6.1 | "Why does one company in Taiwan make everyone's chips?" | Rhymes well with the container story, but narrower FDE payload |
| 9 | `origins/enterprise-identity/` | Kerberos/SAML/SCIM = 0 | "Why can't you sell software to a company until you have SSO?" | Least dramatic; most operationally useful to the audience |

### Cost

| | Entries | Words |
|---|---|---|
| Stage 0 — the probe | 1 history file | ~1,600 |
| Stages 1–2 — the gap proper | 6 origins | ~17,600 |
| Stage 3 — conditional | 3 origins | ~8,800 |
| **Series total, maximum** | **9 origins + 1 history** | **~28,000** |
| §9 exception — optional, one industry | 1 industry triple | ~24,000 |

For comparison, Phase 3 added ~228,000 words. The series recommendation is **~12% of that**, the tested entry point is **0.7%**, and even with the §9 exception the whole programme is under a quarter of the last one.

---

## 9. A second finding you did not ask for — kept separate on purpose

A sweep of the 250 against the US economy turned up **seven genuine industry absences.** They are real, and they are reported because suppressing them to keep the recommendation tidy would be the opposite failure to the one this assessment exists to correct.

**But they are a different project, and I am not folding them into the series build.** None of them blocks an episode. They serve the vault's *original* purpose — the prospecting index — which is not what was asked about.

| Absence | The mechanic it is a consequence of | Vault coverage |
|---|---|---|
| `residential-real-estate-brokerage` | The MLS as a compulsory cooperative database; NAR cooperative-compensation and its 2024 unwinding; IDX syndication | "realtor", "listing agent", "NAR settlement" → **0 files.** `proptech-platforms` is explicitly *rental*, not sale-side |
| `sports-betting-operations` | *Murphy v. NCAA* (2018) voiding PASPA → 38 state licensure regimes, each requiring geofencing, KYC and integrity feeds | "sports betting", "sportsbook", "PASPA" → **0 files** |
| `ambulatory-surgery-centers` | Medicare's separate ASC payment system (1982) + the Anti-Kickback safe harbour permitting physician ownership | "surgery center", "Stark Law", "anti-kickback" → **0** |
| `clinical-diagnostic-labs` | CLIA '88 certificate tiers as a market-entry gate; the FDA/LDT boundary; PAMA | "clinical laboratory" → **0.** The vault has ~17 `*-labs` pockets, none of them human clinical |
| `fire-life-safety-inspection` | NFPA 25 / NFPA 72 — recurring revenue created by statute rather than demand | "NFPA 25" → **0** |
| `aba-autism-therapy-providers` | State autism insurance mandates (2008→2021) + the 2019 CPT 97151–97158 codes | "applied behavior analysis" → **0** |
| `solid-waste-recycling-haulers` | RCRA Subtitle D (1991) forcing consolidation onto route density; EPR statutes | "waste hauler", "roll-off", "EPR" → **0** |

### The one thing here that *is* a series problem

**Five of those seven are industries manufactured by a statute whose statute appears nowhere in the vault.** That is precisely the blind spot the vault already diagnosed in itself — *"Epic appears in 92 files as an integration constraint and HITECH in none."*

Which exposes a genuine cohesion weakness in the series, independent of whether those industries ever get built:

> **"A law can manufacture a software market" is currently one anecdote (HITECH) presented as a general pattern.**

One instance is a story; two is a pattern. The cheap fix is **not** to build seven industries (~170,000 words, and in the prospecting direction, not the series direction). It is to build **one** as the second instance.

**Recommended single exception: `sports-betting-operations`** — full `industries/` + `problems/` + `niches/` triple, ~24,000 words.

- It is the cleanest modern HITECH analogue in existence: a **2018 Supreme Court decision** that manufactured a nationwide technology industry in six years, with a hard date and no invention involved.
- It unlocks a genuinely tech-first episode: **"Why does the betting app know which side of the state line you're standing on?"** — geolocation compliance is a mechanic the audience physically experiences.
- It is the only one of the seven that is simultaneously a strong prospecting target and a strong episode, so the ~24,000 words are not spent twice.

`residential-real-estate-brokerage` is the strongest *prospecting* absence of the seven — ~100k brokerages, the largest 1–50-person US service population the vault omits, and the MLS rhymes directly with the vault's existing "standardisation precedes digitisation" thread (MICR 1956, the ISO container 1968, the UPC 1973). If a second industry is ever built, build that one. It is not needed for the series.

### False positives — checked, present, do not re-flag

These look absent by filename and are covered as Pass-2 pockets: e-discovery, title & settlement, PEO, benefits brokerage, Medicare Advantage, 340B, cannabis cultivation and testing, background screening, EOR, SMB GovCon (AS9100/DFARS/CMMC/DCAA/NIST 800-171), franchising, ghost kitchens, music publishing, drone operations, EVV/Medicaid HCBS, appraisal management, credentialing, litigation funding, alarm monitoring, travel nursing.

---

## 10. Verification status of every date in this document

Held to the vault's own standard: a negative finding is a real finding.

**Verified this session (web):**
- **IBM unbundled 23 June 1969**, splitting program products from system control programs; systems engineering hourly, education per-student, maintenance monthly. ✅
- **The Netflix Prize ran Oct 2006 → 21 Sept 2009**; BellKor's Pragmatic Chaos won $1M at 10.06% improvement with a 107-algorithm ensemble — **and Netflix never deployed it**, stating the accuracy gains "did not seem to justify the engineering effort needed to bring them into a production environment." A linear blend of two earlier algorithms shipped instead. ✅
- **The AWS "excess retail capacity" origin is a myth** — Werner Vogels on record; AWS would have burned through Amazon.com's spare capacity within two months of launch, and Amazon's servers were customised and not shareable. The real trigger was the Merchant.com build around 2000 exposing the need for reusable internal services. ✅ **Flagged because an episode writer will walk straight into this one.**
- **CUDA:** G80 shipped 2006; CUDA 0.8 February 2007, 1.0 June 2007. ✅
- **Taylor's pig-iron story is itself contested.** Wrege & Perroni (1974) showed eight specific details in the 1911 account do not match other evidence, and that Taylor's own telling changed between 1901, 1903 and 1911. "Schmidt" was Henry Noll; the Bethlehem work ran 1898–1901. ✅ **A gift for a vault whose house style is myth-killing.**

**Verified in-vault (already sourced there, not re-checked):** S3 14 March 2006 / EC2 25 Aug 2006; VisiCalc 17 Oct 1979; Lotus 1-2-3 26 Jan 1983; SAP R/3 6 July 1992; AdWords 23 Oct 2000; Amazon Marketplace 6 Nov 2000.

**Partially corroborated — usable, but say what the source is:**
- **Where Apple's 30% came from.** The lineage does hold up, and it is a better episode than I expected. The 70/30 split dates to the **iTunes Music Store (2003)**: labels took 70¢ of the 99¢ song price. It came out of Jobs's 2002 negotiation with the five major labels, and the trade was explicit — **Apple gave the labels 70% of music revenue and kept 100% of iPod hardware revenue.** Multiple secondary sources attribute the App Store's reuse of the number to a **WSJ interview in which Jobs said he took it from iTunes' 30¢ per song.** ⚠️ I did not retrieve that interview itself; this is secondary reporting of a primary source, which is a weaker status than the vault's bar and should be closed before script.
  **Why this matters for the episode:** the 30% was never derived from the cost of running a software store. It was the price of getting record labels to say yes to selling *music* in 2002, and software inherited it in 2008 without anyone re-deriving it. That is the owner's episode shape exactly — a number you pay on every app, set by a negotiation about something else entirely.

**NOT verified — do not assert:**
- **"Antitrust created the software industry."** Contested — there is a substantive dissent from the AEI side. Leave unflattened, per house style.
- **TSMC 1987 / Morris Chang, NSFNET's 30 April 1995 decommissioning, VMware 1998–2001, Akamai 1998, the Bezos API mandate ~2002.** All named from general knowledge and **not checked this session.** The Bezos mandate in particular traces to a 2011 blog post, not a primary source — treat with the same suspicion the vault applies to the Greg Stuart quote.

---

## 11. The one open question

**Delivery format is still unknown** — written, spoken, video, length, tone.

The handover argued this "materially changes what a gap even means." **I disagree, mildly, and it is worth saying why:** the vendor gap is a gap whether an episode is a 2,000-word essay or a 10-minute video, because it is a gap in the *causal chain*, not in the runtime. Nothing in this assessment is contingent on the answer.

Where it *does* matter is downstream — episode count, how much mechanism survives the edit, and whether §10's "not verified" list needs closing before or after a script exists. Worth settling before anything script-shaped is written; not worth blocking this build on.

---

## 12. Summary

**The vault needs no new niches at all, and it needs one new industry rather than seven.** What it needs is **six origins' worth of the other side of the transaction** — and one cheap file first, to prove that claim before spending on the rest.

The vault already documents, exhaustively, what it is like to *live with* technology that someone else's business decision shaped. It has no account of the businesses that made those decisions. That is the whole gap, and it sits directly on the owner's stated thesis: **business is the ultimate entity tech works towards.** Right now the vault can only argue that from the receiving end.

### If you read nothing else

1. **Build `history/database-platform-vendors.md` first.** One file, ~1,600 words. If a vendor-side note does not produce a better episode than the vault already produces, stop and build nothing else.
2. **Then the six origins.** Cloud hyperscalers and packaged-software vendors are the two that unblock the most; scientific management is the one that repairs the series' own argument.
3. **The best single episode available** is the Netflix Prize — a $1,000,000 algorithm that was never deployed — because it independently re-proves what `origins/airlines/the-mechanism.md` already argues: the algorithm was the cheap part. Two cases making the same point forty years apart is what cohesion actually looks like.
4. **Do not build the seven industries in §9 for the series.** They are a prospecting project. If you build one, build `sports-betting-operations`, because it is the second instance of "a law manufactured a software market" — a claim the vault currently makes on the strength of a single example.
