# Remote Sensing Turned Into Scouting Priority

**Niche:** [[niches/agtech-platforms/digital-agronomy-advisory/profile|Digital Agronomy & Advisory]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Satellite imagery covering every field in the country every few days is free or nearly free, and agronomists use it to look at pictures rather than to decide which fields to walk this week.
**Tags:** #cnns #semantic-segmentation #change-point-detection #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #transfer-learning
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An agronomist covering thirty thousand acres cannot walk all of it every week and chooses where to go from a route, a memory of which fields were problematic, and a grower's phone call. Meanwhile every one of those fields has been imaged several times since the last visit, and the imagery contains a change signal — an area that has diverged from its own trajectory or from comparable fields — that would point directly at where to walk. The imagery is displayed in the platform as a map the agronomist may or may not open.

## What Already Exists
Sentinel and Landsat imagery is free with revisit intervals of a few days; commercial constellations offer higher resolution and cadence at modest cost. Vegetation index computation is trivial. Change detection on satellite time series is a mature remote sensing discipline. Crop classification and anomaly detection from imagery are well-developed applications with substantial published work. Cloud masking and atmospheric correction are solved. Every component is available and most of it is free.

## The Customization Gap
The adaptation is to produce a visit priority rather than a picture. It requires: (1) within-field change detection against the field's own history and against comparable fields in the same region and crop stage, since absolute index values are nearly meaningless and the signal is deviation; (2) growth stage awareness, because the same index value means different things at different stages and generic alerting is noisy for exactly this reason; (3) prioritisation across the agronomist's whole book with route efficiency included, so the output is this week's visit list rather than a per-field alert stream; (4) confirmation capture at the visit — what the agronomist actually found where the imagery flagged — which is the labelling loop that makes the detection better and which no product closes; and (5) honest treatment of what imagery cannot see, since the most economically important early-season problems are frequently below the canopy or in the soil, and a product that implies otherwise trains its users to distrust it.

## Target Customer
Independent consulting firms whose economics are acres per consultant, retail agronomy organisations with large territories, and the agronomy platform vendors displaying imagery today.

## Impact If Solved
Where to walk this week is the single decision that determines an agronomist's effectiveness, and it is currently made without the observation that arrives free every few days. Closing the confirmation loop is what separates a persistent alerting product from one that improves, and it costs the agronomist a tap at a visit they were making anyway.
