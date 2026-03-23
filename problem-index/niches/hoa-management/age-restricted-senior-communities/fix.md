# Age-Restriction Compliance Verification and Tracking

**Niche:** [[niches/hoa-management/age-restricted-senior-communities/profile|Age-Restricted Senior Communities]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Fix (Pain Point)
**One-liner:** The Housing for Older Persons Act requires that 80% of units in a 55+ community be occupied by at least one person 55 or older — but tracking compliance requires verifying occupant ages at move-in and re-verifying at ownership changes, a manual process that 60% of age-restricted communities perform inconsistently, risking loss of their age-restriction exemption from familial status Fair Housing protections.
**Tags:** #automation #compliance #data-integration

## The Problem
To maintain 55+ age-restriction status under the Housing for Older Persons Act (HOPA), a community must: (1) ensure at least 80% of occupied units have at least one resident 55 or older; (2) publish and follow policies demonstrating intent to be age-restricted; (3) verify compliance through reliable surveys or affidavits. The community manager must collect age verification from new residents at move-in, track occupancy changes, and maintain documentation proving ongoing 80% compliance. In practice: managers collect age verification inconsistently, unit ownership changes occur without notification, and adult children move in without age-qualified status being re-verified. A community that falls below 80% compliance loses its HOPA exemption — meaning it can no longer restrict occupancy by age, fundamentally changing the community's character and reducing property values by 10-20%.

## Why It's Still Broken
HOA management platforms track unit owners but not individual occupant ages. Age verification is a sensitive personal data request that managers handle awkwardly — asking a resident to prove their age feels intrusive. No standardized verification workflow exists — some communities use affidavits at purchase, others rely on driver's license copies, others don't verify at all. The compliance data (which units have age-qualified occupants) isn't integrated with the ownership/occupancy tracking in the management platform.

## What a Fix Looks Like
An age-restriction compliance module that: (1) maintains occupant records with age verification status per unit; (2) triggers re-verification requests when ownership changes are detected (from deed recordings or management platform ownership updates); (3) calculates current 80% compliance ratio with a dashboard visible to the board; (4) generates annual compliance survey/affidavit packages for all residents; (5) alerts the manager when compliance approaches the 80% threshold (at 83%, begin proactive verification of unverified units).

## Who Feels the Pain
Community managers at 55+ communities who face the risk of HOPA non-compliance — approximately 15,000-20,000 age-restricted communities nationally.

## Impact If Fixed
Compliance verification becomes systematic instead of ad hoc. Communities that currently can't prove 80% compliance (because records are incomplete) can demonstrate compliance confidently. The existential risk of losing HOPA exemption — which would decrease property values by 10-20% across the community — is mitigated through continuous monitoring.
