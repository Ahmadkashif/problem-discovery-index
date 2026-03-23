# Academic Calendar-Aware Demand Forecasting

**Niche:** [[niches/coffee-shops-independent/campus-adjacent-shops/profile|Campus-Adjacent College Town Shops]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No demand forecasting tool accounts for academic calendars — the single strongest demand driver for campus coffee shops.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact #data-integration

## The Problem
A campus coffee shop's demand is governed by the university calendar more than any other factor: first week of classes (surge), reading week (surge), finals (peak surge), winter break (cliff), spring break (cliff), summer (60% drop). Within semesters, demand shifts by the hour as class schedules change — a 10:15 class break drives a 10-minute spike. No forecasting tool ingests academic calendar data (semester start/end, exam schedules, class time blocks) as features, so owners forecast from gut feel and get surprised every September and May.

## Why Nobody Has Built This
The feature requires institution-specific calendar data that isn't available through standard APIs — semester dates, finals schedules, and class times must be scraped from university registrar websites or manually entered. Each campus shop serves a different institution with a different calendar. The addressable market (~3,000-5,000 campus-adjacent independents) is too small for generic demand forecasting vendors to build for, and too fragmented for a one-size-fits-all solution.

## What to Build
A demand forecasting module that takes university calendar data (semester dates, exam periods, breaks, graduation) and class schedule blocks as features alongside standard POS history, weather, and day-of-week signals. Outputs hourly demand forecasts that correctly predict the September 2 enrollment-day surge and the December 15 finals-end cliff. Includes a calendar import tool that parses common university registrar formats.

## Target Customer
Independent coffee shop owners within 0.5 miles of a college or university campus, doing $300K-$1M annually with 40-70% student customer base.

## Impact If Built
Reduces staffing misallocation during calendar transitions by 30-50%, preventing $2,000-$5,000/month in labor waste during summer and $1,000-$3,000/month in lost revenue during unexpected demand spikes (move-in week, homecoming).
