# AI Agents & Platform Opportunities — Aerospace Parts Suppliers

**Industry:** [[aerospace-parts-suppliers|Aerospace Parts Suppliers]]

---

## 1. First Article Package Agent
#ai-agent #object-detection #large-language-models #transformers #compliance #automation #quick-win

**Concept:** An agent that takes a drawing or model, a purchase order and the material and process certificates, and assembles the AS9102 package. It balloons every requirement including notes, builds Form 3 ready for measurements, fills Form 2 from the certs and checks each special processor against Nadcap status and the customer's approved list, and completes Form 1 with the reason for a full or partial FAI. It applies the prime's own FAI rules and watches for changes (a new sub-tier processor, a drawing revision, a production lapse) that trigger a delta FAI.
**Inputs:** Drawing PDFs and scans, MBD files, PO clauses, customer supplier-quality requirement documents, mill and special-process certs, CMM exports, the shop's past accepted FAIRs.
**Outputs / Actions:** Ballooned drawing; draft Forms 1–3 with confidence flags; a list of missing evidence; upload to the customer's portal; a register of part numbers due a delta FAI.
**Why now:** Vision-language models can now read scanned drawings and feature control frames well enough to propose balloons, and AS9102 Revision C (2023, per vendor summaries) plus primes' tighter flowdowns have raised the paperwork per part just as rates climb. A two-week MVP (auto-balloon a public sample drawing and fill Forms 1–3 from the AS9102 template) is the owner's proposed demo.
**Market:** Quality managers at ~1,000+ firms in the two codes and several thousand more machine shops, processors and distributors on AS9100 (estimate). The vendor field is Net-Inspect, DISCUS, High QA, InspectionXpert and GroundControl (YC, 70+ facilities and almost 1,000 reports a month by its own count). On 2026-10-24 GroundControl's YC page listed only an Account Executive, and the others showed no engineering openings that could be confirmed, so this is the right demo to take to quality managers but not yet a confirmed hiring lead. The vault already holds the CMM-to-Form-3 step as [[niches/contract-manufacturing/aerospace-precision-machining/build|CMM-to-FAI Automated Report Generation]].

---

## 2. Government Spare-Parts Bid Agent
#ai-agent #large-language-models #gradient-boosting #logistic-regression #revenue-impact #automation

**Concept:** An agent that reads every new DLA and military-service solicitation in the shop's federal supply classes, screens each for approved-source restrictions, technical data availability, first article test requirements and specialty-metals clauses, estimates cost and win probability from the shop's job history and public award history, and drafts the quote for the estimator to approve before the close date.
**Inputs:** DIBBS and SAM.gov solicitations, NSN and CAGE cross-references, technical data packages, award history, the shop's routings, capacity and job actuals.
**Outputs / Actions:** Bid/no-bid list with the reason; priced draft quotes; source approval request drafts where a part is worth qualifying for; a won/lost ledger that improves the price model.
**Why now:** Solicitation text and technical data can be read and cross-checked by LLMs at the volume DLA publishes, and award history is public, so the screen that used to take an estimator's morning can run overnight.
**Market:** Small and mid-size suppliers and distributors that sell to DLA, plus the primes' spares groups. **SalesPatriot** (YC W25, San Francisco and Warsaw) is the hiring lead: on 2026-10-24 its YC page listed a Lead Forward Deployed Engineer ($150K–$200K), a Forward Deployed Engineer ($100K–$135K, new grads OK) and a Full Stack Engineer ($150K–$200K) in San Francisco, and its own careers page listed the FDE and Full Stack roles. Its site cites Echelon Supply & Service and FDH Aero as customers and an October 2026 sustainment partnership with S&K Aerospace. Bid tools such as Cleat.ai, BidPulsar, SAM Search and Starbridge compete on finding solicitations; the contest is who lifts awards per quote.

---

## 3. Sub-Tier and Outside-Processing Control Tower
#ai-platform #survival-analysis #gradient-boosting #time-series-forecasting #data-integration #workflow-orchestration

**Concept:** A platform that tracks every lot through outside heat treaters, platers, NDT and coating houses, predicts completion dates from each processor's real history, chases status automatically by email and portal, and answers each prime's delinquency list with dates that hold. Upstream, it maps which sub-tier processors and material sources each part depends on, so a processor losing Nadcap accreditation or a mill delay shows up as named at-risk lines.
**Inputs:** ERP routings and lot moves, processor emails and portals, Nadcap accreditation status, customer portals and need dates, material receipts and certs.
**Outputs / Actions:** Predicted dates per lot and line; automated status requests; pull-forward and alternate-processor proposals; drafted delinquency responses; sub-tier risk alerts.
**Why now:** Rate breaks at Boeing (the 737 moving from 42 to 47 a month in 2026 with more planned, per its 10-Q) and Airbus's Pratt & Whitney engine shortage have made supplier on-time delivery a board topic, and agents can now read processor emails and drive portals that never got APIs.
**Market:** Tier-2 and tier-3 suppliers and the primes' supplier-management teams. Hiring leads confirmed on their own boards on 2026-10-24: **First Resonance** (ION, used by aerospace and space hardware makers) listed Forward Deployed Engineer roles in Los Angeles (Data and Integrations, $150K–$190K; an FDE Engineering Leader, $180K–$220K), Ohio ($130K–$170K) and Forward Deployed Software Engineer roles in San Francisco, Seattle and New England ($145K–$175K). **Exiger**, which maps defence industrial base supply chains, listed Forward Deployed Engineers in Huntsville, Alabama and South Ogden, Utah, a Lead FDE in Huntsville and a Senior FDE in McLean. The multi-tier mapping archetype is indexed as [[niches/contract-manufacturing/supply-chain-risk-intelligence/profile|Multi-Tier Supply Chain Risk Intelligence]].

---

## 4. Drawing-to-Quote Platform for Aerospace Job Shops
#ai-platform #cnns #gradient-boosting #feature-engineering #revenue-impact #automation

**Concept:** A platform that reads an RFQ package of drawings, models and PO terms, extracts features and requirements, proposes a routing including outside special processes and FAI cost, and prices it from the shop's own job actuals. It records every quote and outcome, so estimates converge on what jobs really cost.
**Inputs:** RFQ emails and portals, drawings and STEP models, material price feeds, the shop's routings, job actuals and won/lost history.
**Outputs / Actions:** Priced, routed quotes; flags for requirements that add cost (Nadcap processes, tight true position, source-controlled material); a quote-versus-actual ledger by part family.
**Why now:** 3D and drawing understanding has reached the point where routing proposals are useful, and tier-1s are re-sourcing detail parts to new suppliers as rates climb.
**Market:** AS9100 machine shops and the custom-parts networks that route work to them. **Paperless Parts** listed a Platform Engineer II, a VP of Engineering and Services Engineers on its Greenhouse board on 2026-10-24. **Vendra** (YC S24, ITAR-registered custom-parts network for aerospace and defence) listed a Full Stack Engineer ($100K–$140K) and a Cloud Infrastructure & Security Engineer ($130K–$150K). CADDi showed engineering roles only on aggregators; Hadrian's own Ashby board (hadrian-automation) lists a Forward Deployed Engineer in Los Angeles at $223K–$359K. The estimating archetype for general fabrication sits in [[niches/metal-fabrication/estimating-and-quoting-automation/profile|Estimating & Quoting Automation]].
