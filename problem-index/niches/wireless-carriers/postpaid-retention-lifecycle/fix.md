# Churn Models Blind at the Promo-Credit Cliff

**Niche:** [[niches/wireless-carriers/postpaid-retention-lifecycle/profile|Postpaid Phone Retention & Upgrade Lifecycle]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Customers locked by 36-month device credits look loyal to the churn model right up to the month the credits end.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche (decisioning platforms, retention analytics vendors and the carriers' own lifecycle teams) is fighting to pick, line by line, the cheapest save offer that actually changes a postpaid customer's decision to port out, and whoever measures save-offer uplift most accurately takes the account.

## The Problem
A customer on a device promotion forfeits the remaining credits by leaving, so they stay. Churn models trained on recent history learn that these customers rarely churn and score them low. When the credits end, the lock disappears and a cohort that looked safe becomes the most targeted segment in the market. The model notices only after the port-outs arrive.

## Why It's Still Broken
Churn models are usually built as monthly classifiers on current features, not as time-to-event models that know when each customer's lock expires. Promotion data sits in the promotion engine, not in the analytics warehouse, and the 24–36-month terms mean the last cliff was years ago.

## What a Fix Looks Like
Rebuild churn as a survival model with the lock-expiry date as a covariate, so risk is scheduled rather than discovered. Join promotion enrolments and credit end dates to every line. Schedule retention contact before the cliff, and report model accuracy separately for locked and unlocked customers.

## Who Feels the Pain
Retention teams surprised by cohort churn spikes, finance teams whose forecasts miss, and care agents fielding the calls from customers already shopping elsewhere.

## Impact If Fixed
A mostly data-plumbing change turns the biggest predictable churn event in the business into a scheduled retention calendar.
