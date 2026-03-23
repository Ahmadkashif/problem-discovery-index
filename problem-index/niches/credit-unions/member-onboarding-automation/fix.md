# New Member First-Year Attrition

**Niche:** [[niches/credit-unions/member-onboarding-automation/profile|Member Onboarding & Cross-Sell Automation]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** CUs spend $200-$500 to acquire each new member, then lose 15-25% within the first year because share-only accounts receive no proactive engagement — and the CU doesn't notice the member leaving until the account balance hits zero.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
A new member opens a share account with a $25 minimum deposit. They never set up direct deposit, never activate their debit card, and never return to the branch. After 3 months of dormancy, the CU has no mechanism to detect this at-risk trajectory. After 12 months, the member closes the account or simply abandons it. The CU discovers the attrition in a quarterly membership report — long past the point where intervention could have changed the outcome. First-year attrition is the single largest leak in the CU's member growth pipeline, costing $500K-$2M annually for a mid-size CU when factoring in acquisition cost, lost lifetime value, and the marketing spend to replace the lost member.

## Why It's Still Broken
CU core platforms track account status (open, closed, dormant) but don't measure engagement trajectory. A member with a $25 balance, no transactions, and no product adoption looks identical to a new account in the system — there's no "at-risk" flag. Member engagement scoring requires computing behavioral indicators (login frequency, transaction volume, product adoption, direct deposit presence) that core platforms don't aggregate into a single risk score. Marketing teams send retention communications on calendar-based schedules (30-day email, 60-day postcard) rather than behavior-triggered interventions.

## What a Fix Looks Like
A first-year member engagement tracker that computes a weekly engagement score for every member in their first 12 months, based on: direct deposit setup (yes/no and timing), debit card activation and usage frequency, mobile/online banking login frequency, transaction volume and diversity, and product adoption count. Members falling below engagement thresholds at specific milestones (day 14 no direct deposit, day 30 no debit card activation, day 60 single-product-only) trigger automated outreach tailored to the specific engagement gap. A branch manager dashboard shows at-risk new members for proactive personal outreach. The system learns which intervention types work for which engagement gaps by tracking intervention-to-engagement conversion rates.

## Who Feels the Pain
VP of Marketing who manages member growth targets and sees acquisition investment wasted on members who leave within a year, and branch managers whose headcount and budget depend on membership growth metrics that net attrition undermines.

## Impact If Fixed
Reduces first-year attrition from 15-25% to 8-12% through early detection and targeted intervention. For a CU acquiring 2,000 new members per year, retaining an additional 200-400 members preserves $100K-$400K in acquisition cost and $500K-$2M in lifetime membership value. Converts reactive membership reporting into proactive engagement management.
