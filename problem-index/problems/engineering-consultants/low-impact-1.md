# Code Compliance Checking for Building/Civil Design

**Industry:** [[engineering-consultants|Engineering Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic compliance platforms cover IBC and ASCE 7 national standards but miss the thousands of local jurisdiction amendments that actually govern permit approval.
**Tags:** #bert #transformers #transfer-learning #feature-engineering #loss-functions #entropy-cross-entropy-kl-divergence #evaluation-metrics #compliance

## The Problem
Every engineering design must comply with building codes, but the applicable code is never just the International Building Code or ASCE 7 — it is the locally adopted version with jurisdiction-specific amendments covering seismic coefficients, wind speed maps, stormwater detention requirements, fire separation distances, and ADA pathway widths. A structural engineer designing a mixed-use building in Austin, TX operates under a different effective code than one doing the same work in Denver, CO, even though both nominally reference IBC 2021. Engineers currently check compliance by manually cross-referencing local amendment PDFs, municipal ordinances, and zoning overlays against their design calculations.

## What Already Exists
ICC's DigitalCodes provides searchable national code text, and tools like Autodesk's code checking features in Revit can verify certain geometric constraints against IBC. Some startups (UpCodes, Computertalk) offer searchable code databases with some jurisdiction coverage. These tools handle the base code reasonably well and can flag obvious violations like insufficient stair width or incorrect egress counts.

## The Customisation Gap
Local amendments are where permits get rejected. A city may have adopted IBC 2021 but with 47 local amendments that modify snow load factors, increase seismic importance factors for certain occupancy types, or impose stricter energy code requirements than the base IECC. These amendments are published as PDFs or municipal ordinance sections with inconsistent formatting and no structured data. The gap is extracting these jurisdiction-specific rules into machine-readable form and layering them on top of national code checks — especially for stormwater, which varies enormously by municipality and is rarely covered by any existing tool.

## Impact If Solved
Engineers save 4-8 hours per project on code research for unfamiliar jurisdictions and reduce the risk of permit rejection due to missed local amendments — a rejection that typically costs 2-4 weeks of schedule delay and $5K-$15K in redesign labor.
