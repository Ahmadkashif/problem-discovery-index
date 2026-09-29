# The Proof That Cannot Leave the Prospect's Network

**Niche:** [[niches/synthetic-data-providers/solutions-engineer-proofs/profile|The Solutions Engineer]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The convincing proof requires the prospect's real data, the prospect cannot send their real data to a synthetic data vendor, and the resulting compromise is a demo on public data that proves nothing.
**Tags:** #compliance #data-integration #automation #evaluation-metrics #worker-facing #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a prospect's dataset into credible evidence without a person building it by hand — and whoever does that takes the account, because proof-of-concept turnaround is what decides these deals.

## The Problem
The prospect's question is whether this works on their data. Their data is the data they bought synthetic generation to avoid sharing, and the irony is not lost on anybody in the room. The compromise is a demo on a public dataset, or on a heavily masked extract that has already lost the structure the proof was meant to test. The prospect sees evidence about a different problem, the engineer knows it is unconvincing, and the evaluation extends by weeks while both sides negotiate a data sharing agreement for a product whose purpose is to make data sharing unnecessary.

## Why It's Still Broken
Vendors are built around a hosted service because it is easier to operate, and running inside a customer's environment means supporting arbitrary infrastructure. Legal review of a data-sharing agreement for a proof of concept is slow and frequently ends in refusal, which is the correct outcome and is nobody's fault. The masked-extract compromise is available and superficially reasonable, which lets everyone avoid the harder fix. And the failure is diffuse — deals stretch rather than die — so it never becomes a tracked problem.

## What a Fix Looks Like
Move the proof to the data. Ship a self-contained package that runs inside the prospect's environment with no outbound connectivity — generation, evaluation and the evidence pack — so the prospect's data never leaves and the engineer never sees it, which resolves the contradiction the whole evaluation is stuck on. Return only the evidence artefacts, reviewed by the prospect before release, since that is the disclosure they can approve quickly and it contains no records. Support a schema-only first pass, where the prospect shares structure and statistics but no rows, which produces a genuinely informative proof in days rather than weeks of legal review. Make the package auditable and inspectable, because a security team asked to run a vendor binary on production data will read it. Handle the common infrastructure shapes rather than all of them, since covering the main environments removes most of the friction and chasing the rest is where this kind of effort usually dies. Track evaluation elapsed time as a metric, because the harm here is delay and nobody currently measures it. And stop presenting public-dataset demos as evidence, since everyone present knows what they are worth.

## Who Feels the Pain
Solutions engineers presenting evidence they know is unconvincing; prospects whose evaluation stalls in legal review for a product meant to prevent exactly that; and vendors losing deals to elapsed time rather than to capability.

## Impact If Fixed
The proof requires the data the product exists to avoid sharing, and the workaround proves nothing. A self-contained package that runs inside the prospect's network — returning only prospect-reviewed evidence — dissolves the contradiction, and a schema-only first pass delivers a real proof before legal review even starts.
