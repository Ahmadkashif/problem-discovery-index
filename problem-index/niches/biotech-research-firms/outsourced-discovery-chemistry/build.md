# A Cycle-Time Ledger for Every Design

**Niche:** [[niches/biotech-research-firms/outsourced-discovery-chemistry/profile|Outsourced Discovery Chemistry & DMTA Services]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Sponsors buy chemistry for its speed and cannot see where a design spends its weeks between the Monday meeting and the assay result.
**Tags:** #survival-analysis #gradient-boosting #graph-neural-networks #feature-engineering #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to shorten the sponsor's design–make–test cycle — designs in on Monday, compounds made, purified and assayed within days — from a location the sponsor's partners and acquirers will accept once the BIOSECURE list is published, and whoever turns cycles fastest from an acceptable jurisdiction takes the account.

## The Problem
A design chosen on Monday passes through route design, reagent sourcing, synthesis, purification, analytical QC, shipping, sample registration and the assay queue before its result returns. Each step is owned by someone different on two continents. Sponsors know the total feels like four to eight weeks (estimate) and cannot say which step to fix or which CRO is faster.

## Why Nobody Has Built This
The steps are recorded in different systems on each side of the contract, and CROs have little incentive to expose their internal timing. Sponsors switching CROs because of BIOSECURE have no baseline to compare against.

## What to Build
A shared ledger keyed to each design: timestamped status from the CRO's ELN and logistics, the sponsor's registration and assay systems, and a survival model of time-to-result per step. A synthesis-risk model trained on the CRO's route history flags designs likely to fail or take more than a cycle, so chemists can swap them before the batch is committed. Cycle time becomes a measured service level by CRO, site and country.

## Target Customer
Heads of chemistry at sponsors running two or more chemistry CROs; CROs outside China competing for transferred work on demonstrated speed.

## Impact If Built
A measured cycle time turns the BIOSECURE transition from a leap of faith into a comparison, and every week removed from the cycle compounds across dozens of cycles per programme.
