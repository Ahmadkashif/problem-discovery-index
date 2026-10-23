# The Hazard-Tree Call Nobody Can Audit

**Niche:** [[niches/electric-utilities/vegetation-wildfire-mitigation-programs/profile|Vegetation Management & Wildfire Mitigation Programmes]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** An inspector marks a tree for removal or leaves it standing, and after a fire nobody can show what they saw or why.
**Tags:** #cnns #object-detection #tacit-knowledge-ml #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to show regulators that each trimming and hardening dollar removed measurable ignition and outage risk, and whoever ties completed work to risk reduced, span by span, takes the account.

## The Problem
Hazard-tree assessment is a judgement call: lean, decay, root damage, species, strike potential toward the line. Experienced foresters make it in seconds. Contract inspectors vary widely, and the record is often a code in a tablet form. After an ignition or outage, investigators ask whether the tree was inspected and what was found, and the record can't answer.

## Why It's Still Broken
Inspection forms were designed for work dispatch, not evidence. Photos are optional or unlinked, and inspector consistency is never measured.

## What a Fix Looks Like
Require georeferenced photos with each assessment, and capture the inspector's reason codes. Periodically have senior foresters re-assess a blind sample to measure agreement by inspector and contractor. The labelled photos then become training data for a model that flags likely misses for review.

## Who Feels the Pain
Utility foresters accountable for contractor quality; regulators investigating ignitions; inspectors who did the right thing but can't prove it.

## Impact If Fixed
A photo-backed record for every hazard-tree call and measured inspector agreement on a ~5% blind re-inspection sample (estimate), which also starts a labelled dataset of the expert forester's eye.
