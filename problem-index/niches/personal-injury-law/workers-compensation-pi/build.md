# Workers' Comp Impairment Rating & Benefit Calculator

**Niche:** [[niches/personal-injury-law/workers-compensation-pi/profile|Workers' Compensation PI]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Workers' comp plaintiff attorneys get a single tool that computes impairment ratings, benefit entitlements, and settlement ranges using state-specific schedules — replacing manual lookups across AMA Guides, state rate tables, and benefit formulas that produce costly calculation errors.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
A workers' comp plaintiff attorney must calculate their client's benefits and projected settlement value using a chain of state-specific rules. First, compute the Average Weekly Wage (AWW) from pay stubs, which varies by state — some states include overtime, some don't, some use 52-week lookback, some use 26. Then apply the state's compensation rate (typically 66.7% of AWW, but subject to state minimums and maximums that change annually). Then determine the impairment rating using the AMA Guides (a 600-page reference with body-part-specific rating tables) or state-specific rating guides (Florida uses its own, not AMA). Then apply the state's Permanent Partial Disability schedule to convert the impairment rating to weeks of benefits. An experienced WC attorney can look at a case and estimate the settlement value within 10-15% in five minutes. A new attorney takes hours and still gets it wrong. This is classic tacit knowledge — the experienced practitioner has internalized the interaction of AWW rules, impairment tables, and PPD schedules through hundreds of cases.

## Why Nobody Has Built This
The rules are state-specific (50 states + DC + federal FECA), change frequently (states update benefit maximums and rate tables annually), and interact in complex ways (the AWW calculation affects the compensation rate which multiplies by the PPD weeks which are derived from the impairment rating). Maintaining an accurate, current rules engine across all jurisdictions is an ongoing data management burden. Additionally, the impairment rating process involves medical judgment — interpreting how a specific injury maps to the AMA Guides' body-part-specific rating tables requires understanding medical terminology, range-of-motion measurements, and diagnostic criteria. No existing tool bridges the gap between medical documentation and impairment rating calculation.

## What to Build
A workers' comp calculation platform with three modules. (1) AWW Calculator: input pay stubs or W-2 data, select state, auto-compute AWW using state-specific rules (overtime inclusion, lookback period, concurrent employment). (2) Impairment Rating Estimator: input diagnosis, body part, and functional limitations; the system suggests likely impairment rating ranges from the applicable guide (AMA 5th/6th edition or state-specific) with confidence intervals. A gradient-boosted model trained on historical impairment rating determinations predicts the likely rating given the medical inputs, capturing the tacit knowledge of experienced rating physicians. (3) Benefit & Settlement Calculator: given AWW and impairment rating, compute TTD/TPD/PPD benefit amounts, maximum benefit caps, and projected settlement range based on historical settlements in that jurisdiction for similar injuries. All three modules integrated into a single workflow.

## Target Customer
Workers' comp plaintiff attorneys in small-to-mid-size firms (1-20 attorneys) who handle WC claims as a significant practice area and currently compute benefits manually using state-published tables and the AMA Guides reference book.

## Impact If Built
Eliminates benefit calculation errors that cost clients thousands (a 1-point impairment rating error in Pennsylvania can change a PPD award by $5,000-$15,000). Reduces settlement valuation time from hours of manual calculation to minutes. Captures the tacit knowledge of experienced WC attorneys and rating physicians, enabling new attorneys to produce accurate valuations without years of experience.
