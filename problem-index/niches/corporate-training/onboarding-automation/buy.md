# Role-Specific Training Path Auto-Assignment

**Niche:** [[niches/corporate-training/onboarding-automation/profile|Employee Onboarding Automation]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** LMS platforms like Cornerstone and Docebo support learning paths, but assigning the right path to each new hire based on role, department, location, and compliance requirements requires manual L&D intervention for every hire.
**Tags:** #automation #data-integration #quick-win #workflow-orchestration

## The Problem
An L&D administrator at a 2,000-person company must manually determine and assign the correct training path for each new hire. A sales rep in California needs: company orientation, product training, Salesforce training, CA-specific sexual harassment training, and sales methodology training. A software engineer in Texas needs: company orientation, security awareness, engineering onboarding, CI/CD pipeline training, and TX-specific workplace safety training. With 50+ roles across 10+ states, the L&D admin maintains a lookup table mapping role + location to training path and manually creates the assignment in the LMS for each hire. This takes 15-30 minutes per new hire and errors (wrong training assigned) are discovered weeks later.

## What Already Exists
Cornerstone, Docebo, and Absorb all support learning path creation and assignment. Most provide some rule-based auto-assignment capability (assign path X to all users in group Y). HRIS platforms (BambooHR, Workday) maintain role and location data.

## The Customization Gap
The missing piece is a dynamic rule engine that: (1) pulls role, department, location, and compliance-relevant attributes from HRIS in real time; (2) evaluates against a maintained rule set (role + location + department = specific training path); (3) auto-assigns the correct learning path in the LMS on the hire's start date; (4) handles edge cases (dual-role employees, temporary assignments, mid-year state transfers) without manual intervention; and (5) audits assignments against compliance requirements to flag gaps before they become audit findings.

## Target Customer
L&D administrators at companies with 500+ employees across multiple locations and roles who spend 15-30 minutes per new hire on manual training path assignment and risk compliance gaps from incorrect assignments.

## Impact If Solved
Eliminates 15-30 minutes of L&D admin time per new hire (250-500 hours annually at a company hiring 1,000/year), reduces training assignment errors from 5-10% to near zero, and ensures compliance training coverage from Day 1 rather than discovered retroactively during audits.
