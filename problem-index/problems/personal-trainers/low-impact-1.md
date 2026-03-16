# Client Booking & Session Package Management

**Industry:** [[personal-trainers|Personal Trainers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic scheduling tools don't understand session packages, makeup policies, or the financial mechanics of a trainer's cancellation-heavy business.
**Tags:** #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
Trainers sell sessions in packages (10-packs, monthly subscriptions, punch cards) with complex cancellation and makeup rules — 24-hour cancellation policies, storm/illness exceptions, rollover sessions, and expiration dates. When a client cancels, the trainer must decide whether to charge the session, offer a makeup, or extend the package, then manually update the remaining balance, reschedule, and fill the now-open slot. With 15-30 active clients each managing different package types, the bookkeeping becomes a part-time job.

## What Already Exists
Calendly, Acuity Scheduling, and Mindbody handle appointment booking. Trainerize and TrueCoach have basic scheduling features. These tools treat each session as an isolated appointment — they have no concept of package balances, makeup session tracking, conditional cancellation policies, or the financial relationship between a missed session and the trainer's weekly revenue.

## The Customisation Gap
The scheduling system needs to understand package math: decrementing session counts based on attendance and cancellation policy, tracking makeup session eligibility windows, calculating prorated refunds for early termination, and predicting which open slots are most likely to be filled by waitlisted clients. It also needs cancellation pattern detection — flagging clients who are trending toward dropout (3+ cancellations in a month) so the trainer can intervene before losing the client entirely.

## Impact If Solved
Trainers reclaim 2-4 hours per week currently spent on manual package tracking and schedule Tetris, and reduce revenue leakage from uncollected cancellation fees estimated at 8-12% of gross billings.
