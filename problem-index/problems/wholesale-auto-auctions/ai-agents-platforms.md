# AI Agents & Platform Opportunities — Wholesale Auto Auctions

**Industry:** [[wholesale-auto-auctions|Wholesale Auto Auctions]]

---

## 1. Arbitration Case Agent
#ai-agent #large-language-models #k-nearest-neighbors #workflow-orchestration #compliance #worker-facing

**Concept:** An agent that opens every arbitration claim already assembled. It pulls the announcement, condition report, photographs and trouble codes, cites the NAAA guideline clause, threshold and filing window that apply, and retrieves the most similar settled cases. It drafts the evidence request to the buyer and the notice to the seller. It answers out-of-window and under-threshold claims with the clause, and proposes an adjustment for the rest from past settlements. The admin decides.
**Inputs:** Claim intake (portal, phone transcript, email), the sale record and announcement, the condition report, post-sale inspection results, buyer repair estimates, the auction's case history, and the June 2026 guideline text.
**Outputs / Actions:** Case summary with the governing clause; drafted messages; a proposed adjustment with a range; routing to post-sale inspection; a case record that shows why each decision was made.
**Why now:** The 1 June 2026 guidelines changed what announcements protect (generic "No Arb" banned, warning lights no longer enough, ADAS added, 2% for cars at $50,000 and up), so every admin is applying new rules from memos. LLMs can now read repair-estimate PDFs and policy text reliably enough to draft the case.
**Market:** Arbitration departments at Manheim, Carvana's ADESA, OPENLANE, ACV and ~200–250 independent auctions. The digital players are building in-house now. ACV lists a Software Engineer IV, Arbitrations (Chennai, posted 2026-08-27) and an Analytics Engineer III, Assurance, to "surface insights on arbitration risk" (Buffalo, virtual or Toronto, 2026-08-19). OPENLANE is hiring a claim-resolutions technical specialist in Canada (2026-10-08). Independents are the reachable buyers for a vendor product. The contest is [[niches/wholesale-auto-auctions/arbitration-post-sale-claims/profile|Arbitration & Post-Sale Claims]].

---

## 2. Pre-Sale Disclosure Checker
#ai-agent #large-language-models #gradient-boosting #compliance #quick-win #automation

**Concept:** An agent that sits between check-in and the lane. For each car it decodes the VIN through NHTSA vPIC, pulls recall campaigns from the NHTSA recalls API, reads the seller announcement and condition report, and returns the lines that will not protect the seller under the 2026 rules. Examples are a generic "No Arb", a warning light announced without its cause, ADAS equipment present but unmentioned, and a "park it" recall. It proposes specific wording or a red-light, as-is sale. This is the two-week MVP, productised.
**Inputs:** Announcement text and sale light, condition-report fields and codes, VIN, expected price against MMR, the vPIC decode, recall campaigns, and the seller's claim history.
**Outputs / Actions:** A risk list with clauses and expected cost; suggested announcement text; a hold on publishing the listing until the seller accepts or overrides; a log for the auction's assurance team.
**Why now:** The guideline change made every legacy announcement template a liability, the NHTSA APIs are free, and LLMs map free text to defect categories well enough for a rules layer to act on.
**Market:** Auctions' consignment desks, commercial consignors uploading thousands of units, and dealer groups selling wholesale. ACV is hiring for the inspection and data side: a Software Engineer III, Vehicle Intelligence (Buffalo, NY, posted 2026-07-22) and Machine Learning Engineers III and IV on its ML inspection team (Buffalo, virtual or Toronto, from 2026-07-02). OPENLANE lists an MLOps Engineer in Carmel, Indiana (2026-10-20). Assurance products such as DealShield and Go Green price the same risk after the fact. The contest is [[niches/wholesale-auto-auctions/announcement-disclosure-checks/profile|Announcement & Disclosure Checks]].

---

## 3. Title Chase Agent
#ai-agent #survival-analysis #large-language-models #workflow-orchestration #automation

**Concept:** An agent that works the title-absent queue every morning. It ranks open titles by risk of breaching the auction's window, then emails and texts sellers and lienholders with the specific ask: payoff confirmation, release, overnight tracking. It reads the replies, updates the record, warns buyers before they can return the car, and escalates to the clerk only when a call is needed.
**Inputs:** Sold-without-title list, title windows, issuing state and ELT status, lienholder and payoff records, seller history, inbound emails and tracking numbers.
**Outputs / Actions:** A ranked worklist; outbound messages; updated title status; buyer notices; a weekly report of late titles by seller for account managers.
**Why now:** Title work is document reading and follow-up, which LLM agents now do reliably, and ACV says it already automates some title processing "through machine learning", so buyers have seen it work.
**Market:** Auction title departments and the commercial consignors (fleets, lenders) whose late titles cost their own sales. Title clerk roles were open at ACV in Texas on 2026-10-28. The contest is [[niches/wholesale-auto-auctions/title-absent-sales/profile|Title-Absent & Title-Defect Sales]].

---

## 4. Commercial Remarketing Channel Platform
#ai-platform #causal-inference #gradient-boosting #time-series-forecasting #revenue-impact

**Concept:** A platform that decides for every commercial unit (off-lease, rental, fleet, repossession) where and when to sell it. The options are the captive's upstream private-label sale, an open digital auction, a physical lane with simulcast, or holding a week. It estimates net proceeds against MMR after fees, transport and depreciation, learns from the consignor's own results, and recommends a floor.
**Inputs:** Unit condition and location, MMR and the Manheim index trend, channel fees and transport costs, the consignor's sale history across channels, and Cox's off-lease and rental volume outlook (off-lease +23% in 2026).
**Outputs / Actions:** Channel and timing recommendation per unit; floor price; a monthly report of net-to-MMR by channel for the consignor's remarketing director.
**Why now:** Off-lease supply is rising fast, with EVs going from ~10% to ~16% of off-lease units in 2026 and less predictable values. Consignors now sell across private-label, digital and physical channels at once, so the channel choice is a measurable decision.
**Market:** Remarketing directors at captives, banks with lease books, rental companies and fleet lessors. OPENLANE powers more than 40 private-label remarketing sites and is hiring an AI First Software Engineer (Carmel, IN, 2026-09-29) and a Staff Software Engineer (remote US or Canada, 2026-10-21). CarGurus' open Software Development Engineer II (Boston, 2026-10-14) is a retail-leads role, not a CarOffer wholesale one. The lender's side is [[niches/sales-finance-companies/repossession-and-remarketing/profile|Repossession, Remarketing & Deficiency]] and the fleet lessor's is [[niches/fleet-managers/fleet-lease-residual-analytics/profile|Fleet Lease Residual & Remarketing Analytics]]. The auction's contest is [[niches/wholesale-auto-auctions/commercial-consignor-remarketing/profile|Commercial Consignor Remarketing]].
