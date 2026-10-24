# Three-Way Reconciliation of Orders, Fills and Passes

**Niche:** [[niches/idd-group-homes/medication-administration/profile|Medication Administration by Med-Certified DSPs]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most group-home medication errors start as a mismatch between what the prescriber ordered, what the pharmacy sent and what the MAR says, caught only when someone counts.
**Tags:** #large-language-models #logistic-regression #feature-engineering #compliance #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make every medication pass by a med-certified DSP match the current order, and whoever keeps medication errors that reach the critical-incident threshold lowest takes the account.

## The Problem
A doctor changes a dose at an appointment, and the paper order comes home in a folder. The pharmacy's next cycle fill still has the old dose. The MAR is updated by whoever is on shift, or not. DSPs pass what the blister pack says, and the error surfaces at the monthly nurse review, or in the ER.

## Why Nobody Has Built This
eMARs record passes; pharmacy systems record fills; orders arrive as paper or fax from many prescribers. No product reconciles all three for a residential provider without a pharmacist on staff.

## What to Build
A service that reads new orders (photographed paper, faxes, e-prescriptions), compares them with the pharmacy's fill data and the eMAR, and flags any mismatch before the next pass. It routes each flag to the delegating nurse with the source documents. It classifies every recorded error against the state's critical incident threshold and files the report when one is reached. A risk score ranks houses and residents by error likelihood: many medications, recent changes, new staff.

## Target Customer
Directors of health services at agencies with 20+ homes; long-term care pharmacies serving IDD providers.

## Impact If Built
Catching order-to-fill mismatches before the pass could cut reportable medication errors by ~33% (estimate) and save delegating nurses hours of monthly reconciliation.
