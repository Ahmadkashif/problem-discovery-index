# Checking the Package Before It Lists

**Niche:** [[niches/game-asset-marketplaces/automated-asset-validation/profile|Automated Asset Validation]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Broken packages reach buyers because nothing between upload and listing actually opens them.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #data-integration #compliance #descriptive-statistics #quick-win #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to catch what is wrong with an asset at upload rather than after a buyer finds it, and whoever automates that review takes the account.

## The Problem
A submitted asset package may have missing textures, broken material references, prefabs that do not instantiate, scripts that do not compile, files in the wrong format, no documentation, or a category that does not match the contents. Human reviewers look at a description and a screenshot. The package is never actually imported and exercised until a buyer does it, and the failure then costs a refund, a review and the buyer's trust in the whole catalogue.

## Why Nobody Has Built This
Review was designed as a policy check rather than a technical one. Automated import testing requires engine infrastructure the marketplace does not run. Reviewer headcount is a cost centre nobody wants to grow. And the failures are absorbed by buyers rather than appearing as a platform metric.

## What to Build
Import it and exercise it before it lists. Import every submission into the relevant engine versions automatically and report what failed, which is the core and catches the majority of defects mechanically. Detect broken and missing references, which is the commonest single defect and is trivially found. Instantiate prefabs and compile scripts rather than checking that files exist, since existence is not function. Validate the technical profile against the category's norms, as a mislabelled asset wastes everyone's time. Check documentation and demo scene presence against a standard, which is where the quality floor actually sits. Render a standard preview from the asset itself rather than trusting the creator's screenshot, which is frequently from a different tool entirely. Give the creator the report so they can fix it, which turns rejection into improvement. Score submissions so human review concentrates on the ambiguous cases. Re-validate the catalogue on each engine release, which keeps quality current rather than historical. And publish the check list so creators can self-test before submitting.

## Target Customer
Asset marketplaces and storefronts, curation and operations teams, engine vendors, and asset pipeline tooling providers.

## Impact If Built
The package is never actually imported until a buyer does it, and every defect is therefore discovered at the buyer's expense. Automated import and instantiation at submission catches most of it before listing.
