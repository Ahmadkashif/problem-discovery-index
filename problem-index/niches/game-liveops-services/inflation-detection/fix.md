# Rewards Stopped Meaning Anything and Nobody Can Date It

**Niche:** [[niches/game-liveops-services/inflation-detection/profile|Inflation Detection]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** The team agrees the economy is broken, agrees it happened gradually, and cannot say when or because of what.
**Tags:** #quick-win #descriptive-statistics #change-point-detection #evaluation-metrics #time-series-forecasting #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to make a slow compounding economic drift visible while it is still cheap to correct — and whoever builds the instrument that shows it takes the account.

## The Problem
A familiar conversation on a mature live game: rewards do not feel rewarding, the shop is irrelevant to established players, progression has flattened, and everyone agrees it has been getting worse for a while. Nobody can say which change started it, because no series exists to look back along. The team's options are to guess at a correction or to do nothing, and both are bad.

## Why It's Still Broken
Nothing was recorded as a time series — an economy with no historical index cannot be diagnosed retrospectively, however complete the raw data, because the question is about a trend nobody computed. Parameter changes are not logged against outcomes. The symptom is qualitative and arrives late. And reconstructing the history feels like a project rather than a query.

## What a Fix Looks Like
Reconstruct the history from the transaction log, which is still there. Backfill the currency stock and price index from historical transaction data, which is the fix and is usually a day of SQL rather than the project it is imagined to be. Overlay the parameter change history onto the series, since the inflection points and the change dates usually line up immediately. Compute reward value in real terms over time, as that series is what the players are describing. Identify the change points statistically rather than by eye, which avoids arguing about where the trend turned. Separate the effect of a specific event from the long trend. Compare cohorts by join date, because the complaint is usually loudest among veterans whose economy diverged first. Quantify the correction needed rather than guessing at it, which is what makes the fix survivable with the community. Publish the series from that day forward so this never recurs. Keep a parameter change log joined to it as standing practice. And name the specific change that started it where the evidence supports it, since that is what stops the same decision being repeated.

## Who Feels the Pain
Live teams arguing about a problem nobody can date; designers facing a correction they cannot size; players in an economy that stopped working; and leadership told the game is in decline.

## Impact If Fixed
An economy with no historical index cannot be diagnosed retrospectively, however complete the raw data, because the question is about a trend nobody computed. Backfilling the index from transaction history usually dates the cause on the first chart.
