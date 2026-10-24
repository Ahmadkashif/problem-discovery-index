# Predicting the Fine Before the Truck Leaves

**Niche:** [[niches/consumer-products-makers/otif-routing-edi-compliance/profile|OTIF, Routing-Guide & EDI Compliance]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compliance fines are predictable from order, carrier and appointment data before shipment, yet makers learn about them weeks later as deductions.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #feature-engineering #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep a maker's shipments inside each retailer's routing guide and on-time, in-full targets, and whoever keeps the maker's compliance fines lowest as a share of shipments takes the account.

## The Problem
Late appointments, short picks, wrong labels and late ship notices cause most fines, and the signals exist in the warehouse and carrier systems the day before the truck leaves.

## Why Nobody Has Built This
EDI vendors check document format, not outcome risk, and fine data sits in finance.

## What to Build
A model trained on past shipments and their fines that scores each outbound load for fine risk by cause, checks it against the retailer's current guide, and tells the shipping lead what to fix (split the load, re-book the appointment, re-send the notice) while there is time.

## Target Customer
Supply-chain leads at makers shipping to several big-box retailers, and the 3PLs that serve them.

## Impact If Built
Compliance fines fall from ~1% of shipment value to ~0.5% (estimate), ~$250K a year at a $50M maker, with fewer disputes downstream.
