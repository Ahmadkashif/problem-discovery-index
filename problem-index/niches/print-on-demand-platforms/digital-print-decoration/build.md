# A Screen Colour That Cannot Exist on Fabric

**Niche:** [[niches/print-on-demand-platforms/digital-print-decoration/profile|Digital Print Decoration]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A merchant picks a vivid colour on a screen, the achievable gamut on that fabric through that process does not contain it, and nobody tells anybody until the customer sees the result.
**Tags:** #numerical-methods #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #optimal-transport #automation #cnns
**Contested on:** Every serious competitor in this sub-niche is fighting to get a screen colour onto a specific fabric so that it survives washing and matches what the customer saw — and whoever does that keeps the margin, because colour and durability are what every complaint is about.

## The Problem
A design uses a saturated orange that looks correct on the merchant's display and in the mockup the platform generated. Printed direct-to-garment on a cotton blend it becomes a duller, browner orange, because the ink set and substrate cannot reach that saturation. The customer receives something noticeably different from the listing image and complains. The gamut limitation was knowable before printing — it is a property of the ink, the substrate and the process, measurable with a printed target and a spectrophotometer — and neither the merchant nor the platform checked, because nothing in the workflow holds a profile for that combination.

## Why Nobody Has Built This
Colour management requires profiles per device and substrate, and a distributed partner network with dozens of facilities and hundreds of garment options is a large profiling exercise nobody has undertaken. The mockup generator composites the artwork onto a product photograph, which makes the design look correct regardless of what the print can do. The complaint is attributed to expectations rather than to a measurable gamut limit. And the discipline that would fix it lives in commercial printing rather than in software engineering.

## What to Build
Characterise the combinations and check against them. Build and maintain device and substrate profiles across the network — printed targets measured per facility, per machine, per garment family — which is the investment that everything else here depends on and which no competitor has made. Check every artwork against the achievable gamut for its intended combination before printing, and report which colours cannot be reproduced and what they will become, which is a direct answer where a warning is not. Apply gamut mapping deliberately rather than letting the raster processor's default decide, since the default rendering intent frequently produces the worst available approximation and choosing it per artwork is a real improvement. Render the mockup through the profile so the listing image resembles the print, which is the single most effective way to align the customer's expectation with reality and is currently working against it. Monitor profile drift with periodic printed targets, since machines and ink lots move and a profile from a year ago is fiction. Report colour accuracy per facility, which makes the routing decision possible. Give merchants a palette of reliably reproducible colours for each product, which is a simple, popular and preventive product feature. And make the profile set a network asset rather than a facility one, since a new partner should inherit a characterisation approach rather than start from nothing.

## Target Customer
Digital print production operations, partner facilities, platform prepress engineering, and the merchants whose colours do not survive.

## Impact If Built
The gamut limit is measurable before printing and nothing in the workflow holds the profile that would reveal it. Rendering the mockup through the profile aligns the listing image with the print and is currently doing the opposite.
