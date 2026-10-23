# Exception Root-Cause Learning Across the Fleet

**Niche:** [[niches/electric-utilities/ami-meter-data-operations/profile|AMI Meter Data Operations]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Meter data analysts resolve the same kinds of exceptions thousands of times a month and the resolutions are never used to resolve the next one.
**Tags:** #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn every exception in interval meter data into a correct bill and a correct grid model without a truck roll, and whoever resolves the most exceptions automatically, without a billing error reaching a customer, takes the account.

## The Problem
VEE rules flag gaps, spikes, reverse flow and zero usage. Analysts open each exception, look at the interval profile, neighbours on the same transformer, recent work orders and events, and choose an action: estimate, re-read, send a field order, flag for theft review, update the solar flag. Those choices and their outcomes (what the field technician found) are recorded but never learned from.

## Why Nobody Has Built This
Meter data management vendors ship rule engines, field outcomes sit in work management, and exception volume is treated as a staffing problem.

## What to Build
A model trained on past exceptions, the analyst's chosen action and the field finding. Features come from the meter's profile, its transformer neighbours' voltage and usage, communications health, events and recent service orders. It predicts root cause and best action with confidence, auto-resolves high-confidence routine cases, and sends analysts the ambiguous ones with an explanation. Every field order closes the loop.

## Target Customer
Meter operations directors at utilities with 500,000+ AMI meters and exception backlogs.

## Impact If Built
~30%–50% of routine exceptions auto-resolved and ~10%–20% fewer unnecessary truck rolls (estimate), with correct bills issued days sooner and analyst time moved to theft, safety and grid-model issues.
