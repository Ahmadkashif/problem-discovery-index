# Building on Somebody Else's Page

**Niche:** [[niches/conversion-optimization-firms/the-frontend-developer/profile|The Front-End Developer]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The code runs on a page that changes without notice and the first sign of breakage is a client email.
**Tags:** #worker-facing #automation #workflow-orchestration #evaluation-metrics #change-point-detection #data-integration #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to let a developer modify a page they do not control, across browsers they do not have, without finding out it broke from the client — and whoever equips them takes the account.

## The Problem
The developer writes script that manipulates a live page whose markup they did not write, cannot see in source, and which changes on the client's release schedule without notice. They test in whatever browsers they have. The variant runs for weeks. When the client ships a change that alters a selector, the variant breaks silently for some or all of the variant group, and the first indication is somebody noticing.

## Why Nobody Has Built This
The position exists because client-side testing lets an agency operate without engineering access, which is the commercial premise. Nobody has built monitoring for injected variants. Release notification across an organisational boundary does not exist. And the breakage is discovered by the client, so it is experienced as an agency failure.

## What to Build
Monitor the variants and detect the page changing underneath them. Monitor every running variant continuously in the wild and alert when it fails to apply, which is the core and converts silent breakage into a notification. Detect changes to the underlying page that would affect a variant's selectors before they break it, which is achievable by watching the page. Verify variants across the browsers and devices the client's traffic actually uses, from analytics. Write variants against resilient selectors rather than brittle paths, which is craft the tooling could assist. Obtain release notification from the client as a contractual step, since the failures cluster around deployments. Capture screenshots across configurations for review rather than relying on one developer's browser. Exclude sessions where the variant failed from the results, which is both correct measurement and the developer's defence. Give the developer visibility of how the variant is actually rendering in the field. Report variant failure rates as a quality metric, so the problem is visible to whoever staffs the work. And make the developer's first knowledge of breakage an alert rather than an email from the client.

## Target Customer
Conversion optimisation firms, front-end and engineering leadership, testing platform vendors, and monitoring tooling providers.

## Impact If Built
The code runs on a page that changes without notice and breakage is discovered by the client. Continuous variant monitoring with change detection turns a silent failure into an alert.
