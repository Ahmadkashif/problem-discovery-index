# Multi-SKU Visual Quality Inspection with Per-Product Calibration

**Niche:** [[niches/food-manufacturing/large-cpg-plants/profile|Large CPG Plants]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No vision inspection system handles the multi-SKU reality of a CPG plant — where 50-200 different products run on the same lines with different visual acceptance criteria, and the inspection model must switch profiles at every changeover without data science intervention.
**Tags:** #cnns #transfer-learning #evaluation-metrics #tacit-knowledge-ml #revenue-impact

## The Problem
A large CPG plant runs 50-200 SKUs across its production lines, with changeovers happening multiple times per day. Each SKU has a different visual acceptance standard: acceptable color range for a chocolate bar differs from a granola bar; fill level tolerance for a soup can differs from a yogurt cup; surface texture standards for a cracker differ from a cookie. Current vision systems (Cognex, Keyence) can be programmed per-SKU, but each program requires hours of engineering setup and calibration — impractical for a plant running 200 SKUs with frequent changeovers. QA inspectors handle this flexibility effortlessly (they know what "good" looks like for each product from experience), but inspectors fatigue, take breaks, and have shift changes that create quality gaps.

## Why Nobody Has Built This
Building a multi-SKU inspection system requires: (1) per-SKU model profiles trained from inspector-labeled images for each product, (2) a changeover interface that an operator (not a data scientist) can use to switch profiles in under 30 seconds, and (3) continuous learning that adapts to seasonal ingredient variation (the acceptable color of a cracker changes slightly when flour suppliers change between crop years). The training data requirement — thousands of labeled images per SKU per defect type — is prohibitive at the SKU count of a large CPG plant. Few-shot learning and foundation models that reduce the per-SKU data requirement are now technically feasible but have not been productized for food manufacturing.

## What to Build
A multi-SKU visual inspection platform with: (1) rapid model calibration — train a per-SKU inspection profile from 50-100 images captured during a calibration run, using a pre-trained food product vision backbone fine-tuned with few-shot learning; (2) operator-controlled profile switching — at changeover, the operator selects the next SKU from a touchscreen menu and the inspection profile updates automatically; (3) seasonal drift adaptation — the system flags when inspector overrides (accepting products the model rejects) indicate the acceptance standard has shifted, and prompts the QA lead to update the model's reference baseline.

## Target Customer
VP of Quality and automation engineers at large CPG food plants running 50+ SKUs on shared production lines. Approximately 2,000-3,000 plants in the US.

## Impact If Built
Enables 100% inline visual inspection across all SKUs — replacing sampling inspection that catches only 10-20% of defects. Reduces customer complaints and retailer chargebacks by 40-60%. Eliminates the quality gap during inspector breaks, shift changes, and fatigue periods. For a plant with $100M annual output, preventing 0.3% of defective product from reaching retailers saves $300,000+ in chargebacks and credits annually.
