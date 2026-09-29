# Two Businesses, One Report

**Niche:** [[niches/audio-adtech-networks/the-ad-operations-specialist/profile|The Ad Operations Specialist]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Host-read sponsorships live in a spreadsheet and a shared drive, dynamically inserted campaigns live in an ad server, and one person reconciles them both against a client who wants a single report.
**Tags:** #worker-facing #workflow-orchestration #data-integration #automation #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to let one person run two incompatible businesses and report them as one — and whoever does that removes the reconciliation that consumes the category's operational capacity.

## The Problem
A client buys a campaign with host-read sponsorships on three shows and dynamically inserted spots across a network. The host-read side is tracked in a spreadsheet, with scripts in a shared drive, reads verified by listening and delivery counted by episode. The dynamic side is in an ad server with impressions, pacing and frequency data. At month end the specialist merges them into one report, reconciling two definitions of delivery, two notions of an impression and two timelines, by hand. Then does it for the next client. The category's split personality is resolved monthly by a person with a spreadsheet.

## Why Nobody Has Built This
Ad servers were built for dynamic insertion and host-read predates them, so the two never shared an object model — the split is historical and nobody has reunified it because each side works adequately alone. Host-read's bespoke feel discourages systematisation. The reconciliation is invisible work performed by one role. And clients receive a report, so the process appears to function.

## What to Build
Give the two businesses one object model. Represent a campaign as a set of placements that may be dynamic or host-read, with a shared delivery concept, which is the foundation and is what makes a single report a query rather than a reconciliation. Normalise the delivery definitions explicitly, since a host-read delivery and a dynamic impression are genuinely different and a shared model must express the difference rather than average it. Track host-read through the same pipeline, connecting to that niche's workflow, so both sides produce data rather than one producing artefacts. Generate the client report automatically, which is the visible deliverable and the bulk of the monthly work. Flag delivery risk across both types early, since a host-read miss and a dynamic underdelivery both threaten the campaign and are currently monitored separately. Verify host-read airing automatically, which removes the manual listening. Reconcile against invoicing, since billing errors across two systems are common and are found by clients. Give the specialist a single operational view of everything in flight, which is what they assemble mentally. Support the client-facing conversation with evidence from both sides. And measure the hours spent on reconciliation, because that figure is the cost of the split and nobody has counted it.

## Target Customer
Ad operations teams at podcast networks and publishers, the specialists themselves, and the platform vendors whose products cover only half the business.

## Impact If Built
The split is historical and each side works adequately alone, which is why nobody reunified them and one person resolves it monthly. A shared placement and delivery model turns the report from a reconciliation into a query while still expressing the genuine difference between the two products.
