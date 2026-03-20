# AI Agents & Platform Opportunities — Medical Device Manufacturing

**Industry:** [[medical-device-mfg|Medical Device Manufacturing]]

---

## 1. DHR Compilation Agent
#ai-agent #large-language-models #transformers #attention-mechanisms #data-integration #compliance

**Concept:** An autonomous agent that assembles complete Device History Records by querying MES, ERP, LIMS, QMS, and sterilization monitoring systems for all records associated with a production lot — compiling them into the DHR structure, verifying completeness against device-specific requirements, and flagging missing records before the lot is released.
**Inputs:** Production lot number; device master record (defining which record types are required for this device type); API connections to MES (batch records, in-process inspection), ERP (component traceability, labeling records), LIMS (test results), QMS (nonconformance reports, deviation records), sterilization monitoring (cycle records, BI results)
**Outputs / Actions:** Assembled DHR document package with indexed sections; completeness checklist with pass/fail per required record type; missing record alerts routed to responsible department; DHR package stored in QMS document control system ready for quality review and lot release approval
**Why now:** MES and ERP platforms in regulated manufacturing now expose production data through REST APIs (Opcenter, Plex, 42Q all have API layers). LLMs can parse and organize heterogeneous document formats into structured DHR sections. The manual DHR assembly cost (2-4 hours per lot) is a concrete, measurable time savings that justifies adoption even in conservative regulatory environments.
**Market:** Every FDA-regulated medical device manufacturer producing finished devices — approximately 6,500 registered establishments in the US. Mid-size manufacturers ($20M-$500M revenue) are the sweet spot: large enough to produce significant lot volumes but not large enough to have built custom integration solutions. Pricing: $2,000-$5,000/month based on lot volume.

---

## 2. CAPA Investigation Agent
#ai-agent #bert #large-language-models #transfer-learning #word-embeddings #feature-engineering #compliance

**Concept:** An agent triggered by a new CAPA investigation that automatically gathers relevant data from across the quality system — correlating complaint clusters with production records, component lots, and supplier data — and generates a preliminary root cause hypothesis with supporting evidence for the quality engineer's review, reducing investigation time from weeks to days.
**Inputs:** CAPA trigger (complaint cluster, nonconformance trend, audit finding); complaint narratives and metadata from QMS; production batch records from MES; component lot traceability from ERP; supplier incoming inspection data; historical CAPA records for similar failure modes
**Outputs / Actions:** Complaint cluster analysis (failure mode grouping with supporting complaint excerpts); production parameter correlation (which parameters, lots, or date ranges correlate with the complaint cluster); supplier lot correlation (which component suppliers/lots are over-represented in affected production batches); preliminary root cause hypothesis with confidence level and linked source records; recommended investigation steps for the quality engineer to verify or refine the hypothesis
**Why now:** NLP models (BERT, LLMs) can now cluster and classify medical device complaint narratives with adequate accuracy. The data integration challenge — joining complaints to production to components to suppliers — is tractable with current API-based integration tools. The regulatory environment is increasingly demanding faster CAPA closure (FDA consent decrees commonly require 60-day CAPA timelines).
**Market:** Medical device manufacturers with >50 open CAPAs per year — typically companies with $50M+ revenue and established post-market surveillance programs. The CAPA bottleneck is universal in the industry and is the most frequently cited FDA 483 observation. Pricing: $3,000-$8,000/month based on CAPA volume and system integration complexity.

---

## 3. Design History File Audit Readiness Agent
#ai-agent #large-language-models #transformers #attention-mechanisms #compliance

**Concept:** An agent that scans a device's Design History File (DHF) for completeness against FDA Design Controls requirements (21 CFR 820.30) — verifying that design inputs trace to design outputs, that verification and validation records exist for each design requirement, that risk management artifacts are linked, and that design reviews are documented — generating an audit readiness score and a gap report before an FDA inspection or internal audit.
**Inputs:** DHF document index from QMS document control; design input requirements list; design output specifications; verification and validation test reports; risk management file (per ISO 14971); design review meeting records; design transfer documentation; design change records
**Outputs / Actions:** Traceability matrix: design input → design output → V&V record → risk control, with pass/fail per requirement; completeness score by Design Controls sub-requirement (design input, output, review, verification, validation, transfer, changes); gap report: specific missing documents, broken traceability links, and unsigned records; recommended remediation actions prioritized by FDA audit risk
**Why now:** QMS platforms (Greenlight Guru, MasterControl) now structure DHF documents with metadata that enables programmatic traceability checking. LLMs can parse design input/output documents to extract requirements and verify traceability. The FDA's focus on Design Controls during inspections (especially for Class III devices) makes audit readiness a persistent anxiety for quality and regulatory teams.
**Market:** Medical device companies with active design projects — approximately 4,000 US companies filing 510(k)s, PMAs, or De Novos annually. Greenlight Guru's customer base (purpose-built for device companies) is the natural integration target. Pricing: $1,500-$4,000/month, positioned as audit insurance.
