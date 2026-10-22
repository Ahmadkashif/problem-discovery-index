# The Installer Charged for the Plant's Repeat

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]
**Type:** Worker Life Changing
**One-liner:** An installer who does a clean job is scored, and often docked pay, when the same customer calls back within weeks, even when the repeat came from a plant problem upstream of the house that the installer was never allowed to fix.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #worker-facing #workflow-orchestration #data-integration

## The Problem
Installation and service-call work at cable and fibre operators is done by employee technicians and, at many operators, by contract firms whose technicians are paid per completed job or per point (estimate). A common quality measure is the repeat: the same account generating another trouble call within a window such as 30 days. For contract installers the repeat can come with a chargeback; for employees it shows up in scorecards and route assignments.

But a repeat is often not the installer's fault. The installer verifies signal at the tap and in the home, builds the drop and the inside wiring, and leaves the customer working. If an impairment upstream — a failing amplifier, a tap that loosens in the cold, ingress from another drop on the same leg — later degrades service, the account repeats and the metric points at the last person who touched it. The installer typically has no say over plant maintenance and no record of what the plant looked like when they left.

## Why It Matters to the Worker
It is pay and reputation. A contract installer docked for repeats they did not cause loses money they cannot contest without evidence. Employee installers see their scorecard and job assignments shaped by metrics that mix their workmanship with the plant's condition. Good installers learn to over-replace — new connectors, new splitters, new modems on every job — to protect themselves, which makes the job slower and the metric noisier. Disputes come down to a supervisor's opinion.

## What a Solution Looks Like
At closeout, the installer's phone automatically snapshots what the network can see: signal levels and pre-equalization at the modem or ONT, the same readings for neighbouring homes on the tap or splitter, and photos of the drop and connections. When the account repeats, a model compares the new symptoms to the closeout snapshot and the neighbours' trends, and attributes the repeat as likely workmanship, likely plant or likely customer equipment, with the evidence attached. Plant-attributed repeats route to maintenance and are excluded from the installer's score and chargebacks.

## Impact If Solved
Installers stop paying for problems they did not cause, disputes are settled by evidence rather than argument, and over-replacement of good parts drops. Operators get cleaner metrics: a repeat rate that measures workmanship, and a separate plant-repeat signal that tells maintenance where to look.
