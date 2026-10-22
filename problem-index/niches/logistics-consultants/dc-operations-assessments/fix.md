# Findings Written From Memory on the Flight Home

**Niche:** [[niches/logistics-consultants/dc-operations-assessments/profile|DC Operations Assessments]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The assessor sees thirty things in three days and writes up the twelve they remember, without the evidence the client will ask for.
**Tags:** #large-language-models #transformers #worker-facing #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to find, in a two-to-five-day visit, the few constraints that actually cap a building's throughput, and whoever turns a walk-through into a quantified, defensible list fastest wins the implementation work that follows.

## The Problem
After the visit the assessor drafts the findings on the flight or in the hotel: a slide per issue, a photo, an estimated saving. Observations made on day one are half-remembered by day three; photos are unlabelled; the link between what was seen and which shift, zone and SKU it involved is lost. When the client's operations manager disputes a finding, the evidence is thin, and the finding is dropped.

## Why It's Still Broken
Writing up during the visit competes with observing, and the assessor's priority on site is to see as much as possible. Nothing in the current workflow captures observations in a form that can be written up later without memory.

## What a Fix Looks Like
Time-stamped voice notes and photos captured during the walk, automatically transcribed and grouped by process step and location, with a draft findings list produced each evening for the assessor to correct. Each finding carries its evidence — photo, time, zone — so it survives the client's challenge.

## Who Feels the Pain
Senior assessors writing up late at night; junior consultants reconstructing evidence afterwards; DC managers presented with findings they cannot verify.

## Impact If Fixed
More of what the assessor saw reaches the report, with evidence attached, and the write-up stops being a reconstruction.
