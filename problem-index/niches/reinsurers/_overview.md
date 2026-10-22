# Niche Analysis — Reinsurers

**Parent Industry:** [[industries/reinsurers|Reinsurers]]

## Niche Selection

A reinsurer prices a promise to pay its clients' worst years, mostly in the few weeks before 1 January, 1 April, 1 June and 1 July. The central judgement is the lead underwriter's adjustment of vendor catastrophe models to each cedent, and it is recorded without reasons. Around it sit a casualty business priced on trend assumptions that are graded years later, a facultative desk reading single-risk documents, and a back office reconciling money and collateral cedent by cedent. Third-party capital adds a layer of investors who see the risk only through managers' reports. The eight niches below split the industry by what vendors and internal teams compete over. This hub covers the property-casualty side; life reinsurance is covered from the carrier side under [[industries/life-insurance-carriers|Life Insurance Carriers]]. Market sizes are estimates of analytics, modelling, tooling and specialist staff spend in each niche (~$5B a year in total), not of reinsurance premium or capital.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Property Catastrophe Treaty Underwriting | 🔵 High Market Share | ~$1.5B | High (models), Low (adjustments) | CUO Property, Head of Cat Pricing |
| 2 | Casualty Treaty Reinsurance | 🔵 High Market Share | ~$1.2B | Medium | CUO Casualty, Chief Reserving Actuary |
| 3 | Facultative Reinsurance Underwriting | 🟠 Low Digitized | ~$400M | Low | Head of Facultative |
| 4 | Reinsurance Claims, Technical Accounting & Collateral | 🟠 Low Digitized | ~$600M | Low | Head of Reinsurance Operations |
| 5 | Retrocession Buyers & Sellers | 🟣 Underserved Audience | ~$150M | Medium | Head of Retrocession; retro portfolio manager |
| 6 | ILS Investors & Sidecar Capital Providers | 🟣 Underserved Audience | ~$100M | Medium | Head of Alternatives at a pension fund or endowment |
| 7 | Submission & Exposure Data Preparation | ⚡ Highly Automatable | ~$300M | Medium | Head of Exposure Management |
| 8 | Treaty Wording & Contract Certainty | ⚡ Highly Automatable | ~$150M | Medium | Head of Wordings |

## Why These Niches

Property catastrophe treaty underwriting takes the largest share because every property programme runs through it at the renewal and the own-view-of-risk adjustment is where price is won or lost. Casualty treaty is second: the other half of treaty demand, made urgent by social inflation, and the reinsurer's widest cross-cedent data asset. The two low-digitized niches are where reading still dominates. Facultative underwriters decide on single risks from engineering surveys and loss runs sent by email. The back office agrees statements, cash calls and collateral by hand against a 90-day penalty line. The two underserved audiences are served by tools designed for someone else. Retrocession buyers and writers must model books of treaties with tools built for locations. The institutions behind $136B of third-party capital (Aon) learn their event losses from managers' reports. The two automatable niches are the most mechanical steps in the renewal: turning a cedent's spreadsheet into a model-ready file, and comparing a renewal wording with the expiring contract, the slip and the model clauses.

## Niches

- [[niches/reinsurers/property-cat-treaty-underwriting/profile|🔵 Property Catastrophe Treaty Underwriting]]
- [[niches/reinsurers/casualty-treaty-reinsurance/profile|🔵 Casualty Treaty Reinsurance]]
  - [[niches/reinsurers/casualty-xol-trend-pricing/profile|🎯 Casualty Excess-of-Loss Trend & Development Pricing]]
  - [[niches/reinsurers/programme-quota-share-oversight/profile|🎯 MGA & Programme Quota Share Oversight]]
- [[niches/reinsurers/facultative-underwriting/profile|🟠 Facultative Reinsurance Underwriting]]
- [[niches/reinsurers/claims-accounting-collateral/profile|🟠 Reinsurance Claims, Technical Accounting & Collateral]]
- [[niches/reinsurers/retrocession-buyers-sellers/profile|🟣 Retrocession Buyers & Sellers]]
- [[niches/reinsurers/ils-investors-sidecar-capital/profile|🟣 ILS Investors & Sidecar Capital Providers]]
- [[niches/reinsurers/submission-exposure-data-prep/profile|⚡ Submission & Exposure Data Preparation]]
- [[niches/reinsurers/treaty-wording-contract-certainty/profile|⚡ Treaty Wording & Contract Certainty]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Casualty Treaty Reinsurance is not. Writing its sentence produced two contests with different winners. On excess-of-loss layers the contest is the trend and development selection on long-tail severity, won by whoever's selections still hold when the adverse development arrives. The input is cedents' ceded triangles and large-loss listings, and the clock is the renewal and the reserve review. On quota shares behind MGAs and fronting carriers, the contest is detecting a programme's underwriting drift in monthly bordereaux before the loss ratio shows it. Different data, different people and a monthly clock, so it decomposes into **Casualty Excess-of-Loss Trend & Development Pricing** and **MGA & Programme Quota Share Oversight**. The programme sub-niche is the capacity provider's side of the same programmes whose fronting carriers are logged under [[industries/property-casualty-insurers|Property & Casualty Insurers]]. It does not claim the fronting carrier's oversight work.

Two terminal calls were close. **Reinsurance Claims, Technical Accounting & Collateral** could split into claims review and accounting. It is kept whole because loss advices, statements, cash calls and collateral all end in one agreed balance per cedent on the same quarter-end clock, and the same team usually owns the outcome. Disputed claims that go to arbitration leave the niche for the advisers logged in Pass 2. **Submission & Exposure Data Preparation** overlaps with property cat underwriting. It is kept separate because its contest, the fewest manual fixes per file, is won by data tooling and offshore teams rather than by underwriters, and brokers and Supercede compete in it too.

Three candidates were considered and rejected. **Specialty treaty (marine, energy, aviation, cyber)** was rejected because the contest splits by line with no common winner, and cyber aggregation is already profiled as [[niches/property-casualty-insurers/cyber-cat-aggregation-modelling/profile|🔍 Cyber Catastrophe & Aggregation Modelling Vendors]]. **Parametric and public-sector risk transfer buyers** were considered as an underserved audience. The contest, designing a trigger with basis risk a public buyer can defend, is real, but the buyers are too few to make a niche. Sovereign and regional disaster pools number a handful of buyers worldwide, and US public entities are already covered by [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]. **Life and accident-and-health reinsurance** is outside this build, although NAICS 524130 includes it (RGA and the US life arms of Munich Re and SCOR, recalled). It gets no niche here because the hub covers the property-casualty side. The vault's only coverage of it is from the carrier side: [[niches/life-insurance-carriers/life-reinsurer-underwriting-research/profile|🔍 Life Reinsurers' Underwriting Research & Mortality Studies]] and [[niches/life-insurance-carriers/inforce-block-acquirers/profile|🔍 In-Force Block Acquirers & Closed-Block Consolidators]].

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. This pass covers seven positions in the value chain: aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry. It looks for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`. Pockets already profiled under other industries are linked in the prose below rather than profiled again.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Single-Peril & Climate Model Specialists | Data vendor | 20-150 | 47 | Below threshold |
| 10 | Industry Loss Index Providers | Data vendor | 10-40 | 46 | Below threshold |
| 11 | Cat Bond Risk Modelling & Calculation Agents | Specialist advisory | 10-40 | 43 | Below threshold |
| 12 | Cat Model Validation & Own-View-of-Risk Consultancies | Specialist advisory | 10-80 | 39 | ⚠️ Kill switch |
| 13 | Reinsurer Property-Cat Pricing & Portfolio Analytics Units | Payer & intermediary | 50-300 | 38 | Below threshold |
| 14 | Reinsurance Commutation, Claims Audit & Arbitration Support | Specialist advisory | 10-50 | 38 | ⚠️ Kill switch |
| 15 | Casualty Treaty Actuarial & Loss-Trend Units | Payer & intermediary | 20-150 | 36 | Below threshold |
| 16 | P&C Legacy & Run-Off Acquirers | Aggregator/rollup | 20-100 | 34 | ⚠️ Kill switch |
| 17 | ILS Fund Managers | Aggregator/rollup | 10-60 | 33 | Below threshold |
| 18 | Reinsurer Research Institutes & Published Catastrophe Databases | Supplier | 30-100 | 27 | Below threshold |
| 19 | Reinsurance Supervisors (BMA & NAIC Reinsurance Groups) | Regulatory | examination staff | — | Fails gate |
| 20 | ILS Market Data, Indices & News Services | Data vendor | <10 | — | Fails gate |
| 21 | Reinsurance Submission & Placement Platforms | Supplier | production only | — | Fails gate |
| 22 | Reinsurance Collateral Trustees & Letter-of-Credit Banks | Payer & intermediary | production only | — | Fails gate |
| 23 | Reinsurance Trade Associations & Loss Development Study | Association | <10 | — | Fails gate |

## Why These Pockets

No pocket qualifies, and the central finding is the same as for the carriers: the reinsurer itself passes the gate and fails on Q1. Its cat pricing units (38) and casualty actuarial units (36) are large and sit on the widest cross-cedent data in insurance, but their insight is priced into premium, scored with the other risk-bearer units under the batch 6 ruling. The ILS fund managers (33) monetise research through returns, like hedge funds. The one indexed reinsurance-adjacent qualifier is already in the vault and is not profiled again: [[niches/public-adjusters/catastrophe-modelling-firms/profile|🔍 Catastrophe Modelling Firms]] (56), which every pocket at the top of this table orbits. Other neighbours are linked rather than re-profiled: [[niches/independent-insurance-agents/reinsurance-broking-analytics/profile|🔍 Reinsurance Broking Analytics]] (47), [[niches/property-casualty-insurers/cyber-cat-aggregation-modelling/profile|🔍 Cyber Catastrophe & Aggregation Modelling Vendors]] (47), [[niches/property-casualty-insurers/insurer-financial-strength-ratings/profile|🔍 Insurer Financial Strength Rating Agencies]] (47, kill switch), which rate reinsurers too, and [[niches/property-casualty-insurers/pc-reserve-opinion-actuaries/profile|🔍 P&C Reserve Opinion & Reserve Review Actuaries]] (48, kill switch). The list continues with [[niches/property-casualty-insurers/fronting-carrier-programme-oversight/profile|🔍 Fronting Carriers' Programme Oversight]] (36), [[niches/satellite-operators/catastrophe-imagery-analytics/profile|🔍 Catastrophe Event Imagery & Damage Analytics]] (40) and [[niches/independent-insurance-agents/mga-program-underwriters/profile|🔍 MGAs & Program Underwriters]] (52). On the life and benefits side: [[niches/life-insurance-carriers/life-reinsurer-underwriting-research/profile|🔍 Life Reinsurers' Underwriting Research & Mortality Studies]] (38, kill switch), [[niches/life-insurance-carriers/inforce-block-acquirers/profile|🔍 In-Force Block Acquirers & Closed-Block Consolidators]] (34, kill switch), [[niches/pension-funds/prt-insurer-pricing-teams/profile|🔍 Pension Risk Transfer Insurer Pricing Teams]] (36, kill switch), [[niches/pension-funds/longevity-analytics-providers/profile|🔍 Pension Longevity Analytics & Pooled Mortality Data]] (42), [[niches/title-insurance-carriers/title-reinsurance-markets/profile|🔍 Title Reinsurance Markets]] (fails gate), [[niches/self-insured-benefit-pools/public-entity-excess-underwriters/profile|🔍 Public Entity Excess & Reinsurance Underwriters]] (39) and [[niches/self-insured-benefit-pools/medical-stop-loss-underwriters/profile|🔍 Medical Stop-Loss Underwriters & MGUs]] (43, kill switch).

The near-misses share one shape: an estimate that is the invoice, graded later by a known outcome, sold by a handful of firms. The single-peril and climate modellers score highest (47), with a scorecard that matches the cyber cat modellers line for line. Industry loss index providers (46) are the strongest clean case on substance and the pocket the P&C build left to this industry. PCS and PERILS own the only industry-wide contributed loss and exposure data in their territories. Every preliminary estimate is later graded by its own final figure, and contributors supply data so that it can be aggregated, so no kill switch applies. They fall short on scale: analysts grow with the number of events, the reporting dates are their own, and the buyer market is two firms. The single-peril modellers and the cat bond modelling agents (43) are scored consistently with the cyber cat modellers under lessons (h) and (i). The cat bond agents are the capital-markets teams of the indexed modellers themselves, one organisation family logged for Stage E. Their gap to the natural-peril modellers' 56 is the same scoring gap, not a difference in substance; the batch 6 review put that pocket at ~50 under the later lessons.

The kill switches are the usual ones. Model validation consultants (39) work on clients' portfolios and clients' model licences. Commutation and arbitration advisers (38) are retained through counsel. Run-off acquirers (34) price from sellers' data rooms, as the life consolidators do. Five positions fail the gate outright. The reinsurance supervisors hold the market's best catastrophe exposure returns, but their Bermuda staff are examiners rather than a named 10+ analytics unit, and the NAIC slice belongs to the state regulator family. The other four are ILS data and news services, submission and placement platforms, collateral trustees, and the trade associations. The lesson for a research-insight engine is that reinsurance insight is already sold by modellers and index providers; the gap is inside the reinsurer, in the own-view-of-risk adjustments nobody grades.

## Niches — Pass 2
- [[niches/reinsurers/single-peril-climate-model-specialists/profile|🔍 Single-Peril & Climate Model Specialists]]
- [[niches/reinsurers/industry-loss-index-providers/profile|🔍 Industry Loss Index Providers]]
- [[niches/reinsurers/cat-bond-modelling-calculation-agents/profile|🔍 Cat Bond Risk Modelling & Calculation Agents]]
- [[niches/reinsurers/cat-model-validation-consultancies/profile|🔍 Cat Model Validation & Own-View-of-Risk Consultancies]]
- [[niches/reinsurers/reinsurer-cat-pricing-portfolio-units/profile|🔍 Reinsurer Property-Cat Pricing & Portfolio Analytics Units]]
- [[niches/reinsurers/reinsurance-commutation-arbitration-support/profile|🔍 Reinsurance Commutation, Claims Audit & Arbitration Support]]
- [[niches/reinsurers/casualty-treaty-loss-trend-units/profile|🔍 Casualty Treaty Actuarial & Loss-Trend Units]]
- [[niches/reinsurers/pc-legacy-runoff-acquirers/profile|🔍 P&C Legacy & Run-Off Acquirers]]
- [[niches/reinsurers/ils-fund-managers/profile|🔍 ILS Fund Managers]]
- [[niches/reinsurers/reinsurer-research-institutes/profile|🔍 Reinsurer Research Institutes & Published Catastrophe Databases]]
- [[niches/reinsurers/reinsurance-supervisors/profile|🔍 Reinsurance Supervisors (BMA & NAIC Reinsurance Groups)]]
- [[niches/reinsurers/ils-market-data-news/profile|🔍 ILS Market Data, Indices & News Services]]
- [[niches/reinsurers/reinsurance-submission-placement-platforms/profile|🔍 Reinsurance Submission & Placement Platforms]]
- [[niches/reinsurers/reinsurance-collateral-trustees/profile|🔍 Reinsurance Collateral Trustees & Letter-of-Credit Banks]]
- [[niches/reinsurers/reinsurance-trade-associations/profile|🔍 Reinsurance Trade Associations & Loss Development Study]]
