# Change-in-Scope Rate Adjustments Never Filed

**Niche:** [[niches/community-health-centers/medicaid-pps-wraparound-revenue/profile|Medicaid PPS & Managed-Care Wraparound Revenue]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A health center adds dental, behavioral health or a pharmacy and its cost per visit rises, but its Medicaid PPS rate stays frozen at the old cost base because nobody files the change-in-scope request inside the state's window.
**Tags:** #descriptive-statistics #feature-engineering #compliance #revenue-impact #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to collect the full Medicaid PPS rate on every qualifying health center visit, including managed-care wraparound and change-in-scope adjustments, and whoever leaves the smallest gap between PPS due and PPS collected per Medicaid visit takes the account.

## The Problem
PPS rates rise each year only by an inflation index. When a center changes the type, intensity, duration or amount of its services, it can ask the state to recompute the rate, but only after crossing a threshold (3% in Colorado, 4% in Nevada, 5% in South Carolina) and within a filing window (search summary).

## Why It's Still Broken
The trigger sits in operations: a new dental suite, an integrated behavioral health programme, a mobile unit. The rules sit with finance. The cost analysis needs a full cost report. Small centers file rarely, and some never do.

## What a Fix Looks Like
A monitor that compares cost per visit and service mix by quarter against the base-year rate, flags when a threshold is likely crossed, opens the state's application with the cost data filled, and tracks the window.

## Who Feels the Pain
CFOs and reimbursement managers, and the boards that approved the new service on the strength of revenue projections.

## Impact If Fixed
A 5% rate increase on 40,000 Medicaid visits a year at ~$250 is ~$500,000 a year (estimate), lost for every year the request goes unfiled.
