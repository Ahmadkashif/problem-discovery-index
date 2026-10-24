# The Competency Assessments Done the Week Before the Inspector Arrives

**Niche:** [[niches/clinical-laboratories/physician-office-small-labs/profile|Physician Office & Small Independent Labs]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** Every tester's competency must be assessed on every test system on a fixed schedule, and in small labs it gets done in a rush when an inspection date is announced.
**Tags:** #compliance #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a small moderate-complexity lab inspection-ready on a part-time director's hours, and whoever gets it through its two-yearly inspection with no condition-level deficiency takes the account.

## The Problem
CLIA requires competency assessments for testing personnel semiannually in the first year and annually after that, covering direct observation, result review, QC and maintenance records, blind samples and problem-solving (42 CFR 493.1413 for moderate-complexity testing). In a small lab with staff turnover, these lapse quietly and become one of the most common inspection findings.

## Why It's Still Broken
Assessments are paper forms filled by a supervisor who is also testing patients. Due dates live in someone's calendar, and records of the evidence (which QC review, which PT sample) are scattered.

## What a Fix Looks Like
Track each person's due dates by test system. Assemble the evidence automatically from QC reviews, maintenance logs and PT results already recorded, and prompt the supervisor for the observation and problem-solving elements during normal work. Present a finished form for signature well before it is due.

## Who Feels the Pain
Supervisors doing paperwork at night, testers whose records are incomplete through no fault of their own, and directors who sign what they could not check.

## Impact If Fixed
An inspection finding avoided and roughly a day of supervisor time saved per assessment cycle (estimate) for a lab with four testers and five test systems.
