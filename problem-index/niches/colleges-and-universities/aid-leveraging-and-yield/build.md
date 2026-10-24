# Uplift on Every Grant Dollar

**Niche:** [[niches/colleges-and-universities/aid-leveraging-and-yield/profile|Financial Aid Leveraging & Yield]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Yield models predict who will enroll; none estimates whose decision the aid actually changed, which is the only number that tells a college where its discount is wasted.
**Tags:** #causal-inference #gradient-boosting #tacit-knowledge-ml #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each admitted student's institutional aid so the class arrives at its target size and profile, and whoever brings in the target class at the lowest discount rate takes the account.

## The Problem
A yield model says a student has a 40% chance of enrolling. It does not say whether an extra $3,000 moves that to 55% or 41%. Grids are therefore tuned on predicted yield, and a large share of aid goes to students who would have come anyway, while marginal students are under-offered.

## Why Nobody Has Built This
Uplift needs variation in offers that is not fully explained by the grid, which colleges create but do not record as experiments, and it needs outcomes beyond deposit. Consultancies optimise each client's grid on that client's history and cannot pool records across clients without contract rights.

## What to Build
An uplift model per institution, identified from grid thresholds, policy changes between years, appeal adjustments and a small randomised band where the college agrees to one. Simulation of class size, profile, discount rate and net tuition under alternative grids. An appeal screen showing estimated uplift beside the five most similar past cases and their outcomes.

## Target Customer
VPs for enrollment and aid directors at tuition-dependent private colleges with five or more years of clean admit and aid history.

## Impact If Built
The same class at a lower discount. One point of discount on $60M in gross tuition is ~$600K a year (estimate), with the aid moved to students it actually brings in.
