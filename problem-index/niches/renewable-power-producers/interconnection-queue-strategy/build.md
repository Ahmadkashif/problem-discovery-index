# Survival Odds for Every Queue Position

**Niche:** [[niches/renewable-power-producers/interconnection-queue-strategy/profile|Interconnection Queue Strategy & Development Pipeline]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every developer decides at each deposit whether a queue position will survive, and nobody sells a calibrated probability and timeline for that position built from the full public queue history.
**Tags:** #survival-analysis #gradient-boosting #bayesian-inference #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put money only behind queue positions that will survive their network-upgrade assignments, and whoever has the lowest share of queued megawatts withdrawn after the first cluster study takes the account.

## The Problem
More than 70% of interconnection requests are withdrawn, and 41% of capacity that signed an interconnection agreement from 2000 to 2022 still withdrew (LBNL). Developers learn which positions die by paying for them. Screening tools show where capacity might exist today; they do not say how likely a given request is to reach operation, or when.

## Why Nobody Has Built This
Outcomes take about five years, Order 2023 changed the rules mid-history, and the public data have gaps (in-service dates for only 73% of operational projects). The expert's view that would improve a model sits in committee decks. Siting vendors have focused on land and capacity maps, which demo better than survival curves.

## What to Build
A competing-risks survival model over every request in the LBNL Queued Up file, refreshed from ISO queue files through gridstatus and EIA-860, with substation-level features (megawatts queued at the point, prior withdrawals there, study phase, vintage, transmission owner). It returns odds of operation and a months-to-operation distribution per request. A position ledger then records the interconnection lead's estimate at each deposit and shows where she and the model disagree before the money is posted. This is also the two-week MVP: the public model alone is buildable in that time.

## Target Customer
Vice presidents of interconnection at IPPs and developers with 20+ queue positions, and acquirers pricing development-stage portfolios.

## Impact If Built
Cutting the share of queued megawatts withdrawn after the first cluster study from ~60% to ~45% (estimate) saves a developer with ~$50M a year of deposits at risk ~$5M a year in forfeited deposits and wasted development spend.
