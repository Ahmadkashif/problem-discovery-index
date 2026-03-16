# Property Boundary Interpretation from Historical Deed Language and Field Evidence

**Industry:** [[land-surveyors|Land Surveyors]]
**Type:** High Impact
**One-liner:** Senior surveyors translate 100-year-old deed descriptions into modern coordinates by reading physical evidence in the landscape alongside archaic legal language — this tacit knowledge is retiring at 3,000-4,000 PLS per year, and no system exists to capture the judgment that transforms raw measurements into legally defensible boundary determinations.
**Tags:** #bert #cnn #multiclass-classification #nlp #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem

A property boundary is not a GPS coordinate — it is a legal interpretation. A deed might describe a boundary as "thence north 47 degrees east 342 feet to an iron pin set in the bank of Miller's Creek, thence along the meanders of said creek to the stone wall at the northwest corner of the James Withers tract." Translating this into a modern coordinate requires the surveyor to determine: what magnetic declination was in effect when the deed was written (bearing corrections change over centuries), where Miller's Creek ran in the year of the deed (creeks migrate), whether the iron pin was found or is missing (requiring reconstruction of the corner from other evidence), and whether the "stone wall" still exists or has been removed and must be located from remnant evidence.

An experienced surveyor in a given county has performed 500-2,000 boundary surveys in that area. They know the local deed language conventions: that "to the creek" means centerline in deeds before 1920 but bank edge in deeds after 1950, that the county's early surveyors used a specific magnetic compass that introduced a consistent 2-degree error, that "the old county road" referenced in 200 deeds was relocated in 1938 and its original centerline follows a specific tree row visible on 1930s aerial photography. This knowledge — accumulated over decades of resolving ambiguities in the same geography — is what allows a senior surveyor to spend 4 hours on a boundary that would take a junior surveyor 12 hours, or to avoid the 2-3 return trips to the field that occur when initial interpretations prove wrong.

With 3,000-4,000 surveyors retiring annually and only 1,500-2,000 new licensees entering the profession, this accumulated interpretive knowledge is being permanently lost. No written manual captures it because it is county-specific, deed-era-specific, and accumulated through thousands of individual resolutions rather than through generalizable rules.

## Why It's Hard

**Data collection challenge:** Capturing this knowledge requires pairing three data streams that have never been systematically connected: (1) the historical deed language for each parcel, (2) the physical evidence observed in the field (monuments found, fence lines, tree lines, topographic features), documented through photos and field notes, and (3) the surveyor's final boundary determination (the plat and legal description). Most deed records are in county recorder offices, many undigitized. Field evidence is documented in handwritten field notes or point files without photographic context. The final plat exists as a filed document but is not systematically linked to the reasoning that produced it. Building a training dataset requires retroactively connecting these three sources across thousands of past surveys.

**Labeling challenge:** Boundary determinations are not objective measurements — they are professional judgments. Two experienced surveyors may resolve the same ambiguous deed call differently, and both can be legally defensible. "Correct" depends on which legal principles are applied (following the senior deed, the monuments, the intent of the parties, the long-acquiesced line), and different states have different hierarchies of these principles. Training labels are inherently contested — a boundary that went unchallenged for 20 years may still be "wrong" by another surveyor's interpretation. The model must learn to predict a distribution of defensible interpretations rather than a single "right" answer.

**Deployment challenge:** A surveyor legally stamps each survey with their personal license. No model can replace this professional judgment — the surveyor must be the decision-maker, and the model must be an advisory tool that accelerates and informs rather than replaces. This means the model's recommendations must be interpretable: not just "the corner is here" but "based on the 1847 deed call, the 1920 magnetic declination, and the stone remnant found at these coordinates, the most likely corner position is here, with a secondary possibility 4.2 feet northeast if the deed's bearing is interpreted as true north rather than magnetic." The surveyor must trust the model's reasoning enough to use it, but not so much that they stop applying their own judgment.

## What a Solution Looks Like

A two-input system that processes both deed language and field evidence to produce boundary interpretation recommendations. The NLP component (BERT-based) ingests deed text and extracts structured calls: bearings (with era-appropriate declination correction), distances (with unit interpretation — chains, rods, varas, feet), monument descriptions (classified by type and permanence), and adjoiners (linked to their own deed records). The computer vision component (CNN-based) processes field photographs and drone imagery to identify physical evidence: monument remnants (iron pins, stone markers, concrete monuments), occupation lines (fence rows, tree lines, mowed edges), and topographic features referenced in deeds (creek banks, ridgelines, road centerlines).

The system combines these inputs to propose corner positions with confidence intervals and alternative interpretations, each linked to the supporting evidence chain: "Corner position A (confidence 78%): supported by found iron pipe matching 1952 deed description, consistent with bearing from Corner 1 after magnetic correction. Corner position B (confidence 22%): based on stone remnant 4.2 feet NE, consistent with interpretation of bearing as true north." The surveyor reviews the recommendation, applies their professional judgment, and either accepts or adjusts.

## Implementation Path

Phase 1 (6-9 months): Build the NLP pipeline for deed language parsing. Train on a corpus of digitized deeds from 3-5 counties, with structured extraction of bearings, distances, monuments, and adjoiners. Validate against survey plats to confirm extraction accuracy. This phase delivers standalone value as a deed research acceleration tool.

Phase 2 (9-12 months): Build the field evidence classification system. Train on labeled field photographs from cooperating survey firms — monument types, occupation evidence, topographic features. This requires partnerships with 10-20 firms willing to systematically photograph field evidence and tag it against deed calls.

Phase 3 (12-18 months): Integration — connecting deed interpretations with field evidence to produce boundary recommendations. This phase requires the paired dataset: deed + field evidence + surveyor's determination. Train on 1,000-5,000 completed boundary surveys with full documentation. Deploy as an advisory overlay in Carlson Survey or AutoCAD Civil 3D.

Team: 2 ML engineers, 1 NLP specialist, 1 CV specialist, 1 licensed PLS with 20+ years experience, 1 legal consultant for boundary law. Total timeline: 18-24 months to production-quality system.
