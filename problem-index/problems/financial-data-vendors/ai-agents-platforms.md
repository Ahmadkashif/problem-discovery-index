# AI Agents & Platform Opportunities — Financial Data Vendors

**Industry:** [[financial-data-vendors|Financial Data Vendors]]

---

## 1. Collection Copilot With Decision Capture
#ai-agent #tacit-knowledge-ml #large-language-models #k-nearest-neighbors #evaluation-metrics #worker-facing #automation

**Concept:** An agent embedded in the collection tool that reads each new filing before the analyst does. It pre-maps every line item with calibrated confidence, skips the fields that match the issuer's settled history, and for each judgement item presents the issuer's prior treatment, the closest precedents at peer issuers and the relevant policy paragraph. Every analyst action — accept, override, escalate, the passage they were reading — is captured as a structured decision record. It is the capture mechanism and the assistant at once, which is the only way the capture survives earnings season.

**Inputs:** Filings and XBRL; the vendor's standardised template and policy library; historical mappings per issuer; resolved client tickets; analyst actions in real time.
**Outputs / Actions:** Pre-mapped templates with confidence; precedent panels; escalation to seniors with the disagreement history attached; a growing decision corpus; consistency reports across issuers and analysts for content leadership.
**Why now:** Long-context models can read a full 10-Q with footnotes in seconds, and retrieval over millions of prior decisions is cheap; what was missing was the willingness to treat the collector's judgement as the asset rather than the cost.
**Market:** Content and data operations leadership at every fundamentals vendor and at the smaller specialists building model-ready data (Daloopa, Calcbench and others); the buyer already owns a large collection budget.

---

## 2. Number Lineage and Discrepancy Agent
#ai-agent #large-language-models #bert #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration

**Concept:** An agent that answers "why does this number differ" for client data specialists and, eventually, for clients directly. It assembles a value's lineage — source page, as-reported components, adjustments and policy version, restatement history — reconciles it against the company's own press-release figure and the vendor's prior value, decomposes the difference into named items, and retrieves how the same question was answered before. When the answer is a genuine error, it opens the correction with content operations and tracks it to release.

**Inputs:** Client question; value lineage and audit logs; methodology documents; restatement history; resolved tickets; company press releases.
**Outputs / Actions:** A sourced explanation with the decomposition; a draft reply; correction tickets routed upstream; root-cause statistics that tell collection which fields generate the most confusion.
**Why now:** The explanation is a retrieval-and-synthesis task over documents the vendor owns, which current models do well when every claim is tied to a source.
**Market:** Every terminal and fundamentals vendor's client service organisation; the measurable outcome is time-to-answer on the tickets clients raise immediately before their own deadlines.

---

## 3. Exchange Policy and Declaration Agent
#ai-agent #large-language-models #bert #feature-engineering #evaluation-metrics #compliance #workflow-orchestration

**Concept:** An agent that reads every exchange's market-data policy and fee schedule each time it changes, converts it to versioned structured rules, joins those rules to entitlement and usage events, and drafts the monthly declarations with every figure traceable to a rule. It reviews client non-display self-declarations against policy categories and flags usage that contradicts them, and before an audit it reproduces historical declarations under the policy then in force.

**Inputs:** Exchange policy documents and fee schedules; entitlement system events; client declarations; contracts.
**Outputs / Actions:** Draft declarations per exchange; policy-change impact reports; mismatch flags; audit packs with provenance.
**Why now:** The policies are prose that changes annually, which was the barrier to automating them; reading and structuring prose is now cheap and checkable.
**Market:** Vendors' exchange-relations and entitlements teams, redistributors, and large consuming institutions' market data offices, all of whom face the same audits.

---

## 4. Private-Markets Research Agent
#ai-agent #large-language-models #graph-theory #transformers #evaluation-metrics #data-integration #automation

**Concept:** An agent that does the first pass of private-markets collection: monitors pension board agendas and filings, files and tracks FOIA requests, extracts cash flows and NAVs from the responses, watches Form D and press releases for new rounds, and drafts the outreach to a GP when a figure is missing or inconsistent. Researchers verify and handle the relationships; the agent handles the document chase.

**Inputs:** Public pension disclosures and FOIA responses; regulatory filings; news; the vendor's entity graph; researcher verification decisions.
**Outputs / Actions:** Extracted fund and deal records with confidence; entity-resolution proposals; drafted FOIA requests and GP queries; coverage gap reports.
**Why now:** Document extraction from inconsistent PDFs and routine correspondence drafting are both now reliable enough to run at volume with human verification.
**Market:** Private-markets data vendors and the research teams of large LPs and consultants who maintain their own databases.
