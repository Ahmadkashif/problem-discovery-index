# Catching It Where It Is Created

**Niche:** [[niches/digital-accessibility-firms/build-regression-prevention/profile|Build Regression Prevention]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The defect is found months later at full cost and could have been caught at the commit that created it.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #compliance #data-integration #descriptive-statistics #change-point-detection #quick-win
**Contested on:** Every serious competitor in this niche is fighting to stop new accessibility failures reaching production, because remediating them afterwards costs many times more — and whoever catches them in the build takes the account.

## The Problem
Accessibility defects are created continuously by ordinary development and found periodically by audit. The gap between creation and discovery is months, during which the defect ships, propagates through reuse, and becomes expensive to fix because the code has moved on and the developer who wrote it has forgotten it. The mechanically-detectable subset could be caught at the commit, and mostly is not.

## Why Nobody Has Built This
Accessibility tooling was built for auditors rather than for pipelines. Adding a check that fails builds is resisted when the existing codebase has thousands of violations. Nobody owns the developer experience of accessibility. And audit revenue depends on finding these later.

## What to Build
Check at the point of change, against a baseline. Run automated checks in the pipeline on every change, which is the core and is straightforward once the baseline problem is solved. Baseline the existing failures so only new ones fail the build, since a check that fails on a legacy codebase is disabled within a week and that is why most attempts have failed. Test at component level in the design system, where a single fix prevents every future instance. Report failures in the developer's own workflow with the fix explained rather than the criterion cited. Cover the mechanically-detectable subset honestly and say so, because presenting pipeline checks as full coverage recreates the conformance illusion at a new point. Include keyboard interaction tests, which are automatable and are usually omitted. Track new defects per release so the trend is visible and attributable. Fail loudly on the design system and warn on application code, which puts the strictness where the leverage is. Provide the developer with an explanation and a corrected example rather than a violation identifier. And measure defects found in audit that a pipeline check would have caught, which is the number that justifies the whole thing.

## Target Customer
Engineering teams and platform engineering, accessibility firms offering enablement, design system teams, and testing tool vendors.

## Impact If Built
A defect created at a commit and found months later costs many times more to fix, and the mechanically-detectable subset could have been caught immediately. Baselined pipeline checks at component level are what make prevention survivable.
