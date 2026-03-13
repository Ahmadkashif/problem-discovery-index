# AI Agents & Platforms — Medical Billing

**Industry:** [[medical-billing|Medical Billing]]
**Derived from:** [[problems/medical-billing/high-impact|High Impact]], [[problems/medical-billing/low-impact-1|Low Impact 1]], [[problems/medical-billing/low-impact-2|Low Impact 2]], [[problems/medical-billing/worker-life-1|Worker Life 1]], [[problems/medical-billing/worker-life-2|Worker Life 2]]

---

## 1. Pre-Submission Claim Scrubbing Agent
#ai-agent #revenue-impact #compliance

**What it does:** An agent that intercepts every claim before submission, runs it against a continuously updated denial prediction model and payer-specific rule engine, and either auto-fixes correctable issues (missing modifier, incorrect POS code) or routes the claim to a human with a specific diagnosis and recommended fix. It learns from every denial that gets past it to improve its rules.

**Who uses it:** Billers (review flagged claims), billing company owners (denial rate dashboards)
**Decisions it makes/augments:** Claim validation (automates), auto-correction for known fixable issues (automates — biller can review), routing of unfixable claims with diagnosis (augments biller's investigation), rule updates from new denial patterns (automates detection — human confirms new rule)
**Why an agent:** Claim scrubbing requires real-time decision-making on every claim, integration with a dynamic knowledge base of payer rules, and a learning loop that incorporates new denial patterns. The agent must also manage timing — holding a claim for review costs money if it delays timely filing.
**Compounding value:** Every denied claim that was missed is a training signal. The agent's denial prevention rate improves continuously. Across a billing company's client base, patterns in one specialty inform rules for others.

---

## 2. AR Follow-Up Agent
#ai-agent #worker-facing #automation

**What it does:** An autonomous agent that handles the first tier of AR follow-up. It checks claim status via electronic 276/277 transactions and payer portals, categorizes the result (paid and needs posting, pending with estimated date, denied with reason, no record found), and routes each claim to the appropriate next step. For denied claims, it pre-writes the resolution (resubmission with correction, appeal with supporting docs, patient billing). The human AR specialist handles only the complex cases that require judgment or phone calls.

**Who uses it:** AR follow-up specialists (handle escalated cases), billing managers (monitor aging AR)
**Decisions it makes/augments:** Claim status checking (automates), status categorization (automates), resolution path determination (automates for standard denials — specialist reviews complex cases), appeal/resubmission generation (automates draft)
**Why an agent:** AR follow-up is the perfect agent use case: high-volume, repetitive first step (check status), branching decision tree (what to do based on status), and an escalation path to humans for edge cases. The agent eliminates the 60-70% of AR specialist time spent on hold or navigating portals.
**Compounding value:** Learns payer-specific resolution patterns. Builds a knowledge base of which denial reasons respond to which resolution approaches per payer. Reduces average days in AR as resolution speed increases.

---

## 3. Payer Intelligence Platform
#ai-platform #compliance #data-integration

**What it does:** A platform that aggregates payer rule changes, denial patterns, reimbursement trends, and policy updates into a unified intelligence layer for the billing company. It monitors payer bulletins and policy feeds, extracts structured rule changes, maps them to affected clients, tracks denial rates by payer/code/reason over time, and generates actionable alerts ("Blue Cross IL changed modifier policy for ortho codes — update your scrubbing rules by April 1, affects 3 of your clients").

**Who uses it:** Senior billers (rule implementation), billing company owners (payer relationship management), coders (coding guidance updates)
**Decisions it makes/augments:** Rule change detection and extraction (automates), client impact mapping (automates), denial trend analysis (automates), alert prioritization (automates — ranks by revenue impact)
**Why a platform:** Payer intelligence compounds — every rule change, denial pattern, and reimbursement anomaly adds to the knowledge base. A platform that maintains this institutional knowledge prevents the "tribal knowledge" problem where critical payer insights live only in senior billers' heads.
**Network effects:** Multi-billing-company deployment creates the largest payer rules database in the market. Denial patterns across the user base surface payer behavior changes faster than any individual company can detect.

---

## 4. Coder Workspace & Context Platform
#ai-platform #worker-facing #ml-nlp

**What it does:** A coding workspace that batches work by specialty and client, presents relevant context (client preferences, payer rules, applicable LCDs/NCDs, provider's recent coding history), and provides AI-assisted coding suggestions. When the coder opens a chart, the platform pre-suggests CPT/ICD codes based on the documentation, highlights documentation gaps that would support a higher code, and flags compliance risks. Reduces context-switching by organizing work into specialty-focused sessions.

**Who uses it:** Medical coders, coding supervisors (quality review)
**Decisions it makes/augments:** Code suggestion from documentation (augments — coder decides), documentation gap identification (automates), compliance risk flagging (automates), work batching by specialty/client (automates)
**Why a platform:** Coding quality depends on context — the same documentation might be coded differently depending on the payer, the specialty norms, and the client's preferences. A platform that maintains and surfaces this context per coding session transforms coding from a memory-intensive task to a supported decision task.
**Network effects:** Aggregate coding patterns across users improve suggestion accuracy. Cross-coder quality comparison enables training and benchmarking.

---

## 5. Payment Reconciliation & Contract Compliance Agent
#ai-agent #revenue-impact #automation

**What it does:** An agent that processes incoming ERAs, validates payments against contracted rates, auto-posts correct payments, flags underpayments with the specific contract term being violated, identifies secondary billing triggers, and calculates accurate patient responsibility. For each ERA batch, it produces a reconciled summary: X claims auto-posted, Y underpayments flagged ($Z at stake), W items need human review.

**Who uses it:** Payment posting staff, billing managers (underpayment recovery), client relationship managers (contract compliance reporting)
**Decisions it makes/augments:** Payment validation against contracts (automates), auto-posting of correct payments (automates), underpayment identification (automates), secondary billing triggers (automates), patient responsibility calculation (automates — staff reviews edge cases)
**Why an agent:** Payment reconciliation requires claim-by-claim judgment against client-specific contracts, real-time processing of ERA batches, and coordination across multiple systems (PM system, contract database, patient ledger). The agent orchestrates this multi-system workflow continuously as ERAs arrive.
**Compounding value:** Builds a payment accuracy database per payer that identifies systematic underpayment patterns. Over time, this data supports contract renegotiation ("this payer has underpaid $45,000 in the last 12 months on 99214 — here's the evidence").
