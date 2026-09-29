# Build: Continuous Fieldwork

**Niche:** Fieldwork Delivery
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Test controls throughout the period from connected evidence rather than in a concentrated window, so capacity spreads, exceptions surface while they can still be remediated, and the associate's month is not a crisis.
**Tags:** #evaluation-metrics #confidence-intervals #time-series-forecasting #compliance #automation #workflow-orchestration #data-integration #worker-facing
**Contested on:** Whether fieldwork is spread across the period or compressed into a window.

## The Problem

An engagement is structured as a period of fieldwork. The period ends, evidence is requested, testing happens over several weeks, exceptions are discussed, and the report is issued.

That structure made sense when evidence had to be requested and produced. It produces three problems now.

Capacity concentrates. Most clients' periods end at similar times, so the firm's fieldwork demand is heavily seasonal, which means the same staff work extreme hours for several months and are underutilised for others.

Exceptions arrive too late to fix. A control that failed in month three is discovered in month fourteen, by which point the period is closed and the exception is in the report. Both parties would have preferred to know in month three.

And the work is compressed into the worst possible shape — bulk evidence requests, waiting, chasing, then intense testing — rather than spread.

Testing continuously is available for most controls. The same integration that would enable full-population testing enables it throughout the period, which means a control failure surfaces within days.

## Why Nobody Has Built This

**The engagement model is point-in-time.** Fees, scheduling, client expectations and the report itself are all built around a period examined afterwards.

**Continuous testing sounds like more work.** Testing throughout the period appears to cost more than testing once, until the automation is in place, at which point it costs less.

**The client may not want early warning.** A control failure discovered in month three must be remediated or it becomes an exception, which is more work for the client than discovering it when the period is closed and the exception is unavoidable.

**Fee structures do not accommodate it.** A fixed fee for a period-end engagement does not naturally extend to continuous monitoring, and the commercial model would need to change.

**Independence questions arise.** An auditor testing continuously and flagging failures for remediation edges toward advising, which is a real professional boundary that needs careful handling.

**Nobody measures the seasonality cost.** Overtime, quality variation and attrition during peak periods are not tracked against the concentration that causes them.

## What to Build

**Test connected controls monthly.** For every control whose population comes through an integration, run the test each month rather than once. The work is automated, the result accumulates, and the period-end engagement becomes a review of accumulated evidence rather than a testing exercise.

**Surface exceptions immediately, with a defined boundary.** A control failure flagged within days, reported to the client, with the auditor stating the fact and not the remedy — which keeps the independence line clear while giving the client the chance to act.

**Reserve fieldwork for the unautomatable.** Interviews, walkthroughs, judgement-dependent controls and anything without connected evidence. These are a fraction of the programme and are the part that genuinely needs an associate on site.

**Restructure the fee.** A continuous engagement priced as an annual subscription rather than as a period-end project, which is a better commercial fit and smooths the firm's revenue as well as its capacity.

**Smooth the capacity deliberately.** With testing distributed, staffing can be level rather than seasonal, which is the change that most improves the associate's experience.

**Report the trend, not the snapshot.** Continuous testing produces a picture of how controls operated over time rather than a binary at the end, which is more informative and is available once the testing is continuous.

**Track hours against fee honestly.** The overrun currently absorbed by associates should appear in the firm's own reporting, because it is the number that justifies restructuring the delivery model.

## Target Customer

Audit firm operations and practice leadership, for whom seasonal capacity concentration is the central delivery problem and continuous testing is the only structural answer.

Clients with mature compliance platforms, who already have the continuous evidence and would prefer early warning of a control failure to an exception in a report.

Compliance platform vendors, for whom auditor-facing continuous testing is an obvious extension and would make their customers' audits cheaper.

## Impact If Built

Capacity spreads across the year, which addresses the seasonal concentration that drives the overtime, the quality variation and the attrition in this industry.

Exceptions surface while they can still be remediated, which is better for the client than discovering them in a report and is the strongest commercial argument for the change.

And the period-end engagement becomes a review of accumulated evidence rather than a compressed testing exercise, which is a fundamentally better use of the scarce senior time it currently consumes.
