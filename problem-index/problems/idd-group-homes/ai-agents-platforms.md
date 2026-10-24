# AI Agents & Platform Opportunities — IDD Group Homes

**Industry:** [[idd-group-homes|IDD Group Homes]]

---

## 1. Spoken Shift Report Agent
#ai-agent #large-language-models #transformers #compliance #revenue-impact #worker-facing #automation

**Concept:** An agent the DSP talks to at the end of a shift, or in short bursts during it. From a few minutes of speech it drafts the day's ISP-mapped progress note for each resident, the bowel, fluid, sleep and seizure logs, behaviour data entries and MAR exceptions, in the state's documentation format and the agency's record system. It asks one or two follow-up questions where a note would fail an audit ("Which step of Jamie's cooking goal did you work on?"). It also flags anything that reads like a reportable incident and drafts that report before its deadline. The house manager sees which residents' outcomes went undocumented this week.
**Inputs:** DSP speech or typed notes; each resident's ISP outcomes, behaviour support plan and health risk plan; attendance; MAR; state documentation and incident rules.
**Outputs / Actions:** Draft notes and logs written into the record system for DSP sign-off; follow-up prompts; draft incident reports; weekly documentation-gap and audit-risk reports for house managers and QIDPs.
**Why now:** Speech models now handle accented, noisy speech well enough for a DSP workforce that often works in a second language, and LLMs can map free narrative to plan outcomes with citations. The vendors are hiring for exactly this. Kibu, an IDD documentation platform that says it serves 480+ organisations in 48 states, lists a Senior Software Engineer to build AI features with LLMs, hybrid in Stamford, CT, or remote for strong candidates. iCareManager lists a Senior AI Engineer for its emrgen.ai documentation module (opened 2026-10-10; the posting names no location and says the role works with its engineering team in Pakistan), plus a Principal Software Engineer and a Senior DevOps engineer. Both were checked on their own careers pages on 2026-10-24.
**Market:** Every residential agency pays from DSP hours saved and billed days protected; the buyer is the COO or VP of compliance. Therap is the incumbent record system across 15,000+ agencies, and SETWorks markets itself as "AI-native", so a new entrant either integrates with the record system or replaces it. No forward deployed engineer role was found at any IDD vendor.

---

## 2. Critical Incident Command Platform
#ai-platform #bert #large-language-models #logistic-regression #compliance #workflow-orchestration #data-integration

**Concept:** A platform that runs every critical incident from first report to closed corrective action. It classifies each narrative against the state's definitions and starts the reporting clock. It assembles the investigation file: statements, the behaviour plan, the staffing roster, MAR records and prior incidents for the same person. It tracks every deadline the state sets and drafts the corrective action plan. A state edition links Medicaid claims and protective services data to provider reports to find unreported incidents, which the Access Rule requires.
**Inputs:** Incident reports from providers or the agency's record system; state definitions and timeframes; staff statements; claims and ER notifications; investigation outcomes.
**Outputs / Actions:** Category and deadline per incident; investigation packets; deadline alerts; corrective action plans and their closure evidence; dashboards of the 90% initiation, completion and corrective-action metrics each state must report.
**Why now:** From 9 July 2027 every state must meet 90% timeliness on initiating and completing investigations and completing corrective actions, and from 9 July 2029 it must run an electronic incident system that collects, tracks and trends incidents (89 FR 40542). Many state DD agencies and providers will buy or upgrade in the next two years. LLMs can draft investigation summaries and corrective actions from messy statements.
**Market:** Two buyers. Providers' compliance directors buy the provider edition. State DD and Medicaid agencies buy the state edition through procurement, which is slow but not a kill switch. Therap's general event reports and state-built systems are the incumbents.

---

## 3. House Staffing Agent
#ai-agent #time-series-forecasting #survival-analysis #gradient-boosting #worker-facing #workflow-orchestration

**Concept:** An agent that keeps every house staffed without forcing doubles. It forecasts call-offs by house and shift and books voluntary standby cover in advance. On a call-off it offers the shift by text to qualified DSPs in order of likely acceptance, checking med certification, person-specific training, driver's licence, gender preferences and weekly overtime, and it confirms cover before anyone is mandated. It tracks mandated shifts per person, flags new DSPs whose schedules match the pattern of early leavers, and shows the director overtime cost by house.
**Inputs:** Schedules, timeclock and payroll exports; staff qualifications and training records; resident staffing requirements; DSP availability and preferences.
**Outputs / Actions:** Shift offers and confirmations; standby bookings; mandated-overtime ledger; early-tenure risk list for supervisors; weekly overtime and coverage reports.
**Why now:** Turnover averaged 37% in 2024, 64% of leavers went within a year, and 26% of agencies turned away referrals for lack of staff (NCI). Overtime is now the main fill source. Phone-based shift marketplaces have trained DSPs to accept offers by text. Netsmart, whose myEvolv platform serves human-services providers including IDD agencies, had 35 engineering openings on its own Workday board on 2026-10-24, onsite in Overland Park, KS and Bengaluru. HHAeXchange, an adjacent home-care and self-direction platform, lists principal, staff and senior software engineers in the United States on its own Lever board.
**Market:** Directors of residential services at agencies with 20+ homes. Generic workforce-management tools (UKG, When I Work) and IDD record-system scheduling modules compete for it, and none of them forecasts.

---

## 4. Rate Evidence Platform for Provider Associations
#ai-platform #linear-regression #feature-engineering #large-language-models #revenue-impact #data-integration

**Concept:** A platform that lets a state's provider association, or a multi-state operator, build its own evidence for rate negotiations. Member agencies upload payroll and cost data voluntarily. The platform computes each service's cost per unit, wage and benefit levels, turnover and vacancy, and the share of habilitation payments reaching direct care workers in the Access Rule's own definitions. It benchmarks those against the state's rate model assumptions and drafts testimony and comment letters for each rate study and budget cycle.
**Inputs:** Member payroll and general ledger exports; claims and units billed; the state's published rate models and assumptions; NCI State of the Workforce state results.
**Outputs / Actions:** Cost-per-unit and compensation-share benchmarks by service; gap analyses against state rate assumptions; draft public comments and legislative testimony; the provider-level figures each member will need for its state's compensation-share report from 2028.
**Why now:** States must report the share of habilitation payments spent on direct care compensation from 9 July 2028 (89 FR 40542). Rate studies are under way, such as New Mexico's DD, Mi Via and Medically Fragile waiver review by Burns & Associates, whose comment period closed 19 December 2025. Providers usually arrive at these with spreadsheets.
**Market:** State provider associations and the largest multi-state operators (Sevita serves ~50,000 people in 40 states, Home Health Care News). Small and fragmented by state, but every rate cycle repeats, and consultancies currently do this work engagement by engagement.
