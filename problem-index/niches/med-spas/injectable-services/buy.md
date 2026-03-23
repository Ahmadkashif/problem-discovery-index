# Med Spa PMS with Injectable-Specific Inventory Management

**Niche:** [[niches/med-spas/injectable-services/profile|Injectable Services (Botox/Fillers)]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Med spa practice management systems track product at the SKU level but cannot manage unit-level injectable inventory across vials, injectors, and patients.
**Tags:** #linear-regression #time-series-forecasting #tabular-ml #automation #data-integration

## The Problem
A vial of Botox contains 100 or 200 units. An injector uses 20-60 units per patient, meaning one vial serves 2-5 patients. Between patients, the remaining units must be tracked by vial, by injector, by time (reconstituted Botox expires within hours). Filler syringes are sometimes split across two facial zones in one patient or across two patients. Practice management systems track "purchased 10 vials of Botox this month" but not "Vial #7 has 40 units remaining, reconstituted at 10am, assigned to Dr. Smith." This gap causes product waste, inaccurate per-treatment cost tracking, and inventory shrinkage.

## What Already Exists
AestheticsPro, PatientNow, and Nextech handle appointment booking, before/after photos, and high-level inventory (SKU-level ordering and depletion). Allergan and Galderma provide manufacturer-level product tracking for loyalty programs. None track unit-level consumption per vial per treatment per injector.

## The Customization Gap
The PMS needs injectable-specific inventory layers: vial-level tracking with reconstitution timestamps, per-treatment unit deduction linked to patient charts, multi-injector vial sharing with usage attribution, expiration alerts for reconstituted product, and real-time profitability calculation per treatment based on actual product consumed (not average). This is fundamentally a granularity problem — moving from SKU-level to unit-level inventory.

## Target Customer
Med spa owners managing $10,000-50,000/month in injectable product spend who currently track consumption on spreadsheets or not at all.

## Impact If Solved
Reduces product waste by 8-12% ($800-6,000/month per practice), provides accurate per-treatment profitability data, and eliminates inventory discrepancies that indicate potential product diversion.
