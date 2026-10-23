# AI Agents & Platform Opportunities — Ocean Shipping Carriers

**Industry:** [[ocean-shipping-carriers|Ocean Shipping Carriers]]

---

## 1. Booking and Bill-of-Lading Document Agent
#ai-agent #large-language-models #transformers #automation #data-integration #quick-win

**Concept:** An agent that reads booking requests and shipping instructions from email, PDF, spreadsheet or portal, creates or updates the booking, drafts the bill of lading in the carrier's system or the DCSA eBL schema, reconciles it with the booking and cargo rules, and sends the shipper a draft with doubtful fields highlighted. Exceptions go to a documentation agent with the reason attached; clean SIs go straight through.
**Inputs:** SI and booking emails and attachments; booking records; shipper history and past amendments; party master data; dangerous goods, reefer and manifest rules by trade lane.
**Outputs / Actions:** Booking drafts; draft and final B/L data; exception queue with reasons; shipper confirmation messages; amendment-risk flags; a log of every field changed and why.
**Why now:** LLMs read free-form shipping instructions accurately enough to draft rather than merely extract. DCSA's open booking and eBL standards give a target schema, and the carriers' pledge to issue 50% of bills electronically within five years and all of them by 2030 forces the data to be structured anyway.
**Market:** Carriers' documentation centres, NVOCCs that issue their own house bills, and forwarders sending SIs. Agent vendors are hiring engineers for this kind of deployment now, checked on their own boards or YC job page on 2026-10-24. Pallet lists Software Engineer, Agent Delivery (San Francisco, $135,000–$180,000) and Deployment Strategists (San Francisco or New York) and names ocean carriers among its segments. Reform (YC W24) lists two Forward Deployed Engineer roles (San Francisco, $125K–$175K) and already extracts bills of lading for forwarders. Flexport lists a Forward Deployed Engineer, Supply Chain Solutions (San Francisco). Sedna lists Senior Delivery Engineers in London and Athens. The two-week MVP turns a booking-request email into a booking, then turns the shipper's SI into a draft B/L against the confirmed booking. It runs on synthetic documents and the public DCSA schemas, because real SIs and bills belong to shippers, forwarders and the carrier.

---

## 2. Demurrage and Detention Billing Compliance Agent
#ai-agent #large-language-models #logistic-regression #compliance #workflow-orchestration #automation

**Concept:** An agent that rebuilds each container's free-time clock from contract or tariff terms, terminal availability, holds and vessel events. It issues invoices that carry every 46 CFR 541 element inside the 30-day window, and it triages disputes by reason with the milestone evidence attached and a drafted response, tracking each against the 30-day resolution limit.
**Inputs:** Contract and tariff free-time terms; container milestones from carrier systems and visibility feeds; terminal closures and appointment availability; customs holds; dispute emails.
**Outputs / Actions:** Compliant invoices or a decision not to bill; certification evidence packs; dispute classifications, evidence and draft replies; root-cause reports on charges repeatedly waived.
**Why now:** The 2024 FMC rule made late or incomplete invoices void and put every dispute on a clock. Container event data from DCSA interfaces and visibility vendors is now good enough to rebuild the clock automatically.
**Market:** Ocean carriers and NVOCCs billing in US trades; marine terminal operators' own demurrage billing belongs to the queued port-terminal-operators industry. Portcast (Singapore) lists a Senior Machine Learning Engineer and project44 a Senior Forward Deployed Engineer (Chicago), both on their own boards. Neither sells billing compliance today; both hold the milestone data it needs.

---

## 3. Allocation and Booking-Materialisation Platform
#ai-platform #gradient-boosting #survival-analysis #evaluation-metrics #tacit-knowledge-ml #revenue-impact

**Concept:** A platform for liner trade desks that logs every acceptance, overbooking, protect and roll decision with a one-click reason. It scores each booking's probability of loading on its sailing, recommends an overbooking level per sailing with the customers driving the risk, and grades desks and model weekly against what loaded.
**Inputs:** Booking and load history; customer and forwarder behaviour; rate paid against index rates (Drewry WCI, Xeneta, Freightos FBX); competitor capacity and blank sailings; desk decisions.
**Outputs / Actions:** Booking-level load probabilities; sailing overbooking recommendations; roll-candidate lists that protect key accounts; desk scorecards; handover packs when a trade manager moves.
**Why now:** Cheap drafting of structured decision records from chat and booking context makes capture possible without asking desks to type. Late-2026 overcapacity as Red Sea routings reopen makes every empty slot costlier.
**Market:** The top container lines and regional carriers. Ten carriers hold most capacity and the large ones build in-house, so this sells as an embedded build or to mid-sized carriers without revenue-management teams. No vendor was found hiring for carrier revenue management specifically. Xeneta, whose benchmarks feed the model, lists a Senior Data Engineer (Oslo, Hamburg, London or Bucharest).

---

## 4. Vessel Emissions and Performance Reporting Agent
#ai-agent #gaussian-processes #large-language-models #compliance #worker-facing #automation

**Concept:** An agent on board and ashore that takes each figure once (soundings, flow meters, engine data, bunker delivery notes) and generates noon reports, charterer formats, EU MRV and ETS records, FuelEU data and IMO DCS submissions. It checks every figure against a weather-corrected baseline before it leaves the ship and keeps a verifier-ready audit trail toward the 31 March and 30 September dates.
**Inputs:** Ship sensor and noon data; weather hindcasts; bunker delivery notes; voyage records; monitoring plans.
**Outputs / Actions:** All recurring reports from one record; consistency flags in plain language; verifier evidence packs; allowance and FuelEU balance forecasts per ship.
**Why now:** The EU ETS reaches 100% of 2026 emissions and FuelEU Maritime has applied since 2025 (search summary), so emissions data now carries money. Satellite bandwidth on ships has improved enough for continuous sync (estimate).
**Market:** Shipowners, ship managers and operators. ZeroNorth, Kongsberg, StormGeo and the class societies compete. On its own careers page ZeroNorth lists only optimisation analyst roles in Mumbai and Chennai, not engineers. Windward (Applied AI Engineer, Tel Aviv), Kpler (engineers in London, Athens, Paris and Singapore) and Marcura (Senior Back-End Engineer, Dubai and Athens) are the maritime data vendors with engineering roles open.
