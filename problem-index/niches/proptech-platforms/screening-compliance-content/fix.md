# The Criteria Configured Once by Someone Who Has Left

**Niche:** [[niches/proptech-platforms/screening-compliance-content/profile|Screening Compliance Content]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Screening criteria are set at property onboarding by a regional manager working from a national template, are never reviewed, and are applied to every applicant thereafter by a system that has no idea whether they are still lawful.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #automation #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in tenant screening is fighting to apply the criteria that are lawful in this specific city, for this specific property, at the moment of application — and whoever keeps that rule set correct takes the account.

## The Problem
A portfolio has 140 properties across nine states. Each one's screening criteria were configured during onboarding, at different times, by different people, from whatever template was current. Nobody has looked at them since. Some are stricter than the operator's stated policy, some are looser, several are unlawful where they sit, and the operator cannot produce a list of what criteria are currently applied at each property without opening 140 configuration screens. When a complaint arrives about one property, the first question — what were your criteria and when were they set — takes a week to answer.

## Why It's Still Broken
Configuration is a setup task with no review cycle, and nothing prompts anyone to look at it again. The screens are per property, so there is no portfolio view; producing one has never been asked for because nobody realised it was absent until they needed it. And the people who configured them have generally moved on, taking with them any record of why a particular threshold was chosen.

## What a Fix Looks Like
Build the portfolio view and the change log first, which is a report rather than a project. Show every property's current criteria side by side, with the date each was set, by whom, and what it was before — so divergence from policy is visible at a glance and the outliers are obvious. Add an annual review obligation with the comparison against the operator's stated policy and against the jurisdiction stack where that content exists. Log every criteria change with the reason, which turns configuration into a reviewable act rather than an invisible one. And instrument outcomes: approval and denial rates by property and by denial reason, which is the pattern data that both an operator's own counsel and an enforcement body would examine, and which the operator should be the first to see rather than the last.

## Who Feels the Pain
Compliance officers who cannot state their own portfolio's criteria; regional managers inheriting settings nobody can explain; and applicants denied by thresholds that do not reflect the operator's own stated policy, let alone the local law.

## Impact If Fixed
The portfolio view is a report against existing configuration data and typically reveals substantial unintended divergence across properties. Outcome instrumentation is the more consequential half: denial pattern data exists in every one of these systems, is examined by nobody, and is exactly what a fair housing review would request.
