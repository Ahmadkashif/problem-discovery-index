# Machine Learning Opportunities — Digital Accessibility Firms

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]
**Derived from:** [[problems/digital-accessibility-firms/high-impact|High Impact]], [[problems/digital-accessibility-firms/low-impact-1|Low Impact 1]], [[problems/digital-accessibility-firms/low-impact-2|Low Impact 2]], [[problems/digital-accessibility-firms/worker-life-1|Worker Life 1]], [[problems/digital-accessibility-firms/worker-life-2|Worker Life 2]]

---

## 1. Programmatic Flow Traversal and Blocking-Failure Detection
#graph-theory #gradient-boosting #transformers #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #automation

**Problem statement:** The industry reports conformance violations while the question is whether a disabled person can complete a task, and those diverge in both directions — pages that pass every check and are unusable, and violations no user ever encounters.

**ML task:** Traverse critical user flows programmatically through the accessibility tree with a keyboard and focus model, detect the failure classes that actually block completion, and rank findings by blocking impact per assistive technology class
**Input data:** Rendered accessibility trees across flow steps; focus order and focus retention across dynamic transitions; interactive element reachability and labelling; live region and announcement behaviour captured across screen reader and browser pairings; client analytics identifying which flows matter; findings from real-user testing as the validation set.
**Target:** Whether a flow step is completable for a given technology class, validated against real assistive technology user testing.
**Evaluation metric:** Agreement with real-user outcomes is the only meaningful validation, and it must be reported with the classes where the simulation is blind stated explicitly — a traversal can find a focus trap and cannot tell you whether the experience makes sense, and a product implying otherwise is selling the same assurance that made overlays a problem. Report recall on confirmed blocking failures and be conservative about claiming passes.
**Scope:** The system should be able to say a flow is blocked and should never be permitted to certify that one is accessible. That asymmetry is the design principle and the ethical line; automated passes here are the specific failure this field has already lived through. 2-3 engineers with assistive technology expertise, 9-12 months.
**Data availability:** Accessibility trees and focus behaviour are directly capturable. Cross-technology behaviour capture requires an automation harness per screen reader and browser pairing, which is the substantial engineering.

---

## 2. Judgement-Criterion Assistance With Carried Uncertainty
#transformers #cnns #large-language-models #bert #semantic-segmentation #evaluation-metrics #confidence-intervals #compliance

**Problem statement:** Automated scanning covers the criteria decidable from markup; the ones requiring judgement — whether alternative text is meaningful, whether heading structure reflects organisation, whether error messages are understandable — are where the real barriers live and are checked only in expensive manual passes.

**ML task:** Assess judgement-requiring criteria from rendered content and context, producing ranked candidates for human review rather than verdicts
**Input data:** Rendered pages with images, surrounding content and DOM structure; existing alternative text and labels; heading hierarchy against content organisation; error and instructional text; component identity for grouping; auditor adjudications as labels.
**Target:** Whether an expert auditor would record a finding, on the same criterion.
**Evaluation metric:** Precision at the review threshold, and separately the calibration of the confidence, because the output's entire safety depends on uncertainty being carried honestly. The two failure modes are asymmetric and both are serious: a false violation creates wasted remediation, and a false pass creates an assurance nobody should have — the second is precisely the criticism that has been levelled at automated conformance claims in this field and must be measured and reported explicitly.
**Scope:** Under no circumstances should a conformance claim rest on a model's judgement; the output is a prioritised queue for an expert. Component-level dismissal — recognising that a finding concerns a recurring component so one triage decision suppresses it everywhere — removes most of the triage volume and requires component recognition rather than page analysis. 2 ML engineers plus an accessibility specialist, 6-9 months.
**Data availability:** Rendered content is abundant. Auditor adjudications exist in firms' report histories and are the label source.

---

## 3. Fix-Level Grouping, Impact Prioritisation and Effort Estimation
#graph-neural-networks #k-means-clustering #gradient-boosting #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #automation

**Problem statement:** Four thousand findings arrive in a backlog organised by criterion and page, prioritised by WCAG level, when they usually reduce to a few dozen component defects and what matters is whether a task is blocked.

**ML task:** Group findings by the fix that resolves them, rank by blocking impact on flows real users take, and estimate remediation effort from the client's own codebase history
**Input data:** Findings with their DOM context and location; component identity derived from markup and design system linkage; client analytics on flow usage; technology-class blocking assessments; historical remediation efforts with the fix types and time taken; design system component inventory.
**Target:** The grouping a remediation engineer would produce, the blocking status of each group, and actual effort taken.
**Evaluation metric:** For grouping, the reduction from finding count to fix count at unchanged coverage — this is the number that makes a report legible to a team estimating sprints, and blast radius per fix is the figure that gets work scheduled. For prioritisation, whether the top-ranked fixes correspond to the barriers real-user testing identified as blocking. Effort estimates need interval calibration, not point accuracy.
**Scope:** Routing findings to the design system rather than to page teams is the difference between remediation and permanent improvement, and requires linking a finding to the component that produced it. Pairing it with a CI check that prevents reintroduction is what stops the rescan finding everything again. 2 engineers, 4-6 months.
**Data availability:** Findings and codebases are available during engagements. Historical effort data exists at remediation firms and is rarely structured.

---

## 4. Audit Documentation Generation From Expert Observation
#large-language-models #transformers #bert #k-nearest-neighbors #gradient-boosting #evaluation-metrics #worker-facing #tacit-knowledge-ml

**Problem statement:** Scarce expert auditors spend the bulk of their time writing the same descriptions of the same patterns, mapping findings to criteria, and documenting one recurring component hundreds of times because the report is organised by page.

**ML task:** Draft structured findings — criterion mapping, description, severity, remediation guidance — from an auditor's short note or recording, with component-level instance enumeration
**Input data:** Auditor observations in whatever form is fastest to capture; DOM and accessibility tree context at the point of the finding; component identity and its instances across the site; the firm's historical findings corpus with expert-written descriptions and criterion mappings; WCAG criteria and technique documentation.
**Target:** The structured finding the auditor accepts after review.
**Evaluation metric:** Criterion mapping accuracy against expert labelling, and edit distance between the draft and the auditor's final version as the practical measure of whether it saves time. Measure the rate at which auditors override the drafted severity, since severity is a judgement about people and a drafting tool that quietly homogenises it would flatten the most important part of the report.
**Scope:** The corpus of expert-written findings is the firm's accumulated pattern knowledge and turning it into the drafting substrate is how the field scales past the small number of qualified people. Drafting assistance should extend to the disabled specialists doing real-technology testing, so the documentation burden does not fall hardest on the people doing the hardest part of the work. 2 engineers, 4-6 months.
**Data availability:** Firms hold years of expert-written reports, which is an unusually good corpus for exactly this task.
