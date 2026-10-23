# Behaviour Patterns That Predict the 4 p.m. Fall

**Niche:** [[niches/skilled-nursing-facilities/long-stay-dementia-residents/profile|Long-Stay Residents Living with Dementia]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Falls and distressed behaviour among residents with dementia follow daily rhythms, staffing gaps and unmet needs, and nobody puts those records side by side.
**Tags:** #survival-analysis #gradient-boosting #hidden-markov-models #feature-engineering #tacit-knowledge-ml #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to cut falls with major injury and antipsychotic use among long-stay residents with dementia, and whoever moves the MDS long-stay falls and antipsychotic measures that feed SNF VBP and Five-Star takes the account.

## The Problem
Experienced aides know that a resident gets restless in late afternoon, tries to stand when she needs the toilet, or is calmer with a particular aide. That knowledge is not written down. When the resident falls, the incident report records the location and injury, not the pattern that preceded it.

## Why Nobody Has Built This
Behaviour charting is sparse and inconsistent. Sensor vendors detect events but do not see the care record. EHR vendors hold the record but see no events. Long-stay Medicaid residents bring little revenue, so few products are built for them.

## What to Build
A per-resident model that joins behaviour entries, toileting and meal times, sleep and movement from sensors or video, staffing on the unit, medications and falls. It identifies each resident's high-risk windows and likely triggers, such as unmet toileting needs, pain, fatigue or a shift change. It produces a short care-plan prompt ("offer toileting at 3:30", "assign consistent aide") and tracks whether falls and as-needed psychotropic use fall afterwards.

## Target Customer
Chief clinical officers at chains with large long-stay populations, and dementia-care programme vendors.

## Impact If Built
Preventing ~1–2 falls with major injury a year in a 100-bed building (estimate) moves the long-stay falls measure that enters SNF VBP in FY 2027 and avoids hospital transfers. It also removes reasons to reach for an antipsychotic, all measured on the same MDS items CMS uses.
