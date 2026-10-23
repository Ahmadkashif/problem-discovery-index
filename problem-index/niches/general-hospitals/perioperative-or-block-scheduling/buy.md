# Airline Revenue Management Adapted to OR Blocks

**Niche:** [[niches/general-hospitals/perioperative-or-block-scheduling/profile|Perioperative Services & OR Block Scheduling]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines forecast no-shows and release seat inventory on a schedule. An OR block is perishable inventory with the same shape, held by surgeons who rarely give it back early.
**Tags:** #time-series-forecasting #bayesian-inference #optimization-fundamentals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn released and unused OR block minutes into staffed, completed cases, and whoever fills the most released minutes without adding overtime takes the account.

## The Problem
Blocks are allocated months ahead. Whether a surgeon will fill Tuesday's block is predictable from their booking curve, vacation calendar and clinic volumes. Hospitals still wait for voluntary release.

## What Already Exists
Airline and hotel revenue-management systems forecast demand by booking curve and set overbooking and release rules. LeanTaaS iQueue and Qventus apply forecasting to OR block release nudges.

## The Customization Gap
OR adaptation needs:

- booking curves per surgeon and service rather than per flight;
- clinical constraints (urgent cases protected, cancer cases prioritised);
- block policies that tie future allocation to utilisation thresholds;
- surgeon-specific release politics (who can be nudged, who must be asked by the chair);
- forecasts that hold up for low-volume surgeons with sparse history, where hierarchical models borrow strength across peers.

## Target Customer
OR committees and perioperative leaders renegotiating block policy.

## Impact If Solved
Predicting under-use two to three weeks out, rather than waiting for release at ~48–72 hours (recalled), gives schedulers time to fill slots with ready cases.
