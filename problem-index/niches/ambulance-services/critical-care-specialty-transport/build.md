# Adverse-Event Capture and Risk Model for Every Critical Care Transport

**Niche:** [[niches/ambulance-services/critical-care-specialty-transport/profile|Critical Care & Specialty Care Transport Teams]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Transport monitors and ventilators record every second of a critical care run, yet the team's quality review starts from a narrative, and no model warns which patients will crash en route.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to move ICU-level patients between hospitals without harm en route, and whoever has the fewest in-transport adverse events per 100 critical care transports takes the account.

## The Problem
Programme directors review adverse events by reading charts. The monitor's blood pressure trend, the ventilator's alarms and the pump changes that would show when and why a patient deteriorated are on separate devices, downloaded rarely if at all. Teams cannot say which patients, sending units or transport durations carry the most risk.

## Why Nobody Has Built This
Device data formats differ by manufacturer, critical care programmes are small, and ePCR vendors build for the volume of 911 work.

## What to Build
A pipeline that joins monitor, ventilator and pump data to the ePCR for every critical care transport, codes adverse events automatically from the data (sustained hypotension, desaturation, unplanned airway events, infusion interruptions) for clinician confirmation, and trains a risk model on the pre-departure state: diagnosis, pressor doses, ventilator settings, distance. High-risk transports get a pre-departure checklist and a medical-control call.

## Target Customer
Directors of hospital-based and private critical care transport programmes, and hospital systems that own them.

## Impact If Built
If a programme running 3,000 critical care transports a year with 4 adverse events per 100 (an estimate) cut that by a quarter, it would avoid ~30 events a year among its sickest patients.
