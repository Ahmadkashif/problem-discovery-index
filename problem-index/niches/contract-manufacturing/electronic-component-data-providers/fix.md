# Every Field Is Presented as Verified, Whatever Its Source

**Niche:** [[niches/contract-manufacturing/electronic-component-data-providers/profile|Electronic Component Data Providers]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** A compliance declaration obtained directly from the manufacturer and one inferred from a similar part appear in the same record in the same format, and the engineer designing against it cannot tell which is which.
**Tags:** #data-integration #confidence-intervals #probability-distributions #evaluation-metrics #descriptive-statistics #compliance #feature-engineering #worker-facing #survival-analysis #revenue-impact

## The Problem
A component record assembles fields from very different sources: values extracted from the current datasheet, values carried forward from a prior revision, compliance declarations obtained directly from the manufacturer, declarations inferred from a part family, lifecycle status from an announcement, and lifecycle status estimated by model. The interface presents them identically. That matters most exactly where the stakes are highest — a regulatory compliance declaration that was inferred rather than obtained is the difference between a shipment clearing customs and a shipment stopped, and an engineer approving a part has no way to see which they are relying on. The provider knows the provenance of every field; it is in the ingestion record and it is not surfaced, because the product was built to look authoritative and complete.

## Why It's Still Broken
Completeness has been the competitive dimension in this segment for two decades — coverage counts are what appear in sales comparisons — and any visible gap reads as a weakness rather than as honesty. Provenance is also captured for internal traceability in a form that means nothing to a subscriber without translation. And no customer has asked, because none has seen a product that offered it and none knows how much of the record is inferred.

## What a Fix Looks Like
Provenance and confidence surfaced per field: obtained from the manufacturer, extracted from a current datasheet, carried forward from a prior revision, or inferred, with the date and, where inferred, the basis. Presented as a simple consistent signal an engineer can read in seconds, with detail on demand. Compliance fields deserve the strongest treatment, because the consequence of relying on an inferred declaration is a stopped shipment and a supplier corrective action, and that is a distinction the subscriber must be able to see. Downstream, exports and API responses carry provenance with them rather than laundering inferred values into an authoritative-looking table in a customer's own system. Internally the same surfacing turns inference rate into an operational metric that content investment can be managed against, which is what makes it compound rather than being a single disclosure.

## Who Feels the Pain
Design engineers approving parts on fields they assume were verified; compliance teams whose declarations rest on inferences they cannot see; contract manufacturers whose shipments stop over a component that was declared compliant on a family assumption; and the provider, whose reputation absorbs a failure the subscriber was given no way to anticipate.

## Impact If Fixed
Converts the product's largest unstated risk into a differentiator, using data already held. In a market converging on coverage, showing the basis of the record is a stronger position than showing the largest count — and it directly addresses the failure mode that costs subscribers the most money.
