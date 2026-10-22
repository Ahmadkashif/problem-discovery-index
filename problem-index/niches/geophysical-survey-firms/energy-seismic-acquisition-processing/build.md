# A Record Linking Acquisition Choices to Image Quality

**Niche:** [[niches/geophysical-survey-firms/energy-seismic-acquisition-processing/profile|Energy Seismic Acquisition & Processing]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Survey designers choose receiver density, source effort and offsets on modelling and habit, because nobody has ever joined what was recorded in the field to how good the processed image turned out.
**Tags:** #gradient-boosting #causal-inference #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to deliver a usable seismic image over the client's acreage at the lowest cost per square mile", but it hides two contests with different winners: field crews compete on clean source and receiver points recorded per crew-day across permit gaps and weather, and processing houses compete on depth images that tie the wells before the lease or drilling decision. Decomposed into contested sub-niches below.

## The Problem
A 3D survey's cost is set by its design: how many receiver and source points per square mile, what offsets and azimuths, how much vibrator effort per point. Denser is better and more expensive. Designers use forward modelling and experience; clients push for cheaper; permit refusals force skids and gaps that change fold locally. Months later a processing house delivers an image whose quality varies across the survey — and nobody measures how much of that variation came from design choices, skids, field noise or processing.

## Why Nobody Has Built This
The three records sit with three parties. The contractor holds the acquisition logs and skid files, the processor holds the flows and attribute volumes, and the client or library owns the data and the wells that later test it. Each survey is treated as a one-off, and contractual data ownership discourages anyone from pooling across surveys.

## What to Build
A survey-quality ledger that, for each bin, stores the as-acquired geometry (fold, offset and azimuth distribution, skids, noise metrics) and the processed-image quality (signal-to-noise, frequency content, well-tie quality), and models which acquisition variables explain image quality after controlling for geology. Delivered to the client or library as a design-evidence report, and to the contractor as a bidding tool showing where cheaper designs cost nothing and where they cost the image.

## Target Customer
Multi-client libraries and operators commissioning repeat surveys in the same basins, and contractors who want to defend a design in a bid.

## Impact If Built
Even a few percent of channel count trimmed where it adds nothing, or added where it matters, is material on surveys costing millions, and replaces design-by-argument with evidence.
