# Deed Plotting Software with Conflict Detection

**Niche:** [[niches/land-surveyors/deed-conflict-resolution/profile|Deed Conflict Resolution]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** DeedPlotter and Legal Description Mapper plot legal descriptions geometrically, but they don't detect conflicts — they show two polygons on screen and leave it to the surveyor to visually identify where they disagree.
**Tags:** #automation #tabular-ml #data-integration #quick-win

## The Problem
When a surveyor needs to compare adjacent legal descriptions, they use deed plotting software to convert each description into geometry. The software plots each description as a polygon, and the surveyor visually inspects the overlap. But visual inspection of two complex polygons (20+ calls each, with curves and monument references) is unreliable — subtle bearing differences of 0°15' create gaps that are invisible at common zoom levels but represent real boundary conflicts. The surveyor must manually compare each call pair between the two descriptions, bearing by bearing, distance by distance, to identify discrepancies. The plotting software does geometry; the conflict detection is entirely manual.

## What Already Exists
DeedPlotter (Greenbrier Graphics) is the most widely used deed plotting tool — it accepts typed legal descriptions and generates polygonal plots. Legal Description Mapper performs similar functions. Some CAD packages (Carlson Survey, AutoCAD with COGO tools) can plot descriptions from coordinate input. All of these tools plot geometry but don't compare it — they show the shape, not the conflict.

## The Customization Gap
The tool needs a comparison mode: input two or more legal descriptions that share a common boundary, and the system automatically (1) identifies the shared boundary segment in each description; (2) compares bearing, distance, and monument calls between descriptions for each shared segment; (3) highlights discrepancies above a configurable tolerance (e.g., bearing >0°05', distance >0.50 feet); (4) computes the area of overlap or gap created by the conflict; (5) classifies the conflict severity (within survey tolerance, minor discrepancy, significant conflict requiring resolution). The output is a tabular conflict report alongside the graphical plot.

## Target Customer
Licensed land surveyors performing boundary surveys. Title examiners who review surveys and descriptions for title insurance underwriting.

## Impact If Solved
Automates the manual call-by-call comparison that currently takes 30-90 minutes per adjoiner pair. Catches sub-visual conflicts that manual inspection misses — estimated 10-15% of boundary conflicts involve bearing differences under 0°15' that are invisible on a standard-scale plot. Reduces the skill threshold for conflict analysis, enabling survey technicians to do preliminary analysis that currently requires a licensed surveyor.
