# Rollback That Nobody Trusts

**Niche:** [[niches/ci-cd-platforms/deployment-and-release-safety/profile|Deployment & Release Safety]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Rollback exists in every deployment system and is used reluctantly, because nobody has verified it recently and a failed rollback during an incident is worse than the incident.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor here is fighting to make a bad release stop itself before most users see it — and whoever does that takes the release account, because the alternative is that a human notices and reacts, which is what happens almost everywhere.

## The Problem
A release is causing problems. The obvious action is to roll back. The engineer hesitates: the last rollback anyone remembers was eight months ago, there has been a database migration since the previous version, they are not certain the old version is compatible with the current schema, and a failed rollback halfway through would be substantially worse than the current degradation. So they attempt a fix forward instead, which takes forty minutes and is done under pressure by someone who is now also responsible for the original problem.

## Why It's Still Broken
Rollback is treated as a capability that exists rather than a procedure that is exercised, and anything unexercised decays. Schema migrations are the specific mechanism: once a migration is applied, the previous version may not run, and few organisations enforce the backward-compatible migration discipline that would preserve the option. Nobody measures rollback success rate or duration, because rollbacks are rare and each is handled as an incident detail. And the hesitation is entirely rational given the uncertainty, which means the fix is to remove the uncertainty rather than to exhort people to roll back faster.

## What a Fix Looks Like
Exercise it and make it safe by construction. Practise rollback routinely in production on a schedule, which is the only way to know it works and is standard practice in organisations that depend on it — an unexercised rollback is an untested code path in the most critical position available. Enforce backward-compatible migrations as a rule checked in the pipeline, so that the previous version can always run against the current schema, which is what preserves the option and is a discipline rather than a tool. Report rollback readiness per service continuously: is the previous version deployable, is the schema compatible, when was this last verified — so the engineer at the decision point has a fact rather than a fear. Measure rollback duration and success rate, which turns a rare and frightening action into a known quantity. Make it one action rather than a procedure, since the number of steps is directly proportional to the hesitation. And separate rollback from roll-forward as an explicit decision with stated criteria, so the choice is made deliberately rather than defaulting to the option that feels less frightening.

## Who Feels the Pain
Engineers choosing between two frightening options during an incident; users experiencing forty minutes of degradation that a rollback would have ended in two; and organisations whose most important recovery mechanism is untested.

## Impact If Fixed
Scheduled rollback practice converts an untested critical path into a known one, and enforced backward-compatible migrations preserve the option that most often turns out not to exist. A readiness indicator at the decision point replaces the hesitation with a fact.
