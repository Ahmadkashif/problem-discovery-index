# AI Agents & Platform Opportunities — Proptech Platforms

**Industry:** [[proptech-platforms|Proptech Platforms]]

---

## 1. Leasing Response Agent
#ai-agent #large-language-models #transformers #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #worker-facing

**Concept:** An agent that answers every rental enquiry within seconds, at any hour, in whatever channel it arrived. It answers the actual question from live listing and availability data, qualifies naturally through conversation — move date, budget, occupancy, pets — books a tour into the agent's real calendar or issues self-guided access where supported, and runs the follow-up sequence itself. It escalates to the agent when a prospect asks something it should not answer, when the conversation turns substantive, or when qualification is ambiguous.

**Inputs:** Enquiry text from listing syndication, web forms, SMS and voice; live unit availability and pricing; property policies; agent and self-tour calendars; historical conversion patterns by lead source and prospect profile.

**Outputs / Actions:** Immediate qualified responses. Booked tours. Scheduled, timed follow-up rather than weekly chasing. Structured prospect records with stated requirements. Escalation to the agent with full context. It never quotes a price or a policy that is not live in the system, and it never makes a representation about eligibility.

**Why now:** Speed to lead is the strongest controllable driver of leasing conversion and has always been bounded by whether a human was at the desk. Conversational qualification is now reliable enough to run unsupervised on routine enquiries, and the escalation boundary is easy to draw conservatively.

**Market:** Every property management platform, and multifamily operators directly. Occupancy is the number the entire business runs on, which makes the value statement short. Roughly 20 million professionally managed US rental units.

---

## 2. Turnover Orchestration Agent
#ai-agent #gradient-boosting #time-series-forecasting #convex-optimization #evaluation-metrics #workflow-orchestration #automation #worker-facing

**Concept:** An agent that runs the make-ready from notice-to-vacate to listing. It predicts the likely scope from the unit's age, tenancy length, work order history and inspection comparison, sequences the tasks with their dependencies, books vendors against their real availability, and publishes a ready date that leasing can commit to. When a scope surprise appears it re-sequences and re-books automatically rather than waiting for the site manager to work the phone. The manager sees exceptions only: a vendor who did not show twice, a scope materially larger than predicted, a turn that will miss its date and what that costs.

**Inputs:** Notice to vacate; unit history and age; move-in and move-out inspections with photographs; work orders during tenancy; vendor availability and historical lead times; leasing demand for the unit type.

**Outputs / Actions:** A sequenced make-ready plan with vendor bookings and a committed ready date. Automatic re-planning on scope change or vendor failure. Vendor confirmations and reminders. Listing date synchronisation with leasing. Exception alerts with cost attached. It books work within pre-authorised scope and price limits and escalates anything beyond them.

**Why now:** Inspection photography through platform apps has become standard, which makes scope prediction possible for the first time. The scheduling itself was always classical optimisation waiting on an honest duration estimate.

**Market:** Multifamily and single-family rental operators of any scale, sold through the platform vendors. Days vacant is a headline portfolio metric, which makes the payback directly computable from the operator's own reporting.

---

## 3. Screening Compliance Platform
#ai-platform #large-language-models #bert #transformers #change-point-detection #compliance #workflow-orchestration #automation

**Concept:** A platform that maintains jurisdiction-correct screening criteria for every property in a portfolio. It continuously monitors state, county and municipal code changes and ordinance adoptions relevant to tenant screening — criminal history restrictions and lookback limits, individualised assessment requirements, source-of-income protections, application fee caps, notice requirements — extracts the operative rule, and flags every affected property. It also provides the structure the individualised assessment requirement demands, so that where a jurisdiction requires the landlord to consider nature, recency and relevance before denying, the process is documented per applicant rather than handled in email.

**Inputs:** Municipal and county code repositories, ordinance adoption feeds, state legislative trackers, fair housing enforcement guidance; the operator's property locations; current screening configurations.

**Outputs / Actions:** A rule change queue with the extracted requirement, the affected properties and a proposed configuration change, always for legal review rather than automatic application. A per-property compliance posture view. Structured individualised assessment workflow with documented reasoning and retained records. Adverse action notices generated to jurisdiction-specific requirements.

**Why now:** Screening rules have fragmented to city level over the last several years, past the point where any operator can track them by hand, and municipal code is public, machine-readable in aggregate, and completely unmonitored. Extraction from legal text is now good enough that review is faster than research.

**Market:** Property management platform vendors and large multifamily and single-family operators. The buyer is general counsel rather than operations, which is a different and generally faster budget. The failure it prevents is a fair housing action, not an inefficiency, which changes how the value is argued.
