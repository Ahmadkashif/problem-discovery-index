# Estimating Accuracy Invisible Until Jobs Complete

**Niche:** [[niches/metal-fabrication/estimating-and-quoting-automation/profile|Estimating & Quoting Automation]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Fix (Pain Point)
**One-liner:** A fabrication shop owner doesn't know whether a job is profitable until it ships — by which time the work is done, the quote is locked, and any over-run is absorbed as a sunk cost with no mechanism to adjust future pricing for similar work.
**Tags:** #automation #revenue-impact #worker-facing

## The Problem
Fabrication job profitability is a trailing indicator — the owner knows the job made or lost money only after it completes, ships, and the actual labor and material costs are tallied (if they're tallied at all). For a job with a 6-week fabrication timeline, the owner may not learn about a 30% labor over-run until weeks after the work is finished. The estimator has already quoted 20 similar jobs in the interim using the same assumptions that caused the over-run. The financial damage compounds: by the time the over-run is discovered, the shop has committed to more work at the same inaccurate pricing.

## Why It's Still Broken
Real-time job cost tracking requires operators to log time per job as they work — a data collection step that competes with production. Most shops don't track time at the job level (operators clock in for the day, not per job), so actual labor cost per job is estimated from total shop hours rather than measured directly. Without per-job time tracking, actual cost visibility is available only at the monthly financial statement level — too late and too aggregate to identify specific job-level problems.

## What a Fix Looks Like
A lightweight per-job time tracker: operators tap to start/stop a timer when they begin and end work on a specific job. Material consumption is recorded at the job level (material pulled from inventory is deducted against the job). A mid-job dashboard compares hours-to-date and material-to-date against the quote, flagging any job that is trending more than 15% over estimate. The alert fires mid-production — while there's still time to investigate the over-run (is it a one-time issue or a systematic estimating error?), adjust remaining work (can the remaining operations be done more efficiently?), or at minimum, flag the quote assumptions for correction on future similar jobs.

## Who Feels the Pain
Shop owners who discover at the end of the month that margin was worse than expected but can't identify which specific jobs caused the shortfall, and estimators who never learn whether their assumptions were accurate.

## Impact If Fixed
Enables mid-job cost intervention — catching over-runs at 40-60% completion rather than 100%. Provides the actual-vs-quoted data that drives systematic estimating improvement. For a shop running 40 jobs/month where 8 over-run by more than 20%, catching half of those over-runs mid-job and recovering 50% of the excess cost saves $50,000-$150,000 annually depending on shop size and average job value.
