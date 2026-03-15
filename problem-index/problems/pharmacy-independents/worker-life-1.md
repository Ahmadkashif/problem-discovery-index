# Drug Interaction Alert Prioritization and Alert Fatigue Reduction

**Industry:** [[pharmacy-independents|Independent Pharmacies]]
**Type:** Worker Life Changing
**One-liner:** Pharmacists who currently override 90%+ of drug interaction alerts because they're clinically insignificant get a ranked, contextualized alert system where the 10% that actually matter are visually prominent and the rest are suppressed or summarized — so the real warnings get acted on instead of habituated past.
**Tags:** #gradient-boosting #ranking #tabular-ml #worker-facing #compliance

## The Problem
Every pharmacy management system generates drug-drug interaction (DDI) and drug-disease interaction alerts at dispensing. The problem is alert fatigue: PMS systems flag every coded interaction without clinical contextualization, generating 50-100+ alerts per pharmacist shift, of which 90-95% are either clinically insignificant for this patient's specific profile or duplicates of alerts the pharmacist has reviewed and accepted before. The result is that pharmacists have learned to habitually click "override" on interaction alerts without reading them — a dangerous cognitive shortcut that occasionally causes a serious interaction to be dismissed alongside hundreds of minor ones. The severity rating system in most PMS databases (DRUG A — DRUG B — contraindicated) is static and not calibrated to individual patient context (age, renal function, the specific dose combination, whether the prescribers are aware of each other's prescriptions).

## Why It Matters to the Worker
Alert fatigue is not just an efficiency problem — it's a safety and liability problem that sits squarely on the pharmacist's shoulders. When a serious drug interaction causes patient harm after a pharmacist clicked "override," the pharmacist owns the legal and professional consequences. Yet the current alert system makes it structurally impossible to triage alerts thoughtfully at the pace of a busy dispensing workflow. A pharmacist seeing 150+ patients per day cannot read each DDI alert as if it might be the one that matters. The psychological weight of knowing this — that something dangerous might be in the override queue — is a genuine occupational stressor.

## What a Solution Looks Like
A risk scoring model that re-ranks DDI alerts by clinical significance for this specific patient: patient age, renal/hepatic function (if labs are in PMS), specific dose of each drug, whether the DDI is an acute risk vs. a monitoring flag vs. a theoretical interaction, and whether the same drug pair has been reviewed and accepted for this patient before. High-priority alerts (novel combination, dose-dependent risk, patient risk factor elevates severity) are displayed prominently and require explicit acknowledgment with a reason. Low-priority alerts (same combination, same dose, reviewed before, minor theoretical interaction) are collapsed into a summary. The pharmacist's cognitive load focuses on real clinical decisions.

## Impact If Solved
Reduces override-without-reading rate from an estimated 90%+ to under 20% for high-priority alerts. Recovers 5-10 minutes per shift of pharmacist attention currently spent on alert dismissal theater. Most importantly, the genuine interaction catches that are currently buried in noise become visible.
