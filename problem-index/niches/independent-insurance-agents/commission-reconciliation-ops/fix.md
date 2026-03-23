# Unexplained Commission Variance Investigation

**Niche:** [[niches/independent-insurance-agents/commission-reconciliation-ops/profile|Commission Reconciliation Operations]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Fix (Pain Point)
**One-liner:** When a carrier's commission payment does not match the expected amount, the bookkeeper spends 30-60 minutes per variance investigating the cause — a process that involves cross-referencing 3-4 systems and sometimes calling the carrier.
**Tags:** #anomaly-detection #tabular-ml #automation #worker-facing

## The Problem
Commission variances are common: a carrier pays $3,200 when the agency expected $3,400. The cause could be a mid-term endorsement reducing premium, an audit adjustment, a policy cancellation the agency was not notified of, a carrier rate change, a commission rate error, or a timing difference between the carrier's statement period and the agency's records. The bookkeeper must investigate each variance by checking the AMS policy history, the carrier portal for endorsement activity, prior commission statements for adjustments, and sometimes calling the carrier's commission department. At 20-40 variances per month, this investigation consumes 10-20 hours.

## Why It's Still Broken
Variance investigation requires joining data across systems that do not share a common identifier: the AMS policy number, the carrier's policy number, and the commission statement line item may all reference the same policy differently. The root cause of a variance is often a mid-term policy change that was processed in the carrier's system but not yet downloaded to the AMS — a timing issue that resolves itself next month but is indistinguishable from an actual error without investigation. No tool pre-diagnoses variance causes by cross-referencing AMS, carrier download, and commission statement data.

## What a Fix Looks Like
An automated variance diagnosis tool that, when a commission discrepancy is flagged, checks the AMS for recent policy changes (endorsements, cancellations, audits), compares the carrier's commission rate against the agency agreement, checks prior statements for adjustments or chargebacks, and presents the bookkeeper with a probable cause and supporting evidence. The bookkeeper reviews the diagnosis instead of investigating from scratch — resolving the variance in 2-3 minutes instead of 30-60 minutes.

## Who Feels the Pain
Agency bookkeepers who spend 10-20 hours per month investigating commission variances that are mostly caused by predictable and diagnosable system timing differences.

## Impact If Fixed
Reduces variance investigation time by 80%, recovering 8-16 hours per month. Ensures that actual carrier errors (rate discrepancies, missing policies) are identified and disputed within 30 days, recovering an estimated $5K-$20K annually in underpaid commissions at a mid-size agency.
