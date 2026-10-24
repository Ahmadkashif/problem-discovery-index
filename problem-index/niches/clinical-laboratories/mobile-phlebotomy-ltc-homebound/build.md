# A Draw Schedule Planned Around the Facility's Day

**Niche:** [[niches/clinical-laboratories/mobile-phlebotomy-ltc-homebound/profile|Mobile Phlebotomy for Nursing Homes & Home-Bound Patients]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Mobile phlebotomists start at 4 a.m. with a route built from yesterday's faxes, while the orders that matter most arrived overnight.
**Tags:** #optimization-fundamentals #time-series-forecasting #large-language-models #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to complete each draw ordered for a nursing-home resident or home-bound patient, and whoever loses the fewest ordered draws to missed visits and recollections takes the account.

## The Problem
A regional long-term care lab may serve 100+ facilities and home-bound patients with a few dozen phlebotomists. Orders arrive by fax, phone and facility EHR, including stat and timed draws (drug levels, INRs) added late in the evening. Routes are built the afternoon before and patched by phone. Facilities complain when results miss the morning round, and phlebotomists absorb the chaos.

## Why Nobody Has Built This
The lab's LIS knows orders, not routes; facility EHRs know orders, not the lab's capacity; generic route tools know neither. The market is regional and fragmented, so it gets little software attention.

## What to Build
An order-capture layer that reads faxed and EHR orders with a language model and normalises tests and timing. A morning route optimiser schedules draws by facility medication-pass times, timed-draw constraints and phlebotomist skills, and re-plans when stat orders arrive. Each facility gets a live status view per resident: drawn, failed with reason, in transit, resulted.

## Target Customer
Regional labs serving long-term care and home-bound patients, and mobile phlebotomy companies contracted by them.

## Impact If Built
More draws completed on the ordered morning and results before rounds. Lifting completion from ~92% to ~97% (estimates) on 1,000 draws a day avoids ~50 delayed draws daily, each a delayed dosing or treatment decision for a frail patient.
