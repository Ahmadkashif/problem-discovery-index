# Care-Management Platforms Rebuilt for APCM

**Niche:** [[niches/physician-practices/chronic-care-management-programs/profile|Chronic & Advanced Primary Care Management Programs]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Care-management software was built around CCM's 20-minute timer; APCM pays a monthly amount for capabilities instead, and the platforms do not yet track them.
**Tags:** #descriptive-statistics #data-integration #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep enrolled Medicare patients in monthly care management the practice can bill, and whoever keeps the most patients billable every month with documentation that survives audit takes the account.

## The Problem
APCM codes (G0556–G0558) pay monthly without a time threshold. In exchange, the practice attests to a set of capabilities: 24/7 access, continuity, a care plan, coordination across settings, and population-level management. Practices must decide which patients to move from CCM to APCM and prove the capabilities if audited.

## What Already Exists
EHR care-management modules and CCM vendor platforms track minutes, consent and care plans. Billing systems submit the codes.

## The Customization Gap
APCM needs a different layer:

- a capability ledger showing, per patient-month, the evidence for each required element;
- tier assignment by chronic-condition count and Qualified Medicare Beneficiary status, which changes during the year;
- rules for which codes may be billed together (APCM with RPM but not CCM, per vendor guidance, recalled);
- a CCM-versus-APCM revenue comparison per patient, since the monthly amounts differ by tier.

## Target Customer
Primary care groups and FQHC-adjacent practices already billing CCM that want to move eligible patients to APCM.

## Impact If Solved
Capturing APCM for patients not reaching CCM's 20 minutes could add ~$15–$115 per patient-month depending on tier (estimate, from secondary 2026 rate guides via search summary). The capability ledger also makes the audit file a by-product of the work.
