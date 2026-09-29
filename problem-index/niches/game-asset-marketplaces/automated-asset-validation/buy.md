# Continuous Integration From Software Delivery

**Niche:** [[niches/game-asset-marketplaces/automated-asset-validation/profile|Automated Asset Validation]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software delivery made automated build and test on every submission universal, and asset marketplaces review by eye.
**Tags:** #workflow-orchestration #automation #evaluation-metrics #compliance #data-integration #descriptive-statistics #quick-win #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to catch what is wrong with an asset at upload rather than after a buyer finds it, and whoever automates that review takes the account.

## The Problem
Continuous integration made it standard that nothing merges without building and passing tests. The infrastructure is commoditised, the patterns are universal, and matrix testing across multiple runtime versions is routine. Package registries apply the same discipline to third-party submissions. Asset marketplaces accept uploads from thousands of contributors with no build, no test and no matrix, and publish them to paying customers.

## What Already Exists
Automated build and test on submission; matrix testing across runtime versions; artifact validation and linting; automated feedback to the contributor; and gated publication on passing checks.

## The Customization Gap
The adaptation is to artefacts that build inside a game engine rather than a compiler. It requires: (1) an engine as the build environment, with licensing, headless operation and long import times to manage — this is the substantive difference and is the practical reason it has not been done; (2) success criteria that include visual and functional correctness rather than only compilation; (3) a contributor who is an artist and cannot read a build log, so feedback must be translated; (4) matrix dimensions of engine version, render pipeline and platform rather than language version; and (5) a catalogue that must be re-validated when the engine publisher ships, not only when the contributor submits.

## Target Customer
Asset marketplaces, curation and operations teams, engine vendors, and continuous integration tooling providers.

## Impact If Solved
Continuous integration made build-and-test on submission universal and the infrastructure commoditised. A game engine as the build environment, with feedback an artist can read, is what has to be built around it.
