# Machine Learning Opportunities — Content Moderation Services

**Industry:** [[content-moderation-services|Content Moderation Services]]
**Derived from:** [[problems/content-moderation-services/high-impact|High Impact]], [[problems/content-moderation-services/low-impact-1|Low Impact 1]], [[problems/content-moderation-services/low-impact-2|Low Impact 2]], [[problems/content-moderation-services/worker-life-1|Worker Life 1]], [[problems/content-moderation-services/worker-life-2|Worker Life 2]]

---

## 1. Exposure Reduction: What Genuinely Needs Human Eyes
#transformers #cnns #large-language-models #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #worker-facing

**Problem statement:** Reviewers see material at full fidelity that could be presented reduced, review whole items when a segment was at issue, and receive severe categories in whatever order the queue delivers them. The vendor employs the people and carries the documented occupational liability; the exposure is determined by tooling on the platform's side.

**ML task:** Determine which items require human viewing and at what fidelity, isolate the segment at issue, and model cumulative per-reviewer severe-category exposure to enforce rotation
**Input data:** Items with classifier outputs at segment level and severity estimates; historical review decisions and the information actually used to reach them; per-reviewer exposure history by category; queue composition over time; audit outcomes.
**Target:** Whether a correct decision can be reached from a reduced presentation — blurred, greyscale, muted, thumbnail, transcript summary, or an isolated segment — rather than from full-fidelity viewing.
**Evaluation metric:** Decision accuracy under reduced presentation against full-fidelity review is safety-critical and comes first: exposure reduction that degrades decisions has traded one harm for another and must be rejected. Then measure the exposure actually removed — severe items not viewed, minutes of full-fidelity viewing avoided — which is the outcome. Track cumulative severe-category exposure per reviewer as a managed health metric with enforced limits, as every profession with comparable documented risk does.
**Scope:** Several components can be built vendor-side rather than waiting for the client, which matters because the party carrying the liability is not the party controlling the tooling. This is the highest-value application of available models to this industry's own operation. 3 ML engineers plus occupational health input, 9-12 months.
**Data availability:** Review decisions and exposure records exist in workflow systems and are generally not used as health metrics. Client-side classifier outputs require contractual access.

---

## 2. Ambiguity-Aware Quality Measurement
#evaluation-metrics #confidence-intervals #bayesian-inference #hypothesis-testing #gradient-boosting #bert #compliance #tacit-knowledge-ml

**Problem statement:** Quality is agreement with an auditor applying policy literally, which marks contextually correct decisions wrong and teaches reviewers to stop interpreting — producing exactly the enforcement errors that surface publicly. The sample is also small enough that ordinary variation looks like performance difference.

**ML task:** Identify genuinely ambiguous cases, score them against a panel range rather than a single answer, and report reviewer quality with honest sampling uncertainty
**Input data:** Decisions with auditor adjudications; multi-adjudicator panel decisions on a sampled subset establishing the expert agreement ceiling; case features predicting ambiguity; reviewer decision histories; appeal outcomes where the client will share them.
**Target:** Whether a case is one on which experienced reviewers legitimately disagree, and — separately — whether a decision falls within the defensible range.
**Evaluation metric:** The expert agreement ceiling must be measured first and reported, because it is well below one and every quality claim in this industry is implicitly made against an assumption that it is not. Reviewer scores must carry intervals; managing people on a point estimate that noise could produce is both unfair and uninformative, and stating the interval makes "these two reviewers are not distinguishable" sayable, which is frequently the truth.
**Scope:** The commercial obstacle is that a harder metric must be agreed with a client who has no obligation to. The argument that works is that identifying which policy areas produce systematic disagreement is information the platform wants and currently obtains only through public controversy. Negotiating aggregate appeal outcomes per category and language is the version clients are most likely to grant. 2 ML engineers plus a policy specialist, 6-9 months.
**Data availability:** Decisions and audits are complete vendor-side. Panel adjudications must be created. Appeal outcomes sit with the client.

---

## 3. Precedent Retrieval and Policy Change Propagation
#bert #transformers #large-language-models #k-nearest-neighbors #contrastive-learning #evaluation-metrics #compliance #worker-facing

**Problem statement:** Consistency across thousands of reviewers is pursued through training and audit while the most useful guidance — how similar cases were previously decided and why — is not retrievable. Policy updates arrive weekly as bulletins everyone skims.

**ML task:** Retrieve the most similar previously-adjudicated cases with their outcomes and reasoning at the moment of decision, and propagate policy changes as specific consequences rather than as announcements
**Input data:** The full corpus of adjudicated decisions with reasoning where auditors recorded it; policy documents and their version diffs; each reviewer's own case mix and audit history; the case currently in front of the reviewer.
**Target:** Whether a retrieved precedent is judged relevant and whether its availability improves decision consistency.
**Evaluation metric:** Consistency is the measurable outcome — agreement between reviewers on matched case types before and after precedent availability — rather than retrieval relevance in isolation. For policy changes, measure the share of affected reviewers who correctly apply the new rule in the following week, against the current bulletin baseline. Precedent that is confidently wrong is worse than none, so retrieval must show its reasoning and its source rather than asserting an answer.
**Scope:** Each client's policy is different, so nothing transfers between accounts — which is exactly why a vendor serving several platforms should build this as a system taking a policy and a case corpus rather than as a bespoke build per client. Capturing auditor reasoning on hard cases is the prerequisite and builds the case law this industry lacks. 2 ML engineers, 6-9 months.
**Data availability:** Decisions exist; reasoning mostly does not and must start being recorded.

---

## 4. Per-Language Performance and Locally Grounded Escalation
#transfer-learning #bert #transformers #large-language-models #contrastive-learning #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** Classifier performance and reviewer availability are both worst in the languages where platform growth is fastest and where moderation failure has been connected in public findings to serious offline harm. Aggregate multilingual scores hide the gap.

**ML task:** Measure and improve per-language classification with locally-labelled data, and build escalation paths staffed by people with regional context
**Input data:** Locally-labelled data per language and dialect created deliberately; code-switched and slang-heavy content; regional context from local expert panels and civil society input; reviewer coverage and volume by language; incident history by market.
**Target:** Per-language precision and recall against locally-adjudicated labels — never an aggregate multilingual score.
**Evaluation metric:** Report per language and per dialect, always separately. A model performing well on average across fifty languages may be unusable in fifteen, and the aggregate is the mechanism by which that stays invisible. Measure coverage relative to volume and risk, which identifies where resourcing is thinnest and is currently determined by contract negotiation and labour market availability rather than by need.
**Scope:** Local context is the part no model supplies: whether a phrase is a threat depends on who says it to whom in what situation, and in markets with active conflict that knowledge sits with people in the region. The operational design — regional expert panels, civil society input, escalation staffed by people with context — is the substance, with the model in support. Decision support is most valuable for reviewers working with the least automated assistance, which is the same population. 3 ML engineers plus regional specialists, 12 months.
**Data availability:** Locally-labelled data largely does not exist and creating it is the project. This is the binding constraint and the reason the gap persists.
