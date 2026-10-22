# AI Agents & Platform Opportunities — Pension Funds

**Industry:** [[pension-funds|Pension Funds]]

---

## 1. Private Markets Commitment Memory Platform
#ai-platform #large-language-models #survival-analysis #evaluation-metrics #tacit-knowledge-ml #revenue-impact

**Concept:** A platform that keeps a structured record of every commitment and re-up decision a pension makes: the thesis for the manager, the concerns, the signals the officer saw and the alternatives declined. It drafts each record from the officer's notes, GP letters and statements for one-click confirmation, and grades each record later against vintage-adjusted fund outcomes. When a GP comes back for its next fund, it gives whoever now covers the relationship the full history, including what the departed officer saw and how it turned out.
**Inputs:** Re-up memos and board packets, officers' meeting notes, GP quarterly letters and annual meeting materials, capital account statements and cash flows, consultant recommendations, public peer fund outcomes.
**Outputs / Actions:** Commitment records; re-up briefs showing past signals and outcomes; programme-level scorecards of which signals and conviction levels carried information; handover packs when staff leave.
**Why now:** Language models can draft structured records from unstructured notes cheaply enough that capture does not depend on officer discipline. Years of public pension private markets disclosures, obtained through public-records requests, give the outcome labels.
**Market:** Large public plans and their private markets consultants. Monitoring platforms are the natural incumbents but record what GPs report, not what the plan decided and why.

---

## 2. Fee and Carry Verification Agent
#ai-agent #large-language-models #transformers #compliance #automation #data-integration

**Concept:** An agent that reads each LPA, amendment and side letter once, keeps the fee and waterfall terms as executable rules, and recomputes every quarter's management fee, offsets, expenses and carried interest from the capital account statement. It drafts queries to the GP for unexplained differences, then assembles the annual public fee and carry report that California's Government Code 7514.7 requires, in the ILPA template's categories.
**Inputs:** Partnership documents, quarterly statements and notices, ILPA templates, the plan's commitment list.
**Outputs / Actions:** Recomputed fee and carry per fund; variance list with citations to the clause; draft GP queries; the board-ready annual disclosure and a public records version.
**Why now:** ILPA's updated templates apply from Q1 2026 and give a common target schema. Clause extraction from long legal documents is now accurate enough to draft terms for specialist review.
**Market:** Public pension private markets and investment operations teams, and the consultants who prepare fee reports for smaller plans; adjacent to monitoring platforms and fund administrators.

---

## 3. Employer Reporting Review Agent
#ai-agent #gradient-boosting #change-point-detection #compliance #workflow-orchestration #automation

**Concept:** An agent that sits on the employer reporting portal and reviews every payroll file for pensionability, not just format. It applies the plan's pay-code and tier rules, flags spikes in the final-average window and new pay codes, and drafts the correction request to the employer's payroll clerk with the rule cited. It tracks each employer's error history so the audit team can choose which employers to audit.
**Inputs:** Employer payroll submissions; member tier and position data; plan rules; historical compensation reviews and audit findings.
**Outputs / Actions:** Accepted, held or corrected records; employer correction requests; member-level alerts before retirement; risk-ranked employer audit plans.
**Why now:** Disallowed-compensation rules such as California's 2022 law put the cost of misreporting on employers, which makes early detection worth paying for. System modernisation projects are replacing employer portals across many states.
**Market:** Statewide and large county retirement systems, buying directly or through their pension administration system vendor; employer audit teams are the internal champion.

---

## 4. Member Counseling Copilot
#ai-agent #large-language-models #k-nearest-neighbors #worker-facing #automation #workflow-orchestration

**Concept:** A copilot for retirement system counselors and member self-service. On every call or message it summarises the member's record, identifies the applicable plan rules and precedents, runs estimates and option comparisons, and drafts the answer and confirmation letter with citations. It routes the cases that need a benefit analyst and logs question types so the system can fix the communications that generate calls.
**Inputs:** Member records from the pension administration system; plan statutes, policies and past determinations; call transcripts and secure messages; the benefit calculation engine.
**Outputs / Actions:** Call summaries; cited answers; estimates; drafted letters; escalations; a daily view of why members are calling.
**Why now:** Retrieval over statutes, policies and determinations is reliable enough to cite. CEM benchmarking makes member-service gaps visible to boards: North Carolina's 25-minute average wait in March 2026 sat beside a cost of $33 per member against a $130 peer average.
**Market:** Public retirement systems and the administrators of multiemployer and corporate plans; pension administration system vendors are partners or competitors.
