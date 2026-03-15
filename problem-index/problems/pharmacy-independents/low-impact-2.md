# Medication Adherence Risk Scoring and Proactive Outreach

**Industry:** [[pharmacy-independents|Independent Pharmacies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic patient outreach tools exist for health systems but aren't calibrated to the independent pharmacy's specific adherence metrics — Medicare Part D star ratings measures, PDC (Proportion of Days Covered) thresholds, and the specific drug categories that trigger DIR fee adjustments.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation

## The Problem
Medication adherence is a clinical outcome measure and a financial performance metric for independent pharmacies at the same time: patients on chronic medications (statins, oral diabetes drugs, RAAS inhibitors) who miss refills drive down the pharmacy's PDC scores on those drug classes, which directly drives up DIR fee rates from Medicare Part D PBMs. The pharmacy has both a clinical incentive (patient health) and a financial incentive (DIR fee avoidance) to identify non-adherent patients and intervene proactively. But most independent pharmacies have no systematic adherence tracking — they react when a patient hasn't refilled in 30 days rather than predicting which patients are at risk of lapsing before the gap opens.

## What Already Exists
MTM platforms (Outcomes MTM, Mirixa) track PDC scores for enrolled patients and generate targeted intervention lists for Medicare star ratings. These tools are narrowly focused on Part D star ratings metrics, require patient enrollment in MTM programs, and are primarily physician-facing rather than pharmacist-workflow-embedded. General health system CRM platforms (Salesforce Health Cloud, Phreesia) track patient engagement but aren't calibrated to pharmacy-specific adherence metrics. No tool systematically predicts refill risk at the individual patient level for an independent pharmacy's full chronic patient population.

## The Customisation Gap
What's needed is a risk model embedded in the PMS that scores every chronic medication patient weekly: probability of missing the next refill based on their refill pattern history, gap timing, seasonal patterns (adherence drops during holidays and summer), and the specific drug class. The model surfaces the top 20 patients at highest adherence risk each week for pharmacist outreach — a targeted list, not the entire patient roster. The DIR fee exposure linkage is the customization layer: the model should weight adherence risk higher for drug classes that are active DIR fee performance metrics for the pharmacy's specific PBM contracts.

## Impact If Solved
A pharmacy that improves PDC on star-rating drug classes by 5 percentage points can see DIR fee reductions of 2-4% on affected plans. For a pharmacy with $2M in annual Part D claims, that's $40,000-80,000 in DIR fee savings, plus the clinical benefit to patients who stay on therapy.
