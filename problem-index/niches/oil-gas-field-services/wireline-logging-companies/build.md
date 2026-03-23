# Automated First-Pass Log Interpretation

**Niche:** [[niches/oil-gas-field-services/wireline-logging-companies/profile|Wireline Logging Companies]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product generates a complete first-pass petrophysical interpretation from raw wireline log data — identifying formation tops, calculating water saturation, and flagging productive zones — as a starting point for petrophysicist review.
**Tags:** #cnn #lstm #multiclass-classification #time-series-forecasting #tabular-ml #tacit-knowledge-ml

## The Problem
A petrophysicist receiving a new well's log data spends 4-16 hours on initial interpretation: loading curves, identifying formation tops by comparing to offset wells, selecting appropriate interpretation models (Archie, dual-water, shale-corrected), applying cutoffs for porosity and water saturation, calculating permeability from empirical correlations, and flagging zones that meet pay criteria. This initial pass produces a draft interpretation that is then refined through iteration and peer review. The 4-16 hours of initial interpretation is largely pattern matching against previously interpreted wells in the same basin and formation — exactly the kind of task that ML should accelerate.

## Why Nobody Has Built This
Log interpretation depends on geological context: the same gamma ray reading means different things in the Permian Basin versus the Bakken. Saturation calculations require parameters (Archie's cementation and saturation exponents) that vary by rock type. Formation top identification requires pattern recognition across multiple curves simultaneously, informed by regional stratigraphic knowledge. Building an automated interpreter requires training data — thousands of interpreted wells with expert labels — that is proprietary to operators and service companies. No public dataset of labeled log interpretations exists, and operators are reluctant to share proprietary geological intelligence.

## What to Build
A basin-specific auto-interpretation engine trained on previously interpreted wells from the same geological setting. Given raw LAS data, the system: identifies formation tops by comparing curve signatures to labeled offset wells, selects interpretation parameters appropriate for each formation, calculates porosity, water saturation, and permeability using the selected models, applies pay cutoffs to flag productive intervals, and generates a draft interpretation report. The petrophysicist reviews, corrects, and approves the draft — reducing interpretation time from 4-16 hours to 1-3 hours of review and refinement. Each correction feeds back into the model's training data.

## Target Customer
Independent wireline logging companies and operator petrophysics teams processing 50+ well logs per year who need to accelerate interpretation turnaround from days to hours.

## Impact If Built
Reduces initial interpretation time by 60-80% (saving $2,000-$10,000 per well in petrophysicist time), enables same-day preliminary interpretation versus the current 3-7 day turnaround, and standardizes interpretation quality across junior and senior petrophysicists.
