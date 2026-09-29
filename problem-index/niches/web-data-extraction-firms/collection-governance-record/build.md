# No Continuous Record of What Is Being Collected

**Niche:** [[niches/web-data-extraction-firms/collection-governance-record/profile|Collection Governance Record]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Robots parsers, rate limiters and legal review processes all exist, and no firm maintains a continuous, queryable record of what it is collecting from where, under what permission, for whose stated purpose.
**Tags:** #compliance #data-integration #graph-theory #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to maintain a continuous, queryable account of what is being collected, from where, under what permission and for whose purpose — and whoever does that takes the account, because it is the evidence that makes the whole business defensible.

## The Problem
A firm receives a letter from a target site's counsel. To respond they need to know what they have collected from that host, over what period, at what rate, under which customer's account, for what stated purpose, and what the site's terms and robots directives said at each point in that period. Every element exists — in request logs, in an onboarding document, in a customer contract, in nobody's archive of the site's historical terms — and assembling it takes a week of engineering and produces an incomplete answer. The firm cannot describe its own activity, which is an untenable position for a business whose principal risk is precisely that activity.

## Why Nobody Has Built This
The record spans legal, sales and engineering, and belongs to none of them. Logs were built for billing and debugging rather than for governance, so the joins are awkward. Historical terms and directives were never archived, which makes retrospective reconstruction genuinely impossible rather than merely hard. And the record's absence only hurts when somebody asks, which is rare enough to keep the work below the line and catastrophic enough when it happens.

## What to Build
Assemble the record from the traffic. Join request logs to the approval that authorised them, so every request traces to a customer, a job, a declared purpose and a review decision — which is the structural piece and requires an identifier carried through the pipeline rather than any new data. Archive each target's robots directives and terms of service continuously with timestamps, so the firm can state what the site said at the time of collection rather than what it says now, which is the single most valuable artefact here and is trivially collectible going forward. Maintain a live per-host inventory: what is collected, at what rate, for whom, since when. Record the customer's declared purpose in structured form and make it queryable, since purpose determines permissibility and currently lives in prose. Detect change in a target's directives or terms and raise it against the collections it affects, which the fix note develops. Make the whole thing queryable, so a question about one host is answered in minutes rather than a week. Support immediate suspension of a collection by host, customer or purpose, since the ability to stop is part of being able to defend. And retain it as evidence, because the record's value is that it exists contemporaneously rather than being reconstructed under pressure.

## Target Customer
Extraction firms and their leadership, their legal and compliance functions, their customers who inherit the risk, and the target sites on the other side.

## Impact If Built
A business whose principal risk is its own activity cannot currently describe that activity. Archiving targets' directives and terms with timestamps is trivially cheap going forward and is the artefact that lets a firm state what a site permitted at the time rather than now.
