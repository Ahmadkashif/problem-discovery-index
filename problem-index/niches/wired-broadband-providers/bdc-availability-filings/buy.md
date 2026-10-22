# Address Matching Tools Adapted to the Fabric

**Niche:** [[niches/wired-broadband-providers/bdc-availability-filings/profile|Broadband Data Collection & Availability Filings]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Address validation and geocoding are mature commodities; matching an operator's records to Fabric location IDs needs rules those tools don't carry.
**Tags:** #k-nearest-neighbors #large-language-models #feature-engineering #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a semiannual availability filing reconciled to the current Fabric that survives the challenge process, and whoever delivers it with the fewest engineer-hours and the fewest sustained challenges takes the account.

## The Problem
Operators geocode billing addresses and passings with a commercial service and then spend days hand-matching the residue to Fabric points.

## What Already Exists
Address validation and geocoding services (USPS-certified CASS tools, Esri and commercial geocoders, Smarty, Melissa) and entity-resolution software used in marketing and logistics.

## The Customization Gap
The Fabric needs: matching to Fabric location IDs rather than postal addresses, including rural points with no street address; unit counts for multi-unit buildings; handling of locations the Fabric misses (which become Fabric challenges); version diffs as the Fabric is revised every six months; and outputs in BDC file format with technology and speed per location.

## Target Customer
Filing teams at operators and consultancies that already license a geocoder.

## Impact If Solved
Days of manual matching shrink to an exception review, every cycle.
