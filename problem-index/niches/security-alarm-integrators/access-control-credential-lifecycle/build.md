# Explaining Who Can Open Which Door, and Why

**Niche:** [[niches/security-alarm-integrators/access-control-credential-lifecycle/profile|Access Control & Credential Lifecycle]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Large access-control systems accumulate thousands of door groups and exceptions that no one can justify, and auditors now ask for the justification.
**Tags:** #k-means-clustering #graph-theory #feature-engineering #large-language-models #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep the access-control system's cardholders and door permissions exactly in step with the client's HR and IT identity records, and whoever makes every hire, transfer and termination reach the doors the same day takes the account.

## The Problem
Over a decade, an enterprise access system collects access levels created for one project, one contractor or one executive, and cardholders who inherit them on transfer. A physical access review asks managers to approve lists they cannot read, so they approve everything. Excess access is invisible until an incident.

## Why Nobody Has Built This
Access platforms store permissions but not the reasons for them. Logical identity tools have role mining but don't model doors, schedules and areas, and integrators bill for changes rather than for keeping the model clean.

## What to Build
Role mining for physical access. It clusters cardholders by department, job code, location and actual door usage from the transaction log, proposes a small set of roles that explain most permissions, and flags outliers: access never used in 90 days, access no peer has, access granted outside HR attributes. The access review becomes "approve these few dozen exceptions" instead of "approve these thousands of rows."

## Target Customer
Corporate security directors at multi-site enterprises with 10,000+ cardholders, and the integrators who manage their access platforms under service agreements.

## Impact If Built
Access reviews become meaningful and fast, excess access shrinks, and the integrator that runs them is tied to the client's audit cycle.
