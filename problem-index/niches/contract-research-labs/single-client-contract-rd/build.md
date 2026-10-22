# Scoping a Fixed-Price Study from the Lab's Own History

**Niche:** [[niches/contract-research-labs/single-client-contract-rd/profile|Single-Client Contract R&D]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Labs price fixed-scope industry studies from a senior engineer's memory of similar jobs, when the actual hours, facility time and outcomes of every similar job are in their own records.
**Tags:** #tacit-knowledge-ml #gradient-boosting #large-language-models #k-nearest-neighbors #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to answer one sponsor's technical question inside a fixed scope and hand over the results and IP with no ownership dispute, and whoever delivers a result the sponsor can act on with the cleanest handover gets the next statement of work.

## The Problem
A sponsor asks for a quote. A section manager who has run similar studies estimates tests, specimens, cell hours and analysis time, and the quote goes out. Underestimates come out of the lab's margin or end in an awkward change-order conversation that sours the relationship; overestimates lose the job to a competitor.

## Why Nobody Has Built This
Project data is organised by charge number, not by technical content, so "similar past studies" cannot be found except by asking people. Labs treat estimating as senior judgement rather than as a data problem.

## What to Build
A scoping assistant that reads the sponsor's request, retrieves the most similar past studies by technical content, shows their estimated versus actual hours, facility time, change orders and sponsor follow-on, and proposes an effort range with the drivers named. The section manager adjusts and confirms, and the final estimate is stored for later grading.

## Target Customer
Section managers and commercial program managers at institutes and private labs quoting dozens of fixed-price studies a year.

## Impact If Built
Fewer underpriced studies and fewer mid-project change orders protect both margin and the sponsor relationship, which is what decides the next statement of work; cutting overruns by a third on a $20M commercial portfolio is worth several hundred thousand dollars a year (estimate).
