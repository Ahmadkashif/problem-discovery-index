# Report Production and Finding Triage

**Industry:** [[penetration-testing-firms|Penetration Testing Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A quarter to a third of a tester's billable time goes into writing up findings they already understand, in a document format that changes per client.
**Tags:** #large-language-models #bert #transformers #gradient-boosting #k-nearest-neighbors #evaluation-metrics #automation #workflow-orchestration

## The Problem
The deliverable is a report, and producing it is a substantial share of every engagement. Each finding needs a description, a technical explanation, reproduction steps, evidence, an impact assessment, a severity rating and a remediation recommendation. Then an executive summary for people who will not read the findings, and a format that matches whatever the client's template requires.

Much of it repeats. The same weakness classes appear across engagements with the same explanations and largely the same remediation advice, rewritten each time because the previous version lives in a past report rather than in a reusable form.

Severity rating is inconsistent in a way clients notice. Two testers rate similar findings differently, scoring frameworks are applied with judgement, and the same firm can produce different severities for equivalent issues across engagements — which undermines the prioritisation the client depends on.

Evidence capture is the tedious middle. Screenshots, request and response pairs, and command output must be collected during testing, sanitised of anything sensitive, and assembled — and it is done at the point when the tester wants to keep testing.

## What Already Exists
Reporting platforms exist — PlexTrac, Dradis, AttackForge and the internal tooling most firms build — with finding libraries, templating and workflow. Testing tools export findings in structured formats. Scoring frameworks provide a severity vocabulary. Some firms maintain curated finding libraries with approved language. Penetration testing as a service platforms deliver findings continuously through a portal rather than as a document, which is a genuine improvement.

## The Customisation Gap
Finding libraries hold generic text and the value is in the specificity. What makes a finding useful is the client's context — which of their systems, reachable from where, exploitable by whom, affecting what data — and generating that from the evidence rather than pasting a library entry is where the tester's time actually goes.

Severity consistency is a calibration problem nobody treats as one. A firm's own history of findings and ratings supports a model that flags when a proposed severity is out of line with how the firm has rated comparable findings before, which addresses the inconsistency at the point of writing rather than at the quality review.

Evidence assembly should happen during testing, not after. Capturing requests, responses and commands with automatic association to the finding they support, and automatic sanitisation of credentials and personal data, removes the collection burden and improves the evidence quality — since evidence gathered retrospectively is always thinner.

And deduplication across a client's engagement history is the piece that would most change the client's experience. A finding that is the third instance of the same issue in three years should be reported as such, with the remediation history attached, rather than as a new discovery — which is the difference between a report and a relationship.

## Impact If Solved
Report production consumes a large share of the most expensive hours in this business and produces a document that repeats itself across engagements. Context-specific generation from captured evidence, severity calibration against the firm's own history, and deduplication against the client's engagement history would return that time to testing while making the deliverable more useful — particularly the recurrence view, which tells a client something no single report can.
