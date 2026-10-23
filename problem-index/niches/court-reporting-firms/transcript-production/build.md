# Edit-Cost Estimate Before the Job Is Assigned

**Niche:** [[niches/court-reporting-firms/transcript-production/profile|Transcript Production (Scoping, Proofreading & Digital Transcription)]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A production manager assigns a 300-page expedited transcript without knowing whether it is a clean two-speaker deposition or a technical, crosstalk-heavy one that will take three times as long to edit.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #workflow-orchestration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to turn a raw capture into a certifiable transcript by the delivery date at the lowest edit cost per page. But a stenographer's raw CAT file and a digital reporter's multi-channel recording are different inputs, worked by different people under different legal exposure, and the contests have different winners. Decomposed into contested sub-niches below.

## The Problem
Agencies route edits to scopists, proofreaders and transcriptionists by availability and per-page rate. Difficulty shows up only afterwards, when a job misses its expedite deadline or a scopist refuses the next one from that reporter.

## Why Nobody Has Built This
Edit time is not recorded anywhere: freelancers invoice pages, not hours. The features that predict difficulty (untranslate rate, speaker count, overlap, audio quality, technical vocabulary) sit in CAT and audio files that production systems never read.

## What to Build
A difficulty score computed when the raw file or recording lands. For steno, it uses untranslate and conflict density and realtime correction rate; for audio, overlap, signal quality and recogniser confidence; for both, speaker count, case type and vocabulary. It is calibrated against the edit time the editors themselves report. Assignments, deadlines and optional difficulty premiums then follow the score.

## Target Customer
Production managers at agencies and the larger independent firms; scoping and transcription networks pricing their work.

## Impact If Built
Fewer missed expedites, fairer allocation of hard jobs, and the first measured data on what editing actually costs, the input every automation business case in this industry is missing.
