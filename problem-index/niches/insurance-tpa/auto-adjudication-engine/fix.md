# Coordination of Benefits Processing Bottleneck

**Niche:** [[niches/insurance-tpa/auto-adjudication-engine/profile|Auto-Adjudication Engine]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Fix (Pain Point)
**One-liner:** Claims involving members with dual coverage (Medicare, spouse's plan, auto insurance) suspend 90% of the time because COB determination requires information the TPA doesn't have at the point of adjudication.
**Tags:** #data-integration #automation #compliance

## The Problem
Coordination of benefits (COB) applies when a member has coverage under two or more health plans. The TPA must determine which plan pays primary and which pays secondary, then calculate the secondary plan's liability based on the primary plan's payment. In practice, 8-12% of all claims involve COB, and 90% of those suspend for manual review because the TPA doesn't have the primary plan's payment information, doesn't know the member has other coverage, or can't determine the correct COB order based on plan type (employer vs. Medicare vs. auto vs. workers' comp). Each COB suspension costs $15-$25 in examiner research time.

## Why It's Still Broken
COB determination requires information from outside the TPA's system — the other plan's payment amount, the other plan's coverage dates, and the applicable COB rules (birthday rule, gender rule, dependent child rules vary by state). There is no real-time data exchange between TPAs for COB purposes. Examiners call the other plan's member services, wait on hold, get partial information, and manually calculate the secondary payment. The industry attempted to solve this with CAQH COB Smart, but adoption is limited and the data is often stale.

## What a Fix Looks Like
A real-time COB data exchange that queries primary plan payment information at the point of adjudication. When a claim is identified as potentially involving COB (based on member's other-coverage flag or diagnosis/procedure patterns associated with auto accidents or workers' comp), the system automatically queries the primary payer's 835 remittance data, calculates the secondary plan's liability, and adjudicates the claim without examiner intervention. Integrates with CAQH COB Smart, Medicare's BCRC query system, and direct TPA-to-TPA API connections.

## Who Feels the Pain
Claims examiners spend 25-35% of their manual review time on COB claims. Members with dual coverage experience the longest claim processing delays (30-60 days versus 14-day industry standard) because COB research adds weeks to the adjudication cycle.

## Impact If Fixed
Auto-resolves 60-70% of COB suspensions, reducing average COB claim processing time from 45 days to 14 days. Saves $8-$12 per COB claim in examiner time — for a TPA processing 300,000 total claims, this eliminates 16,000-25,000 manual COB reviews annually, saving $200K-$300K.
