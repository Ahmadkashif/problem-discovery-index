# The Sealed Record That Keeps Coming Back

**Niche:** [[niches/investigation-and-screening-firms/candidates-with-records/profile|Candidates With Records]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Screeners refresh national criminal databases on their own schedules, so a record sealed by a court can keep appearing in reports for months.
**Tags:** #change-point-detection #descriptive-statistics #compliance #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a candidate's wrong, sealed or incomplete record corrected or explained before the employer's response window closes, and whoever resolves the most candidate challenges inside that window takes the account.

## The Problem
National criminal databases are assembled from bulk court and corrections data refreshed monthly, quarterly or less often by source. A record sealed or expunged after the last refresh stays in the database. Good practice is to confirm database hits at the source court before reporting, but not every product does, and a candidate who disputed the record once may see it again from another screener.

## Why It's Still Broken
Sealing does not generate a feed; it removes a record silently. Detecting removals means comparing consecutive bulk pulls, which many vendors do not keep.

## What a Fix Looks Like
Keep consecutive source snapshots and flag records that disappear between pulls as possibly sealed or expunged; suppress them from database results pending source confirmation; and maintain a suppression list of every record removed through a candidate dispute so it is not reported again.

## Who Feels the Pain
Candidates who did everything right; screeners facing repeat disputes and accuracy suits; employers who rescinded offers on records that no longer existed.

## Impact If Fixed
A modest data-engineering change stops the most avoidable accuracy errors in criminal screening.
