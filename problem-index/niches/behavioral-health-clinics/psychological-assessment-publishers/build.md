# The Standardization Archive as a Continuously Queryable Norm Base

**Niche:** [[niches/behavioral-health-clinics/psychological-assessment-publishers/profile|Psychological Assessment Publishers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A publisher holds decades of national standardization samples, uses each one to print a fixed set of norm tables, and then cannot answer any question the tables were not designed to answer.
**Tags:** #bayesian-inference #probability-distributions #hypothesis-testing #confidence-intervals #dimensionality-reduction #pca #gaussian-mixture-models #evaluation-metrics #feature-engineering #data-integration #revenue-impact

## The Problem
A standardization sample is the most expensive thing a test publisher ever buys — thousands of participants recruited to census-matched demographic targets, administered under controlled conditions, at a cost running into seven figures and a timeline of years. What is extracted from it is a set of norm tables: score conversions by age band, sometimes by a small number of demographic strata, printed in a manual and fixed until the next restandardization a decade or more later. Everything else the sample contains stays in a file. A clinician asking whether the norms hold for a demographic the sample under-represented, or a researcher asking how the construct's factor structure differs across a subgroup, or a product manager asking whether the item set could support a short form, all require going back to raw data that is archived by project rather than organized as a resource. In practice the answer is usually a new study.

## Why Nobody Has Built This
Standardization samples were collected under protocols and consent frameworks specific to each project, across a period spanning paper administration, early digital, and modern platforms, with data stored in whatever format the project used. Pooling them means resolving instrument versions, scoring conventions, demographic coding schemes, and — critically — auditing what each sample's consent actually permits, which no publisher has systematically done. There is also a professional conservatism with real justification: norms are the basis of clinical and legal decisions, so any suggestion of computing them flexibly rather than publishing them fixed raises legitimate concerns about stability and defensibility, and that concern has stopped the conversation before it reached the archive question.

## What to Build
A unified norm base that holds every standardization and validation sample in a common structure — participant-level responses, demographics, administration conditions, instrument version, and the consent and reuse terms attached to that collection. The consent layer is what makes the whole thing usable rather than a liability, because every query can then state which portion of the archive it is entitled to draw on. With the archive in that form, the publisher gains capabilities it currently sells studies to obtain: norms computable for demographic intersections the printed tables never covered, with explicit uncertainty where sample support is thin rather than silence; cross-instrument analysis, since the same participants frequently completed several measures in a battery; item-level analysis across the full history, which is what short-form and adaptive development actually needs; and detection of norm drift by comparing successive samples on retained anchor items, which is the evidence that should drive restandardization timing and currently does not exist.

## Target Customer
VPs of research and chief psychometricians at assessment publishers running 50-250 research staff, and the product leaders who currently cannot evaluate a new instrument concept without commissioning fresh data collection.

## Impact If Built
Converts the publisher's largest sunk cost into a standing asset. Questions that today require a study become queries, which changes both the economics and the cadence of product development. It also addresses the field's most persistent criticism of the norms themselves — that they are fixed, coarse, and aging between restandardizations — with a defensible answer rather than a promise about the next edition.
