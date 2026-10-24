# Spurious-Result Detection Learned From the Technologists' Own Holds

**Niche:** [[niches/clinical-laboratories/autoverification-result-review/profile|Autoverification & Result Review]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every lab's held-result decisions are a labelled dataset of expert judgement that nobody keeps.
**Tags:** #tacit-knowledge-ml #gradient-boosting #feature-engineering #transfer-learning #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to take routine result review off technologists' hands, and whoever cuts technologist review minutes per thousand results with no rise in corrected reports takes the account.

## The Problem
Technologists release, rerun, comment or reject thousands of held results a week, and the LIS keeps only the action. The lab cannot learn from its best technologists' calls, cannot measure which rules hold real results for no reason, and cannot detect the spurious results its rules let through.

## Why Nobody Has Built This
Middleware vendors sell rules engines and instrument connectivity, and changing release logic means revalidation that labs avoid. Ground truth is scattered across recollections, corrected reports and clinical records. Published models exist for single problems, IV contamination above all, but not as a product.

## What to Build
A held-result ledger that records context, action and a one-click reason, and joins each held result to its outcome automatically. A multi-label model of specimen-integrity failure is trained on pooled patterns and simulated admixtures, then calibrated to each site on its ledger. It sits beside the middleware as a ranked review queue with explanations, and graduates to auto-release only for categories where it beats the lab's best technologists on held-out cases.

## Target Customer
Core lab managers and directors at hospital and reference labs releasing 5,000–100,000 results a day.

## Impact If Built
Releasing five more results in every hundred automatically on 20,000 daily results removes ~1,000 reviews a day, about 8 technologist-hours at ~30 seconds each (estimate), or ~25 review minutes per thousand results. Catching spurious results the rules miss prevents treatment decisions based on a contaminated specimen.
