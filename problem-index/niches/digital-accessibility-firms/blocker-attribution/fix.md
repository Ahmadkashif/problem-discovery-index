# Severity Assigned by Convention

**Niche:** [[niches/digital-accessibility-firms/blocker-attribution/profile|Blocker Attribution & Evidence]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every finding of this criterion is rated high and every finding of that one is rated medium, regardless of what it does to anyone.
**Tags:** #quick-win #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #worker-facing #causal-inference #data-integration
**Contested on:** Every serious competitor in this niche is fighting to say which specific defect blocked which task, how much that matters, and in a form a product team will act on and a legal process will respect — and whoever states that takes the account.

## The Problem
Severity in accessibility reports is assigned by criterion rather than by consequence. Every instance of a given failure type gets the same rating whether it sits on a critical checkout control or on a decorative element in a footer nobody reaches. The engineering team, receiving hundreds of high-severity findings, reasonably concludes that the ratings carry no information and prioritises by whatever is easiest, which is the opposite of what the report intended.

## Why It's Still Broken
Severity is a property of the criterion rather than of the instance — a rating that is the same for every occurrence of a failure type tells the reader nothing about any particular occurrence. Rating by impact requires knowing what the element does. Conventions are inherited from tooling defaults. And nobody has objected, because everyone treats the ratings as noise anyway.

## What a Fix Looks Like
Rate by consequence, using information the auditor already has. Rate each finding by what it does to a task rather than by which criterion it violates, which is the fix and requires only that the auditor say what they saw. Mark the findings that blocked a flow separately and put them first, since those are a short list and the rest is a long one. Consider where the element sits — a critical path control and a footer link are not the same finding. Note how many pages or components share the defect, as a shared component defect is one fix with many instances. Record whether a workaround existed, which changes the rating substantially. Report the blocking findings as a separate deliverable from the full list, which is what the engineering team will actually work from. Keep the criterion mapping for compliance without letting it drive the ranking. Explain the rating basis in the report, so it can be trusted. Review ratings with the client rather than presenting them, since they know which flows matter. And accept a smaller high-severity list, because a hundred high-severity findings communicates nothing.

## Who Feels the Pain
Engineering teams prioritising by ease because the ratings carry no signal; disabled users whose actual barrier sits below a hundred equally-rated items; auditors whose judgement is flattened by a convention; and the remediation budget, spent on the wrong things.

## Impact If Fixed
A rating that is the same for every occurrence of a failure type tells the reader nothing about any particular occurrence. Rating by task consequence, with blockers listed separately, makes the report prioritisable.
