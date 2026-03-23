# Deed Conflict Resolution

**Parent Industry:** [[industries/land-surveyors|Land Surveyors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1.1B (labor cost)
**Share of Parent Industry:** ~8% of surveyor time
**Digital Adoption:** Low — Deed conflict analysis is done by reading two or more legal descriptions side by side, mentally or manually plotting them, and identifying where they disagree. The entire process is paper-based cognitive work.
**Target Buyer:** Boundary Surveyor / Title Attorney / Title Examiner
**Automation Potential:** High — Parsing metes and bounds descriptions into geometry, comparing geometries for overlap/gap, and identifying specific conflicting calls are rule-based tasks well suited to NLP and computational geometry.

## What Makes This a Distinct Niche
When adjacent property deeds describe boundaries that don't agree — one deed says the boundary runs N45E for 200 feet while the neighboring deed says it runs N47E for 195 feet — someone must resolve the conflict. This is the bread-and-butter analytical work of boundary surveyors and title attorneys. Deed conflicts arise from surveyor error (original surveys were imprecise), scrivener error (deeds were copied incorrectly), natural feature changes (creeks shifted, trees died), and ambiguous descriptions (what is "the large oak tree by the creek"?). Resolving these conflicts requires parsing both legal descriptions, plotting them geometrically, identifying the specific conflicting calls, and applying the rules of construction to determine which description controls. This is painstaking, error-prone, and repetitive — and it's done entirely by hand.

## Current Tools & Gaps
Surveyors plot legal descriptions manually in CAD (AutoCAD, Carlson) by entering each bearing and distance call. Some use deed-plotting software (DeedPlotter, Legal Description Mapper) that automates the geometric plotting but doesn't do the analysis — it shows you two overlapping polygons but doesn't tell you which specific calls conflict or which legal rules apply. Title attorneys read descriptions and mark up conflicts by hand. No tool parses natural-language legal descriptions, identifies conflicting elements, and suggests resolution based on the rules of construction.

## Problems
- [[niches/land-surveyors/deed-conflict-resolution/build|🔨 Build: Automated Legal Description Conflict Analyzer]]
- [[niches/land-surveyors/deed-conflict-resolution/buy|🛒 Buy: Deed Plotting Software with Conflict Detection]]
- [[niches/land-surveyors/deed-conflict-resolution/fix|🔧 Fix: Scrivener Errors in Deeds Going Undetected Until Survey]]
