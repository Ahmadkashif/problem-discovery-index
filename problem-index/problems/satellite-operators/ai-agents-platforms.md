# AI Agents & Platform Opportunities — Satellite Operators

**Industry:** [[satellite-operators|Satellite Operators]]

---

## 1. Fleet Health Memory Platform
#ai-platform #tacit-knowledge-ml #autoencoders #survival-analysis #large-language-models #revenue-impact

**Concept:** A platform that sits beside the mission control system and turns the fleet's telemetry archive, anomaly reports and shift logs into a searchable fleet-health record. It surfaces drifting channels as a quiet ranked shortlist with the most similar historical signatures across the fleet, captures each engineer's flag or dismissal in two clicks, and estimates remaining life for wheels, batteries and amplifiers for the fleet planning and insurance teams.
**Inputs:** Housekeeping telemetry, command logs, anomaly reports, manufacturer correspondence, shift logs, component switch-overs and failures, insurance claims.
**Outputs / Actions:** Ranked precursor shortlist per shift; similar-case packs; structured anomaly records; remaining-life estimates; handover packs when engineers move or retire; evidence files for insurance notifications.
**Why now:** Cheap storage and modern sequence models make fleet-scale unsupervised baselines affordable, LLMs can turn decades of free-text anomaly reports into structured history, and fleet consolidation (SES and Intelsat combined in July 2025) has left operators running satellites whose history sits with another company's engineers.
**Market:** GEO and MEO fleet operators (SES, Eutelsat, Viasat, Telesat, regional operators) and growing LEO constellations; manufacturers' ground software and Kratos-type mission control vendors are the natural incumbents, selling limit checking rather than graded early warning.

---

## 2. Interference Case Agent
#ai-agent #cnns #k-nearest-neighbors #large-language-models #automation #workflow-orchestration

**Concept:** An agent that opens a case the moment carrier monitoring detects interference, classifies its type from the trace, retrieves similar past cases and repeat offenders, starts geolocation where possible, identifies the likely responsible operator or customer, drafts and sends the notification to that operator's NOC, and keeps the customer-facing timeline until the case closes.
**Inputs:** Carrier monitoring alarms and traces, Carrier ID decodes, frequency plans, customer terminal databases, the operator's case history, contact directories of other operators' NOCs.
**Outputs / Actions:** Classified case with likely source; geolocation request; outbound notifications; customer status updates; closure record and repeat-offender statistics.
**Why now:** Trace classification and similar-case retrieval are now cheap and reliable enough to run on every alarm, and LLMs can handle the drafting and chasing that consumes most of an interference engineer's night.
**Market:** Every GEO operator and large teleport; carrier monitoring vendors such as Kratos are adjacent sellers and possible partners. A modest, existing buyer category (interference management) with an unowned case workflow.

---

## 3. Orbital and Spectrum Filing Watch Agent
#ai-agent #large-language-models #transformers #compliance #workflow-orchestration #automation

**Concept:** An agent that reads every BR IFIC and FCC public notice, matches new filings against the operator's networks, ranks the ones requiring comment or coordination, computes each deadline, drafts the comment or coordination letter for the regulatory engineer, and keeps the calendar of FCC milestones, ITU bringing-into-use dates and coordination meetings tied to the launch schedule.
**Inputs:** BR IFIC special sections, the ITU space network database, FCC public notices and licences, the operator's filings and coordination agreements, launch manifests.
**Outputs / Actions:** Fortnightly relevance shortlist; computed deadlines; draft comments and letters; milestone alerts; a coordination file per counterpart administration.
**Why now:** The new FCC Part 100 rules (July 2026) reset milestone schedules for every new licence, filing volumes have grown with mega-constellations, and LLMs can now read filings' free-text and technical annexes alongside the structured data.
**Market:** Regulatory teams at operators of every size, ITU filing consultancies and the regulatory counsel who serve them; administrations that file on behalf of foreign operators.

---

## 4. Earth-Observation Order-to-Delivery Agent
#ai-agent #semantic-segmentation #cnns #bayesian-optimization #automation #worker-facing

**Concept:** An agent that takes an imagery order from intake to delivery: checks feasibility against the constellation's passes and the cloud forecast, plans and books the collection, runs target-level quality checks on each scene, passes clean scenes automatically, routes doubtful ones to an analyst with reasons, re-tasks failed collections, and confirms delivery against the customer's acceptance criteria.
**Inputs:** Customer orders and areas of interest, constellation pass predictions, weather and cloud forecasts, collected scenes and processing outputs, reference imagery and terrain, customer acceptance rules.
**Outputs / Actions:** Feasibility answers and quotes; collection plans; quality decisions; re-tasking; delivered products with quality reports.
**Why now:** Earth-observation constellations now collect far more scenes than analyst teams can review, and segmentation models for cloud and artefacts are accurate enough to clear most scenes without a human.
**Market:** Earth-observation operators (Planet, Vantor, BlackSky, Airbus, ICEYE, Capella, Umbra) and the marketplaces that resell their imagery; defence buyers set the strictest acceptance rules and the shortest delivery windows.
