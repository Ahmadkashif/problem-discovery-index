# Model Monitoring Adapted to Furnisher-Driven Attribute Drift

**Niche:** [[niches/credit-bureaus/lender-credit-files/profile|Consumer Credit Files for Lending]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic model monitoring tells a lender that an input drifted; it cannot tell them that the drift is one large furnisher changing how it reports.
**Tags:** #change-point-detection #evaluation-metrics #hypothesis-testing #feature-engineering #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to win the lender's retro study — the archive test in which each bureau's file and attributes are scored against the lender's own booked and declined applicants — and whoever shows the most lift on that population takes the account.

## The Problem
Lenders' scorecards and machine-learning models run on bureau attributes. Those attributes move when the world changes and also when furnishers change their reporting — a student loan servicer's new treatment of deferment, buy-now-pay-later lenders starting to furnish, collection agencies dropping medical accounts. The lender sees score distributions shift and approval rates move, and spends weeks finding out whether its applicants changed or the file did.

## What Already Exists
Machine-learning monitoring platforms (Arize, Fiddler) and model-risk tooling in SAS and the lenders' own stacks track feature drift and population stability. Bureaus publish product bulletins.

## The Customization Gap
The adaptation needs: attribute-level drift linked to furnisher and reporting events on the bureau side; population stability decomposed by tradeline type and furnisher category; a bulletin feed that quantifies the expected effect of each reporting change on each attribute; and documentation that satisfies the lender's model-risk reviewers when a model is recalibrated for a data change rather than a behaviour change.

## Target Customer
Model-risk and credit analytics teams at lenders running bureau-based models in production; bureau product teams that want to be the source of that explanation.

## Impact If Solved
Lenders diagnose drift in days instead of weeks, recalibrate for the right reason, and associate the bureau with the explanation rather than the surprise — which matters at the next retro.
