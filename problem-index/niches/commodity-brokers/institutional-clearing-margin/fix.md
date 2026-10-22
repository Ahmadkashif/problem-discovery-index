# Intraday Limits Set Once and Never Revisited

**Niche:** [[niches/commodity-brokers/institutional-clearing-margin/profile|Institutional Clearing & Margin Financing]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** A client's pre-trade and intraday credit limits are set at onboarding and change only after a breach or a complaint.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to give a fund or commercial client the most margin capacity per dollar of the FCM's own capital, through cross-margin offsets, eligible collateral and intraday limits set on the client's real risk, and whoever carries the largest client book per dollar of capital without cutting clients off in a margin spike takes the account.

## The Problem
Pre-trade risk controls at the FCM and the exchange cap order size, position and credit per client. Limits too tight block a client's legitimate hedge in a fast market and send the business to a rival. Limits too loose let a client build exposure the FCM cannot fund. Most limits are set once, at onboarding, and adjusted by email when someone notices.

## Why It's Still Broken
Limit reviews compete with onboarding and incident work in small risk teams, and no system shows how a client's trading pattern has changed since its limits were set.

## What a Fix Looks Like
A weekly review that compares each client's limit use, margin volatility and trading pattern with the levels at onboarding, flags accounts whose behaviour has shifted (a step change in size, new products, new trading hours) and proposes adjusted limits with reasons for a risk officer to approve.

## Who Feels the Pain
FCM risk officers, clients whose hedges are blocked mid-session, and the sales staff who lose accounts over it.

## Impact If Fixed
Limits that track real risk keep good clients trading in fast markets and catch drifting ones before the margin call, at the cost of an hour a week of review.
