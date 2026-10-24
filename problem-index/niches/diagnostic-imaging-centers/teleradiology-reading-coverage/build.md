# Licence-Aware Routing Across a National Reader Pool

**Niche:** [[niches/diagnostic-imaging-centers/teleradiology-reading-coverage/profile|Teleradiology & Outsourced Reading Coverage]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A teleradiology firm can cover a centre's overflow only if each study reaches an eligible, subspecialty-matched reader, and most routing still runs on modality queues that send hard studies to whoever is free.
**Tags:** #optimization-fundamentals #markov-decision-processes #time-series-forecasting #gradient-boosting #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to read the evening, weekend, subspecialty and overflow studies a centre's own radiologists cannot cover, and whoever covers the highest share of the centre's after-hours and overflow studies with peer-review major-discrepancy rates under the contract threshold takes the account.

## The Problem
A neuro MRI arrives at 11:40 p.m. from a centre in one state. Of 60 radiologists on shift, 12 hold that state's licence, eight are credentialed for that centre, and three read neuro. Modality queues do not know this. The study either waits for the morning group, which is a coverage failure, or is claimed by a general reader outside their subspecialty, which is where major discrepancies come from.

## Why Nobody Has Built This
Licensure, credentialing, subspecialty and real-time availability live in different systems. Teleradiology platforms were built when volumes were smaller and reader pools local, and peer-review results have never been fed back into routing.

## What to Build
A routing engine that assigns each study to an eligible reader. It enforces licence and credentialing, matches subspecialty to protocol, and balances workload and difficulty across readers. It uses each reader's peer-review discrepancy history by study type to keep the hardest studies with the readers least likely to miss findings. It forecasts nights when a centre's eligible coverage will run short, so the firm can add licensed readers before studies go uncovered.

## Target Customer
Teleradiology firms and multi-state groups reading for dozens of centres.

## Impact If Built
Raising the share of a centre's overflow studies actually covered from, say, 90% to 97% (estimate) moves volume back from the morning group. Routing subspecialty studies to matched readers can cut major discrepancies on those studies, which keeps the contract under its quality threshold at renewal.
