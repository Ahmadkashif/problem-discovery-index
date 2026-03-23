# Model-to-Estimate Automation for Structural Steel

**Niche:** [[niches/metal-fabrication/structural-steel-fabricators/profile|Structural Steel Fabricators]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform reads a Tekla or SDS2 structural model and automatically generates a fabrication labor estimate — computing weld linear footage by joint type, piece complexity classification, and predicted shop hours per ton — from the geometric data that already exists in the 3D model.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #tacit-knowledge-ml #revenue-impact

## The Problem
Structural steel estimating is the revenue-determining function of a fabrication shop. An estimator reviews the structural model (or preliminary engineering drawings), develops a tonnage and piece count, classifies piece complexity (simple beams vs. complex connections vs. built-up members), estimates weld linear footage by joint type and position, and predicts labor hours per ton for fabrication and erection. An experienced estimator produces this estimate in 2-8 hours depending on project size, but the accuracy depends entirely on their calibrated judgment — understanding which connection details create difficult shop access, which member configurations require multiple handling operations, and where the engineering design will generate change orders. This judgment takes 5-10 years to develop and is the most valuable human asset in a structural steel company.

## Why Nobody Has Built This
Tekla and SDS2 models contain all the geometric data needed for automated estimating — weld lengths, piece counts, material weights, connection complexity. But extracting this data and mapping it to fabrication labor requires: (1) reading the proprietary model file formats, (2) classifying geometric features into estimable categories (connection types, weld positions, member complexity), and (3) calibrating the labor prediction to a specific shop's productivity (a shop with newer equipment and skilled welders fabricates faster than a shop with older equipment and apprentice welders). The model file API access, geometric classification, and shop-specific calibration have not been combined into a product.

## What to Build
A model analysis engine that imports Tekla IFC or SDS2 model files, extracts structural member properties (weight, length, profile), connection details (joint type, weld length, bolt count, access difficulty), and piece complexity features. A gradient boosting model trained on historical estimating data predicts labor hours per ton by piece category, calibrated to the specific shop's productivity history. Output: an itemized estimate showing predicted hours by operation (handling, fit-up, welding, finishing) with confidence intervals, benchmarked against the shop's historical performance on similar work.

## Target Customer
Estimating managers at AISC-certified structural steel fabricators with $10M+ annual revenue. Approximately 2,500-3,500 companies in the US.

## Impact If Built
Reduces estimating time from 2-8 hours to 30-60 minutes per project. More importantly, captures estimating expertise that currently exists only in the estimator's head — protecting the shop when the estimator retires. For a shop quoting $50M annually, improving quote accuracy by 1.5% of margin recovers $750,000 in project profitability.
