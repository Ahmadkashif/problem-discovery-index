# AI Agents & Platform Opportunities — Music Publishers

**Industry:** [[music-publishers|Music Publishers]]

---

## 1. Sync Brief Desk
#ai-agent #transformers #contrastive-learning #large-language-models #tacit-knowledge-ml #revenue-impact #worker-facing

**Concept:** An agent that sits on the sync team's inbox. It parses each incoming brief into structured fields and proposes a short, ranked list of songs that this team's history says the recipient is likely to license, each with clearance status, co-publisher approvals and a fee band from comparable past licences. It drafts the pitch email, then follows the thread so shortlist requests, quotes and outcomes go back into a pitch ledger without the rep typing anything.
**Inputs:** Brief emails and reference tracks; the catalogue's audio, lyrics and metadata; pitch playlists; quote and licence records; clearance and restriction data; the team's past brief-to-outcome records.
**Outputs / Actions:** Ranked pitch list with reasons ("supervisor licensed a similar track in 2025"); draft pitch email and playlist; clearance and fee-band flags; an updated pitch ledger; a weekly view of which catalogue songs are pitched and licensed and which are never surfaced.
**Why now:** Language models can read a brief's loose mood language and parse email threads into structured outcomes cheaply, and audio embeddings make every song in a deep catalogue searchable. Recording the pitch history no longer depends on rep discipline.
**Market:** Sync teams at the majors and at independent publishers. Synchtank and DISCO are the natural incumbents for pitching and asset sharing, but they store pitches rather than learn from them.

---

## 2. Catalogue Underwriting Platform
#ai-platform #time-series-forecasting #survival-analysis #bayesian-inference #data-integration #revenue-impact

**Concept:** A platform that ingests a catalogue's royalty statements in whatever formats the data room holds and normalises them into song-by-source earnings series. It forecasts each song's earnings with intervals, flags concentration and revival dependence, checks income against usage to catch uncollected money, and produces a valuation pack that a buyer, lender or rating agency can trace line by line.
**Inputs:** Data-room statements from societies, sub-publishers, the MLC and DSPs; agreements and schedules of works; streaming and airplay series; comparable transactions; rate determinations.
**Outputs / Actions:** Normalised earnings history; song-level and catalogue forecasts with prediction intervals; concentration and termination-risk report; uncollected-income estimate; a valuation memo and a model file the valuer or lender can audit.
**Why now:** Catalogues now trade and are securitised at a scale that makes forecast error costly. Citrin Cooperman alone priced 566 catalogues worth nearly $13B in 2025, and KBRA has rated about $8B of music royalty asset-backed securities since 2020. Language models can also now parse irregular statement layouts that once took weeks of manual mapping.
**Market:** Catalogue funds and major publishers' acquisition teams, royalty lenders, asset-backed security arrangers and the specialist valuers, who might license it as a tool. It is an existing buyer category served today by spreadsheets and a handful of valuation firms.

---

## 3. Royalty Recovery Agent
#ai-agent #gradient-boosting #hypothesis-testing #workflow-orchestration #data-integration #compliance #revenue-impact

**Concept:** An agent that compares what each work should have earned in each territory and source with what arrived, identifies the likely cause of each gap, and then acts: it registers missing works, files claims and match suggestions at the MLC and with societies, and chases sub-publishers. It schedules all of this against deadlines such as the MLC database snapshot around 10 February 2027 for the first market-share distribution, and the three-year non-distributable rule for EU societies.
**Inputs:** Received statements; registration status by society; usage data by country; deal records; society and MLC portal access; deadline calendars.
**Outputs / Actions:** Ranked gap list with dollar estimates and deadlines; CWR registrations and portal claims filed for approval; chase letters to sub-publishers; a log of recovered amounts by cause.
**Why now:** The MLC's April 2027 market-share date puts a dated deadline on every unclaimed 2021 share, and agents can now operate portal workflows and draft society correspondence that once needed a coordinator for each territory.
**Market:** Independent publishers and administrators, writers' estates and catalogue owners. Royalty auditors and recovery specialists sell this today on contingency, case by case.

---

## 4. Rights Ledger and Termination Monitor
#ai-platform #large-language-models #transformers #compliance #automation #data-integration

**Concept:** A platform that reads every agreement in a catalogue into a clause-cited chain of title. It records who owns and collects each share, in which territory and until when, and computes Section 203 and 304 termination windows, contractual reversions and retention periods. It keeps the registrations at each society consistent with that ledger, so conflicts are prevented rather than resolved.
**Inputs:** Agreements and amendments, schedules of works, Copyright Office records, registrations by society, earnings by song.
**Outputs / Actions:** Chain-of-title ledger with clause citations; termination and reversion calendar ranked by earnings at stake; registration mismatches pushed to coordinators; diligence reports for acquisitions.
**Why now:** Language models extract clauses from old scanned agreements accurately enough for lawyer review. A generation of grants made in the late 1980s and 1990s is now inside the Section 203 window, and catalogue acquisitions make chain-of-title diligence a recurring cost.
**Market:** Publishers' business affairs teams, catalogue buyers' counsel, and writers' estates and their lawyers. Contract management vendors sell the storage layer without the copyright logic.
