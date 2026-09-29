# Lien Resolution Discovered at the End

**Niche:** [[niches/legal-practice-software/mass-tort-claimant-operations/profile|Mass Tort — Claimant Operations at Scale]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Medicare, Medicaid and private liens must be resolved before a claimant is paid, the work takes months per claimant, and firms begin it after settlement — so the last stage of a five-year litigation is the one nobody planned for.
**Tags:** #survival-analysis #evaluation-metrics #descriptive-statistics #time-series-forecasting #workflow-orchestration #compliance #automation #worker-facing
**Contested on:** Every serious competitor in mass tort software is fighting to move forty thousand claimants through record retrieval, proof of exposure and lien resolution without an operation that collapses under its own headcount — and whoever holds throughput per claimant lowest takes the account.

## The Problem
A settlement is announced. Forty thousand claimants expect money. Before any of them can be paid, every lienholder with a claim against their recovery — Medicare's conditional payment recovery, state Medicaid agencies, private health plans, hospital liens — must be identified, the claimed amount verified, unrelated charges disputed, and a final demand obtained. Each of those is a correspondence cycle with a slow institution measured in weeks. Done serially, starting at settlement, it takes a year and generates the ugliest part of the litigation: claimants who won and are not paid, calling a firm that cannot tell them when.

## Why It's Still Broken
Lien resolution is treated as a post-settlement administrative task because that is when the money exists, and because it is typically outsourced to specialist firms who are engaged at that point. Nothing prevents starting earlier — Medicare entitlement and conditional payment inquiry can be initiated long before settlement, and the records needed to dispute unrelated charges are the same records already retrieved for qualification — but starting earlier costs money against an uncertain outcome, and no firm has modelled that trade-off because no firm measures the cost of the delay.

## What a Fix Looks Like
Start lien resolution at qualification rather than at settlement, and treat it as a pipeline with the same instrumentation as every other stage. Identify lienholders as soon as a claimant's records are in hand — the evidence is already there. Open Medicare and Medicaid inquiries in parallel across the inventory rather than serially, batching correspondence and tracking each one with an expected turnaround learned from the firm's own history with that agency. Dispute unrelated charges using the qualification records that have already been reviewed, which is the same reading done twice today. Then forecast: given the inventory's current lien state, when can distribution actually begin, and which claimants are on the critical path. That forecast is what lets a firm tell forty thousand people something true.

## Who Feels the Pain
Claimants who won two years ago and have not been paid; the firm's staff fielding those calls with no answer; and the operations directors who discover at settlement that the last stage is a year long.

## Impact If Fixed
Moving lien work upstream and running it in parallel compresses time-to-distribution from roughly a year to a quarter on a large inventory, which is the single largest improvement available in mass tort operations. It also reuses record review already paid for, so a substantial part of the work is free in a way that is invisible until the two stages are modelled as one pipeline.
