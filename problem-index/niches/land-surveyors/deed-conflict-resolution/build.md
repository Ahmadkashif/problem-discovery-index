# Automated Legal Description Conflict Analyzer

**Niche:** [[niches/land-surveyors/deed-conflict-resolution/profile|Deed Conflict Resolution]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool takes two adjacent legal descriptions, parses them into geometry, and produces a conflict report identifying exactly which calls disagree, by how much, and which description likely controls under the jurisdiction's rules of construction.
**Tags:** #transformer #named-entity-recognition #nlp #tabular-ml #automation

## The Problem
A boundary surveyor receives a deed with a metes and bounds description: "Beginning at an iron pin on the northerly line of Oak Street, thence N45°30'E a distance of 200.00 feet to an iron pin; thence N44°30'W a distance of 150.00 feet..." The neighboring deed describes the shared boundary as "S45°00'W a distance of 198.50 feet." The two descriptions disagree by 0°30' in bearing and 1.50 feet in distance. Is this a significant conflict or normal surveying tolerance? Which deed was recorded first? Are there monuments in the field that control over the written calls? The surveyor must parse both descriptions, plot them, identify every conflicting element, research recording dates and monument priority, and write a conflict analysis. This process takes 2-6 hours per boundary and is repeated for every adjoiner in a boundary survey — a rectangular lot has 4 adjoiners.

## Why Nobody Has Built This
Legal descriptions are natural language with domain-specific notation — bearings (N45°30'E), distances (200.00 feet), monument calls ("to the iron pin set"), and natural feature references ("along the creek"). Parsing them requires NER trained on survey-specific terminology, handling of multiple description formats (metes and bounds, lot-and-block, government survey), and tolerance for historical variations in notation. The conflict analysis layer requires computational geometry (do these polygons overlap, gap, or match within tolerance?) combined with legal reasoning (which calls take priority under the rules of construction?). This cross-domain problem hasn't attracted attention because the market is small and specialized.

## What to Build
A conflict analysis engine with three stages: (1) NLP parser that extracts structured geometry (bearings, distances, curves, monument calls, reference plats) from natural-language legal descriptions in any format; (2) computational geometry engine that plots both descriptions, identifies overlap and gap areas, and pinpoints the specific calls that create the conflict (bearing disagreement, distance disagreement, monument inconsistency); (3) resolution assistant that applies the jurisdiction's rules of construction (natural monuments > artificial monuments > courses and distances > area) and suggests which description likely controls, with case law references. Output: a conflict report with annotated geometry, specific disagreements quantified, and suggested resolution.

## Target Customer
Boundary surveyors, title examiners, and title attorneys. Any professional who must resolve conflicts between adjacent legal descriptions.

## Impact If Built
Reduces deed conflict analysis from 2-6 hours per boundary to 15-30 minutes. On a boundary survey with 4 adjoiners, this saves 6-20 hours. Catches subtle conflicts (0.5-degree bearing differences, 1-foot distance discrepancies) that manual analysis misses. Enables title companies to pre-screen for boundary issues before ordering a survey.
