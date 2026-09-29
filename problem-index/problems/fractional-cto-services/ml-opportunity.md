# Machine Learning Opportunities — Fractional CTO Services

**Industry:** [[fractional-cto-services|Fractional CTO Services]]
**Derived from:** [[problems/fractional-cto-services/high-impact|High Impact]], [[problems/fractional-cto-services/low-impact-1|Low Impact 1]], [[problems/fractional-cto-services/low-impact-2|Low Impact 2]], [[problems/fractional-cto-services/worker-life-1|Worker Life 1]], [[problems/fractional-cto-services/worker-life-2|Worker Life 2]]

---

## 1. Technical Assessment Derived From Repository and Delivery History
#graph-neural-networks #gradient-boosting #change-point-detection #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #tacit-knowledge-ml

**Problem statement:** A fractional CTO forms a consequential opinion about an unfamiliar system in weeks, from interviews and reading, while the evidence that describes the system's real behaviour sits in repository and tracker history and is not used.

**ML task:** Derive an assessment base from version control and delivery data — change concentration, co-change coupling, churn and defect correlation, component stability, ownership concentration and bus-factor exposure, flow and rework characteristics
**Input data:** Full commit history with authorship and file paths; issue and ticket history with estimates, actuals and reopen events; incident records; deployment frequency and lead time; contributor tenure; test coverage and build history where available.
**Target:** Not a label but a characterisation — though where engagement outcomes are retained, the target becomes which measured patterns preceded the problems that actually materialised.
**Evaluation metric:** Agreement with experienced practitioners' independent manual assessments on the same systems is the initial validation. The real measure requires the retained corpus: whether the measured patterns predicted the problems that appeared over the following two years. Report the metrics with explicit caveats about what they cannot see — team dynamics, external constraints, and the reasons behind decisions are invisible to history and are where the practitioner's judgement remains indispensable.
**Scope:** This is an instrument for judgement rather than a replacement for it, and framing matters for adoption in a profession that sells experience. It must run in days under constrained access, which rules out anything requiring extensive instrumentation. 1-2 engineers, 4-6 months.
**Data availability:** Repository and tracker history is complete where access is granted, and read-only history access is frequently obtainable even in diligence contexts where full code review is not.

---

## 2. Key-Person Risk and Capacity Reality Under Diligence Constraints
#graph-neural-networks #gradient-boosting #survival-analysis #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance #time-series-forecasting

**Problem statement:** Diligence reports are written in two to four weeks under restricted access and consistently underweight the findings that post-close post-mortems identify as decisive: key-person dependency, undocumented integrations, and engineering capacity assumptions that were optimistic by a factor of two.

**ML task:** Quantify ownership concentration and bus-factor exposure per critical component, and test the plan's delivery capacity assumptions against the target's own historical throughput, cycle time and rework rate
**Input data:** Commit history with authorship and component mapping; contributor tenure and departure patterns; the growth plan's delivery assumptions; historical throughput, cycle time, estimate accuracy and rework rates; incident and escalation records; dependency and integration inventory.
**Target:** Post-close outcomes where a firm retains them — whether the identified risk materialised, and how actual delivery capacity compared with the plan.
**Evaluation metric:** Until a corpus exists, the measure is whether the analysis surfaces findings that experienced practitioners confirm as material but had not quantified. Once outcomes are retained across deals, base rates become available — which findings actually predicted problems — and that is the instrument no individual's experience can supply. Report capacity divergence as a range, since historical throughput under one set of conditions is an imperfect guide to another.
**Scope:** Ownership concentration is computable in hours from history alone and is almost never quantified in diligence reports despite being the most consistently decisive finding. Private equity operating groups running many deals are the only parties positioned to build the outcome corpus. 1-2 engineers, 4-6 months.
**Data availability:** History access is usually obtainable in diligence; post-close outcome retention is a process decision nobody has made.

---

## 3. Selection Fit Assessment From Operational Evidence
#bert #large-language-models #k-nearest-neighbors #gradient-boosting #confidence-intervals #evaluation-metrics #survival-analysis #tacit-knowledge-ml

**Problem statement:** Platform and vendor selections are durable and expensive to reverse, and rest on vendor documentation, analyst rankings weighted by an inspectable-to-nobody methodology, and the advisor's own small sample.

**ML task:** Assemble structured operational evidence from where it is actually recorded — incident write-ups, engineering blogs, community threads, conference talks — and assess fit against a client's specific constraints, including usage-shaped cost and estimated exit cost
**Input data:** Public incident and postmortem write-ups; engineering blog content and conference talks describing production experience; community threads on operational issues; vendor documentation and pricing models; the client's usage shape, team skills, operational maturity, compliance requirements and growth trajectory; dependency depth and proprietary surface area for exit estimation.
**Target:** Whether a selection met the client's needs at twelve and twenty-four months, retained across engagements.
**Evaluation metric:** Retrieval precision on genuinely relevant operational evidence is the first measure, and recency weighting matters enormously — a platform's operational reality three years ago may be irrelevant. Cost modelling is checkable against realised bills where a client shares them, which is the most concrete validation available. Exit cost estimates should be reported as ranges with the assumptions listed, since the honest answer is frequently a wide range and stating it is the point.
**Scope:** The operational evidence is scattered across sources with wildly varying reliability, and source credibility weighting is most of the work — a vendor's case study and an incident write-up from a team that left the platform are not equivalent inputs. 2 engineers, 6-9 months.
**Data availability:** Public operational writing is abundant and unstructured. Client usage shape requires the engagement. Outcome retention requires the look-back nobody contracts for.

---

## 4. Engagement Context Modelling and Decision Record Extraction
#large-language-models #bert #graph-neural-networks #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration #tacit-knowledge-ml

**Problem statement:** A fractional practitioner reconstructs context on every return visit across several clients, and when an engagement ends the reasoning behind the direction departs with them, leaving a team with a half-executed plan they cannot interrogate.

**ML task:** Assemble a change briefing per client since the last visit ranked by divergence from expectation, and extract decision records — what was decided, what was considered, what was rejected, what it assumes — from engagement correspondence and documents
**Input data:** Repository, ticket and incident activity since the last visit; team communications and meeting records where access is granted; delivery trend data; the practitioner's own notes, recommendations and prior decisions; engagement documents and slides.
**Target:** For briefing, whether the surfaced items are the ones the practitioner would have wanted flagged. For decision extraction, whether the record is accurate and complete as confirmed by the practitioner.
**Evaluation metric:** For briefing, precision at the top of the list — a practitioner with four clients needs three items per client, not a log, and a briefing that returns everything has reproduced the problem. For decision records, completeness on the rejected-alternatives and assumptions fields specifically, since those are what make a plan adaptable and are exactly what current documentation omits. Abstention where no rationale was recorded is correct and must not be filled with plausible reconstruction.
**Scope:** The externalised client model — architecture, decisions and rationale, team structure, open concerns, commitments — is what makes a fractional practice transferable rather than resident in one person's memory, and it is the same artefact that solves the handover problem. 2 engineers, 4-6 months.
**Data availability:** Client system access is granted during engagements; correspondence access varies and is the sensitive input.
