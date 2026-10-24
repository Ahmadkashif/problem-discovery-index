# Screening-to-Exam Referral Tracker

**Niche:** [[niches/optometry-practices/medicaid-childrens-vision/profile|Medicaid Children's Vision & School-Screening Follow-Up]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tracker that takes each failed screening from a school or paediatric office, finds an in-network optometrist, books the exam with the family, and reports completion back.
**Tags:** #logistic-regression #gradient-boosting #large-language-models #workflow-orchestration #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get children who fail a vision screening through a full eye exam, and whoever completes exams for the highest share of referred children takes the account.

## The Problem
Schools and paediatricians screen millions of children, but the referral is a piece of paper. Nobody knows how many referred children ever see an eye doctor, and the practices that accept Medicaid see only those whose families push through.

## Why Nobody Has Built This
The handoff crosses four parties with no shared system: school, family, Medicaid plan and practice. Margins are thin for each. Privacy rules for school and health data differ (FERPA and HIPAA), and the money is spread across state programmes.

## What to Build
Intake of screening referrals with consent. Benefit lookup by state and plan. Matching to nearby in-network optometrists with open paediatric slots. Booking and reminders by text in the family's language, with a no-show risk model that triggers extra outreach. Completion reporting to the school and plan.

## Target Customer
Medicaid managed-care plans and their vision administrators, school districts with vision programmes, and practice groups serving Medicaid children.

## Impact If Built
Raising exam completion among ~2,000 referred children in a district from ~40% to ~60% would get ~400 more children examined a year (estimate).
