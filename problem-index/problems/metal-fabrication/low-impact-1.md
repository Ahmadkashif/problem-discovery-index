# Fabrication Quote Estimation from Drawing Features

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic ML regression models can predict costs from structured inputs, but don't understand fabrication drawing features — weld joint accessibility, distortion risk from asymmetric heat input, the difference between a weld that looks simple and one requiring multiple passes and repositioning — the geometric reasoning that separates experienced fabrication estimators from a spreadsheet.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #confidence-intervals #automation

## The Problem

Fabrication estimating is the revenue-generating function of a job shop: every quote requires an estimator to read engineering drawings, develop a production routing, estimate time per operation, and calculate material cost. An experienced estimator builds this estimate in 30-60 minutes per job for routine work, but the knowledge applied — understanding which geometric features create difficult weld access, predicting where distortion will require post-weld straightening, recognizing which tolerance requirements demand additional setup time — takes years to develop.

Estimating accuracy directly determines job shop profitability. Systematic under-estimation of specific job types (e.g., consistently underestimating weld-out time on assemblies with limited joint access) compounds across the job portfolio before a shop owner identifies the pattern. The estimator who leaves or retires takes their accuracy calibration with them.

## What Already Exists

ProNest and Lantek provide nesting-based material cost estimation for cut parts. SDS/2 and Tekla provide takeoff quantities (linear feet of weld, square footage of surface treatment) from structural models. No platform provides comprehensive labor hour estimation from drawing features — estimating setup time, weld time, distortion correction, and quality inspection time from part geometry and complexity.

## The Customisation Gap

A fabrication quote ML model needs: (1) drawing feature extraction — parsing DXF/DWG geometry and weld symbols to extract estimatable features (joint count by type, linear weld length by position, material thickness combinations, tight-tolerance features); (2) job type classification — recognizing whether a job is structurally similar to historical jobs in the training set; (3) shop-specific calibration — the labor time per weld type varies with the shop's specific equipment, workforce skill level, and fixturing capability. The drawing feature extraction and shop-specific calibration are the domain-specific components that generic regression models can't be off-the-shelf applied to.

## Impact If Solved

Reduces quote cycle time from 30-60 minutes to 10-15 minutes for routine jobs (the model generates the first estimate draft; the estimator reviews and adjusts for non-standard features). More importantly: surfaces historical quoting patterns (which job types the shop consistently under- or over-estimates) enabling systematic accuracy improvement. For a shop quoting 200 jobs per month, improving average quote accuracy by 2% of margin recovers $40,000-$100,000 annually in job profitability.
