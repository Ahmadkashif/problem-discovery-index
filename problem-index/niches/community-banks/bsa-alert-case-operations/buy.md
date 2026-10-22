# Consortium Detection Tuned to the Bank's Own Customers

**Niche:** [[niches/community-banks/bsa-alert-case-operations/profile|BSA/AML Alert & Case Operations]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consortium monitoring platforms already see patterns across thousands of institutions; what they cannot see is that this bank's cash-heavy customers are a seed dealer and two car washes that have deposited the same way for fifteen years.
**Tags:** #gradient-boosting #graph-theory #time-series-forecasting #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to close the alerts that are noise without missing the one that becomes a SAR, and whoever can prove to an examiner that its deprioritised alerts were safe takes the account.

## The Problem
Cross-institution detection models are trained on pooled behaviour. A community bank's customer base is local and seasonal, so the same model flags the same legitimate customers every harvest and every holiday.

## What Already Exists
Verafin and other consortium platforms combine transaction data across many institutions to detect fraud and money laundering patterns, including mule networks and schemes that cross banks. The consortium research teams are profiled under Credit Unions as [[niches/credit-unions/financial-crime-consortium-analytics/profile|🔍 Financial Crime Consortium Analytics]].

## The Customization Gap
The bank needs: (1) customer-level seasonal baselines learned from its own multi-year history, so recurring patterns are expected rather than flagged; (2) its own past dispositions fed back as labels rather than left in the case system; (3) local context (agricultural cycles, tourism seasons, a single large employer's payroll) as features; and (4) documentation of each adaptation for the bank's model validation.

## Target Customer
BSA officers at community banks already on a consortium platform whose false positives come from a stable local customer base.

## Impact If Solved
Fewer recurring false alerts on known customers, without giving up the cross-bank view that catches what one bank cannot see.
