# Turn-Time Prediction for Every Lot Out the Door

**Niche:** [[niches/aerospace-parts-suppliers/outside-special-processing/profile|Outside Special Processing & Sub-Tier Expediting]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Suppliers know when a lot left for the heat treater and roughly when it came back; nobody models how long each processor really takes, by process and season, or predicts when this lot will return.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #large-language-models #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to give production control a trusted completion date for every lot at an outside heat treater, plater or NDT house, and whoever's predicted dates hold best against processors' real turn times takes the account.

## The Problem
The expediter's hot list exists because outside-processing dates are guesses. Processors quote a turn time, then batch by furnace load or tank chemistry, prioritise their largest customers, and slip when an audit or a breakdown hits. The supplier finds out by calling.

## Why Nobody Has Built This
Processors are small firms with their own systems or none; their data is theirs; and the supplier's own history is scattered across packing slips, receiving records and emails.

## What to Build
A model trained on the supplier's own shipments and receipts per processor, process, part family, lot size and season, treating open lots as censored observations, that gives each lot a predicted return date with a range. An agent reads processor emails and portal updates and posts receipt, start and ship events to the lot. Rankings show which processors' quotes hold, and suggestions show where an alternative approved processor would recover a date.

## Target Customer
Production control and operations leaders at detail-part and assembly suppliers that send most parts out at least once.

## Impact If Built
Dates that hold within a few days lift on-time delivery several points (estimate) and cut ~5–15 hours a week of status calls per expediter.
