# The Critical Care Transport Nurse Reconciling Drips in a Moving Truck

**Industry:** [[ambulance-services|Ambulance Services]]
**Type:** Worker Life Changing
**One-liner:** The critical care transport nurse gets back the first fifteen minutes with an ICU patient, now spent hunting through a printed packet for the current infusion rates, ventilator settings and last doses, and with it the confidence that nothing was missed before the doors closed.
**Tags:** #large-language-models #transformers #worker-facing #automation #data-integration #quick-win

## The Problem
A critical care transport team, usually a nurse and a paramedic, moves ICU patients between hospitals: a ventilated stroke patient to a comprehensive stroke centre, a septic patient on two vasopressors to a tertiary ICU, a newborn to a neonatal unit. These are specialty care transports (A0434), and the team is responsible for every drip, pump and ventilator setting from the moment it takes over.

The handoff comes on paper. The sending ICU prints a face sheet, the medication administration record, the last labs and some notes, then gives a verbal report at the bedside while the team is moving the patient onto its own monitor and pumps. The nurse must reconcile, standing up, which infusions are running at what concentration and rate, when the last sedation and antibiotic doses were given, the current ventilator mode and settings, allergies, and any code status. The packet often runs to ~30 pages, is about an hour out of date (both estimates), and misses the one change made at the bedside after it printed. Discrepancies are found en route, in a moving vehicle, with no way to call the sending nurse once the doors close.

## Why It Matters to the Worker
Critical care transport nurses carry the liability of an ICU nurse with none of the ICU around them: no pharmacist, no second nurse, no physician at the bedside. A wrong concentration on a vasopressor or a missed dose of a seizure drug is their error, even when the packet caused it. The work is skilled and rare, and teams are small, so a nurse who loses confidence in handoffs, or feels exposed every shift, leaves for a hospital job. Each handoff is a few minutes of high-stakes reading under time pressure, several times a shift.

## What a Solution Looks Like
A transport handoff summary built from the sending hospital's record before the team arrives. When the transfer is accepted, the sending ICU's MAR, active orders, recent vitals and ventilator flowsheet are pulled through the hospital's interface, a health information exchange or an uploaded PDF. These are condensed into one page: active infusions with concentration, rate and dose units; last and next doses of time-critical drugs; ventilator mode and settings; lines and drains; allergies; code status; and anything changed in the last two hours. Each item is linked to its source. The nurse confirms each line at the bedside against the pumps and the patient, and the confirmed summary seeds the ePCR.

## Impact If Solved
Cutting bedside reconciliation from about fifteen minutes to five (an estimate) gives a team running four transports a shift back 40 minutes. It also removes most of the en-route discoveries behind in-transport medication events, the kind of event critical care transport quality programmes such as GAMUT track.
