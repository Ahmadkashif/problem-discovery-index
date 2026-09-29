# The Engineer Asked to Delete From Systems That Cannot Delete

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Worker Life Changing
**One-liner:** The workflow tool routes a deletion request to an engineer whose warehouse has no deletion path, whose backups are immutable by design, and whose logs were never meant to be queried by person.
**Tags:** #graph-neural-networks #gradient-boosting #large-language-models #confidence-intervals #change-point-detection #evaluation-metrics #worker-facing #compliance

## The Problem
A deletion request arrives at a privacy platform, which orchestrates it across connected systems and routes the rest to people. The rest is substantial: analytics warehouses where the person appears across many derived tables, logs that contain identifiers and were built for append-only retention, backups designed to be immutable, machine learning training sets and the models fitted on them, third-party processors with their own request processes, and internal tools nobody registered.

The engineer receiving this is being asked to do something the systems were not built for. Deleting a row from a warehouse means finding every derived table, every materialised view and every export. Deleting from backups conflicts with the properties backups exist to have. Removing an individual's contribution from a trained model is, in the general case, not something anyone knows how to do.

So the work is scripts, judgement and documented limitations. The engineer writes a query, deletes what they can find, and someone records the request as fulfilled — with the coverage of that fulfilment unstated.

And it recurs. Every request repeats the work, because the previous one produced a script rather than a capability.

## Why It Matters to the Worker
This is an engineer being asked to make a legal guarantee about a system that cannot support it, on a statutory clock, with no good option. Saying the deletion is complete when it covers the systems they could reach is the normal practice and is a position nobody is comfortable in.

The work is unplanned and non-negotiable. Requests arrive continuously with a deadline, and they interrupt roadmap work with a priority the engineer cannot argue with.

The architectural fix — building deletion capability into the data platform — is a substantial project that is hard to justify against features, so the manual work continues indefinitely and the engineer knows it is the wrong solution.

And the accountability is ambiguous in a way that eventually resolves badly. The privacy team records fulfilment, the engineer knows what was actually covered, and if the gap is ever tested the engineer's script is the evidence.

## What a Solution Looks Like
Make coverage explicit. A fulfilment record should state which systems were reached, which were partially reached, which were excluded and why — so the organisation knows its real position rather than a binary confirmation. That is uncomfortable and it is the truth, and it is the precondition for prioritising the fix.

Derive the reach from the data lineage. If the flow graph exists, the set of places a person's data reached is computable rather than remembered, which is both more complete and repeatable.

Build capability rather than scripts. Deletion as a supported operation in the warehouse — identifier propagation to derived tables, deletion-aware materialisation, retention policies on logs, crypto-shredding for backups where deletion is impossible — is the engineering answer, and the recurring manual cost is the business case that nobody has quantified.

Handle models honestly. Removing an individual's influence from a trained model is unsolved in the general case, and the defensible positions — retention limits on training data, retraining cadences, documented limitations — should be stated as policy rather than left to an engineer to improvise per request.

And measure the recurring cost. Engineering hours spent per request, across a year, is the number that justifies the architectural work and is not currently recorded anywhere.

## Impact If Solved
Deletion obligations meet infrastructure that was not designed for them, and the gap is absorbed by engineers writing scripts and privacy teams recording confirmations. Explicit coverage reporting, lineage-derived reach, and treating deletion as a platform capability rather than a per-request task would make fulfilment real — and quantifying the recurring manual cost is what would finally justify building it properly.
