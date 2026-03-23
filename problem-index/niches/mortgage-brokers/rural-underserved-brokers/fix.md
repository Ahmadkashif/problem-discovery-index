# USDA Eligibility & Income Limit Verification Friction

**Niche:** [[niches/mortgage-brokers/rural-underserved-brokers/profile|Rural & Underserved Market Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Brokers manually check USDA property eligibility and household income limits on two separate government websites — a clunky process that causes pre-qualification errors and lost deals.
**Tags:** #automation #data-integration #compliance #worker-facing

## The Problem
USDA Rural Development loans require both property eligibility (the address must be in a USDA-eligible area) and household income eligibility (total household income must be below 115% of area median income, adjusted for household size). Brokers check property eligibility on the USDA's GIS mapping tool and income limits on a separate lookup — neither integrates with the LOS. When USDA updates its eligibility maps (annually) or income limits (annually), brokers who rely on cached knowledge pre-qualify borrowers for properties or income levels that no longer qualify, leading to deal failures discovered weeks into the process.

## Why It's Still Broken
USDA's tools are functional but designed for occasional use by consumers, not for brokers who check 5-15 properties per week. The GIS tool is slow, doesn't batch-check addresses, and requires manual pin-drop verification for properties on eligibility boundaries. Income limit tables are published as PDFs organized by state and county. No LOS vendor has prioritized USDA integration because USDA loans represent only ~5% of overall origination — but for rural brokers, they're 30-60% of business.

## What a Fix Looks Like
An API-driven lookup that takes an address and household profile (size, income) and returns instant USDA eligibility confirmation — both property and income — with alerts when upcoming map or income limit changes would affect pending deals. Integrates with the broker's LOS via webhook or direct plugin so that pre-qualification letters automatically reflect verified USDA eligibility.

## Who Feels the Pain
Rural brokers who process 3-8 USDA loans per month and spend 15-20 minutes per scenario manually checking eligibility, plus the borrowers who get pre-qualified only to discover weeks later that the property isn't in an eligible zone.

## Impact If Fixed
Eliminates USDA eligibility errors that cause an estimated 10-15% of rural deal failures. Saves 15-20 minutes per eligibility check. Enables same-call pre-qualification for USDA scenarios, matching the speed that conventional borrowers expect.
