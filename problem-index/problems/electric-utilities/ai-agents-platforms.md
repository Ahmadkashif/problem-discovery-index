# AI Agents & Platform Opportunities — Electric Distribution Utilities

**Industry:** [[electric-utilities|Electric Distribution Utilities]]

---

## 1. Capacity Screening and Interconnection Platform
#ai-platform #gradient-boosting #graph-neural-networks #large-language-models #tacit-knowledge-ml #data-integration #revenue-impact

**Concept:** A platform that answers "can this feeder take it, and what will it cost?" for every new load or generator request in seconds. It does this by learning from the utility's past study outcomes, feeder loading and the senior planners' recorded quick reads. It runs intake for DER and large-load requests, ranks requests by likelihood of being real, routes only the uncertain ones to full study, and keeps a hosting-capacity map that is checked against what studies actually find. It runs inside the utility's environment because network models are protected infrastructure data.
**Inputs:** Historical study reports, network models (CYME, Synergi, OpenDSS), SCADA and AMI loading, DER registry, request applications and stage gates; public EIA-861, EIA-860, FERC Form 1 and hosting-capacity map data for the territory-level layer.
**Outputs / Actions:** Instant screen per request (fit probability, binding constraint, upgrade cost range, similar past studies); prioritised study queue; refreshed hosting-capacity layers; developer-facing pre-application estimates; commission-ready records of how each request was screened.
**Why now:** Load is growing again: data centres are projected at 6.7%–12% of US electricity by 2028 (LBNL for DOE). Language models can finally extract decades of study PDFs into training data, and vendors are staffing up to deploy this. Gridsight lists a Founding Forward Deployed Engineer for its grid intelligence platform, GridUnity is hiring full-stack and staff engineers for interconnection software, and E Source has forward deployed AI/ML and data engineering roles in its Grid & Operations group (all on their own ATS pages, 2026-10-24). A two-week demo for those teams can ingest published hosting-capacity maps and add territory context from EIA-861, EIA-860 and FERC Form 1. It cannot replicate the study-trained screen, because no public source holds study outcomes.
**Market:** Distribution planning and interconnection departments at ~170 investor-owned utilities and the larger public power and co-op systems; smaller co-ops through their generation-and-transmission cooperatives. The buyer category exists (interconnection portals, planning software, grid analytics) and is contested by Gridsight, Kevala, envelio, GridUnity, PowerClerk and the planning-software incumbents.

---

## 2. Storm Restoration Command Agent
#ai-agent #gradient-boosting #random-forests #time-series-forecasting #large-language-models #workflow-orchestration #worker-facing

**Concept:** An agent for the storm centre that predicts damage and outages by area two to three days before landfall and recommends mutual-assistance crew requests and staging sites. During restoration it regroups outage predictions from AMI pings and crew reports, drafts switching sequences for operator approval, proposes restoration times per area, and logs every released crew and hour for later cost recovery.
**Inputs:** Weather forecasts, vegetation and asset data, OMS history, live AMI last-gasp and restore messages, crew rosters and check-ins, drone and patrol imagery, mutual-aid agreement terms.
**Outputs / Actions:** Pre-storm crew requirement with uncertainty; staging plan; live fault-location groupings; draft switching orders; restoration-time updates for customer communications; a storm cost file mapped to commission prudence schedules or FEMA Public Assistance categories.
**Why now:** Major events drove 80% of 2024 outage hours (EIA), cheap inference makes live regrouping of millions of meter messages practical, and inspection vendors now read storm imagery automatically. Buzz Solutions is hiring a Senior Forward Deployed Engineer and computer vision engineers for grid-asset inspection, and Neara (network digital twins with storm modelling) is hiring US geospatial data science and risk research roles.
**Market:** Storm and emergency management and operations leaders at utilities in hurricane, ice and wildfire territory. Outage management and ADMS vendors are the incumbents; the restoration-time and staging layer is not owned.

---

## 3. Rate Case Discovery and Testimony Consistency Agent
#ai-agent #bert #large-language-models #transformers #compliance #workflow-orchestration #automation

**Concept:** An agent that receives every data request served in a case, routes it to the responsible witness, retrieves prior answers and workpapers from the utility's archive and from public commission dockets, drafts a response, checks it against pre-filed testimony and every answer already served, and tracks procedural deadlines.
**Inputs:** Served data requests; testimony, exhibits and minimum filing requirement schedules; prior responses across cases and jurisdictions; witness list; procedural schedule.
**Outputs / Actions:** Routed requests with drafts; inconsistency alerts; deadline dashboard; confidentiality tier flags; a searchable archive that grows with every case.
**Why now:** Rate requests hit a record in 2025 (nearly $31B, PowerLines). Affordability scrutiny makes every answer a potential disallowance, and language models can now read the account-coded, schedule-referenced language of rate cases. No vendor in the census was hiring specifically for this.
**Market:** Regulatory affairs and rates departments at investor-owned utility holding companies; the outside consultancies and law firms that run discovery for smaller utilities are a second channel. There is no established product category, only e-discovery and docket tools.

---

## 4. High-Bill and Assistance Agent
#ai-agent #large-language-models #gradient-boosting #feature-engineering #worker-facing #compliance

**Concept:** An agent that sits beside customer service representatives and in self-service channels. It explains each bill from the customer's interval data, weather and rate history, detects likely read or meter problems, checks eligibility for payment arrangements, budget billing, assistance programmes and state disconnection protections, and drafts the arrangement or application for confirmation.
**Inputs:** Billing and payment history, AMI interval data, rate schedules and their effective dates, weather, state disconnection rules and assistance programme criteria.
**Outputs / Actions:** Plain-language bill explanation; meter or read exception tickets; recommended arrangement or programme with drafted paperwork; proactive outreach lists before disconnection notices go out.
**Why now:** Record rate increases are reaching bills, language models can explain interval data in plain words, and commissions are scrutinising disconnections and arrears. Bidgely and Uplight sell meter analytics and customer engagement here, though Bidgely's open engineering roles are in India.
**Market:** Customer operations and credit and collections leaders at utilities of every size; billing and engagement vendors are the incumbents, and the assistance-eligibility layer is mostly manual.
