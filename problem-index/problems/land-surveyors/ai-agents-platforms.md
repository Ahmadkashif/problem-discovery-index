# AI Agents and Platforms — Land Surveyors

**Industry:** [[land-surveyors|Land Surveyors]]
**Tags:** #ai-agent #ai-platform #llm #bert #cnn #gradient-boosting #text-generation #text-classification #multiclass-classification #semantic-segmentation #ocr #nlp #computer-vision #tabular-ml #tacit-knowledge-ml #compliance #revenue-impact

---

## Existing AI-Adjacent Platforms

### Trimble Business Center
Industry-leading post-processing software for GNSS data correction, coordinate adjustment, and point cloud processing. Includes some automated classification features for LiDAR point clouds (ground extraction, vegetation filtering) but these are algorithm-based (not ML) and require manual parameter tuning. No deed interpretation, boundary analysis, or deliverable generation automation.

### Carlson Survey
The most popular survey-specific CAD overlay for AutoCAD and IntelliCAD. Handles coordinate geometry calculations, traverse adjustment, and legal description generation from entered data. The legal description generator produces text from coordinates but does not work in reverse (parsing existing descriptions into coordinates). No AI capabilities.

### DroneDeploy / Pix4D
Drone mapping platforms that produce orthomosaic imagery and point clouds from aerial photographs. Increasingly used by survey firms for topographic mapping and volumetric analysis. Offer basic AI features (stockpile detection, change detection) targeted at construction monitoring but not survey-specific deliverables.

---

## AI Agent Opportunities

### 1. Deed Interpretation and Research Agent
**Trigger:** Activated when a new boundary survey project is created and the chain of title documents are uploaded or linked from the county recorder's system.

**Action sequence:**
1. Retrieves all deeds in the chain of title from the county recorder's digital records (or accepts uploaded scans for non-digitized counties)
2. Runs OCR on handwritten deeds and NLP extraction on all deeds to produce structured boundary call tables: bearings (with era-appropriate magnetic correction), distances (converted to modern units), monument descriptions, and adjoiner references
3. Cross-references adjoiner calls with adjacent parcel deeds to identify conflicts, gaps, and overlaps in the deed fabric
4. Pulls historical aerial photography from USGS Earth Explorer for the parcel area, identifying vegetation and topographic features that may correspond to deed-referenced monuments
5. Generates a pre-field research package: annotated deed calls plotted on current aerial imagery, identified potential monument locations, flagged ambiguities requiring field verification, and historical aerial comparison showing landscape changes since the oldest deed

**Value:** Reduces pre-field deed research from 2-4 hours to 30-60 minutes. Identifies deed conflicts and ambiguities before the surveyor goes to the field, reducing return trips caused by encountering unexpected conditions. For a firm doing 200 boundary surveys/year, that's 200-600 hours of saved research time — worth $20,000-$60,000 at $100/hour.

### 2. Field Survey Planning Agent
**Trigger:** Fires after the deed research phase is complete and before the field crew is dispatched.

**Action sequence:**
1. Analyzes the deed research output to identify which corners need field verification and what evidence to look for at each location
2. Pulls terrain data (LiDAR DEM, slope maps) and aerial imagery to assess access routes, vegetation density, and equipment requirements
3. Generates an optimized field plan: suggested setup points for the total station to minimize setups, recommended GNSS observation schedule accounting for satellite geometry and canopy obstruction, and a traverse plan that minimizes crew walking distance while ensuring all corners are visited
4. Estimates field time based on terrain difficulty, number of corners, vegetation density, and historical monument recovery rates for the area
5. Generates a field crew briefing document: map with annotated corner locations, expected monument types, potential access issues, and priority order for corner visits (start with the most uncertain corners to allow re-planning if needed)

**Value:** Reduces field time by 15-25% through optimized routing and setup planning. Prevents the 2-3 return trips per complex survey caused by inadequate pre-planning. For a firm with $800K in annual field crew costs, a 20% efficiency improvement saves $160,000/year. Improves junior crew performance by providing the planning intelligence that normally exists only in the senior surveyor's head.

### 3. Deliverable Generation and QC Agent
**Trigger:** Activated when field data processing is complete and adjusted coordinates are ready for drafting.

**Action sequence:**
1. Ingests processed field data (adjusted coordinates with point codes) and the boundary determination (corner coordinates, boundary lines as approved by the PLS)
2. Identifies the applicable jurisdictional standards (county plat filing requirements, state minimum standards, ALTA requirements if applicable) from the compliance database
3. Generates a draft survey plat: boundary lines with annotated bearings and distances, monument symbols per office standards, area calculation, title block with certification language, and legal description in the jurisdiction's preferred format
4. Runs automated QC checks: mathematical closure (must close within tolerance), bearing/distance annotation consistency with coordinates, area calculation verification, compliance with jurisdictional filing requirements (sheet size, margins, required elements), and comparison of measured vs. record distances (flagging significant discrepancies)
5. Presents the draft plat to the PLS for review with QC results highlighted, discrepancies flagged, and suggested resolutions for common issues

**Value:** Reduces office drafting time from 4-8 hours to 1-2 hours for standard boundary surveys. The QC check catches errors that currently slip through manual review — bearing typos, annotation inconsistencies, missing certification elements — reducing the 5-10% first-submission rejection rate at county recorders. For a firm producing 200 plats/year, the combined time savings and rejection reduction is worth $40,000-$80,000 annually.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Deed OCR and NLP extraction | Build | Integrate with county recorder APIs where available | Historical handwriting OCR requires custom training; legal deed language NLP is domain-specific with no commercial solution |
| Boundary evidence classification | Build | — | No commercial product classifies survey monuments from photographs; requires custom CV pipeline |
| Field planning optimization | Build | Integrate with GIS data (USGS, county LiDAR portals) | Terrain analysis from public data; survey-specific planning logic must be built |
| Plat drafting automation | Build plugin | Integrate with AutoCAD/Carlson | Must work within existing CAD workflows; the automation logic is custom but output format is standard DXF/DWG |
| Compliance database | Build | — | No aggregated source of county filing requirements exists; must be built and maintained, potentially with LLM-assisted monitoring |
| Point cloud classification | Build/Buy | Buy (DroneDeploy for basic) + Build for survey-grade | Generic classification exists; survey-specific feature extraction at tolerance levels requires custom training |
| Project estimation | Build | — | Survey-specific cost estimation models do not exist commercially; must be trained on firm-specific project data |
