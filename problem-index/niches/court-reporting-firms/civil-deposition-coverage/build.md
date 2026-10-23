# A Coverage Forecast for Tomorrow's Depositions

**Niche:** [[niches/court-reporting-firms/civil-deposition-coverage/profile|Civil Litigation Deposition Coverage]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agencies know every booking on tomorrow's calendar and nothing about which ones will cancel, which will run long, and which will go unfilled, so standby capacity is guesswork.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #optimization-fundamentals #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to put a licensed reporter, or a capture method the venue and parties accept, into every booked deposition, including the ones noticed for tomorrow morning, and whoever fills the most short-notice bookings without a cancelled examination takes the account.

## The Problem
A regional agency's calendar for tomorrow may hold a hundred depositions. Some will cancel tonight because the case settled or a witness fell ill. Some will continue to next month. Some will run into a second day. A handful are still unassigned because nobody licensed in that county accepted the page rate. Schedulers handle this with a mental model of which law firms cancel late, which witness types run long, and which reporters say yes after nine at night. That model is good in a veteran scheduler and absent in a new one.

## Why Nobody Has Built This
Booking data sits in each agency's scheduling system, built for invoicing rather than prediction. The national agencies have the volume but treat scheduling as operations. Independents have the local knowledge but no data. And the cost of a dropped job (a furious client, a wasted expert fee) is felt by account managers, not by whoever owns the system.

## What to Build
A forecast for every booking: probability it goes ahead, expected duration, and fill risk given the reporters licensed and available nearby. Train it on cancellation timestamps, case type, noticing firm, witness type, venue, remote or in-person, and lead time. Feed it into a standby policy that holds a reporter, or arranges remote coverage, where the risk-weighted cost of a miss is highest. Report fill rate and dropped jobs per thousand bookings weekly.

## Target Customer
Directors of scheduling at regional agencies with several thousand bookings a year; operations heads integrating acquired firms' calendars at the rollups.

## Impact If Built
A measurable fall in dropped and late-covered depositions, fewer paid standby days that turn out to be unneeded, and a scheduler's judgement that no longer leaves when the scheduler does.
