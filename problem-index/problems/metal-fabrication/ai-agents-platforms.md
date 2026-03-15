# AI Agents and Platforms — Metal Fabrication

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Tags:** #ai-agent #ai-platform #automation #compliance #revenue-impact #tacit-knowledge-ml

---

## Existing AI-Adjacent Platforms

### Hypertherm ProNest / Lantek
CNC nesting software for plasma, laser, and waterjet cutting optimization. ProNest is the market leader for plasma/oxy-fuel; Lantek for fiber laser. Both generate detailed cut programs, nesting layouts, and material utilization reports. Integration target for remnant tracking, material waste analytics, and quote material cost estimation.

### Lincoln Electric CheckPoint / Miller ArcReach
Welding machine data logging platforms from the two dominant welding equipment manufacturers. CheckPoint logs weld parameters (amperage, voltage, wire feed speed, arc time) per weld operator and job. The primary data source for weld process compliance documentation and welder productivity analytics. REST API available on newer installations.

### SDS/2 / Tekla Structures
Structural steel detailing platforms used by structural fabricators. SDS/2 and Tekla generate BOMs, connection details, and weld takeoffs from structural models. The geometry and weld quantity data from these platforms is the input for distortion prediction and labor estimation models.

### JobBOSS / Prodsmart (Job Shop ERP)
Job shop ERP platforms tracking job status, actual vs. quoted hours, material usage, and job cost. The historical actuals database for quote estimation models and job profitability analytics. JobBOSS has a REST API; Prodsmart has real-time production floor tracking integration.

---

## AI Agent Opportunities

### 1. Quote Generation Agent
**Trigger:** New RFQ (request for quote) received with drawing files attached (DXF/PDF).
**Action sequence:**
1. Parse drawing files: extract part geometry, weld symbols, material specification, tolerance callouts, and quantity
2. Classify job type and identify similar historical jobs from the quote database
3. Run labor estimation model: generate operation-by-operation time estimate (fit-up, weld-out, distortion correction, inspection) with confidence intervals
4. Run material cost calculation: query remnant inventory for matching stock; quote new material if no remnant available; apply historical waste factor for this job type
5. Generate draft quote with itemized cost breakdown and 3 most similar historical jobs for estimator reference review
**Value:** Reduces quote generation time from 30-60 minutes to 10-15 minutes of estimator review and adjustment. Surfaces historical quoting patterns — which job types the shop consistently under- or over-estimates — in the quote review interface.

### 2. Weld Process Compliance Documentation Agent
**Trigger:** Job completed (all weld passes logged in CheckPoint / ArcReach).
**Action sequence:**
1. Pull weld parameter log for all welds on the job from CheckPoint/ArcReach API
2. Match each weld record to the applicable Welding Procedure Specification (WPS) from the job router
3. Check parameter compliance: amperage, voltage, wire feed speed, preheat temperature, interpass temperature within WPS limits for each weld pass
4. Flag any out-of-parameter welds with pass ID, operator, deviation magnitude, and WPS reference
5. Generate weld quality record with compliance attestation for customer submittal and internal quality records
**Value:** Eliminates 2-4 hours of manual weld log review per job on AWS D1.1 or ASME Section IX work. Ensures 100% parameter compliance check coverage (manual review often samples). Generates customer-ready compliance documentation automatically at job completion.

### 3. Production Schedule Load Balancing Agent
**Trigger:** Daily at shift start; also triggered when a new job is added to the active queue.
**Action sequence:**
1. Pull current job queue from ERP: all active jobs with operation status, remaining hours, and due dates
2. Pull work center capacity: available hours per operator per station (plasma, press brake, fit-up, welding, finishing) for the next 5 days
3. Score each job by on-time delivery risk: remaining work hours vs. available capacity vs. due date, accounting for operation sequence constraints
4. Identify bottleneck work centers and flag jobs at delivery risk with specific constraint (e.g., "3 jobs require 47 welding hours; 32 hours available in the next 3 days")
5. Suggest resequencing or overtime allocation options to the shop manager
**Value:** Converts daily shop scheduling from informal manager judgment to structured constraint analysis. Identifies delivery risks 3-5 days before they become crises, enabling proactive customer communication and overtime or subcontracting decisions.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Weld visual inspection model | Build | Camera hardware (infrastructure) | CNN fine-tune on weld surface images is custom per standard |
| Quote labor estimation | Build | JobBOSS/Prodsmart actuals (data) | Regression on drawing features is custom |
| Weld parameter compliance check | Build | CheckPoint/ArcReach API (data) | WPS matching and parameter check logic is custom |
| Remnant tracking and matching | Build | ProNest output files (data) | Matching algorithm + inventory integration is custom |
| Distortion prediction | Build | FEA simulation outputs (training data) | Surrogate model is custom |
| Schedule load balancing | Build | ERP capacity data | Constraint analysis and resequencing logic is custom |
