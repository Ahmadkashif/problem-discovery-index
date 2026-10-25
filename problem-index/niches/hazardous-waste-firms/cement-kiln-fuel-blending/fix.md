# Off-Spec Fuel Found at the Kiln

**Niche:** [[niches/hazardous-waste-firms/cement-kiln-fuel-blending/profile|Fuel Blending for Cement Kilns]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A kiln rejects or penalises a fuel load days after it left the blender, and nobody can say quickly which intake loads caused it.
**Tags:** #descriptive-statistics #feature-engineering #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn generators' high-heat-value wastes into fuel that meets a cement kiln's permit and contract specification, and whoever delivers the largest share of blended loads inside the kiln's specification takes the account.

## The Problem
When the kiln's sample disagrees with the blender's, the load is penalised, returned or diverted to an incinerator at a loss. Tracing the cause means reading tank logs and intake records by hand.

## Why It's Still Broken
Intake, tank and shipment records sit in different systems, and the kiln's results arrive as PDFs. Batch genealogy is rebuilt only when there is a dispute.

## What a Fix Looks Like
Record batch genealogy automatically, from each intake load and profile to its tank to the fuel shipment and the kiln's result, so every off-spec event points to the contributing loads and generators, and repeat offenders are re-profiled.

## Who Feels the Pain
Blend planners, kiln fuel managers and the generators whose profiles keep drifting.

## Impact If Fixed
Tracing a dispute in minutes instead of a day, across ~30 disputes a year at a mid-sized plant (estimate), saves ~200 staff hours and stops repeat off-spec intake from the same few generators.
