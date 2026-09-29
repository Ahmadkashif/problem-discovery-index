# The Client Shipped and the Variant Broke

**Niche:** [[niches/conversion-optimization-firms/the-frontend-developer/profile|The Front-End Developer]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A release on Tuesday renamed a class and the variant has been rendering broken since, for half the test group.
**Tags:** #quick-win #automation #change-point-detection #evaluation-metrics #workflow-orchestration #descriptive-statistics #worker-facing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to let a developer modify a page they do not control, across browsers they do not have, without finding out it broke from the client — and whoever equips them takes the account.

## The Problem
Client releases break running variants. A class is renamed, an element moves, a component is rewritten — all routine changes for the client's engineers, none of whom know a test is running on that page. The variant's script no longer finds what it expects and produces a broken layout for the variant group. The test continues collecting data, the results are contaminated, and nobody notices until the numbers look strange or somebody visits the page.

## Why It's Still Broken
Nobody tells the agency — a release calendar that does not include the party running code on the site guarantees that the code breaks without warning, and there is no channel for the notification. Nothing checks the variant after launch. The client's own monitoring sees a healthy page. And the contaminated data looks like a result.

## What a Fix Looks Like
Watch the running variants and ask for the release calendar. Check every running variant daily by loading the page and verifying the modification applied, which is the fix and is a synthetic check anyone can build. Alert on failure rather than waiting for a report. Ask the client for release notification and check variants immediately after each one, which is a process request most will grant. Write selectors defensively so a minor markup change does not break them. Discard data from the period when a variant was broken, which is the correct handling and is currently never done. Check after every client release as a standing step. Keep a record of which releases broke which variants, as the pattern identifies the fragile ones. Tell the client when a release broke a test, which makes the notification request concrete. Pause a test rather than continuing with contaminated data. And treat a broken variant as invalidating the result rather than as a fix to apply and carry on.

## Who Feels the Pain
Developers finding out from the client; strategists reporting contaminated results; clients whose visitors saw a broken page; and the test, whose data is now worthless and is reported anyway.

## Impact If Fixed
A release calendar that excludes the party running code on the site guarantees the code breaks without warning. A daily synthetic check on each running variant turns that into an alert.
