# Two Thousand Lines and One That Matters

**Niche:** [[niches/ci-cd-platforms/build-engineer-support-desk/profile|The Build Engineer Support Desk]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Build and release engineers spend their days as a help desk for pipelines they did not write, failing for reasons that have nothing to do with the platform they maintain.
**Tags:** #bert #k-means-clustering #dbscan #logistic-regression #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a developer resolve their own pipeline failure without a build engineer — and whoever does that takes the platform team's time back, which is currently spent supporting pipelines they did not write.

## The Problem
A developer's pipeline fails. They open the log: two thousand lines of tool output. They scroll, find red text, paste it into the platform channel and ask. A build engineer reads it, recognises within twenty seconds that a credential expired, and replies. This happens perhaps thirty times a day across the organisation, in a handful of recurring shapes, and consumes the time of the people whose job is supposed to be making the platform better — which is the work that would reduce the volume.

## Why Nobody Has Built This
Logs are presented as artefacts to be read rather than as data to be analysed, which is how build tooling has always worked. Classifying failures requires a taxonomy nobody has written down, although the taxonomy is small — infrastructure, dependency resolution, configuration and credentials, test failure, flakiness, resource exhaustion, platform fault — and stable across organisations. The support burden lands on platform engineers who are salaried and available, which makes it invisible in any budget. And vendors see their own faults clearly and the customer's pipeline faults not at all, so they have not considered the whole failure population as their problem.

## What to Build
Classify the failure and tell the developer what to do. Isolate the actual failure from the log automatically — the first genuine error rather than the last red line, which are frequently different and is why developers paste the wrong thing — and present it with the surrounding context rather than the whole file. Classify into the small stable taxonomy and attach the remedy, since a credential expiry, a dependency resolution failure and a real test failure require entirely different actions and the developer's difficulty is telling which they have. Distinguish platform faults from pipeline faults explicitly, which ends the first exchange of most conversations and is the vendor's own responsibility to state. Recognise repeats: this exact failure occurred eleven times this week across four teams, and here is what resolved it, which converts a repeated diagnosis into a lookup. Cluster across the organisation to identify the small number of causes generating most of the volume, which is the platform team's fix list derived from evidence rather than from impression. And surface prior resolutions, since the answer has usually been given before in a chat channel and is recoverable.

## Target Customer
Platform and build engineering teams, CI vendors for whom failure diagnosis is the largest source of customer friction, and engineering leadership counting platform team capacity.

## Impact If Built
The failures fall into a small, stable and mechanically recognisable taxonomy, and classifying them removes most of the queue. The cluster analysis gives the platform team an evidence-based fix list, which is the work the queue currently prevents them doing.
