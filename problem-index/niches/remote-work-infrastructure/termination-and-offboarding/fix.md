# Fix: The Client's Date Drives the Process

**Niche:** [[niches/remote-work-infrastructure/termination-and-offboarding/profile|Termination & Offboarding]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** The client says the last day is the 31st, and the jurisdiction's notice period makes that date unlawful, and nobody says so until it is too late to change.
**Tags:** #compliance #descriptive-statistics #workflow-orchestration #evaluation-metrics #confidence-intervals #quick-win #worker-facing #data-integration
**Contested on:** Whether the earliest lawful date will be stated before anyone commits to a different one.

## The Problem

A client decides to end an engagement and sets a date. It is chosen from their own planning — the end of a quarter, a budget cycle, the completion of a handover — and communicated to the platform as a requirement.

In the worker's jurisdiction that date may be impossible. The statutory notice period given the worker's tenure may run past it. A required consultation may take weeks. A protected status may block it entirely. A process step may have a mandatory waiting period.

By the time this surfaces, the client has told the worker's manager, planned the backfill and in some cases told the worker. Unwinding is expensive and embarrassing, so the pressure runs toward finding a way to make the date work — which is where the unlawful shortcuts happen.

## Why It's Still Broken

The date arrives as a statement rather than as a question, and the platform's account and operations teams receive it as an instruction from the customer.

The earliest lawful date is computable at the moment the client first asks — from the worker's tenure, contract, jurisdiction and status — and nobody computes it, because there is no point in the flow where the question is asked before the date is set.

And the person receiving the request is commercially aligned with accommodating it.

## What a Fix Looks Like

Compute the earliest lawful date first, and make it the starting point.

Put a date calculator at the front of the termination flow. Before the client commits to anything: worker, jurisdiction, tenure, contract type, reason — and the system returns the earliest lawful last day with the components shown, notice period, required steps and their durations, and any blocking status. Two minutes, before the decision hardens.

Check protected status at the same moment. Pregnancy, parental or sick leave, a recent protected complaint, union role — from the platform's own records, with a clear statement where one applies. This is the check most often skipped and most serious when missed.

State the severance and final pay up front. Clients frequently do not know that statutory severance applies or how large it is, and finding out after the decision produces pressure to restructure the termination in ways that are worse.

Make the date a system output, not a field. The client selects from lawful dates rather than typing one. This single interface decision removes the entire dynamic.

Escalate any request to complete before the earliest lawful date to legal rather than to operations, automatically. That is the moment the error happens and it should not be resolvable by an account manager.

And record the advice given. Where a client pressed for an earlier date and was told it was unlawful, that exchange is the evidence that matters if the termination is later challenged, and it currently lives in an email thread.

## Who Feels the Pain

Workers terminated with insufficient notice, no consultation or missing severance, who frequently do not know their own entitlement and so do not contest. Clients, who set a date in good faith and acquire a tribunal claim. Platform operations staff, caught between a customer's instruction and a legal requirement. And the platform, carrying the liability as the legal employer.

## Impact If Fixed

The earliest lawful date is known before anyone commits to a different one, which removes the pressure that causes the shortcuts. Protected status is checked at the start rather than discovered. And the request to do it anyway reaches legal rather than being resolved by whoever owns the account.
