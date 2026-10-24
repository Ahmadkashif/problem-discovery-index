# A Recall Pathway Tracker That Follows the Patient, Not the Worklist

**Niche:** [[niches/diagnostic-imaging-centers/breast-imaging-mqsa/profile|Breast Imaging Centers under MQSA]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A woman recalled from screening drops out of the centre's view the moment she does not book, and the outcomes audit discovers it a year later.
**Tags:** #gradient-boosting #survival-analysis #large-language-models #evaluation-metrics #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get every woman recalled from a screening mammogram through her diagnostic workup, and whoever gets the highest share of recalled patients to a final assessment within 30 days takes the account.

## The Problem
A BI-RADS 0 recall generates a letter and a worklist entry. If the patient does not call, a coordinator may phone twice. If she books at another centre, or her physician's office never follows up, the centre does not know whether she was ever diagnosed. Biopsy pathology often comes back on paper from another provider.

## Why Nobody Has Built This
Tracking systems were built as MQSA record-keeping, not as outreach. Outcome data sits with surgeons, pathology labs and other imaging centres the breast centre does not control.

## What to Build
A pathway tracker with a state per patient (recalled, scheduled, diagnostic done, biopsy recommended, biopsy done, pathology received). It sets deadlines for each state, predicts who is at risk of not completing, and runs outreach by text, call and physician notification. It ingests outside reports and pathology by fax extraction and assembles the outcomes audit continuously rather than once a year.

## Target Customer
Directors of breast centres and women's imaging at multi-site operators.

## Impact If Built
Raising 30-day recall completion by 5–10 points (estimate) moves hundreds of women a year through diagnosis sooner at a large centre. Each completed diagnostic workup and biopsy is revenue that currently leaks.
