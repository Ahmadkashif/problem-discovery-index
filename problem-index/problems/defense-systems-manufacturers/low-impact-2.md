# Bases of Estimate Rebuilt for Every Proposal

**Industry:** [[defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every cost-type or sole-source production proposal needs hundreds of bases of estimate traced to historical actuals, and estimators rebuild them by hand from old proposals and cost reports for each bid.
**Tags:** #large-language-models #bayesian-linear-regression #k-nearest-neighbors #confidence-intervals #compliance #workflow-orchestration #automation

## The Problem
A defence manufacturer pricing a development contract, a production lot or a sole-source spares buy must show the government how every element was estimated. Each work breakdown structure element gets a basis of estimate: the method (analogy, parametric, engineering build-up, actual cost), the historical data behind it, the adjustments and the resulting hours and materials. The cost volume follows FAR 15.408's format, and where certified cost or pricing data is required the company certifies that the data is current, accurate and complete. The FY2026 NDAA raised that threshold to $10M for contracts entered into after 30 June 2026 (from $2.5M since October 2025), which shrinks the certified population but leaves the large proposals exactly as hard.

Estimators and engineers build these documents under the request for proposal's due date. They hunt through prior proposals, cost reports and labour actuals for an analogous job, copy its narrative, adjust it and hope the analogy holds. DCAA's evaluation and DCMA's pricing team then question hours whose basis doesn't trace to actuals, and questioned hours become negotiating losses.

## What Already Exists
Pricing tools such as ProPricer and Excel workbooks build the cost volume; Deltek Costpoint and SAP hold the actuals; parametric tools (SEER, TruePlanning) produce model-based estimates; proposal content platforms (Loopio, GovDash and similar) manage narrative reuse for technical volumes.

## The Customisation Gap
None of these connects an estimate to its evidence. The defence layer is: a searchable archive of past bases of estimate linked to the actuals the job really incurred; analogy selection by work content, not by title; documentation that meets DCAA's and DCMA's expectations for traceability; the TINA threshold that changes by award date; disclosed cost accounting practices and forward pricing rates; and on-premises operation for export-controlled and classified programmes. A tool that proposes an analogy, shows the actual hours behind it with an uncertainty range, and drafts the basis-of-estimate narrative for the estimator to sign would fit the existing review chain.

## Impact If Solved
Shorter BOE builds free estimators for the judgement calls, and bases of estimate that trace cleanly to actuals reduce the hours DCAA or DCMA questions, which on a large production proposal can be worth millions of dollars at negotiation (estimate).
