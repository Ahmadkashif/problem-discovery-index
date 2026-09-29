# Every Field Is Presented as Equally Current

**Niche:** [[niches/commercial-real-estate/cre-property-data-research/profile|Commercial Property Data & Research Platforms]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Fix (Pain Point)
**One-liner:** A rent verified this week and a rent last confirmed in 2021 appear in the same record in the same font, and the subscriber underwriting a deal cannot tell which is which.
**Tags:** #data-integration #descriptive-statistics #confidence-intervals #evaluation-metrics #survival-analysis #probability-distributions #worker-facing #compliance #workflow-orchestration #revenue-impact

## The Problem
A property record is an assembly of facts established at different times by different means with different confidence, and it is displayed as a flat set of values. Some were verified last week by phone with the landlord; some were inferred from a listing; some were carried forward from a research pass four years ago because nothing prompted a recheck. The subscriber sees identical presentation. When a broker builds a comparable set for a valuation, or a lender underwrites against reported rents, they are combining facts of radically different quality with no way to weight them. The company knows the provenance of every field — it is in the audit trail — and does not surface it, because the product was designed to look authoritative.

## Why It's Still Broken
Definitiveness has been the product's positioning since it was a printed directory, and there is a long-standing view that exposing age and method would invite subscribers to discount the data. The audit trail also exists for internal quality management rather than for display, so provenance is captured in a form that is complete but not presentable — method codes, researcher identifiers, and timestamps that mean nothing to a subscriber without translation. And no subscriber has demanded it, because they have never seen a product that offered it and do not know the variation is as large as it is.

## What a Fix Looks Like
Provenance as a visible property of every field: when it was last established, by what method, from what kind of source, and with what corroboration. Presented in a form a working broker can act on in seconds rather than as a metadata panel — a simple, consistent signal of established versus indicative versus stale, with the detail available on demand. Downstream tooling then inherits it: a comparable set built inside the platform can weight or exclude weakly evidenced facts, and an export carries the provenance with it rather than laundering it into a clean spreadsheet. For the company, the same surfacing turns staleness from an invisible internal problem into a visible operational metric that verification allocation can be managed against — which is what makes the improvement compound rather than being a one-time disclosure.

## Who Feels the Pain
Brokers building comparable sets from facts of unknown vintage; appraisers and lenders underwriting against reported rents with no idea which were confirmed; researchers whose careful verification is presented identically to a four-year-old inference; and the platform, whose reputation depends on data quality it currently asks subscribers to take entirely on faith.

## Impact If Fixed
Turns the product's biggest unstated weakness into a differentiator, and does it with data the company already holds. In a market where subscribers increasingly compare sources, being the platform that shows its work is a stronger position than being the one that looks most confident — and provenance display makes verification investment visible to the customer for the first time, which is the argument for the price.
