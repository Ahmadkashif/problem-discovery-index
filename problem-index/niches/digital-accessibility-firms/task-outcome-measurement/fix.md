# Passing Every Check and Still Unusable

**Niche:** [[niches/digital-accessibility-firms/task-outcome-measurement/profile|Task Outcome Measurement]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The scan is clean, the report is closed, and a screen reader user cannot complete the checkout.
**Tags:** #quick-win #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #worker-facing #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to state whether a disabled person can complete the task they came for, rather than how many standards criteria a page fails — and whoever measures that takes the account.

## The Problem
An organisation completes an accessibility programme. The automated scans are clean, the audit findings are closed, the conformance statement is published. A screen reader user still cannot complete the checkout, because the failure is in how a dynamic component announces itself, or an order of operations, or a timing behaviour — none of which any check caught. The organisation believes the problem is solved and the users experience no change.

## Why It's Still Broken
Nobody tried the task — an audit that examines pages against criteria never attempts the journey, so a barrier that only appears in sequence is outside what the method can see. Automated coverage is partial by design. Closing findings is the defined success. And the affected users rarely have a route to report it.

## What a Fix Looks Like
Attempt the task, end to end, with the technology. Walk the three most important flows end to end with a screen reader and keyboard only, which is the fix and takes a day and finds what the audit did not. Do it with an expert assistive technology user rather than an auditor simulating one, since the difference in what is noticed is substantial. Record whether the task completed, not only what was wrong along the way. Repeat with a second screen reader and browser combination, as the divergence between them is where much of the real breakage lives. Test the actual flow including authentication, payment and confirmation rather than sample pages, which is where audits stop. Report the blocking failures separately and at the top, which reframes the remediation list immediately. Give users a working route to report barriers and act on it, which is the cheapest source of real findings. Retest the flows after remediation rather than closing on the ticket. Include the flows in regression testing so they are checked continuously. And publish an honest statement of what was tested rather than a general conformance claim.

## Who Feels the Pain
Disabled users who cannot complete a purchase on a site that claims conformance; organisations who invested and changed nothing for their users; accessibility teams who suspected this; and the credibility of conformance claims generally.

## Impact If Fixed
An audit that examines pages against criteria never attempts the journey, so a barrier that only appears in sequence is outside what the method can see. Walking three flows end to end with real assistive technology finds what the programme missed.
