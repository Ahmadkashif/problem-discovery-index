# PHI Exposure Detection for MSSP SOCs

**Niche:** [[niches/cybersecurity-mssp/healthcare-hipaa-mssp/profile|Healthcare HIPAA Security Services]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No SIEM product can distinguish between legitimate high-volume EHR access (a nurse reviewing a patient panel) and unauthorized PHI exposure (an employee browsing records of non-patients) without healthcare-specific behavioral baselines.
**Tags:** #isolation-forest #anomaly-detection #tabular-ml #tacit-knowledge-ml #compliance

## The Problem
MSSP SOC analysts monitoring healthcare clients receive alerts for "unusual data access volume" but cannot determine whether the access involves PHI or routine clinical data without manually investigating each alert in the client's EHR audit logs. A Tier-1 analyst sees "User X accessed 200 records in 2 hours" — is this a registration clerk checking in a full waiting room, or a billing employee exporting patient lists? The EHR audit log shows which records were accessed, but the SIEM only receives metadata (user, volume, timestamp). MSSP analysts spend 45-60 minutes per alert manually correlating SIEM data with EHR audit logs to determine PHI exposure risk. For healthcare clients generating 50-100 alerts per day, this is unsustainable.

## Why Nobody Has Built This
PHI exposure detection requires understanding the clinical context of data access — which is legitimate for the user's role, department, and current patient assignments. Building this requires EHR-specific integrations (Epic audit log formats differ from Cerner's), role-based access pattern baselines (a nurse's normal access pattern differs from a billing clerk's), and patient assignment correlation (the nurse accessed the record because the patient was on their unit). No SIEM vendor has invested in building these healthcare-specific behavioral models because it requires deep EHR domain knowledge and client-specific configuration.

## What to Build
A healthcare SOC analytics layer that: (1) ingests EHR audit logs alongside SIEM data, (2) builds role-specific access baselines per user (normal access volume, typical record types, usual access hours), (3) correlates access with patient assignment data (was this patient assigned to this user's unit/panel?), (4) scores each access event for PHI exposure risk (unauthorized access to non-assigned patients scores high), and (5) generates prioritized alerts with context ("User X accessed 15 records of patients not on their unit, during off-hours, matching the pattern of snooping"). Reduces alert triage from 45 minutes to 5 minutes per event.

## Target Customer
MSSPs serving 5+ healthcare clients with EHR systems (Epic, Cerner, MEDITECH), where SOC analysts spend 30-40% of their time on healthcare-specific alert triage.

## Impact If Built
Reduces healthcare alert triage time by 80%, from 45 minutes to 5 minutes per alert. Increases true positive detection rate by 3-5x through context-aware analysis. Catches PHI snooping incidents that generic SIEM rules miss entirely — estimated 30-40% of PHI breaches are insider snooping.
