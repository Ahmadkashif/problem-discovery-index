# Classification Decision Audit Trail & Quality Review

**Niche:** [[niches/customs-brokers/hts-classification-workflow/profile|HTS Classification Workflow]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Customs entry systems store the HTS code used for each entry, but they don't document the classification reasoning — why the analyst chose this code over alternatives — which is the critical evidence needed when CBP challenges a classification or during an informed compliance review.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
When CBP challenges an HTS classification ("we believe this product should be classified under 8471, not 8473"), the broker must defend their classification by explaining the analytical reasoning: which GRI applied, which CROSS rulings supported the decision, and why alternative classifications were rejected. This reasoning exists only in the analyst's memory — it was never documented at the time of classification. Reconstructing the classification rationale 6 months or 2 years after the fact (CBP's audit window extends 5 years) is unreliable and time-consuming (4-8 hours per challenged classification).

## What Already Exists
Entry management systems store the HTS code, product description, and entry details. Descartes CustomsInfo provides HTS lookup and ruling search. No system captures the classification decision process: which alternative codes were considered, which GRI was applied, which CROSS rulings were reviewed, and why the final code was selected.

## The Customization Gap
A classification audit trail needs: (1) a decision documentation workflow embedded in the classification process (the analyst notes their reasoning as they classify, not after); (2) fields for alternative codes considered and reasons for rejection; (3) links to the CROSS rulings and GRI sections relied upon; (4) a quality review workflow where a senior analyst can review and approve classifications with high compliance risk (high value, ambiguous products, products subject to ADD/CVD); (5) searchable archive for prior classification decisions on the same or similar products.

## Target Customer
Compliance managers at customs brokerages who need defensible classification documentation for CBP audits and informed compliance reviews.

## Impact If Solved
Defensible classification documentation reduces CBP challenge success rate by providing contemporaneous reasoning that supports the classification. Each successfully defended challenge avoids $10K-$500K in retroactive duty assessment. Audit trail documentation also satisfies reasonable care requirements under 19 USC 1484, reducing negligence penalties.
