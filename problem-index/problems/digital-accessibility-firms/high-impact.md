# Conformance Is Measured and Task Completion Is Not

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** High Impact
**One-liner:** The industry delivers a list of standards violations when the question is whether a disabled person can finish what they came to do, and those two things come apart in both directions.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #gradient-boosting #causal-inference #transformers #compliance #worker-facing

## The Problem
An accessibility engagement produces a conformance report: which WCAG success criteria fail, where, at what severity. It is a rigorous artefact and it answers a different question from the one that matters.

The gap runs both ways. A page can satisfy every testable criterion and still be unusable — a screen reader user who reaches a correctly-labelled form in an order that makes no sense, a focus management pattern that is technically valid and leaves someone lost after a modal closes, a live region that announces so much that the announcement is useless. Conversely, reports contain violations that no user in practice encounters, on components behind a feature flag or in a flow nobody uses, and they consume remediation budget because they are on the list.

What nobody measures is whether the actual tasks can be completed. Can a blind user buy the product. Can a keyboard-only user complete the application form. Can someone using voice control check out. Those are the questions the law is ultimately about and the questions disabled users are asking, and they are answered by expert judgement and small manual test passes, if at all.

The legal environment has entrenched the proxy. Thousands of US web accessibility lawsuits and demand letters a year have made remediation a documented-effort exercise, and a conformance report is the document. That incentive is also what created the market for overlay widgets — products that inject a script promising rapid conformance — which disability advocacy organisations including the National Federation of the Blind have publicly objected to, and which have not prevented litigation against the sites that deploy them. Firms in this industry occupy an awkward position: they know conformance is a proxy, and the proxy is what their clients are buying.

## Why It's Unsolved
Task completion is expensive to measure. It requires real users with real assistive technology attempting real flows, which means recruiting disabled participants, compensating them properly, and running sessions — orders of magnitude more costly than a scan, and not repeatable on every release.

It is also harder to document defensibly. A conformance report maps to a standard with numbered criteria; a task completion finding is a narrative about what happened to a person, which is more useful and less legible to a procurement checklist or a demand-letter response.

The standard itself is the third factor. WCAG is testable by design, and that testability is a genuine achievement — it is why automated tooling works at all. But testability required criteria that are properties of markup and behaviour rather than of outcomes, so a standard that is excellent as a specification is a poor measure of experience, and everyone in the field says so.

And the population is heterogeneous in a way that makes measurement genuinely hard. Screen reader users with different products and configurations, low-vision users with magnification, motor disabilities using switch access or voice control, cognitive disabilities — each encounters different barriers on the same page, and a single completion metric flattens a population whose needs conflict.

## What a Solution Looks Like
Measure flows, not pages. Instrumenting the critical journeys — purchase, application, account recovery, support contact — against assistive technology interaction, and reporting completion and time-to-completion by technology class, changes the deliverable from a list into a statement about people. It also directs remediation to what blocks a task rather than to whatever scanned worst.

Simulate what can be simulated and be honest about what cannot. Programmatic traversal of a flow through the accessibility tree, with a keyboard and focus model, catches a meaningful class of real blockers — traps, unreachable controls, focus loss, unlabelled interactive elements in the path — and does it on every release. It does not tell you whether the experience makes sense, and a product claiming it does is selling the same illusion overlays sell.

Put real users at the centre, funded properly. The expensive measurement is the valid one, and the industry's structure should make it the headline rather than the optional extra. Panels of disabled testers, paid as the experts they are, testing the flows that matter, is what produces findings nobody can dismiss.

Report severity by blocking impact. A violation should be rated by whether it prevents completion of a real task for a real technology class, not by its WCAG level — which is the single change that would make a four-thousand-item report actionable.

## Impact If Solved
This realigns an industry with its purpose. Task-based measurement gives clients something worth buying rather than a document to hold, directs remediation budget at what actually excludes people, and is the defensible position as the legal environment grows more sceptical of conformance asserted by script. For disabled users it is the difference between a site that passes an audit and a site they can use — which is the only outcome any of this was ever meant to produce.
