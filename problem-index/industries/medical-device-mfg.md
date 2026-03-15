# Medical Device Manufacturing

## Profile
**Category:** Manufacturing & Industrial
**Market Size:** ~$180B annually in the US; includes Class I (low-risk), Class II (moderate-risk), and Class III (high-risk) devices across implantables, surgical instruments, diagnostics, capital equipment, and consumables
**Tech Maturity:** Medium-High — ERP and MES are standard, quality management systems are mandated by regulation, but AI/ML adoption is near-zero due to validation burden under 21 CFR Part 820 and ISO 13485
**Workforce:** Manufacturing engineers, quality engineers, production operators, cleanroom assemblers, CNC machinists, quality inspectors, regulatory affairs specialists, process validation engineers — a typical Class II/III device manufacturer runs 200-2,000 employees with 15-25% of headcount in quality and regulatory functions

## Key Pain Themes
CAPA (Corrective and Preventive Action) is the single most consequential quality process and the single most cited deficiency in FDA inspections — CAPA investigations average 45-90 days to close because root cause identification requires cross-referencing complaint data, production records, Device History Records (DHRs), and supplier data across disconnected systems, and the investigation is performed by quality engineers who are simultaneously managing 10-20 open CAPAs. DHR (Device History Record) assembly is a compliance-critical documentation task that requires collecting production records from MES, inspection results from quality systems, component traceability from ERP, and sterilization records from sterilization monitoring systems — assembling the complete DHR for a single lot can take 2-4 hours of manual cross-system data gathering. FDA 510(k) submissions and predicate device searches consume weeks of regulatory affairs time, searching FDA databases for substantially equivalent devices and building comparison matrices that are largely repetitive across submissions. Process validation documentation (IQ/OQ/PQ protocols and reports) follows rigid FDA-expected structures that engineers draft from scratch for each new product or process change despite 80% structural similarity across validations.

## Current Tech Landscape
SAP and Oracle dominate ERP. MES platforms (Camstar/Siemens Opcenter, Rockwell Plex, 42Q) are standard for production tracking in regulated environments. Quality management systems (ETQ, MasterControl, Veeva Vault Quality, Greenlight Guru) handle CAPA, complaint management, document control, and audit management — Greenlight Guru is the category leader for small-to-mid device companies. LIMS (LabVantage, STARLIMS) manages testing data. None of these systems offer AI-assisted root cause analysis, automated DHR compilation, or intelligent predicate device search. The FDA's validation expectations for software used in quality-critical processes (21 CFR Part 11, computer system validation) create a high barrier to AI adoption — any ML model influencing a quality decision must be validated, which most device manufacturers lack the expertise to do.

## Problems
- [[problems/medical-device-mfg/high-impact|🔴 High Impact: CAPA Root Cause Identification and Cycle Time Reduction]]
- [[problems/medical-device-mfg/low-impact-1|🟡 Low Impact: DHR Assembly from Disconnected Systems]]
- [[problems/medical-device-mfg/low-impact-2|🟡 Low Impact: 510(k) Predicate Device Search and Equivalence Analysis]]
- [[problems/medical-device-mfg/worker-life-1|🟢 Worker Life: Quality Inspector Visual Inspection Fatigue]]
- [[problems/medical-device-mfg/worker-life-2|🟢 Worker Life: Process Validation Documentation Burden]]

## Analysis
- [[problems/medical-device-mfg/ml-opportunity|🧠 Machine Learning Opportunities]]
- [[problems/medical-device-mfg/ai-agents-platforms|🤖 AI Agents & Platforms]]
