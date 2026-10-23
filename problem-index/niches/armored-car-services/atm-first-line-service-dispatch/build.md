# Staged-Fault Risk Scoring Before Dispatch

**Niche:** [[niches/armored-car-services/atm-first-line-service-dispatch/profile|ATM First-Line Service & Fault Dispatch]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A deliberately jammed ATM raises the same ticket as a worn card reader, and dispatch sends the same lone technician to both.
**Tags:** #lstms-and-grus #hidden-markov-models #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to restore a faulted ATM fastest without sending a technician into a staged jam, and whoever clears the most faults remotely and sends people only to genuine, risk-checked calls takes the account.

## The Problem
Staged faults are designed to look ordinary. The only differences are in the detail: the sequence of sensor events before the fault, a fault at a machine that rarely faults, a time of day when the site is quiet, repeated faults at nearby machines, a lack of transactions in the minutes before. No dispatcher reads device journals at that level.

## Why Nobody Has Built This
Confirmed cases are few and recorded unevenly, so there was no training set. Monitoring vendors optimise for uptime, not technician safety, and security teams do not see the device data.

## What to Build
A risk score for each fault ticket, computed from the device's event sequence before the fault, the machine's and site's fault history, time, site type, local incidents and recent attacks elsewhere in the fleet. High scores trigger a different dispatch: two people, a delay to daylight, a police or guard escort, or a remote check first. Every technician finding of foreign objects or tampering is captured as a label, so the score improves with the fleet.

## Target Customer
Service delivery and security leaders in carriers' AMS businesses, ATM makers' service arms and independent service organisations.

## Impact If Built
Fewer technicians walking into ambushes, and a dispatch policy the employer can show its staff and their families is based on evidence.
