# ML-Powered Fabrication Estimating from Drawing Features

**Niche:** [[niches/metal-fabrication/estimating-and-quoting-automation/profile|Estimating & Quoting Automation]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform reads fabrication drawing features (weld lengths, joint types, material thicknesses, piece counts, geometric complexity) and predicts labor hours per operation using the shop's own historical estimating and actual cost data — the ML-powered estimating tool that learns from every job the shop has ever produced.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact

## The Problem
Fabrication estimating accuracy depends on the estimator's calibrated judgment — built over years of quoting similar jobs, observing actual production times, and mentally adjusting rates for complexity factors. This judgment is the single most valuable human asset in a fabrication business, and it is completely undocumented. When the estimator retires, the shop's quoting accuracy degrades for 2-5 years until the replacement develops their own calibration. Even an experienced estimator has systematic biases — consistently under-estimating certain job types and over-estimating others — that compound across the job portfolio without detection.

## Why Nobody Has Built This
ML-based estimating requires two things fabrication shops rarely have in digital form: (1) drawing feature data (weld lengths, joint counts, material specs extracted from the engineering drawings they quoted), and (2) actual cost data at the operation level (not just total job cost, but hours per operation per job). Most shops have the total job cost in their ERP/accounting system but not the operation-level breakdown needed to train operation-specific labor models. Building this requires both a drawing feature extraction capability and an actual cost collection mechanism.

## What to Build
A two-part system: (1) drawing feature extraction — importing DXF/DWG files (or structured data entry for shops receiving sketches rather than CAD files) to extract estimatable features: total linear weld feet by joint type and position, piece count, material types and thicknesses, geometric complexity indicators, and tight-tolerance features; (2) gradient boosting regression trained on the shop's historical data — linking drawing features to actual labor hours per operation. For shops with 2+ years of ERP data and 200+ completed jobs, the model identifies systematic estimating patterns and provides data-driven estimates calibrated to the shop's actual productivity.

## Target Customer
Estimators and shop owners at fabrication shops quoting 20+ jobs per month with 2+ years of job cost history. Approximately 8,000-12,000 shops in the US.

## Impact If Built
Reduces estimating time by 40-60% for routine jobs. Surfaces systematic quoting biases (e.g., "you consistently under-estimate fit-up time on assemblies with more than 10 joints by 15%") that improve future accuracy. For a shop quoting $20M annually, correcting a 2% systematic under-estimation bias recovers $400,000 in margin. Captures estimating knowledge that survives estimator turnover.
