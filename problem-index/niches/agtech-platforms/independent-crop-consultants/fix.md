# Tomorrow's Route Planned From Memory

**Niche:** [[niches/agtech-platforms/independent-crop-consultants/profile|Independent Crop Consultants — Acres Per Consultant]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A consultant decides which fields to visit tomorrow from memory of which were problematic and a sense of which are due, spending a large share of the season driving between decisions that were made badly.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #evaluation-metrics #confidence-intervals #time-series-forecasting #automation #worker-facing
**Contested on:** Every serious competitor selling to independent consultants is fighting to raise the acres one person can cover at quality — and whoever cuts the hours between walking a field and delivering a report takes the firm.

## The Problem
Two hundred fields across four counties, each needing a visit at intervals that depend on crop stage, pest pressure, recent weather and what was found last time. The consultant decides tomorrow's route the night before, from memory and a map. Some fields get visited more often than they need and some slip past the window where an observation would have mattered — a pest threshold crossed between visits is the failure that costs a grower real money and is the one the consultant most fears. Meanwhile drive time is a large share of a working day and the route is built by geography rather than by need.

## Why It's Still Broken
Visit scheduling has been treated as the consultant's own judgement, which it substantially is, and no product has attempted to support it because the inputs — crop stage, pest pressure forecast, recent observations, weather, field location — sit in different places. Routing tools exist and optimise driving without knowing which fields need visiting, which is the wrong half of the problem. And consultants are rightly wary of a system that would tell them where to go, having seen products that understood the agronomy poorly.

## What a Fix Looks Like
Rank the fields and then route them. Visit urgency per field is computable from what is already recorded: days since last visit against the interval that crop and stage warrants, the trajectory of anything observed last time, degree-day accumulation toward known pest and disease thresholds, recent weather events, and the imagery change signal where available. Rank by urgency, then solve the route across the selected fields, which is an ordinary routing problem once the selection is made. Present it as a proposed day the consultant edits rather than a schedule, because their judgement about a particular grower or a particular field is frequently the deciding factor and a product that ignores that will be abandoned. Report the coverage statistics nobody has — which fields have gone longest without a visit, and whether any crossed a threshold between visits — because that is the quality measure the consultant is actually managing and currently tracks in their head.

## Who Feels the Pain
Consultants driving more than they walk and carrying the anxiety of fields they have not seen; growers whose field was not visited in the week it mattered; and firms whose capacity is bounded by a planning decision made at ten at night.

## Impact If Fixed
Urgency-ranked routing converts drive time into covered acres, which is the profession's only real lever on capacity. The coverage report is the quieter benefit and addresses the failure consultants worry about most — the field that slipped past its window — which is currently prevented by memory alone.
