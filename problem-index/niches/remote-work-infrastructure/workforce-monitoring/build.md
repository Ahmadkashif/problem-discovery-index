# Build: Output Measurement Instead of Activity Measurement

**Niche:** [[niches/remote-work-infrastructure/workforce-monitoring/profile|Workforce Monitoring]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure what was produced and delivered rather than whether the mouse moved, from the systems where the work actually happens.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #data-integration #causal-inference #worker-facing #compliance
**Contested on:** Whether output can be measured for knowledge work without reducing to activity again.

## The Problem

An employer wants to know whether remote work is working. What they buy is activity tracking, which tells them how many keystrokes occurred and what applications were open. Neither is an answer to their question.

The measures are also weak on their own terms. They are defeated trivially, they penalise work that involves thinking rather than typing, they penalise reading, and they correlate with role and tooling far more than with contribution. A productivity score assembled from application categorisation tells you that a designer spends time in design software, which everyone knew.

What an employer actually wants is delivery: was the work done, to standard, on time. That signal lives in the systems where the work happens — the ticket tracker, the repository, the CRM, the document store, the support queue — and is largely unused because it is harder to package than a keystroke count.

## Why Nobody Has Built This

Activity tracking is easy to build, easy to demo and universal across roles. Output measurement is role-specific, requires integrating the systems where work happens, and produces a different measure for every function — which is a much harder product.

The demand is also partly not for measurement. Some monitoring deployment is about reassurance and control rather than information, and a tool that produced an honest output measure would not satisfy a buyer who wants to see that people are at their desks.

And the vendors have no incentive to validate, because a validation study would probably show the score predicts little.

## What to Build

Delivery measurement from the systems of record, with the limits stated.

**Measure at the work object, not at the keyboard.** Tickets closed and their cycle time and rework rate. Code merged and reverted. Documents produced and used. Support contacts resolved and reopened. Deals progressed. Every function has a system of record and the delivery signal is in it.

**Define the measure with the team, per role.** What counts as delivery differs by function and imposing a single measure across an organisation reproduces the problem activity tracking has. The definition exercise is the work and it is also valuable on its own, because most teams have never articulated it.

**Report at the team level by default.** Individual output measurement in knowledge work is noisy, confounded by task allocation, and corrosive. Team-level delivery over a period is far more robust and is what most questions actually concern.

**State what the measure cannot see.** Mentoring, review, unblocking others, design work that produces no artefact for weeks, and the unglamorous maintenance nobody tickets. A delivery measure that is presented as complete will drive exactly the behaviour that starves those activities, and saying so is what prevents it.

**Validate the claim.** Does the measure correlate with manager assessment, with peer assessment, with the team's own view of a good period. This is a modest study and no monitoring vendor has ever published one.

**Replace rather than add.** The argument for this is that it answers the question activity tracking does not, and it only works if the activity tracking goes away — otherwise the organisation has two measures and the intrusive one wins because it is simpler.

## Target Customer

Employers deploying monitoring who have realised the score does not answer their question, and platforms whose clients ask for monitoring and who would rather offer something defensible. Also the monitoring vendors themselves, for whom output measurement is the only route out of a category whose evidence base is deteriorating.

## Impact If Built

The employer gets a measure of what was delivered rather than of whether someone was moving. The measurement moves to the team level where it is robust. Its limits are stated, which prevents it starving the work it cannot see. And a measure that is actually about the question replaces one that is trivially defeated and corrosive to trust.
