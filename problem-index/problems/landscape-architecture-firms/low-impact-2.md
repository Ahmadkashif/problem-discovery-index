# Landscape Code and Water-Budget Calculations

**Industry:** [[landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every city computes landscape requirements differently — parking-lot islands, buffer yards, canopy and tree-mitigation credits, California's MAWA water budget — and firms rebuild the calculation tables by hand from the municipal code on every permit set.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #compliance #automation #quick-win

## The Problem
Before a site plan is approved, the landscape set must show that it meets the jurisdiction's landscape ordinance. A typical commercial or multifamily project carries a compliance table: one tree per so many parking spaces, island spacing, street-frontage planting per linear foot, buffer-yard widths and plant units by adjacent zoning, percentage of site landscaped, tree preservation and mitigation (diameter inches removed against inches replaced), and canopy coverage at maturity. In California the set must also carry the Model Water Efficient Landscape Ordinance package — a hydrozone table and a water budget showing estimated total water use under the maximum applied water allowance calculated with an evapotranspiration adjustment factor of 0.7 — and in many cities a licensed professional must certify it.

The designer reads the code on Municode or the city's PDF, finds the right table among amendments, and builds a spreadsheet from the CAD quantities. When the plan changes, the table is rebuilt. Reviewers return sets for arithmetic errors and missed provisions, and each resubmittal costs the developer two to six weeks (estimate).

## What Already Exists
Municipal code publishers (Municode, American Legal Publishing, eCode360) host the text. Land F/X and Vectorworks compute areas, plant counts and irrigation hydrozone areas that feed a water-use worksheet. Excel does the rest. Zoning-analysis products for developers cover height, setbacks and density rather than landscape provisions.

## The Customisation Gap
The missing layer is a landscape-specific rule library: each jurisdiction's provisions extracted into structured, versioned rules (with the amendment date), mapped to the CAD objects that satisfy them — trees, shrubs, islands, buffer segments, hydrozones — and recomputed every time the drawing changes. It needs local quirks handled explicitly: which species count toward canopy credit, whether existing preserved trees count toward the requirement, how special landscape areas enter the water budget, and what the reviewer in that city actually checks. General zoning tools ignore planting; CAD tools compute quantities but know nothing about the ordinance.

## Impact If Solved
First-pass approval on landscape provisions saves each permit set one resubmittal cycle on a meaningful share of projects, and turns a half-day of table-building per revision into a recalculation measured in seconds.
