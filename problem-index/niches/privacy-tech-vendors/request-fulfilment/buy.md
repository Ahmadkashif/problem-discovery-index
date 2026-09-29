# Buy: Orchestration and Reconciliation From Data Engineering

**Niche:** Data Subject Request Fulfilment
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering solved distributed execution with verification and reconciliation, and privacy fulfilment sends tasks to humans and records that they said yes.
**Tags:** #workflow-orchestration #evaluation-metrics #confidence-intervals #graph-theory #data-integration #automation #compliance
**Contested on:** Whether a deletion is verified across every system that holds the data, or confirmed across the systems someone remembered and could reach.

## The Problem

Performing an operation reliably across many heterogeneous systems, confirming it actually happened, and reconciling the result is the bread and butter of data engineering. Orchestration frameworks handle retries, partial failures, dependency ordering and idempotency. Reconciliation jobs verify that what was supposed to happen did. Change data capture propagates deletions downstream. Compensating transactions handle the cases where a distributed operation partially fails.

Privacy fulfilment does none of this. It is a ticketing workflow: create tasks, assign to humans, collect responses, close. The mechanism is the same one used for approving expense claims, applied to a distributed data operation with a statutory deadline.

The mismatch shows in exactly the ways an engineer would predict. Partial failures are invisible because the only signal is a human marking a task done. Downstream propagation does not happen because nothing propagates. And verification is absent because ticketing systems have no concept of checking that the work was performed.

## What Already Exists

Orchestration: Airflow, Dagster, Prefect and Temporal, with retries, idempotency, dependency graphs, partial failure handling and durable execution — Temporal in particular is designed for exactly this shape of long-running, multi-system, must-complete operation.

Change data capture: Debezium and the CDC features in modern databases, propagating changes including deletions downstream through pipelines.

Reconciliation: data quality frameworks running assertions after pipeline runs, which is structurally identical to verifying a deletion.

Entity resolution: identity resolution products and open-source record linkage libraries, which solve the subject resolution problem for customer data and are unused in privacy fulfilment.

Privacy fulfilment: the request workflow modules in OneTrust, Transcend, DataGrail and Securiti, with connectors for common SaaS systems and human task routing for everything else.

## The Customization Gap

**Human task routing where durable execution belongs.** A deletion across twenty systems is a distributed transaction with partial failure modes. Modelling it as tickets loses retries, idempotency and failure visibility, all of which orchestration frameworks provide natively.

**No verification step.** Data engineering runs assertions after every job. Fulfilment has no post-condition check, which is the single largest gap and the easiest to close with patterns borrowed directly.

**Deletion does not propagate.** CDC propagates deletions through pipelines and is used for data consistency. Nobody wires it to privacy deletion, so a row removed from the operational database persists in the warehouse and everything downstream of it.

**Entity resolution is not applied.** Identity resolution is a mature capability sold into marketing to unify customer records. The same technique finds every record belonging to a data subject, and privacy platforms use identifier matching instead.

**Idempotency and replay matter here.** A partially completed deletion must be safely re-runnable. Ticketing workflows have no such semantics, so a failed fulfilment is re-attempted by hand.

**The buyer cannot evaluate it.** Privacy operations buys the workflow and cannot assess distributed execution guarantees, which is why the category has competed on connector count rather than on reliability.

## Target Customer

The privacy platforms, who should be building fulfilment on durable execution rather than on ticketing — a rewrite of their most legally exposed workflow using patterns that are standard elsewhere.

Data engineering teams at high-volume organisations, who already build the bespoke deletion pipelines the platforms cannot and would adopt a proper framework.

Temporal or a similar durable execution vendor could plausibly package a privacy fulfilment offering, since the problem is a canonical example of what their technology is for.

## Impact If Solved

Fulfilment becomes a reliable distributed operation rather than a set of tickets, with the failure visibility and retry semantics that the statutory deadline actually demands.

A post-condition verification step is a direct import from data quality practice and would immediately distinguish deletion that happened from deletion that was reported.

And wiring change data capture to privacy deletion would propagate removals downstream automatically, which is where most surviving data actually sits and where every current process stops.
