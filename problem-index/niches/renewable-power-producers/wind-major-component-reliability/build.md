# Failure Alerts Learned From the Engineer's Own Calls

**Niche:** [[niches/renewable-power-producers/wind-major-component-reliability/profile|Wind Turbine Major Component Reliability]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Reliability engineers already decide every week which drivetrain alerts are real, and no system records those calls and uses them to make the next week's alerts better.
**Tags:** #tacit-knowledge-ml #autoencoders #lstms-and-grus #gradient-boosting #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to catch drivetrain and main-bearing damage early enough to repair it uptower, and whoever has the fewest crane-dependent major component replacements per 100 turbines takes the account.

## The Problem
An experienced reliability engineer looks at a bearing temperature creeping up against its neighbours, a change in a vibration spectrum and a power curve that sags at high wind, and decides whether to send a crew, watch for a week or ignore it. That read is the most valuable judgement in wind O&M, and it is exercised in a spreadsheet and an email.

## Why Nobody Has Built This
Vendors sell detection, not judgement capture, and owners rarely let a vendor see enough of the fleet to learn fleet-wide. Labels are scarce because failures are rare and work orders are vague, and engineers disagree with themselves on borderline cases.

## What to Build
A normal-behaviour model per turbine (autoencoder or LSTM residuals on temperatures, power curve and pitch) that raises alerts into a review queue where the engineer records act, watch or ignore with one click. Dispositions and later work orders become labels for a classifier of failure within 30 and 90 days, tuned to a fixed alert budget, and the system reports how often each disposition was right.

## Target Customer
Directors of reliability engineering at IPPs with 1,000+ turbines, especially fleets out of OEM warranty.

## Impact If Built
Avoiding 5 crane-dependent main-bearing or gearbox replacements a year on a 1,000-turbine fleet saves ~$1–2M in repair cost at $225,000–$400,000 each (search summary), plus weeks of lost output per event.
