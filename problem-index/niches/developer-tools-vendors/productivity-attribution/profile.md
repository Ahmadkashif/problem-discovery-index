# Productivity Attribution

**Parent Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to attribute a change in engineering output to a specific tool or practice — and whoever does that credibly takes the category, because every purchase in it is justified by a claim nobody can currently substantiate.

## Profile
**Market Size:** ~$1.9B US engineering analytics and developer productivity measurement
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** None for attribution — dashboards are widespread and answer a different question
**Target Buyer:** Engineering leadership and the finance function asking what the tooling did
**Automation Potential:** Very High — the events are captured; the causal design is missing

## What Makes This a Distinct Niche
Every tool in this category is sold on a productivity claim and no buyer or seller can substantiate one. DORA and SPACE supplied vocabulary and a set of metrics, and neither supplies attribution: a team's deployment frequency rose in the same quarter the assistant was rolled out, two people joined, a release freeze ended and a large refactor completed, and nothing separates those. The measurement problem is genuinely hard — engineering output is multidimensional, the confounders are severe, and the naive metrics are famously gameable — but it is not unanswerable, and the industry has settled on treating it as unanswerable, which is convenient for everybody selling into it. The contest is causal attribution rather than dashboard breadth, and it is now commercially urgent rather than academic because assistant spend has made the unanswered question expensive.

## Current Tools & Gaps
Engineering analytics vendors reporting DORA metrics, cycle time and review throughput; platform dashboards; developer experience surveys. The gaps: everything is descriptive, so a change and its cause are never separated; rollouts happen simultaneously across an organisation, destroying any natural comparison, and nobody stages them deliberately; the measured outputs are proxies that respond to being measured; quality and maintenance consequences appear months later and are attributed to nothing; and vendors avoid the question because a rigorous answer risks being unflattering.

## Problems
- [[niches/developer-tools-vendors/productivity-attribution/build|🔨 Build: Enormous Spend on an Unmeasured Claim]]
- [[niches/developer-tools-vendors/productivity-attribution/buy|🛒 Buy: Causal Inference Applied to Engineering Rollouts]]
- [[niches/developer-tools-vendors/productivity-attribution/fix|🔧 Fix: Rollouts Designed to Be Unmeasurable]]
