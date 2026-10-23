# AI Agents & Platform Opportunities — Facilities Management Firms

**Industry:** [[facilities-management-firms|Facilities Management Firms]]

---

## 1. Building Memory Platform
#ai-platform #tacit-knowledge-ml #lstms-and-grus #large-language-models #worker-facing #revenue-impact

**Concept:** A platform that turns each building's scattered record (BAS trends, alarms, work orders, PM history, subcontractor reports and the engineers' own spoken notes during rounds) into a living memory attached to every asset. It briefs the technician at the equipment, drafts the close-out from what the technician says, and over time learns the early-warning patterns the experienced engineers annotate. It produces a handover pack that keeps the plant's knowledge when staff retire or the account changes hands.
**Inputs:** BAS trend exports, CMMS work orders and PM records, asset registers, subcontractor inspection reports, voice notes from technicians, photos.
**Outputs / Actions:** Asset briefings on the technician's phone, drafted close-outs with failure mode and cause, early-warning alerts ranked for the night shift, and transition handover packs per building.
**Why now:** Speech-to-text and language models make capture nearly effortless for a technician with full hands, and time-series models can now run on the trend data most large buildings already log. Meanwhile an ageing trade workforce has made the loss of building knowledge a recognised cost.
**Market:** Large IFM providers and the in-house facilities teams of hospitals, universities and federal campuses. CMMS vendors are the natural incumbents but sell work-order systems, not memory.

---

## 2. Service Desk Triage Agent
#ai-agent #large-language-models #transformers #automation #workflow-orchestration

**Concept:** An agent that answers or reads every occupant request, asks the one clarifying question that settles priority, checks the site's recent work orders for a repeat, classifies trade and asset, and dispatches the right technician or subcontractor inside the SLA window, escalating to a human only on low confidence or safety risk.
**Inputs:** Calls, emails, portal and app requests; site and asset registers; contract priority definitions; technician schedules and locations; subcontractor rosters and rate cards.
**Outputs / Actions:** Classified, prioritised work orders; dispatches; occupant updates; flags for repeat failures; a daily list of tickets whose priority looks wrong.
**Why now:** Voice and text models can now hold a short triage conversation and classify reliably, and every large provider runs a national service desk whose staffing is a visible cost.
**Market:** IFM providers' service desks and in-house corporate help desks. Competes with CMMS vendors' intake modules and with offshore service-desk outsourcing.

---

## 3. Pass-Through Audit Agent
#ai-agent #large-language-models #gradient-boosting #k-nearest-neighbors #data-integration #revenue-impact

**Concept:** An agent that reads every subcontractor invoice as it arrives, checks it against the work order, the rate card, warranty and service-contract coverage and the not-to-exceed, compares it with similar jobs, and either approves it for rebilling, requests a correction from the subcontractor with the specific discrepancy, or routes it to a coordinator with the reason.
**Inputs:** Invoice PDFs and e-invoices, CMMS work orders, rate cards, warranty registers, contract pass-through and markup terms, dispute history.
**Outputs / Actions:** Approved invoices with an audit trail, correction requests sent to subcontractors, flagged outliers, and a monthly leakage report per account and per subcontractor.
**Why now:** Document-capable language models extract invoice lines reliably enough to automate the reading, and pass-through volumes at the largest providers now run to billions of dollars a year.
**Market:** IFM providers' account finance teams, and client-side real estate teams auditing their providers. Competes with AP automation suites and CMMS invoice modules, which check the NTE and not the contract.

---

## 4. CPARS Evidence Agent for Base-Operations Contracts
#ai-agent #large-language-models #bert #compliance #workflow-orchestration #revenue-impact

**Concept:** An agent for federal base-operations support contractors that maps every work order, inspection and QC record to the performance requirements and the government's quality assurance surveillance plan. It assembles monthly evidence of performance by rating element, warns when a trend is heading toward a Marginal rating, and drafts the contractor's response to each CPARS evaluation inside the 14-day comment window.
**Inputs:** Performance work statement and QASP, CMMS work orders and PM records, QC inspection results, government corrective action requests, prior CPARS narratives.
**Outputs / Actions:** Monthly performance evidence packs by rating element, early-warning reports to the program manager, draft CPARS rebuttals with cited evidence, and a past-performance narrative library for recompete proposals.
**Why now:** Language models can read performance work statements and map unstructured records to them, and the 14-day comment window means a contractor that cannot assemble evidence quickly carries a weaker past-performance record into every future bid.
**Market:** Federal BOS primes and the many small-business and joint-venture FM contractors on installation contracts. There is no established buyer category beyond general proposal-management tools.
