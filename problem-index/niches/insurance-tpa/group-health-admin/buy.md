# Member Portal with Plan-Specific Cost Estimator

**Niche:** [[niches/insurance-tpa/group-health-admin/profile|Group Health Benefits Admin]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic healthcare cost estimators exist but none integrate with TPA-administered plan designs to give members accurate out-of-pocket estimates based on their specific SPD provisions.
**Tags:** #linear-regression #regression #tabular-ml #data-integration #worker-facing

## The Problem
Members covered by self-insured employer plans administered by TPAs cannot get accurate pre-service cost estimates. When a member needs an MRI, they have no way to know their out-of-pocket cost because it depends on their specific plan's deductible status, coinsurance rate, network tier, and any applicable sub-limits — information that lives only in the TPA's adjudication engine.

## What Already Exists
Healthcare cost transparency tools like Turquoise Health, Healthcare Bluebook, and carrier-specific estimators provide price ranges for procedures. Member portals from large carriers (UHC, Cigna) offer plan-specific estimates for their fully-insured products. However, these tools don't integrate with TPA adjudication engines or the custom plan designs of self-insured employers.

## The Customization Gap
The missing piece is a real-time API connection between a member-facing cost estimator and the TPA's adjudication engine. The estimator must query the member's specific plan configuration (current deductible accumulation, applicable coinsurance, network status of the provider, any pre-authorization requirements) and return an accurate estimate. This requires plan-aware logic, not just procedure pricing data.

## Target Customer
TPAs serving self-insured employers with 500+ employees who face member satisfaction and retention pressure from carriers offering superior digital member experiences.

## Impact If Solved
Reduces member call volume by 25-35% (cost-inquiry calls are 30% of TPA call center volume) and improves employer client retention by providing a digital experience competitive with fully-insured carrier portals.
