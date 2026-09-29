# Substantiation Reuse Across a Portfolio of Near-Identical Formulas

**Niche:** [[niches/hair-salons-independent/cosmetic-regulatory-consulting/profile|Cosmetic Regulatory & Safety Substantiation Consulting]]
**Industry:** [[industries/hair-salons-independent|Hair Salons (Independent)]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A colour line is two hundred shades of the same chemistry, and each one gets its safety substantiation assembled as though the firm had never seen the ingredients before.
**Tags:** #graph-ml #ocr #large-language-models #named-entity-recognition #workflow-orchestration #compliance

## The Problem
A professional haircare brand's portfolio is not two hundred unrelated products. It is a handful of base systems with pigment and modifier variations across a shade range, plus line extensions that differ from the parent by a fragrance or a preservative swap. Chemically, the substantiation questions repeat enormously.

The work does not. Each product gets a safety assessment assembled by a toxicologist who pulls ingredient dossiers, checks concentration against precedent and published limits, considers exposure for the product type, and writes it up. The assessment for shade 6N and the assessment for shade 6NA are, on the science, nearly the same document — and they are produced as though independently, because the firm has no representation of the portfolio as a related set of formulas.

MoCRA turned this from an internal quality practice into a regulatory obligation with deadlines. The volume of substantiation work rose sharply and the method for producing it did not change at all.

## Why Nobody Has Built This
Cosmetic safety assessment was a voluntary-ish discipline until very recently. Firms were small, the work was bespoke, and the deliverable was a document written by a named toxicologist whose signature was the point. Tooling built for that world is a document template and a reference library.

Meanwhile the serious regulatory information management systems were built for pharmaceuticals, where a submission is a multi-year programme for a single molecule and the software costs accordingly. Nothing was built for the opposite shape — very high product counts, shallow per-product depth, dense chemical overlap — which is exactly cosmetics.

## What to Build
A formula-aware substantiation system that treats the portfolio as a graph and assembles each assessment from what has already been established.

**Represent formulas structurally**, ingredient by ingredient with concentrations, so the system can compute how a new product relates to everything the firm has previously assessed. Nearest-neighbour retrieval over formula composition is the core primitive: when a new shade arrives, the relevant question is which previously assessed products it sits between, and what the differences are.

**Maintain ingredient assessments as versioned reusable objects** rather than as text inside product documents. An ingredient's safety profile at a given concentration for a given exposure type is a fact about the ingredient. It is currently restated in every document that needs it, which means a change in the literature requires finding every document that mentioned it.

**Generate the differential.** For a new product, the useful output is not a blank template but a draft assembled from the closest prior assessments, with every deviation flagged for the toxicologist: this preservative is 0.4% where the precedent was 0.2%; this pigment has no prior assessment in a leave-on product. The expert reviews and signs the differences instead of rebuilding the whole.

**Track the regulatory frontier automatically.** Ingredient status changes — a new restriction in one jurisdiction, a revised opinion, a concentration limit — and the system should immediately name every product in every client portfolio that contains it. Today that is a manual search when someone remembers to run one.

## Target Customer
Managing director or practice leader at a cosmetic regulatory consultancy, particularly one serving multiple brands with large shade-range portfolios. The economics are plain: capacity is toxicologist hours, toxicologists are scarce, and demand rose on a statutory schedule.

## Impact If Built
The bottleneck in this market is qualified assessors, not demand. A firm that can produce a defensible assessment in a fraction of the hours takes work its competitors are turning away — and does so with better consistency, since a portfolio assembled from shared ingredient objects cannot contradict itself the way two hundred independently written documents routinely do.
