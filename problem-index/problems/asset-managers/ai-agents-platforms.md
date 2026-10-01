# AI Agents & Platform Opportunities — Asset Managers

**Industry:** [[asset-managers|Asset Managers]]

---

## 1. Research Memory Platform
#ai-platform #large-language-models #transformers #causal-inference #evaluation-metrics #tacit-knowledge-ml #data-integration

**Concept:** A platform that turns the research floor's scattered output into a graded, searchable record. It ingests meeting notes, models, recommendations, internal ratings and the PM's portfolio actions, timestamps every judgment, and joins each to subsequent factor-adjusted returns. Analysts and PMs query it in plain language — "what did we believe about this company's margin story in 2023, and what happened" — and successors inherit a coverage history rather than a folder. Access respects information barriers and restricted lists by construction.

**Inputs:** Research management system notes (FactSet RMS, Bipsync, Tamale) and email; model files; recommendation and rating changes; holdings and trades from the order management system; returns and factor exposures; restricted list and wall-crossing records.

**Outputs / Actions:** A recommendation ledger with per-analyst and per-sector hit rates and honest confidence intervals; natural-language search over the firm's own research history; pre-meeting briefs combining the last views, open questions and what would change the thesis; alerts when new company language contradicts a recorded thesis.

**Why now:** Language models can finally read a decade of unstructured analyst notes and extract judgments from them, and the cost of embedding and searching a firm's entire research archive has collapsed. Fee pressure from passive products has made active managers need evidence that their research adds value.

**Market:** Chief investment officers and directors of research at active long-only managers globally — several hundred firms with research floors of twenty or more analysts. Research management system vendors are the incumbents and are adding generative features to their own notes, but not grading.

---

## 2. RFP and Consultant Response Agent
#ai-agent #large-language-models #word-embeddings #k-nearest-neighbors #compliance #automation

**Concept:** An agent that receives an RFP, DDQ or consultant database update, identifies the strategy and vehicle in scope, drafts every answer from the approved library adapted to that context, fills numbers from the performance system, flags conflicts with prior submissions to any consultant, and routes the remaining questions to the right subject expert with a draft attached.

**Inputs:** Incoming RFP and DDQ documents; the content library; past submissions; performance, AUM and characteristics data; consultant database exports.

**Outputs / Actions:** A completed draft with confidence per answer; a consistency report; task routing to investment, operations, compliance and technology owners; a post-submission update to the library.

**Why now:** Retrieval-augmented generation over a firm's own document corpus is cheap and reliable enough for drafting with human review, and the RFP library vendors have shown the demand without solving the strategy-and-date awareness asset managers need.

**Market:** Institutional sales and consultant relations teams at asset managers; an existing buyer category served by Loopio and Responsive, which an asset-management-specific agent would compete with or plug into.

---

## 3. Commentary and Client Reporting Agent
#ai-agent #large-language-models #transformers #evaluation-metrics #compliance #worker-facing

**Concept:** At quarter-end the agent pulls attribution, trades and analyst rationales for every strategy, drafts the master commentary with each claim linked to source, sends it to the PM with the open judgment questions highlighted, applies compliance's marketing-rule checks, and generates every derivative format — fact sheet, client report, database narrative, shareholder report discussion — from the approved master.

**Inputs:** Attribution and performance; trade blotter; research rationales; approved past commentary; compliance rules and prior edits; document templates.

**Outputs / Actions:** Drafts, review packets, compliance flags and finished derivative documents with traceability back to the master text.

**Why now:** Grounded generation with claim-level citation has become practical, and the SEC's tailored shareholder report rule and the marketing rule have both raised the cost of narrative that does not match the numbers.

**Market:** Product specialist, investment writing, client reporting and marketing teams at asset managers; adjacent to fact sheet and reporting vendors such as Kurtosys and DFIN.

---

## 4. Stewardship Operations Agent
#ai-agent #large-language-models #bert #k-nearest-neighbors #compliance #workflow-orchestration

**Concept:** An agent that pre-votes routine ballot items against the firm's own policy, escalates contested and precedent-breaking items with similar past votes and engagement history attached, drafts rationales, logs engagements with objectives and milestones, and assembles the stewardship report and N-PX data from the records rather than from memory.

**Inputs:** Ballots and proxy statements; proxy adviser research; firm voting policy; vote history; engagement notes; PM holdings views.

**Outputs / Actions:** Proposed votes and escalations; draft rationales; engagement tracker; stewardship report sections; N-PX categorisation.

**Why now:** Political and regulatory scrutiny of how managers vote — from both directions — has made consistent, documented, policy-traceable voting a requirement, and language models can now read proxy statements at the volume of a full season.

**Market:** Stewardship and responsible investment teams at large and mid-sized managers; currently served by ISS and Glass Lewis voting platforms, which the agent would sit on top of rather than replace.
