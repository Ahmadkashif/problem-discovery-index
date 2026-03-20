# AI Agents and Platforms — Plumbing Contractors

**Industry:** [[plumbing-contractors|Plumbing Contractors]]
**Tags:** #ai-agent #ai-platform #cnns #gradient-boosting #large-language-models #survival-analysis #transfer-learning #feature-engineering #evaluation-metrics #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### ServiceTitan
The dominant field service management platform for residential and commercial plumbing. Contains service call history, customer records, technician dispatch, price books, and invoice data. All ML projects using plumbing service data are most naturally built as ServiceTitan integrations or data exports. ServiceTitan's own AI features (as of 2025) cover basic scheduling optimization and marketing automation — no craft-skill or diagnostic AI.

### RIDGID SeeSnake
The leading residential sewer inspection camera platform. Footage is recorded locally on the operator's device. No automated defect detection exists on the platform. A partnership or API integration with RIDGID would be the distribution path for a sewer inspection AI model.

### WinCan / Envirosight
Municipal sewer inspection software with AI-assisted defect annotation for large-diameter infrastructure pipe. The residential and light-commercial pipe diameter gap (3"–6") is unserved. WinCan's PACP coding framework is the appropriate defect taxonomy to adopt for any residential sewer AI.

### FieldEdge / Jobber / Housecall Pro
Secondary field service management platforms with smaller plumbing contractor market share. Same data architecture as ServiceTitan — service history, dispatch, invoicing. An AI product should target the ServiceTitan API first, then expand.

---

## AI Agent Opportunities

### 1. Sewer Inspection Report Generation Agent
**Trigger:** Technician completes a sewer camera run and marks the job complete in the field app.
**Action sequence:**
1. Ingest the inspection footage from the camera device or cloud sync
2. Run the sewer defect detection model (per-frame PACP classification + severity scoring)
3. Aggregate frame-level detections into a position-based condition report (defect list, footage timestamp, linear foot position)
4. Generate a customer-facing written inspection report (plain language defect descriptions, recommended action tiers: monitor / schedule repair / urgent)
5. Push the completed report to ServiceTitan job notes and email the customer PDF copy automatically
**Value:** Eliminates 20-30 minutes of post-inspection report writing per camera run. Converts raw footage into a deliverable before the technician drives away.

### 2. Predictive Maintenance Outreach Agent
**Trigger:** Weekly scheduled run against customer database.
**Action sequence:**
1. Query ServiceTitan for all customers with water heater age > 8 years or prior drain service > 18 months ago
2. Score each customer on replacement/service probability using the predictive maintenance model
3. Generate personalized outreach messages for the top-20% risk customers (water heater age, last service date, seasonal framing)
4. Queue outreach in the firm's CRM/SMS platform for owner review and approval
5. Log outreach attempts and customer responses back to customer record
**Value:** Converts a static customer database into a proactive revenue pipeline. Targets customers who are likely to need service before they call with an emergency.

### 3. Quote Generation Agent
**Trigger:** Technician submits a voice note or typed scope description from the field.
**Action sequence:**
1. Transcribe voice input (Whisper or similar ASR)
2. Parse the scope description into structured task codes using the plumbing scope taxonomy (e.g., "water heater replacement 40G gas + expansion tank + permit" → specific labor units + materials list)
3. Pull current material costs from the contractor's price book
4. Generate three tiered quote options (good/better/best) with line-item breakdowns
5. Return quote draft to the dispatcher interface for review and customer presentation
**Value:** Reduces quote generation from 10-15 minutes to under 2 minutes. Enables field quoting without dispatcher involvement on straightforward jobs.

### 4. Permit Lookup and Filing Agent
**Trigger:** New job created in ServiceTitan with a permit-required job type.
**Action sequence:**
1. Identify job type and jurisdiction from the job record
2. Query the permit requirements database for the specific job type + municipality combination
3. Return permit requirement decision (required/not required), fee, inspection type, and typical approval timeline
4. If required: pre-fill the permit application form with job and contractor data
5. Flag jobs missing permit applications 48 hours before scheduled start date
**Value:** Eliminates building department hold time for permit lookups. Reduces permit compliance errors on jobs in unfamiliar jurisdictions.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Sewer defect detection model | Build | — | No existing product for residential diameters |
| Acoustic fault classification | Build | — | No existing labeled dataset or product |
| Service call outcome prediction | Build | — | ServiceTitan data export → custom model |
| Quote generation agent | Integrate | ServiceTitan AI / custom LLM layer | Scope taxonomy is the differentiator |
| Predictive maintenance outreach | Build | — | Requires ServiceTitan data + custom survival model |
| Permit lookup database | Buy/integrate | PermitFlow (partial) | Residential plumbing job types are a gap |
| Documentation automation | Integrate | LLM + ServiceTitan API | Voice-to-report is the differentiator |

---

## Data Infrastructure Requirements

A plumbing contractor implementing any of the above AI capabilities needs:
- ServiceTitan data export or API access (service history, customer records, job outcomes)
- Sewer camera footage organized by job ID and linked to ServiceTitan records
- Equipment photo library with model label OCR for materials installed tracking
- Structured warranty configuration (parts warranty by manufacturer + labor warranty policy)

The firms best positioned to adopt plumbing AI are those already running ServiceTitan with disciplined service code usage — the data quality exists, the integration pathway is defined.
