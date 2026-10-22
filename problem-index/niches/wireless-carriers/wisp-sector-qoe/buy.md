# Enterprise Network Monitoring Recast for Shared Rural Sectors

**Niche:** [[niches/wireless-carriers/wisp-sector-qoe/profile|WISP Sector Congestion & Subscriber Experience]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mature network monitoring tools watch links and devices well but don't model a shared radio sector, where one customer's poor signal slows everyone else.
**Tags:** #time-series-forecasting #feature-engineering #data-integration #automation #worker-facing
**Contested on:** Every serious competitor in this niche (subscriber-experience platforms, radio controllers and traffic shapers) is fighting to find first which sector, link or interferer is pushing which homes below plan at evening peak and what to change, and whoever diagnoses and fixes that fastest takes the account.

## The Problem
WISPs often run general network monitoring alongside radio vendors' dashboards. Thresholds on link utilisation miss the real constraint, airtime on a shared sector, and alerts don't say which customers are affected.

## What Already Exists
LibreNMS, Zabbix, PRTG and similar monitoring platforms, plus Preseem and radio vendors' controllers.

## The Customization Gap
The adaptation needs sector airtime and modulation mix as primary metrics, per-customer experience scores, multi-vendor radio ingestion, interference indicators, and alerts phrased as "these 14 homes are below plan at peak because of X".

## Target Customer
WISPs that already run a general monitoring stack and won't replace it.

## Impact If Solved
The monitoring the WISP already runs starts answering the question customers care about.
