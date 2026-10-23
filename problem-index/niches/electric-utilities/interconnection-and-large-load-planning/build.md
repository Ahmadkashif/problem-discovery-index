# A Study-Outcome Model Trained on the Utility's Own Archive

**Niche:** [[niches/electric-utilities/interconnection-and-large-load-planning/profile|Interconnection & Large-Load Planning]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every utility holds years of interconnection and load studies with known outcomes, and none uses them to predict the next study's answer.
**Tags:** #tacit-knowledge-ml #gradient-boosting #graph-neural-networks #large-language-models #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to tell an applicant quickly what capacity exists and what connecting will cost. But for small distributed generation, storage and chargers the contest is clearing thousands of applications against a hosting number the study later confirms. For data centres and factories it is answering a few huge, often speculative requests with a megawatt figure, date and cost that hold until energisation. Different volumes, buyers and winners, so it is decomposed into contested sub-niches below.

## The Problem
A utility's planning group has run hundreds or thousands of studies over the last decade. Each records a request (size, type, location), the binding constraints found, the upgrades required and a cost estimate, and for many there is a later outcome: built, withdrawn, energised with or without problems, at a final cost. That archive is the closest thing the utility has to a labelled dataset of its senior planners' judgement. Yet each new request starts from scratch with a fresh study.

## Why Nobody Has Built This
The studies are PDFs filed by project number, the network models they used have since changed, and the outcome data sits in work management and accounting systems that don't share keys. Planning software vendors sell the simulation engine, not the learning layer, and network models are protected infrastructure data, which discourages cloud products.

## What to Build
An in-utility pipeline that extracts each study into a structured record, reconstructs feeder features at study date from model snapshots, SCADA and AMI history, and joins outcomes from work orders and energisation records. On that, a model that predicts fit, binding constraint and cost range for each new request, shows the most similar past studies, and records the planner's quick read for comparison. A narrower public-data layer, published hosting-map values plus utility-level context from EIA-861, EIA-860 and FERC Form 1, can serve as a demo and pre-application view. It cannot predict study outcomes, which exist only inside the utility.

## Target Customer
Directors of distribution planning at large IOUs and public power systems with growing request queues and a study backlog measured in months.

## Impact If Built
If ~40%–60% of requests are clear-cut (estimate) and answered in days instead of the weeks to months a study takes, planners get back a comparable share of their study time for the hard cases. The utility also gains a documented screening process to show commissions and developers.
