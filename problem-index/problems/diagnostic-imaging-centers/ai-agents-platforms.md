# AI Agents & Platform Opportunities — Diagnostic Imaging Centers

**Industry:** [[diagnostic-imaging-centers|Diagnostic Imaging Centers]]

---

## 1. Order-to-Scan Intake Agent
#ai-agent #large-language-models #bert #gradient-boosting #automation #data-integration #revenue-impact

**Concept:** An agent that starts when an order arrives by fax, e-referral or HL7 feed. It reads the order and attachments, creates the patient and pending exam in the RIS, and checks eligibility. It finds or requests the authorization and verifies that the approval matches the protocolled CPT code, site and date window. Then it calls or texts the patient to book the first open slot that fits the authorization window, and re-checks the match whenever the protocol, date or site changes. It escalates to a coordinator only when a fact is missing or the benefit manager must be called.
**Inputs:** Faxed and electronic orders, approval letters, payer and benefit-manager portals and APIs, RIS schedules, protocol changes, patient phone and SMS.
**Outputs / Actions:** Pending exams created in the RIS; eligibility and authorization-match results with the failing field; amendment requests sent before the scan; booked appointments and reminders; a daily exception queue.
**Why now:** LLMs read faxed orders and approval letters reliably enough to populate a RIS. CMS-0057-F holds Medicare Advantage and Medicaid plans to seven-day standard decisions from 2026 and requires prior-authorization APIs from 1 January 2027. Voice agents can now hold a scheduling call. An order sent to several centres goes to whichever books first (Capitol Imaging, search summary).
**Market:** Freestanding centre operators and multi-site groups; an existing buyer category (patient access and RIS add-ons). DeepHealth (RadNet) had a Forward Deployment Engineer, HL7 Integration (remote US, $125K–$145K) open on 24 October 2026, and AbbaDox sells a RIS with an AI scheduling agent (search summary). The ordering practice's side of the authorization is [[physician-practices|Physician Practices]]. The payer's side is [[health-insurance-carriers|Health Insurance Carriers]], where Cohere Health was hiring a Sr. Forward Deployed Engineer (US).

---

## 2. Protocol and Order-Appropriateness Copilot
#ai-agent #large-language-models #transformers #bert #tacit-knowledge-ml #evaluation-metrics #worker-facing

**Concept:** A copilot inside the protocolling worklist that proposes a protocol for each order with its evidence and confidence. It flags orders likely to be the wrong exam, and checks the indication against the guideline the patient's radiology benefit manager will apply before the authorization is requested. Routine orders go to one-click radiologist sign-off. Contrast, implant and paediatric sedation cases always route to a human. Every accepted, edited or rejected proposal is logged with its later outcome (recall, repeat, addendum), building the protocol ledger the centre has never had.
**Inputs:** Orders and indications, patient history and lab flags, the group's protocol library, documentation requirements from payers' CMS-0057-F Prior Authorization APIs, benefit-manager imaging guidelines and ACR Appropriateness Criteria where licensed, prior imaging, final reports and addenda.
**Outputs / Actions:** Proposed protocols with confidence; appropriateness and wrong-exam flags; escalations; a per-referrer and per-protocol outcome ledger.
**Why now:** Transformers read messy order text well, and reading groups' protocol histories are now in cloud RIS and PACS systems that can be mined. The radiologist shortage makes the protocolling minutes visible. This is the owner's MVP, reframed. CMS rescinded the AUC programme from 1 January 2024, so no one must buy an "order versus ACR criteria" checker. ACR requires permission to reuse its 279 topics, and the benefit managers' guidelines (EviCore, Carelon) are copyrighted too, so a checker built on either needs a licence (recalled for the benefit managers). The licence-free source is the CMS-0057-F Prior Authorization API. From 1 January 2027, Medicare Advantage, Medicaid, CHIP and federally facilitated exchange plans must use it to list the services that need authorization and identify their documentation requirements. A two-week MVP is a protocol and wrong-exam proposer over synthetic orders for one body part (lumbar spine MRI). It checks each order against API-style documentation requirements, using test data until the 2027 go-live, and is scored against a radiologist's protocols.
**Market:** Reading groups and centre operators, through reading-platform and RIS vendors rather than as a standalone. DeepHealth's three Forward Deployment Engineers and Senior Forward Engineer (remote US) and Sirona Medical's Senior Integrations Engineer (San Francisco) are deployment teams for such features. New Lantern's Client Deployment Lead has been listed since 31 March 2026 and may be stale. HOPPR's foundation model is a likely component: its Forward Deployed ML Engineer role (remote US) appeared on Built In Chicago but not on its own pages on 24 October 2026. CareSelect (Optum) is the incumbent for ordering-side decision support in health-system EHRs.

---

## 3. Reading-Room Preparation Agent
#ai-agent #large-language-models #transformers #word-embeddings #workflow-orchestration #worker-facing

**Concept:** An agent that prepares every study before a radiologist opens it. It ranks the worklist by urgency, turnaround deadline and effort, pulls and summarises relevant priors across sites, and surfaces the referral question and any AI detections. It drafts a structured report for the radiologist to edit and extracts follow-up recommendations into a tracking queue. For teleradiology contracts it routes studies to readers by licence state, credentialing and subspecialty.
**Inputs:** PACS and RIS worklists, priors and prior reports, referral text, AI triage outputs, contracted turnaround by client, reader licensure and credentialing, dictation audio.
**Outputs / Actions:** Ranked and balanced worklists; hung priors with summaries; draft reports; follow-up recommendations pushed to tracking; turnaround-breach alerts.
**Why now:** Report-drafting models are now in production use (Rad AI, Mosaic Reporting at Radiology Partners-affiliated practices since June 2026 per search summary, DeepHealth Reporting Pro), and cloud reading platforms make the worklist programmable.
**Market:** Radiology groups, teleradiology firms and centre operators that employ readers. On 24 October 2026 Rad AI was hiring a Staff Software Engineer, Speech (remote US, $187K–$265K), Continuity and Reporting engineers and ML research scientists in San Francisco. DeepHealth had a Forward Deployment Engineer, Reporting Pro and one for the Viewer (remote US). DeepHealth also listed machine learning engineers in Paris and Australia (remote), a clinical AI devices software engineer in France and a research scientist in the UK, and 5C Network listed computer-vision and vision-language model roles on-site in Bengaluru. Microsoft PowerScribe is the dictation incumbent. Clinical speech vendors' data teams are analysed under [[document-preparation-services|Document Preparation Services]].

---

## 4. Multi-Site Imaging Operations Platform
#ai-platform #gradient-boosting #survival-analysis #monte-carlo-methods #optimization-fundamentals #automation #revenue-impact

**Concept:** A platform for operators running dozens to hundreds of centres. It forecasts demand and no-shows by site and modality, sets slot lengths from protocols, prices overbooking, and fills same-day gaps from waitlists that respect authorization windows. It schedules technologists across sites to match scanner demand, and tracks scanner uptime, accreditation, MQSA and IDTF enrolment deadlines by site. It reports completed paid exams per scanner hour as the operator's core metric.
**Inputs:** RIS bookings and outcomes, scanner logs and service events, technologist rosters and credentials, payer mix and authorization status, accreditation and enrolment records.
**Outputs / Actions:** Site-level schedules and templates; overbooking and waitlist actions; staffing recommendations; compliance-deadline alerts; utilisation dashboards.
**Why now:** Rollups have reached the scale where a point of utilisation is worth millions. RadNet runs 418 centres and Lumexa 192, and RadNet's procedure counts grew double digits in late 2025. Technologist vacancies (CT 19.4%, MRI 17.4%, ASRT 2025) make labour the binding constraint. The CY2027 OPPS proposal to cut off-campus hospital imaging without contrast by 60% would bring hospital-affiliated sites into the same price band.
**Market:** Multi-site operators, health-system imaging joint ventures and direct-to-consumer MRI chains. Prenuvo, which runs whole-body MRI clinics, had a Senior Forward Deployed Engineer open (remote US and Canada) to embed with its clinical and operations teams, plus AI applied scientists in Vancouver. DeepHealth sells RadNet's operating stack to other providers. Most mid-size operators run on RIS reports and spreadsheets today.
