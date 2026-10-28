# Availability Defined Five Ways in Five Contracts

**Niche:** [[niches/renewable-power-producers/fleet-asset-performance-om/profile|Fleet Asset Performance & O&M]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Fix (Pain Point)
**One-liner:** The OEM's service agreement, the lender's model, the PPA and the owner's board report each define availability differently, so the same month produces four numbers and an argument.
**Tags:** #large-language-models #descriptive-statistics #data-integration #compliance #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to recover the most lost energy per dollar of operations and maintenance", but wind and solar lose energy in different ways, to different vendors, on different data: wind is won on avoiding crane-dependent drivetrain failures, solar on clearing the many small inverter, tracker and string losses. Decomposed into contested sub-niches below.

## The Problem
A turbine maker guarantees time-based availability with exclusions for weather, grid and owner-caused stops; the lender's model uses energy-based availability; the PPA has its own guaranteed-output clause. Each month the asset manager recomputes all of them by hand and disputes the OEM's figure when liquidated damages are due.

## Why It's Still Broken
Definitions live in contract text, exclusions depend on event codes that the OEM controls, and the owner rarely has an independent event log.

## What a Fix Looks Like
Read each contract's availability definition into explicit rules, compute every version from one event log the owner controls, and produce a monthly reconciliation that shows exactly which events explain the difference from the OEM's number.

## Who Feels the Pain
Asset managers chasing guarantee payments; finance teams reporting to lenders; OEM account managers defending their figures.

## Impact If Fixed
At a 1 GW wind fleet where availability guarantees are worth ~$1–2M a year in liquidated damages (estimate), an independent reconciliation that wins back a third of the amounts now conceded for lack of evidence is worth ~$0.3–0.7M a year.
