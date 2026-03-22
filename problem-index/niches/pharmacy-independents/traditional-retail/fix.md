# Inventory Deadstock Detection and Demand-Based Reordering

**Niche:** [[niches/pharmacy-independents/traditional-retail/profile|Traditional Retail Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** Independent pharmacies carry $5,000-10,000 in expired or slow-moving inventory because their PMS reorder logic uses simple par levels that ignore demand trends, seasonal shifts, and payer-driven formulary changes.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #automation #revenue-impact

## The Problem
Pharmacy inventory management in PMS systems like PioneerRx and QS/1 uses static par levels: when on-hand quantity drops below a threshold, the system generates a reorder. These par levels are set manually — often when the pharmacy first opens — and rarely updated. When a prescriber switches a patient population from Brand A to Brand B, or a PBM moves a drug to a higher copay tier (reducing demand), the pharmacy continues ordering at the old rate. The result is slow-moving inventory that ties up $5,000-10,000 in working capital and eventually expires. Conversely, under-ordering high-demand items leads to stockouts that send patients to CVS — a loss the independent pharmacy may never recover.

## Why It's Still Broken
Experienced pharmacy techs and owners develop an intuitive sense for what's moving and what's sitting — they notice dust on bottles, remember which drugs they haven't dispensed in weeks, and adjust orders mentally. But this knowledge lives in one person's head and doesn't scale to the 2,000-4,000 unique NDCs a typical pharmacy stocks. Automated inventory optimization tools (Datarithm, RxAlly) exist but cost $500-800/month and require dedicated implementation time. The PMS vendors have no financial incentive to improve inventory analytics because they make money on subscription fees regardless of whether the pharmacy's inventory turns are 8x or 14x per year.

## What a Fix Looks Like
An inventory intelligence layer that connects to the PMS dispensing history and wholesaler ordering data to: (1) flag deadstock — NDCs with no dispensing activity in 60+ days and positive on-hand quantity, with estimated loss if they expire, (2) forecast demand per NDC using a gradient-boosted time-series model trained on dispensing history, seasonal patterns, and payer formulary changes, (3) generate dynamic reorder recommendations that optimize for both service level (minimize stockouts) and working capital (minimize days-on-hand). The pharmacist sees a weekly "inventory health" report: deadstock to return or mark down, reorder quantities adjusted for predicted demand, and total working capital freed by optimizing turns.

## Who Feels the Pain
The owner-pharmacist who writes a $15,000-25,000 monthly wholesaler check and watches $5,000-10,000 of it sit on shelves as slow movers, and the lead technician who manually scans shelves for expired medications during monthly inventory audits.

## Impact If Fixed
Reducing deadstock by 50% and improving inventory turns from the industry average of 10x to 14x frees $3,000-7,000 in working capital per pharmacy and eliminates $2,000-5,000/year in expired medication write-offs. Reducing stockout-driven patient loss by even 5 patients/month recovers $15,000-25,000/year in lifetime prescription value per patient.
