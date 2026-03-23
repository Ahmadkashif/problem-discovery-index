# FMEA Living Document Decay

**Niche:** [[niches/electronics-contract-mfg/automotive-electronics-ems/profile|Automotive Electronics EMS]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** FMEAs (Failure Mode and Effects Analyses) are created during program launch as living documents that should be updated whenever process changes occur or new failure modes are discovered — but in practice, 70-80% of FMEAs are never updated after initial creation, making them audit artifacts rather than operational risk management tools.
**Tags:** #compliance #automation #workflow-orchestration

## The Problem
IATF 16949 requires that PFMEAs (Process FMEAs) be updated when engineering changes are implemented, new failure modes are discovered in production, customer complaints reveal unanticipated risks, and corrective actions from CAPAs change the process. In practice, an automotive EMS provider managing 50-200 active programs has 50-200 PFMEAs that should each be reviewed and potentially updated whenever a relevant event occurs. The quality team does not have the bandwidth to monitor all change events across all programs and trigger FMEA reviews. Result: FMEAs decay into static documents that reflect launch-state risk, not current-state risk. OEM auditors regularly cite "FMEA not updated to reflect current process" as a finding.

## Why It's Still Broken
FMEA updates require domain expertise — the quality engineer must assess whether a change affects a failure mode, whether the severity/occurrence/detection ratings should change, and whether new controls are needed. No system links engineering change orders, CAPA corrective actions, customer complaints, and process changes to the affected FMEA line items and triggers a review. The trigger mechanism (event → FMEA review) is entirely manual and depends on the quality engineer remembering which FMEAs are affected by which changes.

## What a Fix Looks Like
An FMEA management system that monitors change events (ECOs from the PLM system, CAPAs from the QMS, customer complaints from the complaint system, process parameter changes from the MES) and automatically maps each event to affected FMEA line items based on the affected product, process step, and failure mode. When a relevant event occurs, the system creates a review task for the FMEA owner with the triggering event details pre-populated, guides the owner through the RPN (Risk Priority Number) re-evaluation, and tracks that the FMEA update was completed. Dashboard shows FMEA currency status (days since last review, pending review triggers) across the program portfolio.

## Who Feels the Pain
Quality engineers who receive audit findings for outdated FMEAs and must scramble to update 10-20 FMEAs before an OEM audit. Quality directors who report FMEA compliance metrics to OEM customers. Process engineers whose process changes should trigger FMEA updates but have no mechanism to communicate this to the quality team.

## Impact If Fixed
FMEA currency rate improves from 20-30% to 80-90% of FMEAs reflecting current process state. OEM audit findings for FMEA-related nonconformities decrease by 70-80%. FMEAs become operational risk management tools rather than audit artifacts — actually preventing quality escapes by reflecting current process risks.
