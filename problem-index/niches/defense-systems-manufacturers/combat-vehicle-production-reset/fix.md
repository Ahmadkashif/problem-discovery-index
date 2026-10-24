# The Inspection Finding Written on a Clipboard

**Niche:** [[niches/defense-systems-manufacturers/combat-vehicle-production-reset/profile|Combat Vehicle Production & Depot Reset]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** Teardown inspectors record what they find on paper checklists, so the reset line never learns which vehicles bring which problems.
**Tags:** #large-language-models #cnns #object-detection #feature-engineering #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to return vehicles from production and reset on the contracted date, and whoever cuts the share of vehicles held for parts discovered only at teardown takes the account.

## The Problem
An inspector walking a stripped hull marks cracks, corrosion and wear on a paper form or in a free-text work order. The finding drives that vehicle's repair, then disappears into a filing cabinet. Across hundreds of vehicles a year the reset line has no count of which findings recur on which variants or deployments.

## Why It's Still Broken
Paper is fast in a dirty plant, and finding codes were never standardised across lines. The data's value appears only in aggregate, and nobody's job is the aggregate.

## What a Fix Looks Like
A rugged tablet form with standard finding codes and photos, voice notes transcribed and coded by a language model, and a photo model that suggests the finding type and location on the hull. Findings feed a running tally by variant, usage and source unit that planners see weekly.

## Who Feels the Pain
Inspectors re-entering findings, planners ordering parts blind, and programme managers explaining late vehicles.

## Impact If Fixed
A year of coded findings is enough to set parts kits by variant and source, which is the first step to cutting teardown waits.
