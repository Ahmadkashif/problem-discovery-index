# The Assembly That Arrived and Nobody Could Find

**Niche:** [[niches/construction-tech-platforms/mep-prefab-coordination/profile|Mechanical & Electrical — Model-to-Fabrication Chain]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Prefabricated assemblies are delivered to a site, stacked in a laydown yard, and then located by crews walking around looking at labels, which routinely costs more field hours than the prefabrication saved.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor in MEP contractor software is fighting to carry a coordinated model through to a fabricated, delivered, installed and tracked assembly without anyone redrawing it — and whoever closes that chain with the fewest re-entries takes the account.

## The Problem
Three truckloads of fabricated assemblies arrive over a week and are unloaded wherever there is room. A crew needs the assemblies for level four, zone C, today. They walk the yard reading labels, find most of them, cannot find two, and eventually discover them under a stack for a different zone. An hour of a four-person crew is gone. This happens continuously on every prefab-heavy project, is treated as normal, and quietly eats a large share of the labour saving that justified prefabricating in the first place.

## Why It's Still Broken
Nobody measures it. The prefabrication business case is built on shop hours versus field hours and does not include a line for search time, so the loss is real and invisible. Materially tracking a yard means knowing where things were put, which requires someone to record a location at unload — a task with no owner, performed at the least convenient moment, by whoever is driving the forklift. And the labels themselves are printed by the shop system with shop identifiers that mean nothing to the field crew, which is the identity problem showing up physically.

## What a Fix Looks Like
Record location at unload and make the label speak the field's language. A scan at unload with a zone location — which is fifteen seconds per pallet on a phone — gives the yard a map. Labels carry the area and system the assembly belongs to, in the terms the foreman uses, alongside the shop number, so a label is readable without a lookup. A crew asks for what it needs by area and is told where it is. Add the delivery-sequence check that this makes possible: comparing what has arrived against what the next two weeks of installation needs, so a missing assembly is discovered before the crew is standing in the yard rather than after. Measure search time once to size the problem, because the business case for all of this is currently absent from every prefabrication analysis in the industry.

## Who Feels the Pain
Field crews searching yards; foremen explaining why a zone did not start; and operations directors whose prefabrication programme is underperforming its business case for a reason nobody has isolated.

## Impact If Fixed
Yard location tracking is cheap and recovers field hours directly, and the delivery-completeness check prevents the more expensive failure of mobilising a crew to a zone that cannot be completed. Measuring search time is the part worth doing first, because it converts an invisible loss into a number that justifies the rest.
