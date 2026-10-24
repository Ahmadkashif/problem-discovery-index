# Turnaround Measured Into the Practice's EHR, Practice by Practice

**Niche:** [[niches/clinical-laboratories/hospital-outreach-lab-partnerships/profile|Hospital Outreach Programmes & Reference Lab Partnerships]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Labs measure turnaround from receipt to verification; practices judge them on when the result appears in their own EHR, and nobody measures that.
**Tags:** #time-series-forecasting #survival-analysis #descriptive-statistics #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the lab community practices send their routine orders to, and whoever keeps the largest share of each practice's routine order volume year on year takes the account.

## The Problem
An outreach lab reports turnaround as the time between the specimen arriving and the result being verified. The practice experiences something else: the order placed at 10 a.m., the courier pickup at 4 p.m., receipt at 9 p.m., verification at 2 a.m., and the result filed into its EHR inbox, or not, depending on an interface that may be queued, failed or mapped to the wrong provider. Practices leave labs over results that arrive after the patient follow-up call, not over analytical turnaround.

## Why Nobody Has Built This
The timestamps live in five systems: the practice's EHR order, the courier scan, the LIS, the interface engine and the practice's inbox acknowledgement. No one system sees all of them, and the lab does not see the practice's side at all.

## What to Build
A tracker that joins order, pickup, receipt, verification and delivery acknowledgement timestamps per requisition and reports, per practice, the share of results in the EHR before the next clinic session. It predicts which requisitions will miss, from pickup time, test mix and interface health, and alerts client services before the practice notices. Sales gets the same measure as evidence for each new practice.

## Target Customer
Outreach directors at health systems with 200–2,000 practice clients, and client-services leaders at regional independent labs.

## Impact If Built
The lab manages the measure practices actually use. Retaining two practices a year that would otherwise leave, at ~$250,000 of annual testing each, is worth ~$500,000 (estimate) to a mid-size outreach programme.
