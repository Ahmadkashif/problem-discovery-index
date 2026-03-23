# USMCA Certificate of Origin Management for Maquiladora Products

**Niche:** [[niches/customs-brokers/cross-border-maquiladora/profile|Cross-Border Maquiladora Operations]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Trade compliance platforms (Amber Road, Descartes) manage USMCA certificates of origin, but they don't model the maquiladora-specific scenario where US-origin components are shipped to Mexico, assembled into a finished product, and re-imported — requiring a product-specific regional value content (RVC) calculation that traces US-origin value through the Mexican assembly process.
**Tags:** #automation #compliance #data-integration #revenue-impact

## The Problem
A finished product assembled in a Mexican maquiladora from US and non-US components may qualify for USMCA duty-free treatment on re-import to the US — but only if it meets the specific rule of origin for that product (tariff shift, regional value content threshold, or both). Calculating the regional value content (RVC) requires: summing the US-origin material value, adding the Mexican manufacturing cost, comparing to the transaction value, and determining if the RVC threshold (typically 75% for USMCA) is met. This calculation changes every time material sourcing changes (a component previously sourced from the US is now sourced from China — the RVC drops). No automated system recalculates RVC when sourcing changes.

## What Already Exists
Amber Road and Descartes provide USMCA certification management for standard import/export transactions. SAP GTS handles USMCA for large enterprises. These tools manage certificate generation but don't automate the maquiladora-specific RVC calculation that requires tracing component-level origin through the assembly bill of materials.

## The Customization Gap
A maquiladora USMCA tool needs: (1) bill-of-materials integration showing each component's country of origin and value; (2) automatic RVC calculation for each finished product based on current component sourcing; (3) "what if" analysis when sourcing changes ("if we switch this component from US to China, does the product still qualify for USMCA?"); (4) certificate of origin generation with the calculated RVC and tariff shift analysis pre-populated.

## Target Customer
Trade compliance managers at maquiladora operations re-importing assembled products to the US under USMCA preference.

## Impact If Solved
Maintaining USMCA qualification saves 5-25% in duty rates on re-imported products. On $10M in annual re-imports, this is $500K-$2.5M in duty savings. Automated RVC calculation ensures the claim is defensible if CBP audits the certificate of origin.
