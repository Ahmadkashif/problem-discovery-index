# Machine Learning Opportunities — Product Design Studios

**Industry:** [[product-design-studios|Product Design Studios]]
**Derived from:** [[problems/product-design-studios/high-impact|High Impact]], [[problems/product-design-studios/low-impact-1|Low Impact 1]], [[problems/product-design-studios/low-impact-2|Low Impact 2]], [[problems/product-design-studios/worker-life-1|Worker Life 1]], [[problems/product-design-studios/worker-life-2|Worker Life 2]]

---

## 1. Pattern-Level Design Outcome Estimation Across Engagements
#causal-inference #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #k-nearest-neighbors #tacit-knowledge-ml #revenue-impact

**Problem statement:** A studio runs twenty engagements a year making causal claims about interface decisions and keeps none of the evidence, because the outcome lands in the client's analytics after the contract closes. Every project therefore relitigates the same questions from opinion.

**ML task:** Estimate the effect of recurring design patterns — step count in a flow, disclosure strategy, default selection, error handling, form structure — pooled across engagements with context as a covariate
**Input data:** Pre- and post-launch metrics from client analytics under a measurement clause; the design decisions taken, coded at pattern level rather than as project descriptions; product context — audience, device mix, task type, price point; the confounding releases and campaigns in the launch window; staged rollout or holdback assignment where negotiated.
**Target:** Change in the agreed primary metric attributable to the pattern, not to the project.
**Evaluation metric:** Where a staged rollout or holdback exists, the experimental estimate is ground truth and the pooled model should be scored against it. Where it does not, report the pre-post estimate with the confounders enumerated and an interval wide enough to be honest — a confident causal claim from an unstaged full redesign is not defensible and the product should say so rather than produce a number. Evaluate on held-out engagements, since the whole value is generalising to the next client.
**Scope:** Pattern-level coding is the unglamorous prerequisite and the usual point of failure: a project description is not a feature, and without a disciplined pattern taxonomy this degenerates into a portfolio with numbers attached. Thirty engagements is enough to start; three hundred is not required. The binding constraint is contractual access to post-launch data, which is a clause rather than a technology. 1 data scientist plus a design lead, 6-9 months once data access exists.
**Data availability:** Currently near zero and entirely obtainable. This is a negotiation problem wearing a modelling problem's clothes.

---

## 2. Design System Adoption and Bypass Diagnosis
#bert #transformers #change-point-detection #gradient-boosting #k-means-clustering #evaluation-metrics #data-integration #automation

**Problem statement:** A delivered design system diverges from production code the week the studio leaves, and the divergence is invisible until the product looks incoherent enough to fund an audit.

**ML task:** Measure the proportion of rendered UI originating from system components, track drift over time, and cluster bypasses by their cause
**Input data:** The client's component source and rendered output; design token definitions and their usage in code; commit history around bypass introductions; the design system's component APIs and documentation; issue tracker discussion around UI work.
**Target:** Adoption rate per surface and per component, and the cause category for each bypass — missing variant, rigid API, documentation gap, deadline workaround.
**Evaluation metric:** Adoption measured against a manually audited sample for calibration, since an automated estimate that counts imports rather than rendered output will overstate adoption substantially. For cause clustering, agreement with the maintainers' own assessment on a reviewed sample. The operational metric is whether the identified fixes actually reduce subsequent bypasses, which is testable over a quarter.
**Scope:** Per-client codebase conventions are why no generic product exists; the analysis has to be adapted per framework and per repository structure, which makes this a service with a tooling core rather than a product. A component everyone bypasses is a design failure, not a discipline failure, and the cause clustering is what makes that distinction visible. 1-2 engineers, 4-6 months for the first two client stacks.
**Data availability:** Requires codebase access, which clients grant readily for this purpose since the finding serves them.

---

## 3. Project Overrun Forecasting From a Studio's Own History
#survival-analysis #gradient-boosting #confidence-intervals #time-series-forecasting #bayesian-inference #change-point-detection #evaluation-metrics #revenue-impact

**Problem statement:** Fixed-fee engagements are priced from a principal's memory of comparable work, overrun far more often than they underrun, and the causes are recurring and knowable — yet none of them appear in the estimate.

**ML task:** Predict final effort as a distribution from project characteristics at proposal time, and forecast burn trajectory during delivery with enough lead time to intervene
**Input data:** Historical time tracked by project, phase and role against original estimate; project characteristics known at proposal — client size, stakeholder count, sector, engagement type, whether engineering participates in discovery, whether legal review is in scope; change orders with their timing and cause; in-flight burn curves.
**Target:** Final effort against estimate, and at any point during delivery, the projected remaining effort.
**Evaluation metric:** Calibration of the predictive interval matters far more than point accuracy — the commercial use is pricing contingency and the current practice is a nervousness-based margin, so an honest interval is the improvement. For in-flight forecasting, measure how early a twenty per cent overrun becomes detectable with reasonable confidence; three weeks of lead time on a twelve-week project is the difference between a routine conversation and a difficult one.
**Scope:** Sample sizes are small — a studio completes tens of projects a year, not thousands — so this is a hierarchical, few-feature problem where restraint matters and a complex model will overfit immediately. Named risk drivers in the proposal are as valuable as the number. 1 data scientist, 3-4 months.
**Data availability:** Every studio has years of time tracking and uses it only for invoicing. The overrun causes exist in project notes and change orders and need extracting.

---

## 4. Review Feedback Consolidation and Decision Records
#large-language-models #bert #word-embeddings #k-nearest-neighbors #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** Stakeholder feedback arrives across several channels from many people, partly contradictory, with no record of what was already decided — so decisions reopen, rounds multiply, and work finished in week three is still being revised in week nine.

**ML task:** Deduplicate and cluster incoming feedback, classify each item by type, and maintain a decision record linking each closed decision to its rationale and the comments it resolves
**Input data:** Comments from design tools, email, chat and meeting transcripts; the design artefacts they refer to; prior decisions and their stated rationale; commenter role and authority; project phase.
**Target:** Feedback type — an unknown constraint, a preference, a misunderstanding of intent, a usability concern — and whether an item restates something already decided.
**Evaluation metric:** Classification accuracy against designer labelling on a sample, with the constraint category weighted most heavily: missing a genuine constraint buried in a preference-shaped comment is the expensive error, since it surfaces later as rework. For reopening detection, measure the reduction in review rounds over comparable projects, which is the outcome the work exists for.
**Scope:** The classification is the useful part and is well within reach; the decision record is mostly workflow. The distinction between a preference and a constraint is genuinely hard in some cases and the system should surface ambiguity rather than resolve it silently — a stakeholder's preference misclassified as a constraint entrenches exactly the dynamic this is meant to fix. 1-2 engineers, 4-6 months.
**Data availability:** Comment history exists across tools and needs integration. Labelled feedback types must be created and are quick to produce.
