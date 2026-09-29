# Manufacturer Model Databases Wired Into the Record

**Niche:** [[niches/field-service-software/equipment-asset-history/profile|Equipment Asset History]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturers publish specifications, parts breakdowns, service bulletins and warranty terms for every model they sell, and a technician standing in front of one of those models looks it up on a phone browser.
**Tags:** #bert #word-embeddings #large-language-models #k-nearest-neighbors #evaluation-metrics #data-integration #automation #compliance
**Contested on:** Every serious competitor in field service is fighting to populate an equipment record completely without costing the technician a minute — and whoever gets record completeness per visit highest takes the capability everything else in the category depends on.

## The Problem
A model number is captured. It is a string. The platform knows nothing about what it refers to: not the capacity, the refrigerant, the parts that fit it, the service bulletins issued against it, the warranty term, or the common failure modes. All of that is published by the manufacturer and available on the open web, and the technician retrieves it by searching on a phone while standing on a ladder, if at all.

## What Already Exists
Manufacturer product documentation, specification sheets, parts breakdowns and service bulletins are published and largely public. Distributor catalogues carry structured product data. Several commercial product data services aggregate across manufacturers in adjacent industries. Text extraction from technical documentation is commodity. Entity matching from an observed model string to a catalogue entry is the same well-developed problem that appears throughout this vault.

## The Customization Gap
The adaptation is in the matching and in the delivery. It requires: (1) robust matching from a captured model string — which is frequently partial, mis-read, or a variant with suffixes denoting configuration — to a canonical model, with confidence and with the near-misses shown rather than a silent wrong match; (2) serial number decoding per manufacturer to derive manufacture date, which is conventional knowledge held informally in the trades and is one of the highest-value derived fields available; (3) service bulletin and recall matching against the specific serial range, which is a safety matter and is currently dependent on a technician happening to know; (4) parts compatibility surfaced at the point of dispatch so the right part is on the truck, which connects this directly to first-time fix; and (5) maintaining the catalogue as manufacturers release and supersede models, which is a content operation and should be run as one rather than as a one-time scrape.

## Target Customer
Field service platform vendors, distributors who would benefit from their catalogue being present at the point of service, and contractors whose technicians currently search the web on a ladder.

## Impact If Solved
Enrichment converts a captured model number from a string into everything the technician and the dispatcher need, which multiplies the value of the capture the build note makes free. Service bulletin and recall matching against serial ranges is the highest-stakes element and is currently left to individual knowledge, which is not a system at all.
