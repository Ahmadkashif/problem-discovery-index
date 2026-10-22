# Instrument-to-Record Capture That Knows Which Contract Paid

**Niche:** [[niches/contract-research-labs/experimental-records/profile|Experimental Records & Research Data]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Instrument files are saved with cryptic names on the instrument PC, and nobody can later say which experiment, which sample and which contract produced them.
**Tags:** #large-language-models #feature-engineering #k-nearest-neighbors #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to capture each experiment's conditions and raw data at the bench without slowing the scientist, and whoever makes that record complete enough to defend an invention date, a data-rights claim and a final report takes the account.

## The Problem
A scientist runs a sample through a microscope, a diffractometer, a test frame. The file lands on the instrument PC as a timestamped name. The notebook entry, if written that day, says "sample B-14, run 3". Months later, the final report needs the data and a data-rights decision needs to know whether the run was charged to the SBIR award or to internal research.

## Why Nobody Has Built This
Instrument vendors sell per-instrument software; notebook vendors integrate with a handful of popular instruments; and nobody joins the run to the timesheet charge that says who paid.

## What to Build
A lightweight agent on instrument PCs that captures each output file with its metadata, prompts the operator once for sample and project (pre-filled from the scheduling system and the operator's timesheet charge for that hour), and files it to the right notebook entry and sponsor partition. Later, an LLM drafts the methods section of a report from the linked runs.

## Target Customer
Research operations directors at materials, physics and engineering labs with 20–200 instruments.

## Impact If Built
Every data point in a deliverable is traceable to a run, a sample and a funding source, which protects data-rights claims and invention dates and saves days of hunting per final report (estimate).
