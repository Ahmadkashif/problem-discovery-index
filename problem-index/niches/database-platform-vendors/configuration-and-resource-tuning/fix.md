# Tuned Once and Never Measured

**Niche:** [[niches/database-platform-vendors/configuration-and-resource-tuning/profile|Configuration & Resource Tuning]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A database is tuned during deployment, the changes are never measured, and nobody can say whether any of them helped or which one made things worse.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #change-point-detection #quick-win #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to replace a decade of blog posts with a configuration derived from this workload on this hardware — and whoever does that takes the platform team, because the defaults suit almost nobody and the guidance available was written for different machines.

## The Problem
During deployment an engineer applies fourteen configuration changes from an article, all at once, and the database is faster than default. Which of the fourteen helped, whether any hurt, and whether the combination is near optimal are all unknown. Two years later the workload has changed and the configuration has not, and when somebody proposes adjusting a parameter the response is that the current configuration works and nobody wants to touch it — which is a reasonable position given that its effects were never measured and its history is an article nobody can find.

## Why It's Still Broken
Configuration changes are applied in a batch because that is how the guidance is written and because applying them individually means many restarts. Measuring requires a comparable before and after, which means a stable workload and a defined metric, and neither was established. There is no record of why each parameter has its value, so the configuration becomes an artefact nobody understands and nobody will alter. And the caution is rational: an unmeasured change to a working system is a risk with no known reward.

## What a Fix Looks Like
Treat configuration as a tracked, measured and reversible sequence. Record every parameter's value, when it was set, by whom and why, which is a small piece of discipline that converts an opaque artefact into a history somebody can reason about — and its absence is the main reason nobody will touch it. Change one thing at a time where restarts allow, or in small groups where they do not, with a defined metric and a comparison period, so each change has an attributable effect. Use the replay environment for the parameters that cannot be safely varied in production, which removes the risk objection for most of them. Report the measured effect and keep it with the change record, which makes the next adjustment an informed one. Make reversion automatic and immediate, since the willingness to try depends entirely on the ease of undoing. Detect drift between the running configuration and the recorded one, which is a common and surprising finding in long-lived estates. And re-evaluate on a schedule, because the workload changes continuously and a configuration set at deployment is describing a system that no longer exists.

## Who Feels the Pain
Teams with a configuration nobody understands and nobody will change; engineers whose proposed improvement is refused on the basis of an unmeasured status quo; and organisations running two-year-old configurations against workloads that have doubled.

## Impact If Fixed
Recording why each parameter has its value is small discipline and is what converts an untouchable artefact into something a team can reason about. One-change-at-a-time with a measured effect makes each adjustment attributable, which is the practice the whole activity currently lacks.
