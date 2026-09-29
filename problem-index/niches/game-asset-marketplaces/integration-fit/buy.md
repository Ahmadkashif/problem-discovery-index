# Dependency Compatibility From Package Registries

**Niche:** [[niches/game-asset-marketplaces/integration-fit/profile|Integration Fit & Compatibility]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software package registries made dependency and version compatibility machine-readable and enforced, and asset marketplaces use a text field.
**Tags:** #graph-theory #data-integration #automation #evaluation-metrics #compliance #workflow-orchestration #descriptive-statistics #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to answer, before purchase, whether an asset will work in the buyer's engine version, render pipeline and performance budget — and whoever answers it takes the account.

## The Problem
Software package ecosystems solved this decades ago. Packages declare dependencies and version ranges in a machine-readable manifest, registries resolve them, incompatibilities are detected before installation rather than after, and continuous testing across runtime versions is standard practice. Nobody installing a library discovers at runtime that it needed a different language version. Game assets have the same dependency structure — engine version, pipeline, plugins, platform — and declare it in prose.

## What Already Exists
Machine-readable dependency manifests; semantic versioning and range resolution; pre-install compatibility checking; automated testing across runtime versions; and deprecation and breaking-change signalling.

## The Customization Gap
The adaptation is to artefacts that have no manifest and cannot be made to declare one retrospectively. It requires: (1) dependencies inferred from binary and project files rather than declared by the author, since the catalogue already exists and cannot be re-authored — this is the substantive difference and makes extraction the whole problem; (2) compatibility that is graded rather than binary, as an asset may import and then look wrong or run slowly; (3) performance budgets as a dependency dimension, which package registries have no concept of; (4) engine upgrades that break assets on the publisher's schedule rather than the creator's; and (5) a creator population that will not maintain manifests, so the system must work without their participation.

## Target Customer
Asset marketplaces, studios buying at volume, engine vendors, and package and dependency tooling providers.

## Impact If Solved
Package registries made compatibility machine-readable and checked it before installation. An existing catalogue that cannot be re-authored means the manifest has to be inferred from the files, which is the work.
