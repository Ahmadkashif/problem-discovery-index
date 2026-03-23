# Prior Notice Filing Errors & Rejections

**Niche:** [[niches/customs-brokers/fda-regulated-food-cosmetics/profile|FDA-Regulated Food & Cosmetics Importers]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** 10-15% of FDA Prior Notice submissions are rejected due to data entry errors — wrong FDA product code, incomplete manufacturer registration, or missing anticipated arrival information — causing 1-3 day delays while the prior notice is corrected and refiled.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
FDA Prior Notice requires: product code (FDA's proprietary product classification, not HTS), manufacturer name and registration number, country of production, anticipated arrival date and port, and product quantity. Prior Notice must be confirmed before the product can be released. Errors in any field trigger a rejection — the prior notice is returned to the filer for correction. Common errors: the manufacturer's FDA registration has lapsed (manufacturers must re-register biannually), the FDA product code doesn't match the product description, or the anticipated arrival port is wrong (the product code may restrict entry to certain ports). Each rejection adds 1-3 days to clearance while the broker corrects and refiles.

## Why It's Still Broken
Prior Notice data entry is manual: the broker enters the FDA product code (from a lookup), the manufacturer registration number (from a separate FDA database), and the arrival information (from the shipping schedule). Each lookup requires a separate database search. No entry preparation system pre-validates the prior notice fields against FDA databases before submission — the broker enters the data, submits, and discovers errors from the rejection notice.

## What a Fix Looks Like
A Prior Notice pre-validation system that: (1) verifies the manufacturer's FDA registration status is current before submission; (2) validates the FDA product code against the product description and HTS code; (3) checks port eligibility for the product type (some products are restricted to specific ports of entry); (4) verifies arrival date consistency with the vessel schedule; (5) flags all validation errors before submission, enabling correction before the prior notice is filed.

## Who Feels the Pain
Entry writers who file prior notices under time pressure (the vessel is arriving tomorrow) and discover rejections after submission — requiring correction under even greater time pressure.

## Impact If Fixed
Preventing 80% of prior notice rejections eliminates 1-3 day delays per affected entry. On 200 monthly FDA entries with a 12% rejection rate, preventing 19 rejections saves 19-57 days of cumulative delay — and the demurrage, storage, and perishable product degradation costs associated with each day.
