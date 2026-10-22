# An IND Package Planner That Sees the Whole Critical Path

**Niche:** [[niches/biotech-research-firms/glp-safety-assessment/profile|IND-Enabling GLP Safety Assessment]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An IND-enabling package is a dozen interdependent studies bought as separate quotes, and nobody models the critical path that decides the IND date.
**Tags:** #survival-analysis #gradient-boosting #monte-carlo-methods #feature-engineering #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every preclinical CRO is fighting to deliver an audit-clean IND-enabling package on the date the sponsor's IND depends on, but small-molecule and biologics programmes are won on different things — compressing the calendar across disciplines, versus securing or replacing non-human primates — so it is decomposed into contested sub-niches below.

## The Problem
A package typically includes dose-range finding, GLP repeat-dose studies in two species, safety pharmacology, genetic toxicology, toxicokinetic bioanalysis, formulation analysis, pathology and SEND. Each is quoted, scheduled and staffed separately. The real IND date is set by the longest chain of dependencies: test article availability, dose selection from the range-finder, animal arrival, the in-life phase, necropsy, histology, the pathology read, peer review, bioanalysis and report. Sponsors plan it in slides; CRO schedulers see their own department's queue.

## Why Nobody Has Built This
The data lives in different CRO systems, and sponsors buy from several CROs. CROs price studies, not packages. And historical durations by study type and lab are treated as commercially sensitive, so no one has built the reference-class data.

## What to Build
A package planner that turns the sponsor's development plan into a dependency graph of studies, attaches empirical duration distributions to each step from the CRO's own history, simulates the IND date with uncertainty, and shows which step to buy time on: an earlier range-finder, a reserved histology slot, or a parallel bioanalysis method. It updates as events happen and is shared by sponsor and CRO.

## Target Customer
Heads of safety assessment and programme management at preclinical CROs selling integrated packages; nonclinical leads at sponsors whose financing is tied to the IND.

## Impact If Built
Sponsors get a credible date instead of a hopeful one, and a CRO that can show a shorter, honest critical path wins the package rather than the study.
