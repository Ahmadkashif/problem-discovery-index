# AI Agents & Platform Opportunities — Sell-Side Equity Research

**Industry:** [[sell-side-equity-research|Sell-Side Equity Research]]
**Derived from:** [[problems/sell-side-equity-research/high-impact|High Impact]], [[problems/sell-side-equity-research/low-impact-1|Low Impact 1]], [[problems/sell-side-equity-research/low-impact-2|Low Impact 2]], [[problems/sell-side-equity-research/worker-life-1|Worker Life 1]], [[problems/sell-side-equity-research/worker-life-2|Worker Life 2]]

---

## 1. Coverage Memory Platform
#ai-platform #tacit-knowledge-ml #gradient-boosting #large-language-models #evaluation-metrics #revenue-impact

**Concept:** A department-wide record of every published view joined to what happened. For each covered company it holds the estimate history by line item, every management guide against the result, the line items whose surprises moved the stock, the notes and transcript passages behind each revision, and a calibration scorecard per analyst. It is the hand-over file when an analyst leaves and the training file when an associate joins.
**Inputs:** Published estimates and ratings archive; guidance and transcripts; reported results; price data; model versions; published notes.
**Outputs / Actions:** Guidance-bias profiles per management team; "what it trades on" history per stock; private analyst calibration reports; successor briefing packs; a director-of-research view of which coverage carries measured forecasting value.
**Why now:** LLMs make guidance and rationale extraction from years of transcripts and notes cheap, and every department already holds the forecast archive. Post-MiFID II budget pressure means departments must show clients which calls carry information.
**Market:** Directors of research at bulge-bracket, mid-tier and regional brokers; independent research providers. Several hundred research departments globally, sold on franchise retention.

---

## 2. Earnings Morning Agent
#ai-agent #large-language-models #transformers #k-nearest-neighbors #automation #worker-facing

**Concept:** An agent that watches each covered company's release, extracts the numbers, fills the analyst's own model through a learned mapping, builds the variance table against the analyst's estimates and consensus, retrieves the analyst's prior first-take notes, and drafts the note with every figure cited — ready for the analyst before the morning meeting.
**Inputs:** Release feeds; filings; the analyst's model; the analyst's prior notes; consensus data.
**Outputs / Actions:** Proposed model fill with source links and flags; variance table; first-take draft; flagged presentation changes; estimate-submission drafts to aggregators after analyst approval.
**Why now:** Release extraction and grounded drafting are now reliable enough to review rather than redo; the bottleneck has moved to the per-analyst mapping and voice, which are learnable from the department's own history.
**Market:** Research departments of every size; strongest pull at mid-tier and regional brokers where one analyst covers twenty-plus names with one associate or none.

---

## 3. Research Release Pre-Review Agent
#ai-agent #large-language-models #bert #compliance #workflow-orchestration #quick-win

**Concept:** Sits between authoring and supervisory analyst review, checks every draft against Rule 2241, Reg AC, the firm's written supervisory procedures and the live control-room lists, and returns passage-level flags with the rule cited so the reviewer clears clean reports in seconds and spends time on the ones that need judgment.
**Inputs:** Draft reports from the authoring system; disclosure database; restricted, watch and quiet-period lists; written supervisory procedures.
**Outputs / Actions:** Flags with citations; suggested disclosure additions; an audit log of checks per report.
**Why now:** LLMs read regulatory prose and report prose well enough for a bounded checklist, and the earnings-morning release queue is an obvious, measurable bottleneck.
**Market:** Research compliance at broker-dealers; authoring platform vendors as a channel.

---

## 4. Research Value Attribution Platform
#ai-platform #causal-inference #gradient-boosting #confidence-intervals #revenue-impact

**Concept:** Joins every client interaction — reads, downloads, calls, meetings, events, bespoke requests — to broker votes and research payments, and estimates where value is created by analyst, sector and interaction type, for pricing in unbundled markets and for effort allocation everywhere.
**Inputs:** CRM and corporate access logs; readership feeds from platforms; vote results; commission and RPA payments.
**Outputs / Actions:** Per-analyst guidance; client-level value estimates; pricing evidence for subscription tiers; flags where service consumption and payment diverge.
**Why now:** The 2024 FCA rebundling option and continued EU and US divergence mean departments must price and defend research by client, and the data to do it is finally centralised in readership platforms.
**Market:** Heads of research and research sales management at brokers; also asset managers' research budget teams from the opposite side.
