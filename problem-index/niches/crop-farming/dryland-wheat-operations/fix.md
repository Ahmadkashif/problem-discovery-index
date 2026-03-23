# Fallow Management Weed Control Timing

**Niche:** [[niches/crop-farming/dryland-wheat-operations/profile|Dryland Wheat & Small Grain Operations]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Fix (Pain Point)
**One-liner:** During fallow years, weed control timing determines how much moisture is conserved for the next crop — spraying 3 days late allows weeds to consume 0.5-1 inch of stored moisture worth $15-25/acre in next year's crop, but farmers managing 3,000+ fallow acres cannot scout every field daily to catch weed emergence.
**Tags:** #cnns #object-detection #time-series-forecasting #tacit-knowledge-ml

## The Problem
In crop-fallow rotation, the fallow year's purpose is storing moisture for next year's crop. Weeds growing during fallow consume stored moisture — a single flush of kochia or Russian thistle can deplete 1-2 inches of stored moisture in a week if not controlled. The farmer must spray (or till) weeds within 2-3 days of emergence to minimize moisture loss. But a dryland operation may have 1,500-3,000 fallow acres scattered across 15-30 fields, each with different weed pressure timing based on soil temperature, recent rainfall, and weed seed bank. The farmer cannot scout all fallow fields every 3 days — they check fields periodically (weekly or less), miss early weed emergence on some fields, and lose stored moisture that reduces next year's yield.

## Why It's Still Broken
Satellite imagery (Sentinel-2 at 10m resolution, Planet at 3m) can detect weed presence on fallow fields, but the revisit frequency (5 days for Sentinel, daily for Planet) may not be fast enough, and the resolution may not distinguish small weed seedlings from crop residue. Drones could provide higher-resolution imagery but require the farmer to fly every fallow field every 3 days — impractical at scale. No tool integrates weather-based weed emergence prediction (weeds germinate when soil temperature exceeds threshold after rain events) with satellite-based verification to alert the farmer when specific fields need scouting and treatment.

## What a Fix Looks Like
A fallow weed alert system that: (1) predicts weed emergence timing for each fallow field based on soil temperature (from weather stations), recent rainfall, and the field's historical weed pressure patterns, (2) confirms predicted emergence with satellite imagery when available, and (3) alerts the farmer to scout and spray specific fields within the critical 2-3 day window. The farmer receives a priority list: "Fields 7, 12, and 18 are predicted to have weed emergence by Thursday based on Monday's rain and warm temperatures — scout and spray by Friday to preserve stored moisture."

## Who Feels the Pain
Dryland farmers who lose stored moisture worth $15-25/acre on fields where weed control was delayed by 3-5 days. Over 1,500 fallow acres, a 1-inch moisture loss from delayed weed control represents $22,500-37,500 in reduced next-year crop value.

## Impact If Fixed
Weed control timeliness improves from "check when I get to it" to weather-triggered priority scouting. Stored moisture conservation improves by 0.5-1 inch per fallow season on fields where weed control timing was previously suboptimal. Next-year yield improvement of 3-7 bushels/acre on affected fields — worth $15-35/acre at current wheat prices.
