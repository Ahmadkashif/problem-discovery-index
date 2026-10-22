# Shared Night-Shift Operations for Small Fleets

**Niche:** [[niches/satellite-operators/smallsat-newspace-operators/profile|Small Satellite & NewSpace Operators]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A startup with eight satellites can't staff a 24/7 console, so its engineers take turns sleeping with a phone, and a safe-mode event at 3 a.m. waits for whoever wakes up.
**Tags:** #autoencoders #k-nearest-neighbors #large-language-models #worker-facing #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to take a startup's satellites from licence to steady operations without the startup building its own ground network or 24/7 operations team, and whoever bundles ground contacts, mission operations and the regulatory paperwork into one dependable service takes the startup's ground and operations contract.

## The Problem
Small satellites drop into safe mode, lose attitude, miss a ground contact or report a strange temperature. Each event needs someone to look at telemetry at the next pass, decide whether it is urgent, and command recovery. Startups rely on on-call rotations among a few engineers, which burns people out and leaves gaps when a pass is missed.

## Why Nobody Has Built This
Every startup's bus and software differ, so a shared operations service seems to need custom integration for each; large operations contractors price for government missions; and founders are wary of letting outsiders command their spacecraft.

## What to Build
A shared operations centre with standard telemetry and command interfaces, per-customer procedures encoded as playbooks, anomaly triage models trained across many small fleets (the scale no single startup has), and a clear escalation rule: routine recovery executed by the centre within the customer's authorisation, anything unusual escalated with the evidence and the similar past cases attached.

## Target Customer
CTOs and heads of operations at startups operating up to ~50 satellites.

## Impact If Built
Night and weekend coverage without hiring a console team, faster recovery from routine anomalies, and engineers who sleep.
