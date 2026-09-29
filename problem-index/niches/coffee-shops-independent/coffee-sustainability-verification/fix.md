# Every Survey Round Starts From the Instrument, Not the Archive

**Niche:** [[niches/coffee-shops-independent/coffee-sustainability-verification/profile|Coffee Origin Verification & Traceability Services]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Years of farm-level survey rounds sit as separate datasets keyed to the questionnaire that produced them, so the organization can report each round and cannot say what changed between them.
**Tags:** #data-integration #time-series-forecasting #causal-inference #change-point-detection #evaluation-metrics #feature-engineering #hypothesis-testing #dimensionality-reduction #compliance #workflow-orchestration

## The Problem
The most valuable question a verification service can answer is whether conditions at origin are improving, and it is the question the organization is least able to answer about its own data. Each round is designed around the current instrument, fielded, analyzed, and delivered as a report; the dataset is archived keyed to that round's questionnaire. Instruments evolve — items get reworded, response options change, new topics are added as regulation shifts — and nothing records which items are comparable across which rounds. So longitudinal analysis is a bespoke reconciliation exercise every time someone attempts it, which means it is attempted rarely, and the organization's own claim to be tracking change over time rests on comparisons nobody has systematically validated.

## Why It's Still Broken
Rounds are funded and delivered as projects with their own scope and client, so nothing in the operating model has an interest in the round's afterlife. Instrument change is driven by real needs — a new regulation demands new evidence — and the cost of maintaining comparability is paid later by someone else. And because farms are sampled rather than panelled, the same farm is usually not observed twice, which makes the longitudinal question genuinely harder and has been allowed to make it look impossible rather than merely hard.

## What a Fix Looks Like
A cross-round data architecture where the unit of organization is the concept measured rather than the questionnaire that measured it. Every item maps to a versioned concept with an explicit comparability relation to its predecessors — identical, comparable with a stated adjustment, or genuinely broken — recorded when the instrument changes rather than reconstructed later. Farms and geographies carry persistent identifiers so that repeat observation, where it occurs, is recoverable, and area-level estimates remain comparable even when the sampled farms differ. On that base, longitudinal estimation becomes a standing capability rather than a project: change over time reported with the comparability caveats explicit, and the specific places where the series genuinely breaks marked as breaks rather than smoothed over. The same structure supports reusing prior rounds as priors for new ones, which materially reduces the sample needed to detect change — a direct saving on the organization's largest cost.

## Who Feels the Pain
Analysts reconstructing comparability every time a client asks about trend; methodologists who know the archive contains the answer and cannot reach it; roasters and regulators who want evidence of improvement and receive point-in-time snapshots; and the organization, whose accumulated fieldwork is its only durable asset and is stored as a pile of projects.

## Impact If Fixed
Converts a series of commissioned studies into a longitudinal measurement system, which is a categorically more valuable product and the one the market is moving toward as deforestation and due diligence rules demand demonstrated change rather than a snapshot. It also reduces fieldwork cost directly, because a round that can borrow strength from its predecessors needs fewer farms to reach the same precision.
