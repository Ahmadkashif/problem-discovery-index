# The Backtest That Used Tomorrow's Number

**Niche:** [[niches/financial-data-vendors/fundamentals-and-estimates/profile|Fundamentals & Estimates Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Quant clients backtest on fundamentals and consensus history that silently includes restated values and late corrections that were not known on the date in question.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #data-integration #compliance #revenue-impact
**Contested on:** Not terminal as stated — competitors here are fighting either to standardise a new filing correctly within hours and explain every derived number, or to hold the broadest contributed broker estimates and clean them into a trusted consensus; these are different contests with different winners, stated separately in the sub-niches.

## The Problem
A systematic fund tests a signal on twenty years of history. If the vendor's history shows the restated figure rather than the one originally reported, or a corrected estimate rather than the one in the consensus on the day, the backtest has look-ahead bias and the signal looks better than it is. Point-in-time products exist precisely for this, but their coverage is uneven across fields, decades and the vendor's own corrections.

## Why It's Still Broken
Corrections overwrite. A collection error fixed in 2019 for a 2012 filing is often stored as the 2012 value, with no record that the client could not have seen it then. Building true point-in-time history requires the decision record most vendors never kept.

## What a Fix Looks Like
Version every value with as-known dates for original release, restatement and correction, and expose them separately. Publish coverage statistics for point-in-time completeness by field and year, so clients know where the history is reliable. Treat vendor corrections as first-class events in the history. And provide a test clients can run to measure how much of a backtest's result depends on values revised after the fact.

## Who Feels the Pain
Quant researchers whose signals decay on contact with live trading, and the vendor's sales team, who lose systematic clients to competitors with cleaner history.

## Impact If Fixed
Point-in-time integrity is the deciding criterion for quant buyers. Making corrections visible as events converts an embarrassing weakness into a demonstrable quality.
