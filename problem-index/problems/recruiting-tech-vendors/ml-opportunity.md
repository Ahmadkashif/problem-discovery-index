# Machine Learning Opportunities — Recruiting Tech Vendors

**Industry:** [[recruiting-tech-vendors|Recruiting Tech Vendors]]
**Derived from:** [[problems/recruiting-tech-vendors/high-impact|High Impact]], [[problems/recruiting-tech-vendors/low-impact-1|Low Impact 1]], [[problems/recruiting-tech-vendors/low-impact-2|Low Impact 2]], [[problems/recruiting-tech-vendors/worker-life-1|Worker Life 1]], [[problems/recruiting-tech-vendors/worker-life-2|Worker Life 2]]

---

## 1. False Rejection Measurement Through Audit and Marginal Randomisation
#causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #gradient-boosting #evaluation-metrics #compliance #cross-validation

**Problem statement:** A rejected candidate produces no outcome data, ever, so models trained on this record learn which candidates recruiters selected rather than which would have performed — the structural condition behind the field's canonical public failure.

**ML task:** Estimate the false rejection rate through blind expert re-review of sampled rejections, and generate genuine causal evidence by advancing a small random subset of candidates falling just below a screening threshold
**Input data:** Rejected applications with the stage and stated reason; screening scores and threshold position; blind expert re-review judgements; randomised marginal advancement assignment and subsequent stage outcomes; post-hire tenure, promotion and involuntary exit for those eventually hired; demographic data where lawfully available.
**Target:** Disagreement between original and blind re-review; and for the randomised arm, subsequent performance of candidates who would otherwise have been rejected.
**Evaluation metric:** The randomised arm is the only design producing genuine evidence and its cost is low precisely because the candidates are marginal by definition. Report the false rejection rate with its demographic distribution, which is the finding that matters and is invisible under any observational approach. Re-review disagreement measures agreement with a different human rather than performance, and should be labelled as such rather than presented as validation.
**Scope:** The obstacle is operational and political rather than financial — an employer must deliberately interview people their system screened out, which is awkward and cheap. A programme running two years at a large employer would settle questions this field has argued indefinitely. 1-2 data scientists plus an operations sponsor, 18-24 months to a result.
**Data availability:** Applications and decisions are complete; the randomised arm and the re-review both have to be deliberately created and neither exists anywhere as standard practice.

---

## 2. Honest Labelling and Bias Monitoring of Ranking Features
#gradient-boosting #hypothesis-testing #confidence-intervals #causal-inference #bayesian-inference #evaluation-metrics #compliance #probability-distributions

**Problem statement:** Ranking features are described as identifying strong candidates when they predict recruiter agreement, and the two are equivalent only if past selection was accurate and unbiased — which is exactly what nobody has established.

**ML task:** Characterise what each ranking model actually predicts, and monitor whether its output correlates with demographic characteristics conditional on qualifications
**Input data:** Model training labels and their provenance — advancement, hire, recruiter rating; model outputs across the applicant population; applicant qualifications and demographics where lawfully collected; downstream stage outcomes; post-hire outcomes for the hired subset.
**Target:** The model's realised prediction target stated accurately, and conditional demographic correlation in its output.
**Evaluation metric:** For labelling, the deliverable is a description rather than a metric and it is the most consequential honesty available in this market — a model trained on advancement decisions predicts advancement decisions, and saying so would change how these products are bought. For bias monitoring, the specific check is whether output correlates with demographic characteristics after conditioning on qualifications, which is the test that would have caught the canonical failure before deployment rather than after. Report it continuously rather than annually.
**Scope:** Validation against post-hire outcomes covers only the hired population and inherits the range restriction problem, so it establishes less than it appears to; pairing it with the marginal randomisation programme is what makes it meaningful. Performance ratings as a criterion carry their own biases and may validate a model against the bias it inherited. 1-2 data scientists, 6 months.
**Data availability:** Complete for model outputs and decisions; demographic data collection varies by jurisdiction and employer.

---

## 3. Capability Representation Beyond Keyword Matching
#contrastive-learning #bert #word-embeddings #large-language-models #graph-neural-networks #k-nearest-neighbors #dimensionality-reduction #evaluation-metrics

**Problem statement:** Filters exclude by vocabulary rather than capability, which systematically removes career changers, people from adjacent industries and anyone whose experience is described unconventionally — and generative tooling has destroyed the remaining signal on both sides of the application.

**ML task:** Represent demonstrated capability in a form that matches across different descriptions of the same work, and identify equivalence across non-linear career shapes
**Input data:** Application and profile content describing work performed; role requirements as written and as revealed by what actually mattered post-hire; skills taxonomies and their gaps; historical advancement and hire decisions for weak supervision; post-hire outcomes for the hired subset.
**Target:** Whether a candidate possesses the capability a role requires — for which the honest label is unavailable, so the model must be built and presented with that uncertainty rather than as a fit score.
**Evaluation metric:** Recall on candidates who were hired and succeeded but would not have passed a keyword filter is the useful measure, and it is computable retrospectively at any large employer — it directly quantifies what the current filters miss. Resist evaluating against advancement decisions, which reproduces the problem. Report the model's uncertainty prominently: a surfacing tool that says this candidate may be worth reading is defensible, and a fit score is not, given what is knowable.
**Scope:** Requirement deflation belongs alongside it: comparing listed requirements against what post-hire evidence says actually mattered would change who applies at all, more than any ranking improvement. Sourcing diversity — not surfacing the same saturated candidates to every recruiter — is a ranking design choice against nobody's interest. 2-3 engineers, 9-12 months.
**Data availability:** Application content is abundant; capability labels do not exist and the honest design acknowledges it.

---

## 4. Interview Scheduling as Robust Constrained Optimisation
#convex-optimization #optimization-fundamentals #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Panel scheduling across skill coverage, availability, load balance and candidate constraints is solved greedily by messaging, consumes days, and collapses entirely when one interviewer cancels the day before.

**ML task:** Solve panel assignment as a constrained optimisation with substitution robustness as an explicit objective, and predict interviewer cancellation risk
**Input data:** Interviewer skills, availability and current load; panel composition requirements and sequencing constraints; candidate availability and time zone; historical cancellation and reschedule events with their predictors; stage-level cycle time and its relationship to offer acceptance.
**Target:** A feasible schedule maximising substitution options subject to constraints, and the probability that a given interviewer cancels.
**Evaluation metric:** Time from request to confirmed schedule against the messaging baseline, and — the measure that matters more — the proportion of cancellations absorbed by substitution rather than by rescheduling the whole panel. Robustness should be an objective from the start rather than a repair mechanism, since a schedule with more substitution options is worth more than a marginally better one with none. Track stage-level cycle time against offer acceptance, since coordination delay is the largest controllable component of a well-established conversion driver.
**Scope:** Interviewer load balancing should be a standing objective rather than a coordinator's memory, which currently concentrates the burden on whoever says yes and leaves everyone else unpractised. 1-2 engineers, 4-6 months.
**Data availability:** Complete within the applicant tracking system and calendar integrations.
