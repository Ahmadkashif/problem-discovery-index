# Target Market Lending Compliance Monitoring

**Niche:** [[niches/credit-unions/cdfi-credit-unions/profile|CDFI-Designated Credit Unions]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** CDFI CUs must direct a minimum percentage of lending to designated target markets — but they discover whether they're on track only at year-end when the report is compiled, leaving no time to correct course.
**Tags:** #time-series-forecasting #tabular-ml #compliance #automation

## The Problem
CDFI certification requires that at least 60% of lending activity (by dollar or unit count, depending on the award) targets the institution's designated target market — defined as specific geographies (census tracts) or populations (low-income individuals, minority communities). If a CDFI CU's lending mix drifts toward higher-income borrowers or non-target geographies during the year, the annual report will show non-compliance — potentially triggering CDFI Fund corrective action or loss of certification. The problem is that target market compliance is computed annually, not monitored in real time. A CU discovers at year-end that it spent 9 months below the 60% threshold and can't recover.

## Why It's Still Broken
Computing target market compliance requires geocoding every loan to a census tract and comparing borrower income to AMI — a process that most CDFIs only perform during annual reporting because it requires manual data transformation. Real-time monitoring would require automatic geocoding and income classification at the point of loan origination — logic that core banking platforms don't include. Loan officers don't see whether a specific loan will count toward target market compliance when making the decision, so there's no mechanism to adjust lending focus during the year.

## What a Fix Looks Like
A real-time compliance dashboard that classifies every new loan at origination as target-market or non-target based on borrower address (geocoded to census tract) and income level (compared to AMI). The dashboard displays year-to-date target market percentage with trend projection: "At current pace, you'll end the year at 57% target market — below the 60% requirement. Need 25 additional target-market loans in Q4." Alerts trigger when the trailing 3-month target market percentage drops below threshold. Loan officers see target market status on each application, enabling mission-aligned lending decisions without separate research.

## Who Feels the Pain
CEOs and compliance officers at CDFI CUs who discover target market non-compliance too late to correct it, risking CDFI certification — the foundation of their mission-driven business model and source of $500K-$2M in annual CDFI Fund awards.

## Impact If Fixed
Provides 9-month lead time to address target market compliance drift instead of discovering it at year-end. Enables loan officers to factor target market status into lending decisions without manual geocoding. Protects CDFI certification and associated funding — the existential compliance requirement for mission-driven CUs.
