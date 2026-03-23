# Background-Check-to-Job-Match Eligibility Engine

**Niche:** [[niches/staffing-agencies/returning-citizens-staffing/profile|Returning Citizens (Ex-Offender) Staffing]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No staffing tool can take a candidate's criminal record profile, apply the relevant jurisdiction's rules, and identify which open job orders they are eligible for — this matching is done manually by experienced reentry counselors.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #worker-facing

## The Problem
A reentry candidate walks into a staffing program with a specific criminal history: conviction type, severity level, time since conviction, jurisdiction. The staffing coordinator must determine which employers and job types are accessible given this record. This requires knowing: the employer's background check policy (many large employers have "second chance" policies but the details are informal), the applicable jurisdiction's rules (some cities restrict consideration of records older than 7 years, some states ban felony questions on applications), industry-specific licensing restrictions (a fraud conviction bars securities licensing, a drug felony bars pharmacy employment), and client-specific exclusions. Today, an experienced coordinator navigates this manually using personal knowledge, phone calls to employer HR departments, and trial-and-error (submitting a candidate and seeing if they pass the background check). Each placement requires 2-4 hours of eligibility research.

## Why Nobody Has Built This
The rules matrix is enormous: 50 state laws + hundreds of local ordinances + employer-specific policies + industry licensing requirements, all of which change regularly. No single data source contains all relevant rules. Building this requires compiling and maintaining a regulatory database that maps conviction categories to employment eligibility across jurisdictions and industries — a legal research project as much as a technology challenge. The market (reentry staffing programs) is small and typically funded by grants with limited technology budgets.

## What to Build
An eligibility matching engine that takes a structured representation of a candidate's criminal record (conviction type/category, severity, date, jurisdiction) and matches it against: (1) a database of employer background check policies and exclusion criteria, (2) state and local fair-chance hiring laws, (3) industry-specific licensing restrictions, and (4) client-specific requirements for each open job order. The output is a ranked list of eligible job orders with confidence scores and the specific basis for eligibility or exclusion. The system maintains a regulatory update feed to keep the rules database current.

## Target Customer
Reentry staffing coordinators at community organizations and second-chance staffing agencies who currently spend 2-4 hours per candidate researching eligibility for specific employers and job types.

## Impact If Built
Reduces placement research time from 2-4 hours to 15-30 minutes per candidate, increases placement rates by 25-40% by identifying eligible opportunities that coordinators would have missed, and reduces the demoralizing cycle of submission-rejection that discourages reentry candidates.
