# Cross-Manufacturer Equipment Comparison

**Niche:** [[niches/medical-supply-retail/mobility-wheelchair-dealers/profile|Mobility & Wheelchair Dealers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Wheelchair manufacturers each have their own configuration tools, but no tool allows an ATP to compare equivalent configurations across manufacturers — making it impossible to optimize for price, weight, features, and patient fit simultaneously.
**Tags:** #recommendation #data-integration #tabular-ml #revenue-impact

## The Problem
After an assessment, an ATP needs to compare: the Permobil M3 Corpus vs. the Sunrise Medical Q700-UP vs. the Pride Mobility Quantum Q6 Edge 3, each configured to the patient's specifications. Each manufacturer has its own configuration tool with proprietary naming for equivalent features ("Corpus seating" vs. "MPS push-button recline" vs. "Q-Logic EX controller"). Comparing features, weights, dimensions, and pricing across manufacturers requires opening 3 separate configuration tools, translating between naming conventions, and manually building a comparison spreadsheet. Most ATPs default to their familiar brand rather than finding the optimal product for each patient.

## What Already Exists
Permobil MyPermobil, Sunrise Medical's configurator, and Pride's Q-Logic configurator each handle product-specific configuration. HCPCS code references map products to billing codes but don't enable feature comparison. Manufacturer catalogs provide specifications but not side-by-side comparison.

## The Customization Gap
The missing tool is a cross-manufacturer configuration comparator: given a patient's clinical requirements (seat width, weight capacity, tilt angle, drive configuration, cushion type), show all qualifying configurations across manufacturers with side-by-side comparison of weight, dimensions, features, HCPCS coding, and supplier cost. The comparison must normalize manufacturer-specific terminology into standard clinical terms (e.g., "power tilt" regardless of what each manufacturer calls it). Must also show insurance implications: which configurations are covered under the patient's specific plan, and which require patient co-pay upgrades.

## Target Customer
ATPs who currently default to 1-2 familiar manufacturers and want to make evidence-based equipment selections across the full market.

## Impact If Solved
Enables ATPs to select the optimal equipment for each patient rather than their habitual brand, improving patient satisfaction and reducing returns. Identifies cost savings of $500-2,000 per configuration when a less expensive manufacturer offers an equivalent product. Opens competition among manufacturers, potentially reducing supplier costs by 5-10% through informed purchasing.
