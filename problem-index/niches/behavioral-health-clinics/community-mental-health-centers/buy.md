# Multi-Payer + Grant Billing Engine for CMHCs

**Niche:** [[niches/behavioral-health-clinics/community-mental-health-centers/profile|Community Mental Health Centers (CMHCs)]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard behavioral health billing tools handle commercial insurance and Medicare, but CMHCs bill a tangled mix of Medicaid managed care carve-outs, sliding-scale self-pay, state grant funding, and county contracts — often for the same patient across service types — and no commercial tool handles this natively.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #automation #data-integration #compliance

## The Problem
A single CMHC patient might receive individual therapy billed to Medicaid managed care, crisis stabilization billed to a state grant, and case management billed to a county contract — each with different rates, authorization requirements, documentation standards, and reporting obligations. Billing staff must manually determine which funding source covers which service, apply the correct rate, and generate separate financial reports by funding source for grant compliance. Denials from Medicaid managed care plans require resubmission under different authorization rules than fee-for-service Medicaid, and sliding-scale self-pay calculations change when a patient's income is re-verified. This complexity causes revenue leakage of 8-15% at most CMHCs.

## What Already Exists
Practice management billing platforms (CollaborateMD, AdvancedMD, Office Ally) handle standard insurance claim submission and denial management. Netsmart and Qualifacts include billing modules designed for behavioral health. These tools manage commercial insurance and straightforward Medicaid fee-for-service billing competently.

## The Customization Gap
No commercial billing tool models the CMHC funding stack: state-specific Medicaid managed care carve-out rules (which services are carved in vs. carved out varies by state and by managed care plan), grant-funded service tracking with deliverable reporting, county contract rate schedules, and sliding-scale fee calculation tied to income verification windows. The system needs a funding-source prioritization engine — given this patient, this service, this date, which funding source should be billed first, and what's the fallback if denied? It also needs per-funding-source financial reporting for grant compliance, not just per-payer reports.

## Target Customer
Billing managers and CFOs at CMHCs with 50+ clinicians and $5M+ in annual revenue, where the multi-payer complexity is most acute. Approximately 1,200 CMHCs nationally fit this profile.

## Impact If Solved
Recovering even 5% of the 8-15% revenue leakage at a mid-size CMHC ($10M revenue) means $500K-$750K in recaptured annual revenue. Grant compliance reporting shifts from a 20-hour monthly manual process to an automated export.
