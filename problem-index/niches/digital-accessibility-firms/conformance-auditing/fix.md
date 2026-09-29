# The Scan Is Clean and the Audit Has Not Started

**Niche:** [[niches/digital-accessibility-firms/conformance-auditing/profile|Conformance Auditing]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The team ran the scanner, saw no errors, and told procurement the product is accessible.
**Tags:** #quick-win #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #automation #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to cover the portion of accessibility failures that automation cannot decide, because that is where the real barriers are and it requires a person — and whoever closes that gap takes the account.

## The Problem
An automated scan returning no errors is routinely interpreted as a clean bill of health. It is not: it means the decidable subset passed. The remainder — the parts requiring judgement, which is where most real barriers are — has not been examined at all. Teams report conformance on this basis, procurement accepts it, and the product reaches disabled users who cannot use it while an accessibility claim is displayed on the site.

## Why It's Still Broken
The tool's output does not say what it did not check — a report of zero errors is indistinguishable from a report of full coverage unless something states the scope, and nothing does. Coverage is a nuance the interface omits. Teams want the good news. And nobody downstream asks what was assessed.

## What a Fix Looks Like
Report coverage alongside the result, every time. State on every automated report what proportion of criteria the tool can assess and what it cannot, which is the fix and is a paragraph the tooling could add. Distinguish a passing result from an unassessed one in the output, since presenting them identically is what causes the misreading. List the criteria requiring human review explicitly, so the remaining work is visible rather than implied. Require a manual assessment before any conformance claim is made, as a matter of internal policy. Train the teams who run the scans on what the result means, which is a briefing rather than a course. Write accessibility statements that describe the assessment rather than asserting conformance. Check what procurement questionnaires actually ask for, since many accept a scan and would accept better. Include a manual spot check of the critical flows even when a full audit is not affordable, which is cheap and catches the worst cases. Say plainly when a claim is not supported by what was done. And treat an unsupported conformance claim as a risk in its own right, which it increasingly is.

## Who Feels the Pain
Disabled users encountering barriers on a site claiming conformance; organisations making claims they cannot support; accessibility specialists correcting the same misunderstanding repeatedly; and procurement functions relying on a partial result.

## Impact If Fixed
A report of zero errors is indistinguishable from a report of full coverage unless something states the scope, and nothing does. A coverage paragraph on every automated report ends the misreading.
