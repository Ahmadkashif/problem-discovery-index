# Flight Recorder Patterns From Other Systems

**Niche:** [[niches/database-platform-vendors/database-support-engineer/profile|The Database Support Engineer]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Always-on low-overhead recording with a circular buffer and event-triggered retention is a proven pattern in runtimes, aircraft and operating systems, and databases discard their state every second.
**Tags:** #descriptive-statistics #change-point-detection #monte-carlo-methods #graph-theory #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor that takes this seriously is fighting to capture the state that explains an incident while the incident is happening — and whoever does that takes the support organisation, because reconstruction after the fact is most of what database support does.

## The Problem
The flight recorder pattern is well established: record continuously into a bounded circular buffer at low overhead, and persist the buffer when something interesting happens. Aircraft use it, several language runtimes ship it, operating systems provide tracing frameworks built on it, and its overhead characteristics are well understood. Databases expose their diagnostic state live and record almost none of it, so the buffer that would have contained Tuesday's four minutes never existed.

## What Already Exists
Runtime flight recorder implementations with documented low overhead; operating system tracing frameworks with dynamic enablement; circular buffer designs; sampling profilers; and the extended event and wait event infrastructure several database engines already include but rarely enable by default. The pattern and much of the machinery exist inside these engines already.

## The Customization Gap
The adaptation is to database state rather than to execution traces. It requires: (1) selecting what to record, since the useful state is a mixture of point-in-time snapshots — the session list, the lock graph — and event streams, and a pure event trace misses the structural picture that explains a blocking cascade; (2) overhead low enough to be always on, because a recorder that must be enabled after the first incident misses the first incident, and enabling it permanently is the entire point — which constrains the sampling rate and the capture set; (3) trigger conditions specific to database failure modes, since the conditions that precede a lock cascade, a plan flip and a connection exhaustion are different and each warrants a different capture; (4) bounded and predictable resource use, because a diagnostic mechanism that contributes to an incident under load is worse than none and this is the failure mode most likely to discredit it; and (5) redaction, since captured queries contain parameter values and the capture may leave the customer's boundary for support.

## Target Customer
Database engine developers, managed service vendors, database monitoring vendors, and the support organisations who would receive the output.

## Impact If Solved
A proven pattern with well-understood overhead addresses exactly this gap and several engines already contain most of the machinery without enabling it. Always-on operation is the property that matters, since a recorder enabled after the first incident is a recorder that missed it.
