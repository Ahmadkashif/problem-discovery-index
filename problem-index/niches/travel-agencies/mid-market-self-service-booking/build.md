# Touchless Changes for the Trips That Call

**Niche:** [[niches/travel-agencies/mid-market-self-service-booking/profile|Mid-Market Self-Service Booking Adoption]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Self-service booking tools handle the first booking well and send the traveller to an agent for most changes, which is where cost and frustration concentrate.
**Tags:** #large-language-models #gradient-boosting #logistic-regression #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get a growing company's employees to book and change their own trips in the tool without calling an agent, and whoever keeps the highest share of trips booked and serviced touchless takes the account.

## The Problem
Online adoption at mid-market programmes is often reported at ~60-90% of bookings (estimate). The calls that remain are disproportionately changes: a meeting moved, a flight cancelled, a hotel extended. Each becomes an agent-assisted transaction at the higher fee, and a traveller who had to call once is more likely to book the next trip elsewhere.

## Why Nobody Has Built This
Exchanges are the hardest thing to automate in air distribution: fare rules, residual value, change fees, NDC order rules and policy must all be applied together, and getting it wrong produces a debit memo. Tool vendors have prioritised the shopping experience, where demos are won.

## What to Build
A change agent inside the booking tool and chat channels that understands a request in plain language, computes the options with their real cost after fare rules and residual value, checks policy, executes the exchange or refund through GDS or NDC servicing, and updates the hotel and car to match. It predicts which change requests it can complete safely and routes the rest to an agent with the work already done.

## Target Customer
Product leaders at TMCs and booking platforms serving mid-market companies; finance directors who pay the assisted-booking fees.

## Impact If Built
Moving most routine changes to touchless cuts servicing cost and fee disputes, and removes the call that teaches travellers to book outside the tool.
