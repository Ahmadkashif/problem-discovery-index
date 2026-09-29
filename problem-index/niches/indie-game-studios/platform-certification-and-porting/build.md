# Passing Certification the First Time

**Niche:** [[niches/indie-game-studios/platform-certification-and-porting/profile|Platform Certification & Porting]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Four hundred requirements per platform, written for a compliance department, read by a programmer who also does the art.
**Tags:** #compliance #workflow-orchestration #automation #evaluation-metrics #data-integration #confidence-intervals #sets-and-logic #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to get a two-person team through four certification regimes written for studios with a compliance department — and whoever does it multiplies the reachable market without multiplying the team.

## The Problem
Each platform publishes a large requirements document covering behaviours a game must exhibit: how it handles suspension, what happens on controller disconnect, how saves behave, what the store metadata must contain, how age ratings are declared, what terminology may be used. Most requirements are mechanically checkable. A small team reads them, implements what they understood, submits, and finds out weeks later which ones they got wrong — against a launch date that has already been announced.

## Why Nobody Has Built This
Requirements are published as documents because that is how platform holders communicate them, so compliance is a reading exercise rather than a check — a specification delivered as prose gets satisfied by whoever reads it most carefully. The requirements differ per platform and change with each update. Tooling for this exists inside large publishers and is not available outside. And the failures are absorbed by the smallest teams.

## What to Build
Turn the documents into checks. Encode each platform's requirements as automated checks against a build, which is the core and converts a reading exercise into a test run. Run the checks continuously during development rather than at submission, since a requirement discovered in week two is a change and one discovered at submission is a delay. Translate each requirement into what it means for an engine project, because the documents are written for engine-agnostic native development and the teams are using engines. Maintain the checks against platform updates, as requirements change and a stale check is worse than none. Catalogue the actual failure patterns from rejections, since the same handful recur and are the priority. Generate the store metadata and declarations from one source rather than four, which is a large share of the manual work. Manage the build pipelines per platform from one configuration. Predict the risky requirements for a given project's characteristics, so effort is directed. Share the knowledge across studios, as everyone is discovering the same things independently. And price it for a small team, since the studios that most need it are the ones least able to buy tooling.

## Target Customer
Technical leadership at small studios, porting houses, platform holders whose submission queues are full of avoidable failures, and build tooling vendors.

## Impact If Built
A specification delivered as prose gets satisfied by whoever reads it most carefully, which is a poor mechanism for a two-person team. Encoding requirements as automated checks moves every failure from submission to development.
