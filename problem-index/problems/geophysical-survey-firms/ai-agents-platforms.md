# AI Agents & Platform Opportunities — Geophysical Survey Firms

**Industry:** [[geophysical-survey-firms|Geophysical Survey Firms]]

---

## 1. Verified Subsurface Record Platform
#ai-platform #cnns #object-detection #evaluation-metrics #tacit-knowledge-ml #data-integration #revenue-impact

**Concept:** A platform that stores every anomaly a firm calls — location, depth, class, confidence, reason — and pulls back the verification that follows: QL-A test-hole sheets, munitions dig results, core records, drill logs. It matches each verification to the pick it tests, computes the firm's verified hit rate and depth error by method, soil type, target class and interpreter, and uses the graded archive to train and calibrate detection models that rank the next site's candidates with their track record attached.
**Inputs:** Processed GPR, EM and magnetic data and picks from Oasis montaj, RADAN and CAD exports; client verification documents (PDF test-hole sheets, dig logs, core photos); project metadata and site conditions.
**Outputs / Actions:** A verified-call ledger per project; firm-level and interpreter-level accuracy scorecards; ranked candidate lists with similar verified examples; evidence packs for disputes after a strike.
**Why now:** Vision models can now read radargrams and EM grids at useful accuracy, document models can extract test-hole and dig-log tables from scanned PDFs, and DOTs and DoD increasingly require documented quality levels and accredited classification, which makes a verified record commercially valuable on its own.
**Market:** National near-surface platforms (GPRS and its peers), SUE practices at engineering firms, and DAGCAP-accredited classification contractors; adjacent to the subsurface-mapping entrants (Exodigo) who could buy rather than build the verification layer.

---

## 2. Field QC Copilot
#ai-agent #change-point-detection #gaussian-processes #worker-facing #automation #quick-win

**Concept:** An agent on the crew's tablet that holds the project's quality plan as rules, watches the live sensor and GNSS streams, paints coverage as the sensor footprint actually achieves it, flags gaps, drift, lift-off and failed function tests while the crew is beside them, and issues an end-of-day pass/fail with the QC log formatted for the client's QAPP or DOT reviewer.
**Inputs:** Raw logger streams, GNSS quality, planned grid and boundaries, quality-plan tolerances, instrument verification strip results, technician notes and photos.
**Outputs / Actions:** Real-time gap and quality alerts; re-walk instructions; daily QC report; a demobilisation checklist that blocks leaving site with an unresolved failure.
**Why now:** Rugged tablets and phones can run streaming models locally, RTK GNSS is standard on survey crews, and munitions and SUE work now carries written quality objectives a machine can test.
**Market:** Every near-surface crew; sold per crew-month to munitions response contractors, SUE firms and environmental geophysics practices, or bundled by instrument makers.

---

## 3. Seismic Permit Agent
#ai-agent #gradient-boosting #logistic-regression #data-integration #workflow-orchestration #compliance

**Concept:** An agent that manages access for an onshore seismic program: builds the tract list from the survey design and parcel data, predicts refusal and condition risk per tract, drafts outreach letters and permit forms, tracks every agent visit and outcome, translates conditions into crew instructions, re-flags affected source and receiver points as no-permit zones grow, and assembles damage-claim evidence from GPS tracks and photos after recording.
**Inputs:** Survey design, county parcel and ownership records, prior permit history, agent notes, permit templates, crew GPS tracks and photo logs.
**Outputs / Actions:** Tract-level status board; risk-ranked outreach queue; skid and offset proposals for the designer; daily recordable-footprint report for the client; claim files.
**Why now:** Parcel data is now machine-readable in most producing counties, LLMs draft correspondence and parse handwritten permit conditions, and crews already log GPS tracks that make damage evidence cheap.
**Market:** Onshore seismic contractors (Dawson, its Canadian peers) and the permit-agent firms they hire; small, cyclical and concentrated, but each standby day avoided pays for the year.

---

## 4. Deliverable and Report Agent
#ai-agent #large-language-models #transformers #worker-facing #automation #workflow-orchestration

**Concept:** An agent that turns a project's records into its deliverables: drafts methods, QC, results and limitations sections grounded in the field logs and picks; generates anomaly tables and dig lists in the client's format; rebuilds figure sets to the firm's template; and exports utility designations as CAD or GIS layers with ASCE 38 quality-level attributes and the DOT's CADD standards.
**Inputs:** Field logs, instrument settings, QC outputs, processed grids, picks and interpretations, prior signed reports, client templates and CADD standards.
**Outputs / Actions:** Draft report with source-linked statements; anomaly tables and dig lists; figure set; CAD/GIS deliverable; a reviewer checklist of statements the signer must confirm.
**Why now:** Grounded generation with citations is now reliable enough for technical drafting, and the deliverable formats (QAPP tables, DOT CADD standards) are stable and documented.
**Market:** Small and mid-size geophysical firms and SUE practices; per-project pricing fits firms with no IT staff.
