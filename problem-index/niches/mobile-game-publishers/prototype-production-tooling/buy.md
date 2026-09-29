# Platform Engineering From Software

**Niche:** [[niches/mobile-game-publishers/prototype-production-tooling/profile|Prototype Production Tooling]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software organisations built internal platforms to stop every team rebuilding the same scaffolding, and prototype teams rebuild it monthly.
**Tags:** #workflow-orchestration #automation #data-integration #evaluation-metrics #descriptive-statistics #optimization-fundamentals #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to cut the cost and time of getting a testable prototype in front of a paid audience, because the funnel's economics are set by that number — and whoever cuts it takes the account.

## The Problem
Software organisations reached the same conclusion a decade ago: when many teams repeatedly build the same scaffolding, a platform team should build it once. The discipline that followed — golden paths, service templates, automated pipelines, default observability, self-service provisioning and measured developer productivity — is mature and well documented. A publisher running dozens of prototype teams has the identical structure and treats internal tooling as whatever someone had time for.

## What Already Exists
Golden path templates; service scaffolding generators; automated build and release pipelines; observability by default; and developer productivity measurement.

## The Customization Gap
The adaptation is to an artefact that is meant to be thrown away, and to a release target controlled by app stores. It requires: (1) a scaffold optimised for disposability rather than for maintainability, since almost every prototype is deleted — this inverts the usual platform trade-offs and is the substantive difference; (2) app store submission and review in the release path, which no internal software platform has to model; (3) game engine projects rather than services, so the templating works on engine assets and scenes; (4) test campaign provisioning as part of the pipeline, because a build that cannot reach an audience is not done; and (5) default instrumentation aimed at cross-prototype comparison rather than at operating a running service.

## Target Customer
Mobile publishers, prototype and studio engineering leads, engine vendors, and internal developer platform vendors.

## Impact If Solved
Platform engineering exists because repeated scaffolding is a measurable tax. Optimising the scaffold for disposability rather than maintainability, with store submission in the release path, is what makes this a different platform.
