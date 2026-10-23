# AI Agents & Platform Opportunities — Skilled Nursing Facilities

**Industry:** [[skilled-nursing-facilities|Skilled Nursing Facilities]]

---

## 1. Staffing-Gap Intelligence Platform on Public PBJ and Care Compare Data
#ai-platform #time-series-forecasting #gradient-boosting #evaluation-metrics #data-integration #quick-win #revenue-impact

**Concept:** A platform that ingests every quarterly PBJ daily-staffing release and the monthly Care Compare refresh for all ~14,700 certified facilities. It ranks facilities by acuity-adjusted RN, LPN and aide shortfall, weekend dips and contract-staff share, forecasts each facility's next staffing star, and flags who is about to cross the 3-star staffing line that gates the risk-based survey. A chain's VP of operations sees every building against its local market. An MA plan or hospital network sees which preferred SNFs are understaffing. It is built entirely on public, facility-identified data, so it needs no business associate agreement and no EHR integration to start.
**Inputs:** PBJ public use files, Care Compare provider and quality files, CMS-2567 deficiency records, cost report wage data, ownership and chain affiliation files, BLS county wage data; optionally the operator's own schedule and payroll for forward-looking views.
**Outputs / Actions:** Facility and portfolio staffing scorecards; predicted staffing-star changes before release; alerts on PBJ anomalies likely to fail a CMS audit; market wage benchmarks; board-ready summaries drafted by an LLM from the numbers.
**Why now:** The 2024 staffing mandate is gone, but staffing now weighs on stars, two SNF VBP measures and risk-based survey eligibility, and PBJ moved to iQIES in August 2026. A two-week demo on public data is realistic, and the same pipeline sells to operators, REITs, lenders and plans.
**Market:** Regional and national chains (VP of operations, chief nursing officer), healthcare REITs and HUD 232 lenders monitoring tenants, MA plans building SNF networks, and hospital post-acute teams. Workforce vendors are the natural acquirers or partners: SmartLinx, and ShiftKey, which is hiring a Staff AI Engineer for an agentic platform (Ashby, US, checked 2026-10-24).

---

## 2. Medicare Advantage Authorisation and Continued-Stay Agent
#ai-agent #large-language-models #transformers #workflow-orchestration #revenue-impact #automation

**Concept:** An agent that runs the MA paperwork for every managed-care resident. It requests the admission authorisation from the hospital packet, tracks authorised days by plan, and assembles the weekly continued-stay update from therapy and nursing notes in each plan's required format. It submits the update through the plan's portal or the CMS-0057-F prior authorisation API as plans adopt it, drafts peer-to-peer briefs and appeals when days are cut, and times the NOMNC and fast-track appeal steps. Managed care is now 42% of admissions (CLA, 2026), and the three largest MA insurers denied 12% of SNF requests, with nearly all appealed denials overturned (OIG, June 2026). Appeals win, but facilities often lack the staff to file them.
**Inputs:** Hospital referral packets, payer rules and portal requirements, therapy evaluations and progress notes, functional scores, nursing notes, authorisation history by plan and reviewer, denial letters.
**Outputs / Actions:** Submitted authorisation requests and weekly updates; a days-at-risk dashboard; drafted appeals and peer-to-peer briefs with cited evidence; payer-level denial and overturn analytics.
**Why now:** LLMs can write payer-specific clinical summaries from notes, and the federal prior authorisation API deadline (January 2027) gives plans a standard channel. Vendors are funded and hiring: ExaCare (admissions and reimbursement agents) lists Machine Learning, Staff Data and Platform Engineer roles, and Sunbound (revenue operations for SNFs and assisted living) lists four software engineering roles (both on their own ATS, checked 2026-10-24).
**Market:** Every facility with MA residents. The buyer is the administrator or a chain's VP of revenue cycle, paying from recovered days. Competitors include Skypoint's admissions agents, sold with a forward deployed engineering model (its own posted FDE role is in Bengaluru), and billing outsourcers.

---

## 3. MDS and PDPM Documentation Agent in the PointClickCare Ecosystem
#ai-agent #large-language-models #bert #compliance #revenue-impact #worker-facing

**Concept:** An agent inside the EHR that reads the record for each resident with an open assessment window and proposes MDS item codes with linked evidence. It suggests the ARD that captures supportable acuity, flags NTA comorbidities documented but not coded and items coded without support, and drafts the physician or nurse query that would resolve a gap. The MDS coordinator accepts or edits each item. The same agent turns CNA voice notes into Section GG and ADL documentation, closing the loop between the floor and the assessment.
**Inputs:** Chart documents and flowsheets inside the EHR, prior MDS assessments, RAI Manual rules, payer (Medicare or state Medicaid PDPM variant), audit history.
**Outputs / Actions:** Item-level coding suggestions with evidence; under- and over-coding flags; queries to clinicians; projected case-mix; an audit-ready rationale per item.
**Why now:** CMS's FY 2027 rule requires MDS for every resident receiving covered skilled care regardless of payer and asks about PDPM upcoding, so both completeness and defensibility now matter. PointClickCare is hiring a Senior Applied Researcher in AI/ML, Principal ML System Engineers and a Clinical AI Nurse SME (Lever, checked 2026-10-24), and its 400+ partner marketplace is the distribution channel for third parties.
**Market:** ~14,700 facilities, each with one or more MDS coordinators (estimate). Buyers are directors of clinical reimbursement at chains and administrators at independents, competing with Zimmet, Harmony and other consultancies' audit services.

---

## 4. Change-of-Condition and Falls Watch Platform
#ai-platform #cnns #gradient-boosting #survival-analysis #tacit-knowledge-ml #worker-facing

**Concept:** A platform that fuses CNA voice or one-tap "something's different" flags, ADL deviations from each resident's baseline, vitals and labs, and event data from room sensors or privacy-preserving video. It ranks residents by risk of acute transfer or a fall with injury each shift, routes the top few to the charge nurse with the facility's change-of-condition protocol, and later grades each flag against what happened.
**Inputs:** Point-of-care documentation, CNA flags, vitals, orders, notes, sensor and video events, nurse-call logs, transfer and incident records.
**Outputs / Actions:** Per-shift risk lists; nurse prompts; post-fall review clips; facility dashboards on SNF VBP readmission, long-stay hospitalisation and falls-with-major-injury measures; private feedback to aides on how often their flags were right.
**Why now:** Falls with Major Injury (Long-Stay) and Long Stay Hospitalization enter SNF VBP in FY 2027, and within-stay preventable readmissions replace SNFRM in FY 2028. Sensor and video vendors that grew up in memory care are hiring engineers: SafelyYou (API Architect, Data Integration Engineer for EHR pipelines), Inspiren (Staff Backend Engineer, US remote) and Teton.ai (engineers in Copenhagen and London), all checked on their own boards on 2026-10-24.
**Market:** Chains' chief nursing and quality officers, and MA plans and hospital networks paying for lower readmissions. Sensor vendors and EHR vendors are both entering from opposite sides, and the record that joins the two is unowned.
