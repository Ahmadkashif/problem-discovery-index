# Preparer Risk Is Watched Weekly and Understood Annually

**Niche:** [[niches/tax-prep-firms/refund-transfer-banking/profile|Refund Transfer & Advance Banking]]
**Industry:** [[industries/tax-prep-firms|Tax Preparation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The bank monitors thousands of preparation offices for fraud and quality during the season, using thresholds set the previous autumn, and only reconstructs what actually happened after the season is closed and the money is gone.
**Tags:** #change-point-detection #graph-neural-networks #dbscan #confidence-intervals #compliance

## The Problem
Refund products reach the taxpayer through preparation offices — franchise locations, independent shops, seasonal storefronts, numbering in the thousands. The bank's exposure is not really to the taxpayer. It is to the office. An office producing inflated credits, fabricated income, or returns for identities it does not have consent for generates advances that never get repaid, and does it at volume before anyone notices.

So there is a programme risk function watching office-level metrics through the season: funding rates, average refund size, credit claim mix, rejection rates, complaint volume. Offices that cross thresholds get reviewed, restricted, or cut off.

The function works. It is also structurally a season behind.

The thresholds were set in the autumn from last season's distribution. The comparison population is last season's offices. The definition of "unusual" was fixed before this year's filing rules, this year's IRS processing behaviour, and this year's fraud pattern existed. And the label — whether the office's returns actually turned out to be bad — arrives after the refunds resolve, which is after the season, which is after every decision has been made.

The people doing it know this. In a ten-week window with millions of transactions, watching last year's thresholds is what is achievable.

## Why It's Still Broken
The compression is genuine and not solvable by effort. Volume goes from near zero to full in about ten days. Any monitoring baseline computed from a stable period does not exist, because there is no stable period.

The labels are late by construction. Whether a return was fraudulent is revealed by the IRS not paying it, or paying it and later challenging it, and both happen after the advance is made. Supervised learning on outcomes is always training on a season that has ended.

Cutting off an office is expensive and political. Offices are the distribution channel, often under a franchise relationship, and a false positive terminates a legitimate business at the only time of year it earns money. The threshold is therefore set conservatively, which means it catches the obvious and misses the careful.

And the signal that would actually work is relational rather than univariate. A fraud pattern shows up as returns that resemble each other across offices, or as an office whose return population is shaped differently from comparable offices, not as one metric crossing one line. Representing that requires treating preparers, returns and refunds as a connected structure. The monitoring is a table of metrics with thresholds.

The reconstruction that happens in the summer — the post-season review that establishes what really occurred — produces exactly the understanding that was needed in February, and is used to set next autumn's thresholds. Which are then a season behind again.

## What a Fix Looks Like
**Detect change within the season instead of comparing to last one.** The question is not whether an office's numbers exceed a fixed threshold but whether its behaviour has shifted relative to its own recent pattern and to comparable offices filing the same week. That is change detection on a short, fast series, and it works without waiting for labels.

**Build the comparison population dynamically.** Offices should be compared with offices like them — same geography, same client mix, same size, same week of season — not against a single national distribution. Clustering the office population each season produces a peer group that reflects this year, and immediately makes an outlier meaningful.

**Represent the network.** Returns, preparers, refunds, bank accounts and devices form a graph, and organised fraud is visible in it as structure long before it is visible in any single office's metrics. Shared attributes across supposedly unrelated offices are the strongest available early signal and the current tooling does not look for them.

**Attach honest uncertainty to every flag.** An office three weeks into a season has produced few returns and the estimate is correspondingly weak. A flag that arrives with an interval rather than a verdict lets the review team spend its limited capacity where the evidence is actually strong, and makes the conservative threshold unnecessary.

**Close the loop faster with partial outcomes.** Refunds resolve continuously through the season, not all at the end. Early resolutions are a partial label available in real time, and are currently used for reporting rather than for updating the monitoring that produced the decision.

## Who Feels the Pain
The programme risk manager, reviewing threshold breaches at volume with no way to tell a genuinely bad office from a growing one. The honest preparer restricted on a metric that reflected a legitimate change in their client base. And the taxpayer at a fraudulent office, whose return is filed wrong, whose refund is held, and who discovers it months later with no idea why.

## Impact If Fixed
The season is the whole business. Fraud caught in week three prevents the losses of weeks four through ten; fraud caught in June prevents nothing at all. The monitoring function is already staffed, already watching, and already collecting what it needs — it is looking at it a year late.
