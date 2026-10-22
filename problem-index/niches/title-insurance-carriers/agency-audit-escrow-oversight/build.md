# Risk-Ranked Audits From the Underwriter's Own Signals

**Niche:** [[niches/title-insurance-carriers/agency-audit-escrow-oversight/profile|Agency Audit & Escrow Oversight]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The underwriter already holds the signals that precede most agent shortages (late remittances, CPLs without policies, reconciliations that stop arriving) and audits on a calendar instead.
**Tags:** #autoencoders #change-point-detection #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to find an agent's escrow shortage before the money is gone, and whoever detects shortages earliest per audit day spent takes the account.

## The Problem
Field audit capacity is small relative to the agent network, so most agents are visited on a fixed cycle. Shortages develop between visits. The warning signs show up in data the underwriter already has, in remittance timing, CPL and policy counts and the dates reconciliations are submitted. Nobody combines them.

## Why Nobody Has Built This
Confirmed defalcations are rare, so supervised models have little to learn from. Data sits in agency accounting, CPL systems and audit files that were never joined. And the agency sales side resists anything that looks like profiling its agents.

## What to Build
A monthly agent-level feature store built from remittances, CPLs, policies, reconciliation submissions, audit findings, licensing and ownership changes. On it sit unsupervised anomaly scoring against each agent's own history and peers, change-point alerts on remittance and reconciliation behaviour, and a hazard model calibrated on past shortages. Audits are scheduled by score, with a workpaper listing the transactions to test.

## Target Customer
VPs of agency risk at the four families and regional underwriters.

## Impact If Built
Shortages caught months earlier, CPL claims contained, and audit days spent where risk is concentrated.
