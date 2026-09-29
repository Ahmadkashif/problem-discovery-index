# Historical Records Are Interpreted by the Consultant Every Time

**Niche:** [[niches/environmental-consultants/environmental-records-database-providers/profile|Environmental Records Database Providers]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The provider ships a century of fire insurance maps, city directories, and aerial photographs, and thousands of consultants each read the same images of the same property and write the same historical narrative independently.
**Tags:** #cnns #object-detection #semantic-segmentation #transformers #bert #transfer-learning #word-embeddings #evaluation-metrics #tacit-knowledge-ml #data-integration

## The Problem
Half of a Phase I is the historical use reconstruction, and the provider supplies the raw material for it — fire insurance maps showing structures and their labelled uses, city directories listing occupants by address across decades, aerial photographs, topographic sheets. The consultant reads them and writes a narrative: this parcel was a machine shop from the twenties, a dry cleaner from the fifties, vacant thereafter. That interpretation is where the recognized environmental conditions come from and it is the most skilled part of the report. It is also performed from scratch for every property, by every consultant, on every transaction — and the same parcel gets reinterpreted independently each time it changes hands.

## Why It's Still Broken
The provider positions itself as a records supplier rather than an interpreter, partly for good reason: a stated conclusion about historical use is a professional opinion carrying liability the environmental professional is licensed to bear and the data provider is not. That boundary is real. But it has been applied to extraction as well as to conclusion, and extracting what a directory entry says or what a map legend labels is not an opinion. The imagery is also genuinely hard to process — hand-drawn maps in inconsistent conventions, directories in dense small print across many typographies — which made automation impractical until recently.

## What a Fix Looks Like
Structured extraction across the historical corpus, delivered as evidence rather than as conclusion. Fire insurance maps parsed for structures, footprints, and their labelled uses per vintage; city directories parsed into occupant-by-address-by-year records; aerial imagery segmented for developed area and structure change. The output for a parcel is a timeline of extracted observations, each citing the source image and page, which the environmental professional then interprets and signs — preserving exactly the boundary that matters while removing the transcription work that precedes it. Because the extraction is per-parcel and cached, the second consultant to look at a property inherits the first extraction rather than repeating it, which is where the compounding is. And uncertainty must be explicit, since a smudged directory entry read wrongly is worse than one flagged as illegible.

## Who Feels the Pain
Environmental professionals spending the skilled part of their day transcribing rather than interpreting; clients paying for the same historical reconstruction each time a property transacts; junior staff producing weaker historical sections because reading these sources is a learned skill; and the provider, whose most distinctive asset ships as images.

## Impact If Fixed
Turns an archive into a structured historical record of the built environment, which is a categorically more valuable asset and one no competitor can assemble without the same imagery holdings. It also removes the largest repeated manual task in the industry's primary revenue product while leaving the professional judgment — and the liability — exactly where it belongs.
