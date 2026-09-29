# The Catalogue Nobody Has Updated Since Launch

**Niche:** [[niches/data-platform-integrators/model-discovery/profile|Model Layer Discovery]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The catalogue was populated during the implementation and every description has been empty since.
**Tags:** #quick-win #automation #data-integration #evaluation-metrics #workflow-orchestration #descriptive-statistics #large-language-models #compliance
**Contested on:** Every serious competitor in this niche is fighting to make an existing asset findable so nobody builds a duplicate, and whoever makes discovery work takes the account.

## The Problem
Catalogues are bought, deployed, populated during the implementation, and then abandoned. New assets arrive with no description. Old descriptions describe a version that has changed. Ownership fields point at people who have left. Anyone who opens it once and finds it stale does not open it again, and the organisation concludes that catalogues do not work — when what failed was an assumption that humans would maintain it.

## Why It's Still Broken
Maintenance was assumed rather than designed — a catalogue that relies on people updating it after every change will be current on the day it launches and never again. Description is a separate task from the work. Nobody owns currency. And the staleness is self-reinforcing, since nobody who has been disappointed returns.

## What a Fix Looks Like
Stop relying on people and generate what can be generated. Generate a baseline description for every asset from its logic and lineage, which is the fix and fills the catalogue immediately. Regenerate on every change so descriptions cannot go stale. Show last-updated and last-queried dates prominently, so a user can judge whether to trust an entry. Derive ownership from who changes and queries an asset rather than from a field somebody typed. Mark assets with no recent activity rather than presenting everything equally. Prompt for a human description only where the generated one is weak, which concentrates the scarce human effort. Surface the catalogue inside the tools people already use rather than as a destination. Measure whether anyone opens it, which nobody does and which would end the debate quickly. Remove or archive the stale entries, since a catalogue that is half wrong is trusted like one that is entirely wrong. And treat coverage and currency as the catalogue's success metrics rather than the number of assets registered.

## Who Feels the Pain
Engineers and analysts who searched once and gave up; organisations that paid for a catalogue and got a list; the estate, which duplicates because discovery failed; and whoever has to justify the catalogue's renewal.

## Impact If Fixed
A catalogue that relies on people updating it after every change will be current on the day it launches and never again. Generated baselines regenerated on change is what makes currency structural rather than aspirational.
