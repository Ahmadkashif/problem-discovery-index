# HTS Classification Prediction from Product Descriptions

**Industry:** [[customs-brokers|Customs Brokers]]
**Type:** High Impact
**One-liner:** Licensed customs brokers who classify imported products by reading the product description and cross-referencing the Harmonized Tariff Schedule hierarchy — a classification judgment that takes 5-20 minutes per novel product and can be disputed by CBP — get an ML model that predicts the most likely HTS codes from the product description, reducing classification time and providing a defensible starting point for review.
**Tags:** #transformer #bert #text-classification #nlp #compliance #revenue-impact

## The Problem

HTS (Harmonized Tariff Schedule) classification assigns each imported good a 10-digit code that determines its duty rate, any special tariff applicability (Section 301/232), and quota or licensing requirements. The US HTS has approximately 17,000 10-digit classifications organized in a hierarchical structure of sections, chapters, headings, and subheadings.

Classifying a new product requires: (1) reading the product description and identifying the essential character and primary use; (2) navigating the GRI (General Rules of Interpretation) hierarchy to find the most specific applicable classification; (3) checking CBP rulings database for prior binding rulings on similar products. An experienced customs broker classifies familiar product types in minutes; a novel product (a new electronic component, a new chemical formulation) requires 15-45 minutes of research.

The accuracy stakes are high: a classification error on a high-volume import can result in hundreds of thousands of dollars in retroactive duty liability if CBP audits and rejects the classification.

## Why It's High Impact

HTS classification is the core of customs brokerage — the professional judgment that justifies the licensed broker's role. A model that predicts the most likely HTS codes (with confidence scores and alternative candidate codes) reduces the time for routine classifications from 10-15 minutes to 2-3 minutes of review. For a broker handling 50 entries per day, this recovers significant daily capacity.

More importantly, an accurate classification model reduces the misclassification rate — the primary compliance risk in customs. A 1% misclassification rate on a $10M/year import program creates $50,000-$200,000 in potential duty exposure.

## What a Solution Looks Like

A broker workstation integration where the customs broker enters the product description and the model returns: the top-3 HTS code candidates with confidence scores and a rationale for each; a summary of the GRI analysis supporting the top recommendation; any relevant CBP prior rulings for similar products; the applicable duty rate and any tariff program applicability (USMCA, Section 301 list) for each candidate code. The broker reviews the recommendation, applies their judgment on the final code, and files.

## Implementation Path

CBP's CROSS (Customs Rulings Online Search System) database contains 60,000+ binding classification rulings with product descriptions and assigned HTS codes — a labeled training corpus. A fine-tuned transformer (BERT or RoBERTa) on ruling text → HTS code classification: 3-4 month development. ACE integration is the deployment channel. Descartes CustomsInfo or Amber Road is the natural distribution partner.
