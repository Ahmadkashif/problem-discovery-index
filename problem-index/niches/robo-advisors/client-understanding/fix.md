# A Risk Score From 2019

**Niche:** [[niches/robo-advisors/client-understanding/profile|Client Understanding]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The client answered six questions before their first market event and has been allocated from those answers ever since.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #automation #confidence-intervals #compliance #workflow-orchestration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to know the client well enough to keep them invested — and the contest splits cleanly enough that it is not terminal.

## The Problem
A client signed up in a calm market, answered six questions about how they would feel about a twenty percent decline, and received a risk score. They have since lived through a real decline, changed jobs, had a child, and sold half their portfolio at the bottom and bought back three months later. The score is unchanged. The platform knows all of it and has never reconciled any of it with the number that determines their allocation.

## Why It's Still Broken
The questionnaire is completed at onboarding because that is where suitability documentation belongs, and nothing in the process was ever designed to revisit it — the artefact is dated by design. Re-asking feels like friction in a product optimised for frictionlessness. Changing an allocation on inferred grounds raises a supervision question. And nobody reports how stale the scores are.

## What a Fix Looks Like
Revisit the number and show the client the evidence. Report the age distribution of risk scores, which is the fix's starting point and is one query — the result will be uncomfortable and will make the case on its own. Prompt for review after a client's first real drawdown, since that is when a self-report finally has something to be based on. Show the client what they actually did against what they said they would do, because most people do not know and the comparison is the most useful thing the platform could tell them. Trigger review on life events the platform can observe — funding changes, goal edits, large withdrawals — rather than on a calendar. Ask fewer, better questions, as six generic items produce a number with little information in it. Record the reason for every score change, which is both a supervision requirement and the data needed to learn from it. Flag the clients whose behaviour contradicts their score, since they are the ones at risk and they are identifiable today. Keep the inferred and stated scores side by side rather than replacing one with the other, which sidesteps the supervision question while still using the evidence. Make review a two-minute interaction, because the friction argument is real and is only an argument against a bad implementation. And measure how many clients have ever had a score updated, which is the number that shows whether any of this took.

## Who Feels the Pain
Clients allocated from a stale self-report; service associates explaining an allocation that no longer fits; supervisors reviewing suitability on dated evidence; and platforms whose retention depends on a number nobody maintains.

## Impact If Fixed
The questionnaire is dated by design because suitability documentation belongs at onboarding. Prompting after a client's first real drawdown — and showing them what they actually did — turns an artefact into a measurement.
