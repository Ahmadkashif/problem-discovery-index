# Family Petition Timeline Predictor & Visa Bulletin Monitor

**Niche:** [[niches/immigration-law/family-based-petitions/profile|Family-Based Petitions]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict how long a family-based petition will take from filing to green card by category and country of birth, using historical visa bulletin data and USCIS processing trends — replacing the attorney's vague "it could be 5-10 years" with a data-driven estimate clients can track.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
When a family immigration attorney files an I-130 petition, the client's first question is always "how long will this take?" The honest answer depends on the preference category (immediate relative, F1, F2A, F2B, F3, F4), the beneficiary's country of birth (Mexico, Philippines, India, China, and "all other" each have different backlogs), and the unpredictable monthly movements of the Department of State visa bulletin. Experienced attorneys develop tacit intuition about wait times — they know that F2B Mexico has been moving erratically, that "all other" F4 has been stuck for years, and that certain categories sometimes retrogress without warning. But this knowledge is personal, imprecise, and impossible to communicate to anxious clients in a way that sets realistic expectations. New attorneys have no framework for these estimates at all. Meanwhile, the monthly visa bulletin is published as a PDF table that attorneys must manually cross-reference against their active case list to identify which clients can now file for adjustment of status.

## Why Nobody Has Built This
Historical visa bulletin data exists (DOS publishes monthly) but has never been assembled into a clean, machine-readable time series suitable for forecasting. Bulletin movements are influenced by congressional action, executive policy, USCIS processing capacity, and per-country demand — variables that are difficult to model and subject to regime changes. The market (family immigration attorneys) is fragmented into thousands of small firms with limited software budgets, making SaaS distribution expensive. Additionally, any prediction system must handle the fundamental uncertainty honestly — a forecast that says "7 years" and proves wrong damages attorney-client trust more than the current vague estimate.

## What to Build
A platform with three components: (1) a historical visa bulletin database going back 20+ years, parsed into structured time series by category and country, (2) a time-series forecasting model (gradient boosting on engineered features from bulletin movement patterns, congressional calendar, USCIS processing time data, and per-country demand signals) that produces wait time estimates with confidence intervals — not point predictions, (3) a case portfolio overlay where an attorney uploads their active case list (priority dates and categories), and the system auto-monitors each monthly bulletin, flags cases that are newly current, alerts the attorney to file adjustment applications, and warns of potential retrogression. Client-facing: a branded status page per case showing estimated timeline with a visual progress bar, updated monthly after each bulletin release.

## Target Customer
Family immigration attorneys managing 50+ active I-130 petitions across multiple preference categories, currently spending 2-4 hours each month manually cross-referencing the visa bulletin against their case portfolio.

## Impact If Built
Eliminates 2-4 hours of monthly bulletin analysis per attorney, prevents missed filing windows when priority dates become current (each missed month costs the client 30+ days of additional waiting), and reduces "when will it be approved?" client calls by 40-60% through self-service status access. For a firm with 150 active family cases, catching even one missed current-date filing window per year saves the client months and the attorney a malpractice risk.
