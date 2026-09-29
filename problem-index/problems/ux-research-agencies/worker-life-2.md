# Research Operations and the Scheduling Machine

**Industry:** [[ux-research-agencies|UX Research Agencies]]
**Type:** Worker Life Changing
**One-liner:** One person keeps the participant pipeline, the consent paperwork, the incentive payments and the calendar working for every study in the agency, and everything upstream stops when any of it breaks.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #large-language-models #evaluation-metrics #worker-facing #workflow-orchestration #compliance

## The Problem
Research operations is the function that makes studies happen. Screener fielding, participant selection, scheduling across time zones, rescheduling when people drop, consent forms and the data handling that goes with them, incentive payment across countries and payment methods, tool licences and access, and the repository nobody else maintains.

The work is high-volume and interrupt-driven. A participant cancels an hour before a session and a replacement has to be found from the qualifying pool, which is small because the criteria were demanding. No-show rates are substantial and vary by population in ways nobody has quantified, so every study over-recruits by a guess. Incentive payment fails for a participant in a country the payment provider handles badly, and that becomes a two-week correspondence.

Consent and data handling carry real obligation. Recordings of identifiable people, sometimes discussing sensitive matters, with retention commitments and deletion requirements, in an agency working across several client jurisdictions. The research operations person is usually the only one tracking it.

And everything is urgent, because a study has a fieldwork window and a readout date, and the whole timeline collapses backwards onto recruitment.

## Why It Matters to the Worker
This is the role that absorbs every other role's timeline risk. Researchers set readout dates, clients set availability windows, and research operations is left to make the participant supply meet both. When it works, nobody notices; when a session slot goes unfilled, it is visible immediately and attributed here.

The interrupt load is the specific damage. The job cannot be batched — a cancellation at eleven has to be solved by twelve — so it fragments the day completely and leaves no room for the process improvement that would reduce the interrupts.

And the compliance exposure sits with a person who usually has no legal support. Deciding whether a recording can be shared with a client, how long it may be retained, and what a participant consented to are judgement calls with real consequences, made quickly, alone.

## What a Solution Looks Like
Forecast the pipeline instead of guessing at it. No-show and dropout rates are predictable from population, incentive, session length, lead time and prior participation history, and a study that over-recruits by a modelled amount rather than a habitual one wastes fewer incentives and misses fewer slots. Predicting which specific bookings are likely to drop allows a reminder or a standby to be arranged before the gap opens.

Automate the sequence. Screener distribution, selection against criteria, scheduling, reminders, rescheduling, and incentive disbursement are a workflow with clear rules and heavy manual execution.

Make consent and retention a system property. What each participant agreed to, what may be shared with which client, retention clocks and deletion obligations should be tracked and enforced automatically, not remembered — this is both a compliance improvement and the removal of a burden the person carries personally.

Handle the payment failures. Cross-border incentive payment fails in predictable ways by country and method, and routing around the known failure modes rather than discovering them per participant removes a recurring two-week correspondence.

## Impact If Solved
Research operations is a single point of failure for an entire agency's delivery, performed under constant interruption with no forecasting and personal exposure on compliance. Pipeline prediction and workflow automation address the interrupt load directly; systematising consent and retention removes an individual's liability for something that should be infrastructure. Both determine whether the studies upstream actually run on time.
