# Parts Decision Optimization

**Industry:** [[auto-body-shops|Auto Body Shops]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Parts ordering tools can search catalogs, but they can't make the OEM-vs-aftermarket-vs-recycled decision for each part on each repair considering insurance guidelines, shop margin, quality risk, and availability.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #entropy-cross-entropy-kl-divergence #automation

## The Problem
Every collision repair requires dozens of parts decisions: OEM new, aftermarket new, recycled/salvage, or remanufactured. Each option has different cost, quality, warranty, availability, and insurance acceptance characteristics. Insurance companies push alternative parts to reduce claim costs; customers want OEM quality; shops want the option that arrives fastest with best margin. Parts managers make 50-100 of these decisions daily, often under time pressure and with incomplete information about availability.

## What Already Exists
CCC, PartsTrader, and OEM parts networks provide availability search and pricing. Some systems enforce insurer parts guidelines (e.g., "use aftermarket if available for vehicles > 5 years old"). None optimize across all dimensions simultaneously or learn from outcomes.

## The Customisation Gap
An intelligent parts decision system needs to: (1) apply insurer-specific parts guidelines automatically per claim, (2) predict actual delivery time based on supplier history not listed availability, (3) factor fit and quality risk by specific aftermarket manufacturer and part type, (4) calculate true margin impact including warranty claim risk, (5) optimize ordering across multiple repairs to consolidate shipments and hit volume tiers.

## Impact If Solved
Reduces parts-related cycle time delays by 1-2 days through better availability prediction. Improves parts margin 5-10% through optimized supplier selection. Decreases parts-related rework from aftermarket fit issues, which affect 8-12% of alternative parts installations.
