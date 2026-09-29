# AI Agents & Platform Opportunities — Digital Accessibility Firms

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]

---

## 1. Task Completion Measurement Platform
#ai-platform #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #worker-facing

**Concept:** A platform that reports whether people can finish what they came to do, rather than how many criteria a page fails. It instruments the critical journeys — purchase, application, account recovery, support — traverses them programmatically through the accessibility tree with keyboard and focus modelling across screen reader and browser pairings, and reports completion status and blocking failures by assistive technology class. It runs a contracted panel of disabled specialists against the same flows, structured as specialist findings rather than participant quotes, and treats their results as the ground truth the automation is validated against.

**Inputs:** Accessibility trees and focus behaviour across flow steps; cross-technology capture harnesses; client analytics identifying which flows matter; panel findings from disabled specialists; historical remediation and its effect.

**Outputs / Actions:** Flow-level completion status by technology class, which is a statement about people rather than a list. Findings ranked by blocking impact rather than by WCAG level, which is the change that makes a four-thousand-item report actionable. An explicit architectural asymmetry: the system can report that a flow is blocked and is never permitted to certify that one is accessible — automated passes are the specific failure this field has already lived through with overlay products. Outcome feedback to the specialists whose findings drove each fix.

**Why now:** The legal environment is growing more sceptical of conformance asserted by script, procurement requirements are broadening under the European Accessibility Act, and the cross-technology automation harnesses needed to capture real assistive technology behaviour have become practical.

**Market:** Accessibility firms wanting a defensible deliverable, large digital estates under litigation or procurement pressure, and public sector buyers whose obligations are about outcomes.

---

## 2. Remediation Planning Agent
#ai-agent #graph-neural-networks #k-means-clustering #gradient-boosting #large-language-models #evaluation-metrics #workflow-orchestration #automation

**Concept:** An agent that turns an audit into a plan a development team can execute. It groups findings by the fix that resolves them rather than by the criterion that names them — four thousand findings usually reduce to a few dozen component defects — and reports blast radius, so a team can see that one change resolves eleven hundred findings. It ranks by blocking impact on flows users actually take, estimates effort from the client's own remediation history, routes component-level findings to the design system rather than to page teams, and installs CI checks that prevent reintroduction.

**Inputs:** Findings with DOM context; component identity and design system linkage; client flow analytics; blocking assessments by technology class; historical remediation effort by fix type; CI configuration.

**Outputs / Actions:** A fix-level backlog with blast radius and effort, ordered by what actually excludes people. Design system routing for the fixes that should be made once. Regression prevention in CI, which is the only mechanism that stops the next rescan finding everything again. A measurable statement of remediation progress in terms of barriers removed rather than findings closed.

**Why now:** The gap between an audit and a remediated site is where this industry's value currently evaporates, and it is a workflow problem rather than an expertise problem — the grouping, prioritisation and routing are all computable from data the audit already produces.

**Market:** Accessibility firms delivering remediation engagements, in-house accessibility programmes, and design system teams who are the correct destination for most findings and rarely receive them.

---

## 3. Audit Assistance Agent
#ai-agent #large-language-models #transformers #cnns #bert #evaluation-metrics #worker-facing #tacit-knowledge-ml

**Concept:** An agent that gives scarce expert auditors their judgement time back. Before the audit it runs the mechanical groundwork — programmatic keyboard traversal, focus order extraction, accessibility tree capture and screen reader output across technology pairings — and surfaces the divergences between pairings, which is where the interesting findings are. During the audit it drafts structured findings from a short note or recording, mapping to criteria and enumerating every instance of a recurring component so the same pattern is documented once rather than two hundred times. On judgement criteria it offers ranked review candidates with honest confidence, never verdicts.

**Inputs:** Traversal and capture output across technology pairings; auditor observations in whatever form is fastest; DOM and accessibility tree context; component identity and instances; the firm's corpus of expert-written findings; WCAG criteria and techniques.

**Outputs / Actions:** A prepared comparison for the auditor to start from rather than mechanical passes they perform themselves. Drafted findings for review, measured on edit distance and on how often auditors override the drafted severity — since severity is a judgement about people and homogenising it would flatten the most important part of the report. Component-grouped documentation. Drafting assistance extended to the disabled specialists doing real-technology testing, so the documentation burden does not land hardest on the people doing the hardest part.

**Why now:** Auditor scarcity is the binding constraint on the entire industry, the certification pipeline is small, and the people who could widen it have no capacity because they are fully booked writing documentation. Firms hold years of expert-written reports, which is an unusually good corpus for this specific task.

**Market:** Accessibility consultancies and audit firms, in-house accessibility teams, and the assistive technology testing specialists whose expertise the field depends on.
