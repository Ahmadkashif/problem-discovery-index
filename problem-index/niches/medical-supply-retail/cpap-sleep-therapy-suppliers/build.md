# CPAP Patient Lifecycle and Retention Platform

**Niche:** [[niches/medical-supply-retail/cpap-sleep-therapy-suppliers/profile|CPAP & Sleep Therapy Suppliers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform manages the complete CPAP patient lifecycle — from initial setup through 90-day compliance through years of resupply — in a single system, leaving suppliers to stitch together device data, billing, and patient communication across 4-5 disconnected tools.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #data-integration #revenue-impact

## The Problem
A CPAP supplier manages 2,000 active patients at different lifecycle stages: 200 in the 90-day compliance window, 500 due for resupply this month, 300 who haven't reordered in 6+ months (at risk of churning to an online competitor), and 1,000 in steady-state. Each stage requires different actions: compliance patients need daily usage monitoring and proactive coaching; resupply patients need timely outreach with insurance-eligible order suggestions; at-risk patients need retention intervention. But these stages are tracked across separate systems — device compliance in ResMed AirView, billing status in Brightree, patient communication in a CRM or spreadsheet — and no single view shows the patient's complete status.

## Why Nobody Has Built This
CPAP device manufacturers (ResMed, Philips) provide compliance platforms but intentionally limit integration with competitor devices and with billing systems, creating data silos. Brightree provides billing but not clinical/compliance views. Building a unified platform requires API integration with ResMed AirView, Philips Care Orchestrator, insurance eligibility systems, and the supplier's billing platform — a multi-integration challenge that requires partnerships with entities who may not be motivated to cooperate.

## What to Build
A patient lifecycle platform that ingests compliance data from all CPAP manufacturers (via API), billing and insurance data from Brightree, and patient communication history, and produces: a single patient dashboard showing lifecycle stage, compliance status, insurance eligibility for resupply, and communication history; automated lifecycle workflows (compliance coaching emails at days 14/30/60, resupply outreach at insurance-eligible dates, retention campaigns for inactive patients); and a population-level dashboard showing patient distribution by stage with revenue-at-risk metrics for each cohort.

## Target Customer
Independent CPAP suppliers with 1,000+ active patients who currently manage patient lifecycle across 4-5 disconnected systems with manual coordination.

## Impact If Built
Reduces 90-day compliance failure rate from 15-20% to 8-12% through proactive monitoring (each compliance failure costs $800-1,500 in equipment retrieval and lost revenue). Increases resupply revenue by 15-25% through optimized outreach timing. Reduces patient churn to online competitors by 10-15% through systematic retention workflows. On a 2,000-patient supplier, estimated annual revenue impact of $200K-400K.
