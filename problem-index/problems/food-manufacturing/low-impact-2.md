# Allergen Cross-Contact Risk Tracking Across Production Lines

**Industry:** [[food-manufacturing|Food Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** ERP and MES systems track which ingredients go into which products, but none of them model the cross-contact pathways through shared equipment, production sequencing, and sanitation effectiveness that determine whether a "may contain" allergen declaration is actually necessary — or whether inadequate changeover has created an undeclared allergen risk.
**Tags:** #bayesian-network #binary-classification #tabular-ml #compliance

## The Problem
Food manufacturers increasingly run multiple product lines with different allergen profiles on shared equipment. A bakery line that produces peanut butter cookies before switching to a nut-free product must execute a validated sanitation changeover and verify cleaning effectiveness — typically through visual inspection, ATP swabs, or allergen-specific protein swabs. The production scheduling decision of which products run in which sequence on which lines directly determines allergen cross-contact risk, changeover frequency, and sanitation cost. Current scheduling treats allergen changeovers as a constraint but doesn't quantify the risk — it's binary (changeover required or not) rather than probabilistic (what is the residual cross-contact probability given this equipment, this sanitation procedure, and this product sequence?).

## What Already Exists
ERP systems (SAP, Infor) track ingredient allergen declarations and BOM composition. MES platforms log production sequences and sanitation events. Allergen management modules in food safety software (SafetyChain, Alchemy) maintain allergen matrices — which products contain which allergens. Generic scheduling software optimizes for throughput and due dates. None of these systems model the physical cross-contact pathway: which equipment surfaces contact which products, what the sanitation effectiveness is for each allergen on each surface type, and how production sequence affects cumulative cross-contact probability.

## The Customisation Gap
An allergen cross-contact risk engine needs: (1) equipment-surface-to-product contact mapping — which surfaces in the production line contact the product stream, and which are shared across product changeovers; (2) sanitation effectiveness data — validated cleaning performance for each allergen on each surface type, expressed as a probability of adequate removal; (3) production sequence risk scoring — given a proposed schedule, what is the residual cross-contact probability for each product after its preceding changeover; (4) scheduling optimization that sequences products to minimize total changeover cost while keeping cross-contact risk below the plant's acceptable threshold. This physical and probabilistic modeling layer is what generic ERP/MES cannot provide.

## Impact If Solved
Reduces precautionary allergen labeling ("may contain") by identifying which product sequences genuinely require it vs. which have negligible cross-contact risk after validated sanitation — expanding the addressable market for products that can be labeled allergen-free. Prevents undeclared allergen incidents that trigger FDA recalls (average recall cost $10M+). Optimizes production scheduling to reduce unnecessary changeovers, saving 1-3 hours of sanitation time per line per week.
