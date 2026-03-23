# Scrivener Errors in Deeds Going Undetected Until Survey

**Niche:** [[niches/land-surveyors/deed-conflict-resolution/profile|Deed Conflict Resolution]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Fix (Pain Point)
**One-liner:** Typos in legal descriptions — a bearing of N45E written as N54E, a distance of 200 feet recorded as 20 feet — are caught only when a surveyor tries to plot the description years later, at which point correcting the deed requires a quiet title action costing $5K-15K.
**Tags:** #named-entity-recognition #anomaly-detection #nlp #compliance #automation

## The Problem
Legal descriptions are typed into deeds by attorneys, paralegals, and title company staff. These descriptions contain bearings (N45°30'E), distances (200.00 feet), curve data (radius, arc length, chord bearing), and monument references. Transcription errors are common: transposed digits (N45E becomes N54E), dropped decimal points (200.00 becomes 20.00), omitted calls (a leg of the boundary is missing), and copy-paste errors from prior deeds. These errors are not caught at recording — the county recorder records whatever is submitted, with no geometric validation. The error sits in the public record until someone (usually a surveyor, years later) tries to plot the description and discovers it doesn't close, describes the wrong property, or conflicts with the physical evidence. By then, correcting the error requires a corrective deed (if all parties agree) or a quiet title action (if they don't), costing $5K-15K in legal fees.

## Why It's Still Broken
No validation occurs between deed drafting and recording. Attorneys draft descriptions by copying from prior deeds or surveys, introducing copy errors. Title companies review descriptions for completeness but don't plot them geometrically. County recorders have no authority or capability to validate geometric accuracy. The entire real estate recording system assumes the description is correct at submission. The surveyor who discovers the error years later had nothing to do with the original deed and must now clean up someone else's mistake — often at the property owner's expense.

## What a Fix Looks Like
A deed validation tool used by title companies and attorneys before recording: the tool parses the legal description, plots it geometrically, and checks for: (1) mathematical closure (does the description return to the point of beginning?); (2) geometric reasonableness (does the described area match the stated area? are all bearings and distances within plausible ranges?); (3) consistency with the parent parcel or subdivision plat; (4) common scrivener error patterns (transposed digits, missing calls, duplicate calls). The tool flags descriptions that fail validation and identifies the specific problematic elements. Deployed as a pre-recording check, it catches errors before they enter the public record.

## Who Feels the Pain
Property owners who discover years after purchase that their deed describes a different parcel than they occupy, and must pay $5K-15K for legal correction. Surveyors who waste hours chasing description errors that turn out to be typos. Title companies that issue insurance on properties with defective descriptions.

## Impact If Fixed
Prevents an estimated 5-10% of newly recorded deeds from containing scrivener errors. Eliminates the downstream cost of correction (quiet title actions, corrective deeds, survey rework). Catches errors at the point where they're cheapest to fix (before recording, $50-100 in attorney time) rather than the point where they're most expensive (after recording, $5K-15K in litigation).
