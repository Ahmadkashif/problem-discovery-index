# Plan Rules That Live Only in Legacy Code

**Niche:** [[niches/pension-funds/pension-administration-system-modernisation/profile|Pension Administration System Modernisation]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Requirements for a new PAS are written from statute and staff interviews, and the provisions that only the old code knows about are discovered during testing or after go-live.
**Tags:** #large-language-models #transformers #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to move decades of member service, salary and contribution history into a new system that calculates every benefit the old one did, and whoever goes live with the fewest payment errors in the first retiree payrolls takes the account.

## The Problem
Forty years of legislative changes, board policies, court settlements and one-off fixes accumulate in the legacy system's code and in the habits of senior benefits staff. Requirements documents capture what people remember. The rest emerges as defects.

## Why It's Still Broken
Legacy code is in COBOL or older 4GLs that few current staff can read, and the people who wrote the patches have retired. Projects budget requirements gathering as interviews, not code analysis.

## What a Fix Looks Like
Before requirements are signed, run language-model-assisted analysis of the legacy code to extract every benefit-affecting rule with its code location. Reconcile the list against statute, policy and the requirements, and have benefits staff confirm each unmatched rule as current, obsolete or a defect.

## Who Feels the Pain
Project managers whose schedules slip in testing; senior benefits analysts asked to remember decades of exceptions; retirees whose benefit changes at conversion.

## Impact If Fixed
Hidden rules are found in months one to six of the project rather than in year four, when they are most expensive to fix.
