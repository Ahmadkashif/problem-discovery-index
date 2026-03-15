# AI Agents and Platforms — Utility Contractors

**Industry:** [[utility-contractors|Utility Contractors]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #compliance

---

## Existing AI-Adjacent Platforms

### GSSI / Mala Ground Explorer
The leading GPR hardware platforms for subsurface utility detection. GSSI (General Dynamics Mission Systems' geophysics division) has the largest installed base in utility locating. Both platforms produce B-scan data files. GSSI has invested in AI-assisted data interpretation (as of 2025). These are the integration targets for GPR defect detection.

### WinCan / Envirosight
Municipal sewer inspection software with PACP-automated coding capabilities. WinCan AI and Envirosight AI Assist are the leading commercial AI-coded sewer inspection products. For utility contractors, these platforms handle the CCTV coding — the remaining gap is asset management integration.

### ESRI ArcGIS / Trimble
GIS and field data collection platforms. Trimble's field survey devices are the standard for GPS-located as-built data collection on utility construction. ArcGIS is the utility industry standard GIS platform. The as-built documentation pipeline automation bridges Trimble field data to ArcGIS deliverables.

### PHMSA Compliance Database
Federal Pipeline and Hazardous Materials Safety Administration regulation database. Pipeline operators are required to maintain records per 49 CFR Part 192/195. This is the compliance framework that all PHMSA compliance tools must map to.

---

## AI Agent Opportunities

### 1. As-Built Processing Agent
**Trigger:** Field crew marks utility construction segment complete and uploads GPS survey data.
**Action sequence:**
1. Receive GPS survey data file from Trimble or equivalent device
2. Apply the utility owner's attribute mapping schema to transform to the required GIS format
3. Generate GIS layer with all installed utility segments, manholes, and service connections
4. Produce preliminary as-built drawing set with standard symbology
5. Deliver to GIS technician for QA review — not creation from scratch
**Value:** Reduces as-built preparation from 1-3 days to a 2-4 hour review task. Accelerates final invoice submission timeline.

### 2. PHMSA Compliance Monitoring Agent
**Trigger:** Monthly scheduled run for all regulated pipeline assets.
**Action sequence:**
1. Pull all regulated assets from the asset registry with their classification (material, operating pressure, location class)
2. Compute required inspection frequencies per 49 CFR Part 192/195 for each asset class
3. Identify assets due for inspection in the next 30/60/90 days
4. Flag compliance gaps — assets past due for required inspection
5. Generate compliance calendar for the operations team with prioritized inspection list
**Value:** Eliminates the manual tracking burden for smaller gas distribution contractors without dedicated compliance staff. Keeps compliance status current between audit cycles.

### 3. GPR Survey Debrief Agent
**Trigger:** GPR survey crew completes a site scan and uploads B-scan data.
**Action sequence:**
1. Process B-scan data through the utility detection model
2. Overlay detected utilities on a plan view of the scanned area with depth estimates
3. Flag low-confidence detections and areas requiring re-scan
4. Generate preliminary utility location map for crew review
5. Operator confirms/corrects and submits final utility map for excavation clearance
**Value:** Extends the GPR operator's interpretation capability. Catches signatures the operator might dismiss as noise. Produces documentation of the pre-excavation survey for liability protection.

### 4. Patrol Anomaly Routing Agent
**Trigger:** Gas leak detection patrol crew submits photos from daily patrol.
**Action sequence:**
1. Screen patrol photos for gas migration visual indicators using classification model
2. Map flagged photo locations to the patrol route
3. Generate a priority list of flagged locations for instrument follow-up (CGI/FID deployment)
4. Log flagged and confirmed leak locations to the PHMSA-compliant leak survey record
**Value:** Focuses instrument-based leak detection on photo-flagged locations, improving patrol efficiency and detection rate.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| GPR subsurface detection model | Build | GSSI hardware (partial) | GSSI has developing AI product; custom extension for utility contractor workflow |
| CCTV PACP coding | Buy | WinCan AI / Envirosight AI Assist | Existing commercial products; integration is custom |
| As-built documentation automation | Build | Trimble + ArcGIS APIs | Data transformation pipeline is custom per utility owner schema |
| PHMSA compliance tracking | Build | — | Regulation mapping + asset registry integration is custom |
| Gas leak visual indicator detection | Build | — | No commercial product; dataset requires prospective collection |
| CP system anomaly detection | Build | — | Statistical anomaly detection on measurement data; straightforward |
