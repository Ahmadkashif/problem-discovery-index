# Three Gap Lists That Disagree About the Same Patient

**Niche:** [[niches/physician-practices/value-based-primary-care-contracts/profile|Primary Care in Value-Based Contracts (ACOs & MA Risk)]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** The ACO, each MA plan and the EHR send the practice separate care-gap and risk-suspect lists computed from different data, and the MA rooming the patient cannot tell which one is right.
**Tags:** #data-integration #feature-engineering #descriptive-statistics #workflow-orchestration #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep an attributed population's cost under its benchmark, with quality and risk scores complete before the performance year closes, and whoever books the most shared savings per attributed patient with no benchmark or RADV clawback takes the account.

## The Problem
One plan's portal says the patient is due for a diabetic eye exam. The EHR says it was done last spring, as an outside report scanned into the chart. The ACO's list shows a colorectal screening gap that a colonoscopy at the hospital closed two months ago, but the claim has not yet arrived. Staff chase gaps that are closed and miss the open ones.

## Why It's Still Broken
Each list is computed from the data its owner holds. Plans use claims, which lag. EHRs use structured fields, which miss scanned reports. ACOs blend the two months late. Nobody reconciles at the patient level, because each plan's contract pays on its own list.

## What a Fix Looks Like
A patient-level reconciliation that merges every list, matches each gap to evidence (claims, structured results and text extracted from outside reports) and shows one status with its source. Closed gaps are sent back to the plan with the supporting document.

## Who Feels the Pain
Medical assistants rooming patients; quality coordinators working lists; ACO leaders whose quality score sets the sharing rate.

## Impact If Fixed
Removing duplicate and already-closed gaps could cut outreach waste by ~30% (estimate). Each quality point recovered at year end protects a share of savings that runs to six figures for a mid-sized ACO (estimate).
