# AI Agents and Platforms — Roofing Contractors

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### EagleView / Nearmap
Aerial measurement platforms that provide roof geometry (facet area, pitch, ridge/hip/valley linear feet) from satellite and aerial imagery. EagleView's AI-powered condition assessment provides general roof condition scoring. Neither platform provides insurance damage classification at the granularity required for claim supplementing — their AI is optimized for property insurance portfolios, not contractor claim negotiation.

### AccuLynx
Leading roofing CRM with EagleView integration for measurement import, material takeoff calculation, and insurance claim tracking. AccuLynx's own AI features are limited to basic automation. All claim and job data lives here — the integration point for any AI supplement or lead scoring tool.

### CompanyCam
Photo documentation platform widely used in roofing. Organizes job photos by project. No damage classification or compliance checking AI. Integration point for any photo-based AI model.

### Xactimate (Verisk)
Insurance industry standard estimating platform. All supplement negotiations happen in Xactimate format. A supplement generation AI must output Xactimate-compatible line items and scope narratives.

---

## AI Agent Opportunities

### 1. Post-Storm Lead Generation Agent
**Trigger:** NOAA or commercial hail alert for a geographic area within the firm's service radius.
**Action sequence:**
1. Pull hail size and path data for the event (CoreLogic or Verisk hail verification)
2. Query property database (county assessor) for properties in the storm footprint with roof age > 10 years
3. Score each property by claim probability (hail size × roof age × property type)
4. Generate ranked canvas routes for available sales reps
5. Push routes to reps' phones via AccuLynx or CRM
**Value:** Sales reps begin canvasing the highest-probability neighborhoods within hours of a storm event, before competitors arrive.

### 2. Insurance Supplement Generation Agent
**Trigger:** Estimator marks inspection complete and uploads damage photo set.
**Action sequence:**
1. Run damage classification model on all inspection photos
2. Map classified damage types to Xactimate line items using the plumbing contractor supplement knowledge base
3. Cross-reference against carrier-specific approval history to flag commonly contested items
4. Draft the supplement scope narrative with damage descriptions and code citations for each line item
5. Return a draft supplement package to the estimator for review before submission
**Value:** Reduces supplement writing from 60-90 minutes per claim to a 10-minute review task. Captures line items the estimator would have missed.

### 3. Manufacturer Warranty Compliance Agent
**Trigger:** Crew submits installation milestone photos during job.
**Action sequence:**
1. Run compliance classification on each photo against the relevant warranty tier's installation requirements
2. Flag non-compliant photos immediately with specific defect description
3. Allow crew to re-photograph after correction before proceeding
4. Generate end-of-job compliance report with all checkpoint photos and compliance status
5. Submit compliance report to manufacturer warranty portal
**Value:** Catches installation defects before the job is closed, when rework is least disruptive. Reduces warranty claim denials due to documentation failure.

### 4. Material Order Agent
**Trigger:** Estimator approves material takeoff after customer signs contract.
**Action sequence:**
1. Import EagleView measurement report
2. Apply contractor-configured waste factors by roof complexity tier
3. Pull current distributor pricing from preferred supplier portal
4. Generate itemized material order with quantities and cost
5. Submit to preferred distributor or flag for estimator review if price exceeds budget threshold
**Value:** Eliminates manual takeoff calculation errors. Reduces material ordering to a 2-minute approval workflow.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Hail damage photo classification | Build | — | No existing product at inspection-photo granularity |
| Aerial condition scoring | Buy/integrate | EagleView/Nearmap (limited) | Extend with custom damage overlay model |
| Supplement line-item prediction | Build | — | Requires carrier-specific claim history |
| Storm canvas lead scoring | Build | Partial (CoreLogic hail data) | Feature pipeline is custom; model is straightforward |
| Material takeoff calculation | Integrate | AccuLynx + EagleView | Existing integration; waste factor customization is the gap |
| Photo organization/classification | Build | CompanyCam API | Classification model is custom |
| Warranty compliance checking | Build | — | Manufacturer specs define labeling criteria |
