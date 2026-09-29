# Six Schemas, One Truth

**Niche:** [[niches/game-analytics-vendors/the-instrumentation-engineer/profile|The Instrumentation Engineer]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every live client version sends something slightly different and one person reconciles all of it.
**Tags:** #worker-facing #data-integration #workflow-orchestration #automation #compliance #evaluation-metrics #sets-and-logic #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to let one engineer keep data consistent across six live client versions all sending slightly different schemas — and whoever supports that person takes the account.

## The Problem
A live game has several client versions in players' hands simultaneously, each instrumented as it was when it shipped. Events were renamed, parameters added, meanings shifted. The engineer maintains a transformation layer reconciling all of it into consistent metrics, holds most of the special cases in their head, and is the person called when a number looks wrong. The accumulated complexity grows with every release and never shrinks.

## Why Nobody Has Built This
Client version skew is a game-specific problem that general data tooling does not model. The transformation layer is bespoke to each game. The role is one person, so there is no internal advocate. And it works, until they are unavailable.

## What to Build
Make the version mapping explicit and testable rather than resident in one person. Maintain version-aware schema mappings as declared configuration rather than as transformation code, which is the core and is what makes the knowledge transferable. Detect version-specific breakage automatically by comparing distributions across client versions, since a version sending something wrong is visible in the data immediately if anyone looks. Test the transformations, which currently have no coverage and underpin every number the studio reports. Document each special case with the version and reason at the point it is added, as that is the institutional memory currently at risk. Report which versions are live and what share of traffic each carries, which most teams cannot state. Flag when a new build changes a schema before it ships rather than after. Track versions that should be retired, since old clients are a large share of the complexity. Alert on a version whose metrics diverge from the others, which is the earliest sign of a break. Make the whole layer handoverable, which is the actual risk being carried. And give the engineer a way to say what the transformations do to a number, so disputed figures are resolvable.

## Target Customer
Studio data platform teams, game analytics vendors, publishers with multi-title pipelines, and data engineering tooling providers.

## Impact If Built
The accumulated version reconciliation lives in one person's head and grows with every release. Declared version-aware mappings with automatic divergence detection makes it transferable and testable.
