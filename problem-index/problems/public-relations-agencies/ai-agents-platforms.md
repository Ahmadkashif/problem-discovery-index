# AI Agents & Platform Opportunities — Public Relations Agencies

**Industry:** [[public-relations-agencies|Public Relations Agencies]]

---

## 1. Media Relations Memory Platform
#ai-platform #tacit-knowledge-ml #transformers #gradient-boosting #evaluation-metrics #revenue-impact

**Concept:** A platform that turns an agency's scattered outreach (pitch drafts, sends, replies, phone notes) into a pitch ledger joined to the coverage each pitch produced, and learns from it which reporter, angle and access choices work. It drafts each ledger record from the team's own material for one-click confirmation, keeps a living profile of every reporter the agency works with, including what the departed senior publicist knew about them, and ranks reporters and angles for every new story with the evidence shown.
**Inputs:** Outreach platform logs and email, coverage from the monitoring feed, reporters' published work, the client's priority outlet list and message house, senior staff's keep and drop decisions.
**Outputs / Actions:** Ranked reporter–angle lists for each announcement; reporter briefing cards; hit-rate and relevance scorecards by account team; handover packs when staff leave; warnings when a planned pitch conflicts with a reporter's recorded preferences.
**Why now:** Embedding models can represent a reporter by everything they have written at trivial cost, and LLMs can draft structured records from messy outreach notes, so capture no longer depends on staff discipline. Journalists' rising deletion rates make pitch relevance a commercial constraint, not a courtesy.
**Market:** Mid-size and large agencies and in-house teams. Outreach vendors (Muck Rack, Cision, Meltwater) are the natural incumbents but sell databases and send tools, not graded judgement.

---

## 2. Crisis Watch Agent
#ai-agent #change-point-detection #survival-analysis #large-language-models #worker-facing #workflow-orchestration

**Concept:** An agent that runs the overnight watch on a live issue: it monitors news, broadcast, social and reporter inquiries, estimates the chance and timing of escalation, wakes a human only above the senior counsellor's threshold, keeps a single approved fact sheet, checks every new draft statement against it and against any regulatory filing language, and writes the morning handover.
**Inputs:** Monitoring and listening feeds, reporter inquiry logs, the client's approved facts and legal edits, filing drafts (for example a Form 8-K Item 1.05 disclosure), stakeholder lists.
**Outputs / Actions:** Escalation alerts with reasons; draft holding statements and Q&A updated to the latest approved facts; inconsistency flags between statement, customer notice and filing; a reporter-interaction log; handover summaries.
**Why now:** LLMs can keep long, changing fact sets consistent across many drafts, and the SEC's four-business-day cyber disclosure rule has put a statutory clock on a class of crises that agencies and law firms now plan for in advance.
**Market:** Crisis and corporate practices at agencies, cyber-incident communications firms on insurer and law-firm panels, and in-house corporate communications teams. Monitoring vendors sell alerts; nobody sells the escalation call plus the statement discipline.

---

## 3. Coverage Measurement Agent
#ai-agent #bert #large-language-models #causal-inference #evaluation-metrics #automation

**Concept:** An agent that produces each client's monthly measurement report without the account executive's lost day: it collapses syndication, removes false matches, codes each piece for message pull-through, tier, spokesperson and tonality against the client's message house, links coverage windows to the client's own outcome data where access is granted, and drafts the narrative in a Barcelona Principles 4.0-compliant form with no advertising value equivalents.
**Inputs:** Monitoring exports, client message house and priority outlets, campaign calendar, client web analytics and search data, prior months' reports.
**Outputs / Actions:** Coded coverage table with supporting passages; message pull-through and share-of-voice trends; outcome estimates with intervals; a draft report and slide deck; a sample of items flagged for human check.
**Why now:** Few-shot classification with LLMs makes client-specific message coding feasible without training a model per client, and AMEC's 2025 restatement against AVEs gives agencies a reason to replace the metric clients still ask for.
**Market:** Independent agencies that cannot afford analyst-written measurement, and measurement firms themselves (see the Pass 2 pockets in [[niches/public-relations-agencies/_overview|the niche analysis]]), who could use the same pipeline to cut coding cost.

---

## 4. Earned Media AI-Visibility Platform
#ai-platform #large-language-models #causal-inference #time-series-forecasting #revenue-impact #data-integration

**Concept:** A platform that tracks how a client appears in AI assistants' answers across a fixed panel of buyer questions, traces which articles and sources those answers cite, and connects the agency's coverage to changes in citation share, so PR can plan earned media against the sources AI models actually read.
**Inputs:** Scheduled queries to major AI assistants, cited links, the agency's coverage archive, competitor coverage, the client's priority questions.
**Outputs / Actions:** Citation share by question and assistant; the outlets and articles most often cited; coverage targets ranked by expected citation impact; before-and-after estimates around campaigns.
**Why now:** Muck Rack's tracking finds that more than 80% of links cited by AI models are earned media, with journalism around 27% of cited sources, so clients now ask agencies what their coverage does for AI answers, and there is no accepted way to measure it.
**Market:** Agencies selling earned media as AI visibility, and brands' communications and SEO teams. A crowded early market of trackers (including Muck Rack's own Generative Pulse) competes on dashboards; the opening is the causal link from coverage to citation.
