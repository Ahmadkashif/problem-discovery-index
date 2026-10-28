# Work Orders That Say "Replaced" and Not Why

**Niche:** [[niches/renewable-power-producers/wind-major-component-reliability/profile|Wind Turbine Major Component Reliability]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Fix (Pain Point)
**One-liner:** A main bearing comes out after months of alerts and the work order reads "replaced main bearing", so the fleet never learns which alert pattern meant which failure.
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to catch drivetrain and main-bearing damage early enough to repair it uptower, and whoever has the fewest crane-dependent major component replacements per 100 turbines takes the account.

## The Problem
Work orders are written by technicians at the end of a long day in free text, often by a contractor in its own system. Failure mode, root cause and the condition found are missing, so failure prediction trains on dates and part numbers only.

## Why It's Still Broken
Nobody downstream asks for the detail at the time, the OEM or service provider owns the system the order is written in, and there is no standard failure-mode code across platforms.

## What a Fix Looks Like
A short structured close-out on the technician's tablet, prefilled from the alert history and the parts used, with the failure mode picked from a platform-specific list and a voice note transcribed into the record. Historical work orders are back-coded by a language model and reviewed in batches.

## Who Feels the Pain
Reliability engineers building models; technicians re-explaining the same failure; owners paying for repeated failures nobody traced.

## Impact If Fixed
Coding ~5 years of historical work orders on a 1,000-turbine fleet (~20,000 orders, estimate) yields the first labelled failure set the owner has had, at a few weeks' review cost.
