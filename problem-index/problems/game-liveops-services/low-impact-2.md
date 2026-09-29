# Configuration, Segmentation and Rollback

**Industry:** [[game-liveops-services|Game LiveOps Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A live game's behaviour is controlled by thousands of remote configuration values that anyone can change, and the blast radius of any one of them is understood by whoever wrote it.
**Tags:** #change-point-detection #gradient-boosting #time-series-forecasting #graph-neural-networks #evaluation-metrics #automation #workflow-orchestration #confidence-intervals

## The Problem
Live games externalise almost everything into configuration: drop rates, prices, event parameters, difficulty curves, matchmaking settings, feature flags. A mature game has thousands of values, layered by segment and experiment, changed continuously by several teams.

The failure modes are ordinary and expensive. A value pushed with a wrong order of magnitude breaks an economy in an hour. A segment definition overlaps another and a cohort receives two conflicting configurations. An experiment is left running for months after its decision was made. A value is changed for an event and never reverted. Nobody can say which configuration a given player is actually receiving without tracing through the layers by hand.

Rollback is the acute problem. When something goes wrong in a live game the first question is what changed, and the answer requires reading a configuration change log that may not record who changed what and rarely records why. Meanwhile the damage — currency granted, items obtained, progression skipped — is already in player accounts and cannot be reverted without taking things away from people.

## What Already Exists
PlayFab, AccelByte, Beamable and the general-purpose feature flag platforms all provide remote configuration with versioning, targeting and staged rollout. Experimentation frameworks handle assignment and analysis. Most studios have change logs and approval processes of varying rigour. Larger operators run staging environments and canary releases. Incident processes exist and are usually adapted from general software operations rather than designed for economies.

## The Customisation Gap
Generic feature flag tooling assumes reversible changes, and game configuration frequently is not — a drop rate that ran for an hour has permanently distributed items, and turning the flag back does not undo it. The tooling should distinguish reversible from irreversible changes and treat the second category with entirely different controls: simulation before release, tighter approval, staged exposure, and a projected blast radius stated in the terms that matter, which is how much currency or how many items will enter the economy.

Blast radius estimation is the concrete missing capability. Before a change ships, what it will do to grant volumes, economy flows and the affected segment size is computable from the configuration graph and recent telemetry, and presenting it at the moment of the change is the intervention that prevents the order-of-magnitude error.

Segment conflict detection is the second gap: overlapping targeting rules producing contradictory configurations is a graph problem with a clear answer, and it is currently discovered when players compare notes.

And experiment hygiene needs enforcement. Experiments left running long past their decision, configurations set for an event and never reverted, and values nobody remembers the purpose of accumulate in every live game, and an automated inventory of stale configuration with its current exposure is straightforward and absent.

## Impact If Solved
Configuration is the control surface of a live game and it is operated with tooling designed for reversible software changes. Blast radius projection before release, irreversibility-aware controls, conflict detection and stale configuration inventory address the class of incident that most often damages a live economy — and they do it at the moment of the change rather than during the incident review afterwards.
