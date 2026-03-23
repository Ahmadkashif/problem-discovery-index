# Resupply Timing and Patient Outreach Optimization

**Niche:** [[niches/medical-supply-retail/cpap-sleep-therapy-suppliers/profile|CPAP & Sleep Therapy Suppliers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Fix (Pain Point)
**One-liner:** CPAP suppliers call patients for resupply on a fixed schedule (every 90 days) regardless of actual usage patterns or insurance eligibility timing, wasting staff calls on patients who aren't ready and missing patients who are.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact #automation

## The Problem
CPAP resupply is governed by insurance eligibility rules: Medicare allows new masks every 3 months, filters every 2 months, and tubing every 3 months. Suppliers set up automated outreach on these fixed schedules — calling or texting every patient at exactly 90 days. But actual replacement need varies: a patient using CPAP 8 hours/night needs supplies sooner than one using it 4 hours/night; a patient with a well-fitting mask might go 4 months before needing replacement; a patient who just switched to a full-face mask might need a refit at 6 weeks. Fixed-schedule outreach wastes staff time (calling patients who don't need supplies yet) and misses revenue (not calling patients who need supplies earlier than the default schedule).

## Why It's Still Broken
Insurance eligibility windows create a compliance constraint — the supplier cannot bill for replacement supplies before the eligibility date, so outreach timing must align with eligibility. But within that constraint, the optimal contact time varies by patient. Current systems (Brightree's resupply module, third-party resupply outreach services like S3 and SnapWorx) use fixed cadences because they don't integrate device usage data into outreach timing. The device data lives in ResMed AirView or Philips platforms, and the outreach scheduling lives in the billing or CRM system — they're not connected.

## What a Fix Looks Like
A resupply optimization engine that combines insurance eligibility dates (from billing system), device usage data (from manufacturer platforms), and historical reorder patterns (from past transactions) to compute the optimal outreach date per patient per supply category. A patient using CPAP 7+ hours/night gets outreach at day 80 (before the 90-day eligibility, to pre-stage the order). A patient using CPAP 4 hours/night gets outreach at day 100 (they're not ready at 90 days). A patient who hasn't used their CPAP in 30 days gets a different workflow (re-engagement, not resupply). Result: fewer wasted calls, higher conversion per call, and more resupply revenue captured.

## Who Feels the Pain
Customer service reps who make 50-100 resupply outreach calls per day with a 15-20% contact-and-convert rate, and operations managers who know the fixed-schedule approach is inefficient but have no data-driven alternative.

## Impact If Fixed
Improves resupply outreach conversion rate from 15-20% to 25-35% by contacting patients at the right time. Reduces wasted outreach calls by 30-40%, freeing staff for higher-value activities. Increases annual resupply revenue by 10-20% per patient through better-timed outreach — on a 2,000-patient base at $500 average annual resupply, this adds $100K-200K in captured revenue.
