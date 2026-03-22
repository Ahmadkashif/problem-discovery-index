# Ancillary Service Upsell Recommendation Engine

**Niche:** [[niches/home-inspection/ancillary-services-specialty/profile|Ancillary Services & Specialty]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that takes the property address, age, construction type, and geographic risk factors, and recommends which ancillary services (radon, mold, sewer scope, thermal imaging, WDI) the inspector should offer — converting the ancillary upsell from a random suggestion into a data-driven recommendation that increases both revenue and buyer protection.
**Tags:** #gradient-boosting #revenue-impact #quick-win #logistic-regression

## The Problem
Most inspectors offer ancillary services inconsistently. Some ask every client about radon regardless of geography. Some never mention sewer scope even on homes with 40-year-old cast iron drains that are statistically likely to be failing. The decision to offer a specific ancillary service should be driven by property risk factors: radon testing is critical in EPA Zone 1 counties but unnecessary in most of coastal California; sewer scope is essential for homes with original cast iron or Orangeburg sewer lines (pre-1975 construction) but overkill on a 5-year-old PVC system; mold sampling matters when the inspector observes moisture evidence; WDI inspection is required by lenders in many states but is overlooked when not required. Currently, the upsell decision depends on the individual inspector's knowledge and comfort level with each service — inspectors certified in radon always offer radon, while those without certification never mention it, regardless of geographic risk.

## Why Nobody Has Built This
The recommendation logic requires combining property-level data (age, construction type, foundation type, plumbing material, geographic location) with risk databases (EPA radon zone maps, soil type maps, termite pressure maps, sewer material age curves) and local regulatory requirements (state-mandated WDI inspections, radon disclosure laws). This data exists in separate databases — EPA maintains radon maps, USDA maintains soil surveys, state real estate commissions publish inspection requirements — but nobody has combined them into a property-specific ancillary service recommendation. The market (25,000 inspectors) has been too small for data aggregation companies to prioritize.

## What to Build
A pre-inspection property profiler that takes the address (and optionally the MLS listing data) and produces a risk-based ancillary service recommendation card: "Radon: HIGH risk (EPA Zone 1 county, slab-on-grade foundation) — recommend testing. Sewer Scope: MEDIUM risk (1972 construction, likely cast iron laterals) — recommend scope. WDI: REQUIRED (state-mandated for financed transactions). Mold: LOW risk (no moisture indicators visible in listing photos) — offer if moisture evidence found during inspection. Thermal: STANDARD recommendation for pre-1980 homes (insulation assessment)." The inspector shares this recommendation with the buyer when scheduling, increasing ancillary attachment rates while providing a defensible, data-driven rationale for each recommendation.

## Target Customer
Home inspectors doing 200+ inspections per year who offer 2-3 ancillary services but want to increase attachment rates and expand their service menu. Inspectors in markets with high ancillary demand (radon-heavy regions, areas with old sewer infrastructure, termite-prone states) who want to systematize their upsell approach.

## Impact If Built
Increases ancillary service attachment rate from 20-30% to 50-60% through targeted, risk-based recommendations rather than generic offers. Adds $30K-60K in annual ancillary revenue for an inspector doing 300 inspections per year. Reduces liability by ensuring risk-appropriate services are offered — an inspector who recommends against radon testing in a Zone 1 county and the buyer later discovers elevated radon faces potential liability.
