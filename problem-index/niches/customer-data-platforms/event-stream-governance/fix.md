# The Field Whose Meaning Drifted

**Niche:** [[niches/customer-data-platforms/event-stream-governance/profile|Event Stream Governance]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The field is still a string, still populated, still passing validation, and since the refactor it contains something different from what every downstream consumer assumes.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #data-integration #automation #quick-win #compliance #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the event stream a contract product teams cannot break by accident — and whoever does that removes the failure mode that silently corrupts everything downstream.

## The Problem
A status field used to contain one of four values. After a refactor it contains one of eleven, including two that mean roughly what one of the original four meant. Every schema check passes: it is still a string, still present, still non-null. Segments defined on the old values now match fewer people, a journey condition silently evaluates false for a third of customers, and a report's categories shift. Nobody has done anything wrong by the standards of any validation the organisation runs. Structural checking cannot see this class of change, and it is the most common way a customer data stack silently becomes incorrect.

## Why It's Still Broken
Validation checks types and presence because that is what schemas express, and meaning is not in the schema — the contract captures the shape and not the semantics, which is where the breakage lives. A value distribution shift looks like a business change rather than a defect. Downstream consumers assume meanings that were never written down. And the failure produces plausible numbers rather than errors.

## What a Fix Looks Like
Monitor meaning as well as shape. Profile each field's value distribution continuously and alert on significant shifts, which is the fix, requires no schema change, and catches the class of failure that structural validation cannot see. Enumerate categorical values in the contract so a new value is a contract change rather than a surprise, which converts the most common case into something checkable. Record the intended meaning alongside the schema, since the assumption downstream consumers make is currently held nowhere and cannot be verified by anyone. Alert on distribution shifts in the fields that segments actually depend on, so the alerting is prioritised by consequence rather than firing on everything. Compare against the downstream effect, since a shift that changes no audience membership is uninteresting and one that empties an audience is urgent. Flag new values appearing in a field with known members, which is nearly always a deliberate code change with unexamined consequences. Ask the producing team to confirm intent when a distribution moves, which is a short conversation that resolves it correctly. Track which fields have drifted historically, since the same ones recur. Include semantic checks in the same build gate as structural ones where possible, and where not, run them continuously. And measure the interval between a meaning change and its detection, because everything computed in between is wrong in a way nobody will ever correct.

## Who Feels the Pain
Analysts whose numbers shift for reasons nobody can find; marketing teams whose audiences quietly change composition; and organisations whose customer data is incorrect in ways that pass every check they run.

## Impact If Fixed
The contract captures shape and not semantics, so a field that changes meaning passes every validation and breaks everything downstream. Continuous value distribution profiling catches it with no schema change, and enumerating categorical values makes the most common case checkable.
