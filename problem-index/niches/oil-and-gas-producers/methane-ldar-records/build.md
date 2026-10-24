# One Site History From Every Detection Method

**Niche:** [[niches/oil-and-gas-producers/methane-ldar-records/profile|Methane Leak Detection & OOOOb Records]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** OGI surveys, continuous monitors, aerial flyovers and satellites each produce detections in their own system, and nobody joins them into one history per site.
**Tags:** #cnns #change-point-detection #bayesian-inference #feature-engineering #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to find and repair every leak and malfunctioning control device before it counts against the operator, and whoever has the fewest violations found at an EPA or state inspection takes the account.

## The Problem
An operator may have an OGI crew visiting quarterly, continuous sensors on its larger pads, an aerial survey twice a year, and satellite detections arriving from third parties. Each method has different sensitivity and timing. When an aerial survey reports a plume, nobody can quickly see whether the OGI crew found it, the sensor alarmed, or maintenance already fixed it.

## Why Nobody Has Built This
Each detection vendor sells its own dashboard. Fusing them needs site and equipment registries, time alignment and an understanding of each method's detection limits, which no single vendor has reason to build for its competitors' data.

## What to Build
A site-level event model that ingests detections from every method with their detection limits, aligns them to sites and equipment, estimates the probability and likely duration of each emission event, and ties each to a work order and repair proof. It ranks sites for the next survey and produces the per-site record an inspector or third-party detection notice will ask for.

## Target Customer
Emissions programme managers at operators running more than one detection method.

## Impact If Built
For an operator with ~2,000 sites (estimate), one history removes duplicate investigations of the same plume. Prioritising surveys toward sites with recent signals can cut emission-event duration by an estimated ~30%.
