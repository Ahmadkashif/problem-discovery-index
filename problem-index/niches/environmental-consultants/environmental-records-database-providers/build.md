# Geocoding Confidence as a Reported Property of Every Record

**Niche:** [[niches/environmental-consultants/environmental-records-database-providers/profile|Environmental Records Database Providers]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The entire product is a radius search, every radius search depends on where each record was placed on the map, and agency records arrive with addresses that are wrong, partial, or describe a facility rather than a location.
**Tags:** #probability-distributions #confidence-intervals #bayesian-inference #random-forests #evaluation-metrics #hypothesis-testing #feature-engineering #cnns #data-integration #compliance

## The Problem
A Phase I report says a leaking tank site lies four hundred feet from the subject property, and that statement rests entirely on geocoding a record whose source address may be a mailing address, a post office box, a highway crossroads description, or a typo. Geocoding quality therefore determines whether a report includes a record that matters or excludes one that does — the two failure modes that end in professional liability. The provider knows internally that placement confidence varies enormously by record type, agency, and vintage, and the report presents every mapped record identically. The consultant reading it has no way to distinguish a rooftop-accurate placement from one interpolated to a street centroid half a mile long.

## Why Nobody Has Built This
The product's authority comes from looking definitive, and a report annotated with uncertainty invites the question of what the consultant should do about it. Measuring placement accuracy also requires ground truth, which for historical records frequently no longer exists — the facility is gone and the address never resolved cleanly. The tractable route is a modelled confidence rather than a measured error, estimated from source characteristics, address completeness, and agreement between independent geocoding paths, which is real work with no obvious owner in an operation organized around throughput.

## What to Build
Placement confidence as a modelled, reported property of every record. Confidence is estimated from the address form supplied, the geocoding method that resolved it, agreement between independent resolution paths, and the historical accuracy observed for that agency and record type where verification exists. Records whose placement is uncertain enough to change the radius conclusion are flagged rather than silently included or excluded — which is the specific decision a consultant needs help with and currently makes blind. Historical imagery and directory holdings, which the provider already owns, become a verification input rather than a separate product: a record whose modelled location is inconsistent with what the imagery shows at that address is a candidate for review. And the same model directs the research operation at the records where better placement most changes report outcomes, rather than at whatever the intake queue produced.

## Target Customer
Chief data officers and heads of content at environmental records providers running 200-800 researchers, and the environmental professionals whose liability rests on whether a nearby record was correctly placed.

## Impact If Built
Addresses the exact point where the product's failure becomes someone's professional liability, using signal the provider already holds. Reported confidence also differentiates in a segment where competitors sell the same underlying agency records and compete on comprehensiveness claims neither can substantiate.
