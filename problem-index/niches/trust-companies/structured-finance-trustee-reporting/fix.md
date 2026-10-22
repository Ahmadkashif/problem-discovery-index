# Servicer Data That Arrives the Night Before Determination Date

**Niche:** [[niches/trust-companies/structured-finance-trustee-reporting/profile|Structured Finance Trustee Reporting]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Fix (Pain Point)
**One-liner:** The trustee's calculation depends on the servicer's or manager's monthly file, which often arrives late and occasionally wrong, leaving hours to find the error before distributions are fixed.
**Tags:** #change-point-detection #feature-engineering #evaluation-metrics #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to compute every payment-date waterfall, coverage test and investor report correctly from the deal documents and the servicer's or manager's data before the distribution date, and whoever does it with the fewest restatements takes the account.

## The Problem
A servicer report with a mis-keyed collection figure or a pool balance that does not roll forward flows straight into distributions. Analysts check files by eye against last month under deadline.

## Why It's Still Broken
Each servicer has its own format, deals are too varied for fixed rules, and the trustee's role is often described as relying on servicer data rather than verifying it, so validation is under-invested.

## What a Fix Looks Like
Automated validation on arrival: roll-forward checks on balances, comparisons against each deal's own history with flags for breaks in collections, delinquencies and prepayments, and checks against document thresholds and triggers. Exceptions go back to the servicer immediately with the specific question.

## Who Feels the Pain
Trustee reporting analysts on determination dates; investors receiving restated reports; servicers fielding late queries.

## Impact If Fixed
Errors caught on arrival instead of after distribution remove most restatements and give analysts their determination-date hours back.
