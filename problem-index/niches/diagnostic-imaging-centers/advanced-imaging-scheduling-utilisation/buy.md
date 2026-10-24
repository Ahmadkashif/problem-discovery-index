# Infusion-Chair Capacity Software Adapted to the Magnet

**Niche:** [[niches/diagnostic-imaging-centers/advanced-imaging-scheduling-utilisation/profile|Advanced Imaging Scheduling & Scanner Utilisation]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hospitals already buy template optimisation for infusion chairs and operating rooms; the same mathematics fits an MRI scanner once it learns protocols, contrast blocks and authorization windows.
**Tags:** #monte-carlo-methods #optimization-fundamentals #gradient-boosting #time-series-forecasting #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn each MRI and CT referral into a completed, paid exam in the next open scanner slot, and whoever completes the most paid exams per scanner hour takes the account.

## The Problem
Centres know their magnets idle at some hours and overrun at others, but their RIS cannot say which template change would help. Building scheduling optimisation from scratch is beyond an operator's IT team.

## What Already Exists
Capacity and template-optimisation products sold to hospitals for infusion chairs, operating rooms and inpatient beds (LeanTaaS iQueue, Qventus), analysed under [[industries/general-hospitals|General Hospitals]]. They forecast demand by hour, simulate templates and recommend changes.

## The Customization Gap
The adaptation needs exam-level duration from protocol, field strength and coil rather than chair time by drug regimen. It needs resource rules specific to imaging: radiologist on site for contrast hours, anaesthesia blocks, MR-safety screening time, and breast and cardiac coil limits. It needs authorization windows as hard constraints on rescheduling, and a feed from scanner logs for true start and end times. Success has to be measured as paid exams per scanner hour.

## Target Customer
Health-system imaging joint ventures and large operators that already license capacity software for other departments.

## Impact If Solved
Reusing a proven optimisation engine shortens a 12-month build to a 3-month configuration. Even a 5% lift in completed exams per scanner hour pays for the licence on one magnet (estimate).
