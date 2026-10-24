# Shift-Level Behaviour Capture That Graphs Itself for the Clinician

**Niche:** [[niches/idd-group-homes/behavior-support-data/profile|Behaviour Support Plans & Restrictive Intervention Data]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The behaviour clinician sees a month of reconstructed tallies, too late and too thin to tell whether the plan is working.
**Tags:** #tacit-knowledge-ml #hidden-markov-models #survival-analysis #large-language-models #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn DSPs' observations of behaviour into data a clinician uses to revise the plan, and whoever cuts restrictive interventions per resident furthest takes the account.

## The Problem
DSPs are asked to record each target behaviour with its antecedent and consequence while supporting four other people. Most write it up at the end of the shift or not at all. The clinician visits monthly, graphs what exists and adjusts a plan that may already be failing, while holds and PRN doses continue.

## Why Nobody Has Built This
Clinic ABA software assumes a technician with one client and a tablet. IDD record systems treat behaviour data as another form. Neither captures the precursors experienced DSPs notice.

## What to Build
A tap-or-voice capture on the DSP's phone, keyed to the person's plan (target behaviours, known precursors, de-escalation steps), that takes seconds per entry. Data flows into live graphs of behaviour rates, precursors and restrictive interventions per person. The clinician gets alerts when restraints or PRN use rise, and a sequence model shows which precursors and staffing patterns preceded escalations. Plan revisions are pushed back to DSPs' phones the same day.

## Target Customer
Directors of behaviour services at agencies serving residents with high behavioural needs, and the behaviour consultancies they contract.

## Impact If Built
Weekly rather than monthly plan adjustment could cut restrictive interventions for the highest-need residents by ~25% or more (estimate), with fewer injuries to residents and DSPs and fewer critical incidents.
