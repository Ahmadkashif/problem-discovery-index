# Tested Once, on One Screen Reader, Last Year

**Niche:** [[niches/digital-accessibility-firms/at-testing-at-scale/profile|Assistive Technology Testing at Scale]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The conformance statement rests on a test of one configuration, on a sample of pages, before three releases shipped.
**Tags:** #quick-win #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #automation #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to test whether flows complete across the screen reader, browser and operating system combinations users actually have, at a cost that permits doing it repeatedly — and whoever does takes the account.

## The Problem
Accessibility statements typically rest on an annual audit of a sample, on one or two assistive technology configurations. Between audits the product ships continuously. By the time the statement is a few months old it describes a version that no longer exists, tested in a configuration many users do not have. The statement is nonetheless presented, and relied on, as a current description of the product.

## Why It's Still Broken
The testing cadence does not match the release cadence — an annual assessment of a continuously shipping product describes a moment that has already passed, and nothing in the statement says so. Testing is expensive. Nobody requires currency. And the statement's format invites a general claim.

## What a Fix Looks Like
Narrow the claim to what was tested and test the important parts more often. State the scope precisely — which flows, which configurations, which date, which version — which is the fix and costs nothing but honesty. Test the critical flows more frequently than the full audit, since those are where the risk concentrates. Choose the configurations from the client's own user analytics rather than from a general list, which improves relevance at no extra cost. Re-test after any release that touches a critical flow, which requires knowing which releases those are. Include a second screen reader for the critical flows, as the divergence between them is where much of the failure lives. Publish the test date and version alongside the statement. Record what was not tested explicitly, which is the most important sentence in any such statement. Automate the parts that can be automated so the manual budget goes further. Keep a running log of tests so currency is demonstrable. And review the statement when it ages past a defined threshold rather than annually by default.

## Who Feels the Pain
Disabled users relying on a statement that describes an old version; organisations exposed by a claim they cannot currently support; auditors whose careful work is generalised beyond its scope; and procurement functions relying on the statement.

## Impact If Fixed
An annual assessment of a continuously shipping product describes a moment that has already passed, and nothing in the statement says so. Stating the scope precisely and retesting critical flows on release is the honest version.
