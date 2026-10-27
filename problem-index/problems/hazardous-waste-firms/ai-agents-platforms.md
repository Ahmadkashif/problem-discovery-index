# AI Agents & Platform Opportunities — Hazardous Waste Firms

**Industry:** [[hazardous-waste-firms|Hazardous Waste Firms]]

---

## 1. Waste Profile Intake Agent
#ai-agent #large-language-models #bert #compliance #workflow-orchestration #automation

**Concept:** An agent that sits between generators and a TSDF's approval desk. It takes whatever the generator has (safety data sheets, a process description, old profiles, lab reports), drafts a complete profile with proposed waste codes and the DOT description, asks the generator the specific questions an approval chemist would ask, and submits only when the profile is complete. On the TSDF side it attaches the generator's history and a risk note so the chemist starts from the evidence.
**Inputs:** Generator uploads and answers; SDS library; the TSDF's permit acceptance criteria and Waste Analysis Plan; prior profiles and receiving results for the generator; state code lists.
**Outputs / Actions:** Draft profile with cited sources; generator question list; completeness check; risk-ranked submission to the approval queue; annual recertification drafts that highlight what changed.
**Why now:** Language models now read safety data sheets and lab reports into structured fields reliably, and TSDF ERPs (WASTELINQ, Wastebits, Terralink's TDXConnect (search summary)) already expose web profile intake that an agent can fill.
**Market:** TSDF technical-services departments and the ~650 smaller collectors and treaters (estimate); also large generators' EHS teams who submit profiles to several vendors. Profile software exists as forms; nobody sells the drafting and questioning.

---

## 2. Manifest Reconciliation and Discrepancy Agent
#ai-agent #large-language-models #data-integration #compliance #workflow-orchestration #automation

**Concept:** An agent that watches every manifest a transporter or TSDF touches in e-Manifest and in its own ERP, matches each line to the approved profile, scale weight and receiving result, chases missing signatures, drafts discrepancy, exception and unmanifested-waste reports now filed through e-Manifest, and keeps the generator informed. It converts paper and hybrid manifests into data before the facility uploads them.
**Inputs:** e-Manifest records and status; ERP orders and profiles; scale tickets; receiving-lab results; generator contacts; scanned paper manifests.
**Outputs / Actions:** Matched or flagged manifests; draft discrepancy and exception reports for sign-off; generator notifications; data uploads instead of image uploads; a monthly reconciliation report.
**Why now:** The third e-Manifest rule moved discrepancy, exception and unmanifested-waste reports into the system and required generators to register, and EPA's fee gap ($5 electronic against $25 for a scanned image from October 2025) puts a price on every paper manifest.
**Market:** Receiving facilities processing a share of ~2 million manifests a year (EPA) and the transporters that sign them; a natural add-on for TSDF ERP vendors.

---

## 3. Generator Compliance Platform on Public Manifest Data
#ai-platform #change-point-detection #descriptive-statistics #data-integration #compliance #revenue-impact

**Concept:** A platform that builds a compliance view of every generator site from public e-Manifest and RCRAInfo data: inferred monthly status, status shifts, episodic events, waste streams by code and receiving facility, and Biennial Report drafts reconciled to the manifest record. Generators use it to check their own sites; waste vendors use it to serve customers and to find sites whose manifests show unmet needs.
**Inputs:** Public e-Manifest data (released 90 days after receipt (search summary)); RCRAInfo notifications and Biennial Report filings; generator-supplied accumulation logs where granted.
**Outputs / Actions:** Site status timelines; mismatch alerts against notified status; Biennial Report and re-notification drafts; vendor-facing account intelligence on public data only.
**Why now:** e-Manifest has accumulated ~13.5 million manifests from over 575,000 sites since 2018 (EPA), and the third rule's generator registration brings every small and large generator into the system that holds its own records.
**Market:** Multi-site generators' EHS directors, environmental consultants serving them (see [[environmental-consultants|Environmental Consultants]]), and transporters' sales teams. No vendor sells this view today.

---

## 4. Outlet Routing and Capacity Desk
#ai-agent #optimization-fundamentals #dynamic-programming #time-series-forecasting #revenue-impact #workflow-orchestration

**Concept:** An agent for brokers, multi-facility networks and large generators that chooses where each waste stream goes. For every approved profile it lists the facilities whose permits accept it, forecasts their capacity and price, adds freight and the long-term liability of the disposal method (destruction or recycling against land disposal), and proposes a routing plan that keeps committed tons moving when incinerators are full.
**Inputs:** Profiles and volumes; facility permits and acceptance lists; incinerator and landfill capacity signals; contract prices; freight rates; generator policies such as landfill avoidance.
**Outputs / Actions:** Ranked outlets per stream with cost and liability notes; monthly routing plan; re-routing alerts when an outlet closes or a backlog builds; documentation for the generator's vendor-approval file.
**Why now:** Incineration capacity tightened after 2022 (a 50,000–60,000 ton backlog in 2023 (search summary)), new capacity is ramping at Kimball and was planned in Arkansas for 2025 (status unchecked), and PFAS guidance shifts which outlets generators prefer, so routing has become a recurring decision rather than a one-time contract.
**Market:** Hazardous waste brokers, consolidators' national account teams and the corporate EHS departments of large generators.
