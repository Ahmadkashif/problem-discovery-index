# Restoration Times Posted From a Guess

**Niche:** [[niches/electric-utilities/storm-restoration-mutual-assistance/profile|Storm Restoration & Mutual Assistance]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** Estimated restoration times go out to customers and officials early in a storm, are often wrong, and are revised in ways that destroy trust.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to restore the last customer sooner with fewer crew-days, and whoever stages the right number of crews in the right places before the storm arrives takes the account.

## The Problem
Customers, mayors and commissions demand an estimated time of restoration (ETR) as soon as the lights go out. Early in a major event the utility posts global or regional ETRs based on experience. Later it posts per-outage times from the outage system's defaults. Missed ETRs drive repeat calls and complaints and feature in post-storm investigations.

## Why It's Still Broken
ETRs are set before damage is assessed, outage-system defaults ignore storm conditions, and nobody measures ETR accuracy by stage of the storm, so there is no feedback to improve them.

## What a Fix Looks Like
Score past storms' posted ETRs against actual restoration times. Then model time-to-restore per outage as a function of damage type, assessment status, crew availability and access, and post ETRs as ranges with honest confidence that narrow as assessment proceeds.

## Who Feels the Pain
Customers planning around outages, call centre staff, operators asked for times they can't know, and executives questioned afterwards.

## Impact If Fixed
If posted restoration times fall within their range ~80% of the time rather than being revised repeatedly (estimate), repeat calls fall and the utility has a measurable accuracy record to show regulators after the next storm.
