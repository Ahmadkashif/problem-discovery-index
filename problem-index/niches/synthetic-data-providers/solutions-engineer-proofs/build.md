# Every Proof of Concept Built by Hand

**Niche:** [[niches/synthetic-data-providers/solutions-engineer-proofs/profile|The Solutions Engineer]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Solutions engineers hand-build proof-of-concept evidence for every prospect, running work that is nearly identical each time because the product ships generation and leaves demonstration to a person.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #data-integration #worker-facing #probability-distributions #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a prospect's dataset into credible evidence without a person building it by hand — and whoever does that takes the account, because proof-of-concept turnaround is what decides these deals.

## The Problem
A prospect sends a schema and a sample extract. The solutions engineer opens a notebook, profiles the tables, works out the key relationships and the obvious constraints, configures a run, looks at the output, finds the dates are wrong and the cardinalities are flat, reconfigures, runs again, builds a fidelity comparison, produces a privacy summary, assembles thirty slides, and presents on day twelve. Then the next prospect arrives with a different schema and the same sequence begins again. Nothing from the first proof is reusable except the engineer's memory.

## Why Nobody Has Built This
The work looks bespoke because each schema differs, which obscures how identical the process is. Solutions engineering headcount is a sales cost that nobody has been asked to reduce with product, and the engineers are too busy running proofs to build the tooling that would stop them running proofs. The product roadmap is owned by people optimising the customer's experience after purchase. And the proof's quality depends on tacit knowledge — which configurations work for which shapes of data — that lives entirely in a handful of people's heads.

## What to Build
Automate the proof into a pipeline with the engineer at the judgement points. Profile the prospect's schema automatically into a proposed configuration — relationships, key candidates, constraint discovery, column type inference, likely business rules — which is the part that consumes the first several days and is mechanically derivable. Build a configuration recommender from the tacit knowledge, mapping data shape to settings that have worked, since that knowledge is the engineers' real expertise and it currently leaves with them. Generate the evidence pack automatically: fidelity comparison, constraint violation report, privacy attack results, downstream task performance where a task was supplied, in a consistent format that does not need reassembling each time. Keep a proof library indexed by industry and schema shape, so the fourth insurance prospect starts from the previous three rather than from nothing. Record which proofs converted and what they contained, which is the feedback loop that improves the recommender and which no organisation currently captures. Leave the engineer the judgement — what this prospect cares about, which evidence to lead with, what the objection will be — because that is the part that is genuinely theirs. And let the prospect re-run the proof on their own data afterwards, which converts the artefact from a presentation into a trial.

## Target Customer
Vendor solutions and sales engineering organisations across the category, and the prospects whose evaluation currently takes three weeks per vendor.

## Impact If Built
The proof is a near-identical pipeline rebuilt by hand every time. Automatic schema profiling into a proposed configuration removes the multi-day opening, and capturing which proofs converted is the feedback loop that turns individual tacit knowledge into a company asset.
