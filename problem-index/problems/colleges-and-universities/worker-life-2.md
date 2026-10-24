# The Advisor With Four Hundred Students and an Alert Queue

**Industry:** [[colleges-and-universities|Colleges & Universities]]
**Type:** Worker Life Changing
**One-liner:** An academic advisor responsible for several hundred students receives more early-alert flags than they can follow up, cannot tell which ones matter, and finds out which students were really in trouble when they fail to register.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #evaluation-metrics #worker-facing #workflow-orchestration #quick-win

## The Problem
A professional advisor at a public university commonly carries ~300–450 students (estimate). Their tools are a student success platform (EAB Navigate360, Starfish, Civitas, Stellic), the SIS degree audit and the learning management system. Faculty raise early alerts for missed assignments and poor midterm grades. The platform adds risk scores. Holds for unpaid balances, missing immunisation records and unsubmitted forms pile up in the SIS. In week six of a semester an advisor can face dozens of new flags, many of them about the same students, some about students already handled, and the risk score does not say why a student is flagged or what would help.

Meanwhile the students most at risk often send no signal the system is built to catch. They stop logging into the LMS, their financial aid is short for spring because of a satisfactory academic progress problem, they have a hold that blocks registration, or a family situation has changed. Experienced advisors learn to spot these patterns, from the tone of an email or a student who stops replying, and they cannot pass that skill on to a new colleague.

## Why It Matters to the Worker
Advisors went into the work to help students finish, and the caseload turns it into triage by inbox. Every student who stops out unseen feels like a personal failure, even when the advisor never had time to reach them. The administrative half of the job — logging notes, clearing holds, rebuilding degree plans after a change of major — eats the hours that would go to the conversations that change outcomes. Turnover among advisors is high, which breaks the continuity students need.

## What a Solution Looks Like
One prioritised list per advisor per week, ranked by the likelihood that each student fails to re-enroll next term and by what the advisor can do about it. Each entry explains itself: the LMS inactivity, the hold, the aid shortfall, the faculty comment. It ships with a drafted outreach message the advisor edits rather than writes, and the follow-up note logged automatically from the conversation. The list is capped at what one advisor can actually work in a week.

## Impact If Solved
An advisor who spends the week on the thirty students most likely to stop out, rather than the first thirty flags in the queue, reaches students while help still works. Even a one-point gain in term-to-term persistence at a university of 20,000 keeps ~200 students enrolled (estimate). The advisor also gets back several hours a week of note-taking and hold-chasing.
