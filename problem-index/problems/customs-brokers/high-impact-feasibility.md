# Feasibility — HTS Classification Prediction from Product Descriptions

**Industry:** [[customs-brokers|Customs Brokers]]
**Problem:** [[problems/customs-brokers/high-impact|HTS Classification Prediction from Product Descriptions]]
**Problem type:** High Impact

**Problem summary:** Licensed customs brokers who classify imported products by reading the product description and cross-referencing the Harmonized Tariff Schedule hierarchy — a classification judgment that takes 5-20 minutes per novel product and can be disputed by CBP — get an ML model that predicts the most likely HTS codes from the product description, reducing classification time and providing a defensible starting point for review.

## Solution Approach
Stand up a focused pilot that ingests the HTS schedule, CROSS/classification rulings, and a broker's prior classifications to train an assistive classifier, then embed it in the broker's CMS/entry workflow with required human review and audit trails. Start with a narrow product family, track disagreement rates and CBP challenges, and expand coverage as confidence grows.

## Open Source Data
The HTS schedule, CROSS rulings, and trade agreement texts are public; real performance comes from each broker's historical product descriptions, chosen codes, and CBP responses, which are proprietary.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
