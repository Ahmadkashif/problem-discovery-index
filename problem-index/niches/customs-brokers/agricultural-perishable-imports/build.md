# USDA Admissibility Pre-Verification Engine

**Niche:** [[niches/customs-brokers/agricultural-perishable-imports/profile|Agricultural & Perishable Imports]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool pre-verifies USDA admissibility for a specific product from a specific country before the shipment leaves origin — catching inadmissible combinations (product X from country Y is not permitted) before the container is loaded, rather than discovering it at the US port when the shipment is refused entry.
**Tags:** #large-language-models #automation #compliance #revenue-impact

## The Problem
USDA/APHIS maintains a complex admissibility matrix: each agricultural product's import eligibility depends on the country of origin, the specific region within the country, the treatment applied (cold treatment, fumigation, irradiation), and the product variety. A broker's client wants to import mangoes from a new supplier in India. The broker must check: are Indian mangoes admissible? (Yes, but only from approved facilities, only irradiated, only certain varieties.) This admissibility check requires searching APHIS's FAVIR (Fruits and Vegetables Import Requirements) database, which is organized by country and product but not searchable in a way that provides a definitive yes/no with conditions for a specific product-country-treatment combination.

## Why Nobody Has Built This
USDA admissibility rules are maintained across multiple databases (FAVIR, PCIT — Phytosanitary Certificate Issuance and Tracking), regulatory notices (Federal Register), and bilateral agreements (pest-specific import protocols with individual countries). No single structured database contains the complete admissibility matrix with all conditions. Building a comprehensive pre-verification engine requires: (1) consolidating rules from multiple sources; (2) maintaining currency as rules change frequently (new pests, new bilateral agreements, new treatment protocols); (3) resolving ambiguities where rules conflict or overlap.

## What to Build
An admissibility verification tool that: (1) accepts product, country of origin, region, and treatment method as inputs; (2) returns a definitive admissibility status (admissible with conditions, admissible unconditionally, or inadmissible) with the regulatory basis cited; (3) lists all required documents (phytosanitary certificate, treatment certificate, import permit) for admissible products; (4) alerts when admissibility rules change for products in the broker's active portfolio.

## Target Customer
Perishable import customs brokers and agricultural import compliance teams who currently spend 30-60 minutes per product researching admissibility through FAVIR and APHIS publications. Approximately 500-800 brokerages specialize in agricultural imports.

## Impact If Built
Preventing a single inadmissible shipment from being loaded saves $15K-$100K in container shipping costs, product loss, and port storage fees. Reducing admissibility research time from 30-60 minutes to 2-3 minutes per product recovers significant broker capacity.
