# Digital Accessibility Firms

## Profile
**Category:** Digital Professional Services
**Market Size:** ~$1.5B US in accessibility audit, remediation, training and tooling services, growing on a mixture of litigation pressure, procurement requirements and the European Accessibility Act
**Tech Maturity:** Strong automation on a minority of the problem. Deque's axe engine, Level Access, TPGi and Siteimprove all run automated WCAG checks reliably, and automated testing detects only a portion of accessibility failures — the rest requires manual expert review and assistive technology testing. The industry's deliverable is a list of violations, not a statement about whether disabled people can complete tasks.
**Workforce:** Accessibility auditors and specialists, assistive technology testers including disabled testers, remediation engineers, trainers, policy and legal advisors

## Key Pain Themes
The category's central artefact is a conformance report: a list of WCAG success criteria failures, located and severity-rated. Conformance is a proxy. A site can pass every automated check and remain unusable with a screen reader, and it can carry technical violations that no user ever encounters. What matters is whether a disabled person can complete the task they came for, and almost nothing in the industry measures that.

Litigation drives much of the demand and distorts it. A large and growing volume of US web accessibility lawsuits has made remediation a legal risk management exercise, which rewards documentation of effort over user outcome. The overlay widget market grew directly out of that incentive — products promising rapid conformance through a script — and is contested, with disability advocacy organisations including the National Federation of the Blind having objected publicly, and with litigation continuing against sites using them.

The third theme is that remediation findings arrive as a report and enter a development backlog with no priority relative to everything else. A report of four thousand issues, with no statement of which ones actually block a task, is straightforwardly unactionable.

## Current Tech Landscape
Deque's axe is the de facto automated engine and is embedded in many products. Level Access, TPGi, Siteimprove and Evinced provide platforms combining automated scanning with workflow. Testing with real assistive technology — JAWS, NVDA, VoiceOver, Dragon — remains manual and expert. Overlay vendors including AudioEye and accessiBe occupy a contested position in the market. WCAG 2.2 is the current standard with WCAG 3 in long-term development. Procurement requirements — VPATs and ACRs in the US, EN 301 549 in Europe — drive a documentation layer of its own.

## Problems
- [[problems/digital-accessibility-firms/high-impact|🔴 High Impact: Conformance Is Measured and Task Completion Is Not]]
- [[problems/digital-accessibility-firms/low-impact-1|🟡 Low Impact: Automated Scanning Coverage and False Positives]]
- [[problems/digital-accessibility-firms/low-impact-2|🟡 Low Impact: Remediation Prioritisation and Developer Workflow]]
- [[problems/digital-accessibility-firms/worker-life-1|🟢 Worker Life: The Auditor Doing the Manual Pass]]
- [[problems/digital-accessibility-firms/worker-life-2|🟢 Worker Life: The Disabled Tester Whose Expertise Is Priced as Participation]]
- [[problems/digital-accessibility-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/digital-accessibility-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is a field where the measurable proxy and the actual goal have drifted apart under legal pressure, and everyone in it knows. Automated conformance is cheap, documentable and defensible in a demand letter; task completion by a person using assistive technology is expensive, harder to document and is the thing that matters. The opportunity is not better violation detection — that is well served — but measurement of outcome: whether the flows people actually use can be completed, by which assistive technologies, and which specific failures block them. That reframes the deliverable from a list to a statement about people, which is both the honest version of the service and the version that survives a legal environment increasingly sceptical of conformance claims made by script.
