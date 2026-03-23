# Cross-Platform Campaign Anomaly Detection and Health Dashboard

**Niche:** [[niches/marketing-agencies-smb/paid-media-agencies/profile|Paid Media (PPC/Social Ads) Focused Agencies]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product provides a single morning briefing across all clients and all ad platforms showing which campaigns have anomalies, pacing issues, or optimization opportunities — PPC specialists check each platform manually for each client every day.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A PPC specialist managing 20 clients across Google Ads and Meta starts their morning by logging into each account on each platform, checking yesterday's performance against expectations, and identifying issues. This manual scan takes 60-90 minutes per day and relies on the specialist's pattern recognition: "this campaign's CPC jumped 40% overnight — that's unusual" or "this client's conversion rate dropped but their spend is normal — probably a tracking issue." Senior media buyers catch these patterns instantly from experience; junior buyers miss them until the damage accumulates. No tool aggregates all campaigns across all clients and platforms into a single anomaly-ranked view that surfaces the items requiring immediate attention.

## Why Nobody Has Built This
Each ad platform has its own API with different data structures, different metric definitions, and different latency characteristics. Google Ads reports hourly data, Meta may have 24-48 hour attribution delays, and Microsoft Advertising has a different reporting schema entirely. Building a cross-platform anomaly detector requires normalizing these data sources, defining "anomaly" relative to each campaign's own baseline (a 30% CPC increase is normal for a competitive keyword during peak season), and learning the patterns that experienced media buyers flag as concerning vs. those they ignore as normal variation.

## What to Build
A morning briefing system that pulls overnight performance data from all ad platforms (Google Ads, Meta, Microsoft, LinkedIn, TikTok) for all managed clients, computes anomaly scores for each campaign based on deviation from recent baselines (adjusted for day-of-week, seasonality, and budget changes), and presents a prioritized list: "Client A Google Ads: CPC up 45% overnight — investigate keyword competition" / "Client B Meta: conversion tracking stopped firing at 6 PM yesterday — check pixel" / "Client C: budget pacing at 120% — will overspend by $800 this month." The system learns from the specialist's actions: if they investigate an anomaly and find it irrelevant, that pattern is downweighted in future scoring.

## Target Customer
PPC directors and senior media buyers at agencies managing 15-60 client accounts across 2-4 ad platforms, who currently spend 60-90 minutes daily on manual cross-account monitoring.

## Impact If Built
Reduces daily campaign monitoring time from 60-90 minutes to 15-20 minutes, catches anomalies 6-12 hours earlier (before a full day of wasted spend), and enables junior buyers to catch the same issues that currently only senior buyers detect — eliminating the tacit knowledge bottleneck.
