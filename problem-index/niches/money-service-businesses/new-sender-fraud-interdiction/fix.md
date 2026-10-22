# Chargebacks That Arrive After the Cash Was Collected

**Niche:** [[niches/money-service-businesses/new-sender-fraud-interdiction/profile|New-Sender Fraud & Scam Interdiction]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** A stolen-card transfer is paid out in minutes and charged back in weeks, so the fraud model learns about each attack long after it has moved to the next corridor.
**Tags:** #survival-analysis #change-point-detection #hypothesis-testing #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to approve a genuine first-time sender's card- or bank-funded transfer in minutes while stopping stolen funds and scam victims' savings before payout, and whoever separates the two most accurately takes the account.

## The Problem
Fraud rings test a corridor, scale up for a few days and move on. The chargebacks that confirm the attack come back weeks later, by which point the model has been retrained on the old pattern and the ring is elsewhere.

## Why It's Still Broken
Models are trained on settled labels, so they always lag. Early signals — receivers suddenly collecting from many new senders, a payout location spiking — are watched by analysts by eye, not encoded.

## What a Fix Looks Like
Use early proxies as provisional labels (receiver fan-in, first-party reports, issuer fraud alerts) with a survival model for time-to-chargeback, plus change-point alerts on receiver and payout-location activity, so payout holds start within hours of an attack.

## Who Feels the Pain
Fraud analysts, finance teams absorbing losses, and genuine senders hit by blunt corridor-wide rules after an attack.

## Impact If Fixed
Attacks are contained in hours instead of weeks, with narrower rules that leave genuine senders untouched.
