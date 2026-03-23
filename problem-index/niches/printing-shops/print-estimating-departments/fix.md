# Quote-to-Actual Variance Blindness

**Niche:** [[niches/printing-shops/print-estimating-departments/profile|Print Estimating Departments]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Most print shops do not systematically compare quoted cost to actual cost by job — the estimator sends the quote, production runs the job, and the two data sets are never reconciled — meaning pricing errors accumulate for years without detection, eroding margin on specific job types by 5-15%.
**Tags:** #data-integration #revenue-impact #automation

## The Problem
An estimator quotes a job at $2,500. Production completes the job. The actual cost — press time, makeready time, paper consumption, finishing time, outside services — is either not tracked or tracked in a different system than the estimate. Even when both estimated and actual costs are in the same MIS, the variance report is rarely run because: the report requires manual configuration per job category, the data is noisy (individual job variances are high, masking systematic patterns), and no one is specifically tasked with analyzing the data. Result: the estimator consistently under-prices folding jobs (actual makeready is 40% higher than estimated) and over-prices digital short runs (actual cost is 25% lower than estimated) — systematic errors that persist for years because no feedback loop exists.

## Why It's Still Broken
MIS platforms can generate quote-to-actual comparison reports, but these reports require the shop to track actual production time and material per job — a data discipline that adds per-job overhead (operators must clock in/out per job, material must be tracked per job). Many shops track time and material at the daily or weekly level but not per job. Even shops with per-job tracking rarely analyze the data because the analysis requires statistical thinking (filtering noise, identifying systematic patterns) that the estimator and shop owner lack.

## What a Fix Looks Like
An automated variance analysis engine that runs monthly on the MIS job data, identifies systematic estimation errors by job type, press, finishing operation, and customer, and presents actionable findings: "Your makeready estimates for 4-color jobs on Press 2 are systematically 35% low — consider increasing the standard from 25 minutes to 34 minutes" or "Your paper waste factor for coated stock is 2% too high — you are over-ordering paper on every coated job." The analysis runs automatically; the estimator receives a monthly calibration report.

## Who Feels the Pain
Shop owners who see declining margins without understanding the cause. Estimators who lose bids on the jobs they over-price and win too many of the jobs they under-price — a toxic selection effect that erodes profitability. The financial impact is invisible because it manifests as aggregate margin compression rather than individual job losses.

## Impact If Fixed
Systematic pricing errors are identified within 1-2 months instead of persisting for years. Margin improvement of 2-5% across the job portfolio from calibrated pricing. The estimator's confidence increases because they can see whether their pricing is working, not just whether they won the job.
