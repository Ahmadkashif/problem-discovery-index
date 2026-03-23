# ML-Assisted HTS Classification with Ruling Citation

**Niche:** [[niches/customs-brokers/hts-classification-workflow/profile|HTS Classification Workflow]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system takes a plain-language product description, predicts the most likely HTS classification candidates with confidence scores, and surfaces the specific CBP CROSS rulings that support each candidate — converting classification from a 15-45 minute manual research task into a 2-3 minute review-and-confirm workflow.
**Tags:** #bert #transformers #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
An experienced classification analyst reads a product description ("rechargeable lithium-ion battery pack for portable power tools, 18V, 4.0Ah, with integrated charge indicator") and rapidly navigates to the correct HTS classification — drawing on years of experience with similar products, knowledge of CBP's interpretation of "battery pack" vs. "accumulator" vs. "power tool part," and awareness of relevant CROSS rulings. This expertise is deeply tacit: the analyst can't articulate the full decision tree they followed, and their classification may differ from another analyst's on ambiguous products. A junior analyst classifying the same product takes 30-45 minutes of research and may arrive at a different (and possibly incorrect) code.

## Why Nobody Has Built This
HTS classification is a hierarchical multi-class classification problem with 17,000+ classes, where the correct class depends on nuanced product characteristics (material composition, intended use, essential character) that are expressed inconsistently in product descriptions. Training a model requires: (1) labeled examples (product description → correct HTS code) in sufficient volume across the HTS hierarchy; (2) incorporation of GRI (General Rules of Interpretation) logic that determines classification when multiple headings seem applicable; (3) integration with CROSS rulings that serve as precedent for ambiguous classifications.

## What to Build
A classification assistant that: (1) takes a product description as input; (2) predicts the top-3 HTS code candidates with confidence scores using a transformer model trained on CROSS rulings and historical entry data; (3) surfaces the specific CROSS rulings supporting each candidate; (4) shows the GRI analysis path for the top candidate; (5) presents the duty rate and tariff program implications for each candidate; (6) allows the analyst to confirm, override, or research further. The system learns from analyst confirmations and overrides.

## Target Customer
Classification team leads at customs brokerages handling 50+ novel product classifications per month. Approximately 500 brokerages have dedicated classification teams. Average contract value: $18-36K/year.

## Impact If Built
Reducing average classification time from 20 minutes to 5 minutes for the 70% of products that fall into clear categories recovers 10+ analyst-hours weekly on a team handling 200 classifications/month. Classification consistency improves — reducing the CBP audit risk from analyst-to-analyst variation.
