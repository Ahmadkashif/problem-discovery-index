# Feasibility — Pressman Color Matching During Makeready

**Industry:** [[printing-shops|Printing Shops]]
**Problem:** [[problems/printing-shops/worker-life-1|Pressman Color Matching During Makeready]]
**Problem type:** Worker Life

**Problem summary:** Pressmen who spend 20-45 minutes per job adjusting ink density, water balance, and registration by eye to match a PMS swatch or customer proof — the highest-skill task on the press floor and the one most dependent on years of visual calibration that the pressman cannot articulate — could cut makeready color time in half with a model that predicts ink key settings from spectrophotometer scan bar readings.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
