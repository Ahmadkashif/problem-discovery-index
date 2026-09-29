# Testing More Combinations for the Same Money

**Niche:** [[niches/digital-accessibility-firms/at-testing-at-scale/profile|Assistive Technology Testing at Scale]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every combination needs an expert to walk it, so almost none of them are walked.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #data-integration #confidence-intervals #descriptive-statistics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to test whether flows complete across the screen reader, browser and operating system combinations users actually have, at a cost that permits doing it repeatedly — and whoever does takes the account.

## The Problem
Establishing whether a flow works requires a person using a specific screen reader, on a specific browser, on a specific operating system, walking the flow. The number of combinations that matter is larger than any budget, so firms test one or two, once, on a sample of pages. The result is a finding about one configuration at one point in time, presented as a statement about accessibility generally, and it is stale within a release cycle.

## Why Nobody Has Built This
Assistive technology interaction is not scriptable in the way a browser is, so automation has stalled. Expert testers are scarce and the work is manual by nature. Tooling has focused on automated conformance checking, which is a different problem. And nobody has attacked the cost per combination directly.

## What to Build
Attack the cost per combination rather than accepting it. Automate the repeatable parts of a flow walk — navigation, state setup, capturing what the screen reader announced — so the expert's attention goes to judgement rather than to mechanics, which is the core and is where the cost actually is. Capture assistive technology output programmatically where the platform permits, since comparing announcements across combinations is mechanical once captured. Prioritise the combinations that the client's own users actually have, from analytics rather than from a general matrix, which is the cheapest coverage decision available. Define flows once and reuse them across combinations and releases, rather than re-scoping each time. Support distributed and remote testing so expert testers are not constrained by device location. Detect divergence between combinations automatically and route only the divergent cases to a person. Reuse results between releases where the flow has not changed, which requires knowing what changed. Report coverage achieved explicitly, since an untested combination is currently indistinguishable from a passing one. Build a library of known assistive technology behaviours, which is expertise currently held individually. And measure cost per flow per combination, which is the number the whole niche turns on.

## Target Customer
Accessibility firms and consultancies, in-house accessibility teams, assistive technology and testing tool vendors, and quality assurance providers.

## Impact If Built
The combinatorics make comprehensive testing unaffordable, so a finding about one configuration is reported as a statement about accessibility. Automating the mechanics of a flow walk is what makes repeated coverage possible.
