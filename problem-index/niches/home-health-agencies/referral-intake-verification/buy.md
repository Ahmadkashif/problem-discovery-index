# Home Health-Specific Insurance Eligibility Verification

**Niche:** [[niches/home-health-agencies/referral-intake-verification/profile|Referral Intake & Insurance Verification]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic eligibility verification tools (Availity, Waystar) confirm insurance coverage but don't check home health-specific benefit requirements — homebound status, prior authorization, skilled need documentation, and episode limits that determine whether home health services are actually covered.
**Tags:** #decision-trees #feature-engineering #automation #compliance #data-integration #revenue-impact #quick-win

## The Problem
When an intake coordinator verifies insurance eligibility for a home health referral, generic tools confirm that the patient has active coverage. But Medicare home health coverage requires additional conditions beyond active enrollment: the patient must be homebound, the services must be skilled (not custodial), a physician must certify the need, and the patient cannot be in another Medicare Part A episode simultaneously. Medicare Advantage and commercial plans add prior authorization requirements, visit limits, and network restrictions that vary by plan. Generic eligibility tools show "eligible" when the patient has coverage, but they don't verify that home health services specifically are covered under the patient's current benefit structure — leading to agencies admitting patients, delivering care, and discovering weeks later that the claim will be denied.

## What Already Exists
Availity, Waystar, and Experian Health provide real-time insurance eligibility verification for general healthcare. These tools check active coverage, co-pay amounts, and deductible status. Home health EMR platforms (WellSky, HCHB) have basic eligibility check integrations. None of these tools verify home health-specific benefit requirements: they don't check whether the patient has an active SNF or inpatient stay that would preclude home health benefits, whether prior authorization is required by the specific plan, or whether the patient has remaining home health episodes available.

## The Customization Gap
Home health-specific eligibility verification requires: (1) Medicare Part A benefit period analysis — determining whether the patient is in an active benefit period and whether they have home health episodes remaining, (2) Medicare Advantage plan-specific prior authorization requirements and submission workflows, (3) commercial payer home health benefit verification including visit limits, authorized services, and network status, (4) concurrent benefit conflict detection (e.g., patient is still in a SNF benefit period that precludes home health Part A), and (5) Medicaid secondary coverage verification for dual-eligible patients. This requires payer-specific rule engines layered on top of generic eligibility APIs.

## Target Customer
Home health agencies with a diverse payer mix (Medicare FFS, Medicare Advantage, commercial, Medicaid) that experience eligibility-related claim denials exceeding 5% of submitted claims.

## Impact If Solved
Catching ineligible referrals before admission — rather than after care has been delivered — would prevent $200K-$500K in annual write-offs for a mid-size agency. Reducing eligibility verification time from 20-30 minutes per referral to 2-3 minutes through automated home health-specific checks would reclaim 8-12 intake coordinator hours per week.
