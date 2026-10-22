# Water-Budget Worksheets Rebuilt After Every Change

**Niche:** [[niches/landscape-architecture-firms/landscape-code-compliance/profile|Landscape Code Compliance & Water-Budget Calculations]]
**Industry:** [[industries/landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Change a hydrozone or swap a high-water plant for a low-water one and the MWELO worksheet, the hydrozone table and the certification all have to be redone by hand.
**Tags:** #numerical-methods #feature-engineering #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to compute each jurisdiction's landscape requirements correctly from the live drawing so the set passes landscape review on the first submittal, and whoever covers the most jurisdictions accurately takes the account.

## The Problem
In California the landscape documentation package carries a hydrozone table and a water budget: the maximum applied water allowance computed from reference evapotranspiration, landscape area and an adjustment factor of 0.7 (1.0 for special landscape areas), against the estimated total water use of the plants and irrigation as designed. Each plant change, irrigation change or area change alters the numbers, and many offices keep the calculation in a spreadsheet disconnected from the drawing.

## Why It's Still Broken
The worksheet format varies by agency, the plant water-use classifications come from a separate reference, and design software exports areas but not the full calculation in each agency's form.

## What a Fix Looks Like
Hydrozones, plant water-use factors and irrigation efficiencies read from the model; the budget recomputed on every change; each agency's worksheet produced in its required format; and the certification page flagged whenever the numbers move after it was signed.

## Who Feels the Pain
Designers rebuilding worksheets late in the permit cycle; licensed professionals certifying numbers they did not recompute; reviewers returning arithmetic errors.

## Impact If Fixed
Hours removed from every revision and a class of permit rejection eliminated.
