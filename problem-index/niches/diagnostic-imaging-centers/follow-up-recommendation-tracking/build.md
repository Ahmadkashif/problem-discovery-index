# Recommendation Extraction With a Completion Feed Across Providers

**Niche:** [[niches/diagnostic-imaging-centers/follow-up-recommendation-tracking/profile|Follow-Up Recommendation Tracking]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A centre can extract every follow-up recommendation from its reports but cannot see whether the patient had the follow-up somewhere else, so outreach goes to people already done and misses people who are not.
**Tags:** #bert #large-language-models #survival-analysis #gradient-boosting #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get each radiologist's follow-up recommendation done by the date the report gives, and whoever gets the highest share of recommended follow-up exams completed on time takes the account.

## The Problem
Navigators read reports, log "CT chest in 12 months for 6 mm nodule", and call the referrer when the date passes. Half the calls reach patients who were scanned at a hospital; the other half go unanswered.

## Why Nobody Has Built This
Completion data lives in other providers' systems and payers' claims. Centres have no data-sharing path, and reporting vendors stop at extraction.

## What to Build
Extraction of each recommendation into a structured record (finding, modality, interval, due date, guideline). It is matched against the centre's own later orders and against outside completion signals: HIE queries, referrer confirmations and, where agreements allow, payer care-gap feeds. A completion-risk model prioritises outreach. Outreach to referrer and patient runs on due dates, and every closure is documented for the radiologist's record.

## Target Customer
Chief medical officers at multi-site operators and quality chiefs at reading groups.

## Impact If Built
Raising on-time follow-up completion from roughly half to two-thirds or more (estimate) catches more early cancers. It also brings thousands of follow-up exams a year back to a large operator.
