# Cross-Border Maquiladora Operations

**Parent Industry:** [[industries/customs-brokers|Customs Brokers]]
**Category:** Low Digitized

## Profile
**Market Size:** $300-500M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Low-Medium — maquiladora import/export operations involve dual-country documentation (US and Mexico), temporary import tracking under IMMEX, and duty-free material reconciliation managed in spreadsheets and legacy systems
**Target Buyer:** Maquila compliance coordinator or production import manager at manufacturers operating IMMEX programs in Mexico
**Automation Potential:** Medium — IMMEX inventory reconciliation, temporary import tracking, and USMCA certificate of origin management follow deterministic rules but span two regulatory systems

## What Makes This a Distinct Niche
Maquiladora operations involve US manufacturers shipping raw materials, components, or semi-finished goods to Mexican assembly plants under the IMMEX (Maquiladora, Manufacturing, and Export Services) program. Materials enter Mexico duty-free as temporary imports, are assembled into finished products, and re-exported to the US. The customs complexity is in two layers: (1) Mexico-side IMMEX compliance — tracking temporary imports, proving they were used in manufacturing and re-exported within the required timeframe, and reconciling the material-to-product conversion; (2) US-side re-import — claiming USMCA duty preference on the finished goods, documenting the US-origin content, and navigating the tariff classification of the assembled product (which may differ from the classification of its components). The broker must manage both countries' customs requirements for a single production flow.

## Current Tools & Gaps
SAP and Oracle manage some IMMEX inventory tracking for large manufacturers. US customs entry is filed through ACE. Mexican customs entry is filed through VUCEM. No integrated platform manages the full maquiladora customs lifecycle: US export → Mexico temporary import → IMMEX tracking → Mexico re-export → US import with USMCA preference.

## Problems
- [[niches/customs-brokers/cross-border-maquiladora/build|🔨 Build: IMMEX Temporary Import Reconciliation Platform]]
- [[niches/customs-brokers/cross-border-maquiladora/buy|🛒 Buy: USMCA Certificate of Origin Management for Maquiladora Products]]
- [[niches/customs-brokers/cross-border-maquiladora/fix|🔧 Fix: Material-to-Product Conversion Documentation]]
