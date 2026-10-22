# Print-Outcome Preview Before the Press Proof

**Niche:** [[niches/graphic-design-studios/packaging-design/profile|Packaging Design]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A pack approved on a calibrated monitor prints darker, duller or muddier on kraft board or metallised film, and nobody sees it until the press proof, when changing it is expensive.
**Tags:** #gradient-boosting #cnns #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to put a pack on shelf that sells — but that splits into two contests with different winners: proving before the retailer's shelf reset that a redesign will outsell the pack it replaces, and pushing every SKU's artwork through each copy change to press-ready files right first time. Decomposed into contested sub-niches below.

## The Problem
Designers approve colour and contrast on screen, sometimes with a contract proof on coated paper. The pack then prints flexo on uncoated kraft, or gravure on a metallised film, with dot gain, ink limits and a substrate colour that shifts everything. Fine reversed type fills in; a vignette bands; the brand colour lands a visible distance from the approved swatch. Experienced packaging designers anticipate much of this from memory of past jobs; juniors and small studios learn it at the press check.

## Why Nobody Has Built This
Colour-management tools (ICC profiles, proofing systems from GMG and others) model ink on substrate for prepress operators and printers, not as a design-stage preview a studio can use. The outcome data — press proofs and press-check notes against the original files — sits with converters and is rarely returned to the studio.

## What to Build
A design-stage preview that takes the artwork, the named substrate and print process, and the converter's known characteristics, and renders how the pack will actually print: predicted colour shifts on key brand colours, regions where type or linework falls below the process's minimums, and vignettes likely to band. It learns from pairs of submitted files and scanned press proofs contributed by partner converters, improving with every job.

## Target Customer
Packaging studios and in-house packaging teams working with several converters, and converters that want fewer press-check surprises.

## Impact If Built
Fewer redesigns at press check, fewer plate remakes, and junior designers who learn print behaviour before the expensive moment rather than at it.
