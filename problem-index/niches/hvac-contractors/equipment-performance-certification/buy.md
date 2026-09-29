# A Product Catalogue That Turns Over on a Statutory Date

**Niche:** [[niches/hvac-contractors/equipment-performance-certification/profile|HVAC Equipment Performance Certification]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product data management assumes products change when a manufacturer decides to; here a federal rule invalidates thousands at once on a known date.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #ocr

## The Problem
The certification directory holds hundreds of thousands of matched system combinations — an outdoor unit paired with a specific coil and air handler, each pairing separately rated. Manufacturers submit continuously, models supersede one another, and combinations enter and leave.

Then a minimum efficiency standard changes, or a refrigerant is phased down, and a large fraction of the catalogue becomes non-compliant on a single date. Every affected combination has to be identified, transitioned, or retired, and replacements have to be certified and published before contractors need them — because on the effective date a contractor pulling a permit needs the new combination in the directory or the job does not happen.

Managing that is a scramble of spreadsheets, manufacturer correspondence, and manual reconciliation, on a deadline nobody controls.

## What Already Exists
Product information management platforms — Informatica, Akeneo, Salsify, Stibo — handle large catalogues, complex attributes, versioning, and syndication competently. Certification and compliance management systems exist in adjacent industries.

## The Customization Gap
Every generic platform models a product's lifecycle as a manufacturer's decision. Here the lifecycle is set by regulation.

**Regulatory effective dates as the primary lifecycle driver.** Compliance status is a function of the product's rating, the jurisdiction, and the date — a single combination can be compliant in one region and not another on the same day, which is exactly what the last standard change created. No PIM has a concept of a product whose validity varies by geography and time under an external rule.

**The certified unit is a combination, not a product.** A rating belongs to a specific pairing of components, and one outdoor unit may appear in thousands of certified combinations. When it is superseded, every combination containing it is affected. This is a graph problem, and PIM data models are hierarchical.

**Transition planning as a first-class workflow.** Ahead of a standard change the programme needs to know which combinations lapse, which manufacturers have replacements in the pipeline, and where coverage gaps will leave contractors without a compliant option. That is a forecast over the catalogue, and it is currently assembled by hand under time pressure.

**Submission validation against physics and precedent.** Ratings must be checked for internal consistency and against comparable equipment before publication, because a wrong number in the directory propagates into permits and rebate claims immediately. Generic attribute validation checks types and ranges, not whether a claimed efficiency is plausible for that configuration.

**The directory is a downstream dependency.** Code officials, rebate programmes, and contractor software all consume it, so publication is not an internal state change — it is a public event with permitting consequences, and it needs the change control to match.

## Target Customer
Chief Technology Officer or VP of Certification Operations at the certification body, where each regulatory transition is currently absorbed as a manual surge.

## Impact If Solved
Standard transitions are the programme's hardest recurring event and they are becoming more frequent. Handling them as a modelled catalogue lifecycle rather than a scramble means contractors have compliant combinations available on day one — which is the difference between a transition the industry absorbs and one that stalls installations for a season.
