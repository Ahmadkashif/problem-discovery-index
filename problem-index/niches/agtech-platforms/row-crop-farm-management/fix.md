# Yield Data Nobody Cleans

**Niche:** [[niches/agtech-platforms/row-crop-farm-management/profile|Row Crop Farm Management]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Raw combine yield monitor data contains substantial artefacts — fill and flush delays, speed changes, overlapping passes, moisture drift — and it is mapped, stored and analysed as though every point were a measurement.
**Tags:** #descriptive-statistics #numerical-methods #evaluation-metrics #confidence-intervals #hypothesis-testing #change-point-detection #automation #quick-win
**Contested on:** Every serious competitor in row crop software is fighting to tell a grower which of their input decisions actually changed the yield on their own ground — and whoever produces credible on-farm effect estimates takes the account.

## The Problem
A yield map shows a low-yielding strip along one edge of a field. It is not a low-yielding strip; it is the pass where the combine header was partially full, or where the operator slowed for a turn, or an overlapping pass counted twice with half the width. Every yield map carries these artefacts, every grower who has looked closely knows it, and the maps are used anyway — for zone delineation, for prescription writing, for comparing hybrids, and for the yield comparisons that inform next year's input decisions. Conclusions built on uncleaned yield data are unreliable in ways that are invisible on a colour map.

## Why It's Still Broken
Cleaning yield data properly requires understanding the machine's behaviour — the delay between the header and the sensor, the effect of speed and flow changes, how overlapping passes should be resolved — which is equipment-specific work that each platform would have to do per combine model. Published cleaning methods exist in the agronomic literature and are implemented in research tools rather than in commercial products. And the map looks fine, which is the real reason: an artefact-laden yield map is visually plausible and nobody sees the error.

## What a Fix Looks Like
Clean it by default and say what was removed. Standard filters from the published methodology — start and end of pass delays, implausible speed and flow combinations, overlap resolution, moisture and grain flow calibration drift — applied automatically, with the removed proportion and the reason reported rather than silently discarded. Flag calibration problems back to the grower during harvest, when the combine can still be recalibrated, rather than after the season when the data is fixed — this is the highest-value element and is entirely absent today. Report a data quality figure per field and per harvest, so a grower knows which of their yield data supports analysis and which does not. And where the analysis downstream is a trial comparison, propagate the uncertainty rather than treating cleaned yield as exact, since the cleaning reduces the artefacts and does not eliminate them.

## Who Feels the Pain
Growers making input decisions from comparisons built on artefacts; agronomists delineating management zones from maps that partly describe combine behaviour; and anyone attempting the on-farm trial analysis this niche is about, which is unusable on uncleaned data.

## Impact If Fixed
Cleaning is the prerequisite for every quantitative use of yield data and is the difference between an analysis and a picture. In-season calibration alerting is the immediate win, since a miscalibrated combine produces a season of unusable data that nobody discovers until the season is over.
