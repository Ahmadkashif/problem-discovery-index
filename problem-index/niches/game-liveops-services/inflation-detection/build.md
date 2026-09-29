# An Index That Shows the Drift

**Niche:** [[niches/game-liveops-services/inflation-detection/profile|Inflation Detection]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The drift that ruins a game economy compounds for a quarter in plain sight of dashboards that cannot show it.
**Tags:** #time-series-forecasting #change-point-detection #descriptive-statistics #confidence-intervals #evaluation-metrics #automation #data-integration #exponential-smoothing
**Contested on:** Every serious competitor in this niche is fighting to make a slow compounding economic drift visible while it is still cheap to correct — and whoever builds the instrument that shows it takes the account.

## The Problem
Economic drift in a live game is slow, compounding and undetectable in the reports teams actually watch. Revenue holds up for months while the currency stock inflates. Engagement looks stable while the value of every reward erodes. By the time the symptom is obvious — rewards feel meaningless, purchases feel pointless, progression feels flat — the correction required is large, visible to players, and reads as a nerf.

## Why Nobody Has Built This
No index exists, so there is nothing to trend. The analytics stack was built for commercial reporting and economic series were never in scope. Nobody owns economic health as a metric. And the slow failure has no incident to trigger investigation.

## What to Build
Build the index first and alert on it. Construct a price index over a representative basket of in-game goods and track it continuously, which is the core and is the single instrument the category is missing. Measure reward value in real terms — what an hour of play buys — rather than in nominal currency, since that is the quantity players actually experience. Track currency stock, velocity and the sink-to-faucet ratio as standing series. Detect the change point rather than waiting for a threshold, because drift has no level at which it becomes wrong and the useful signal is the inflection. Attribute each inflection to the parameter change or event nearest it, which turns an alert into an action. Break the index out by cohort, as veterans and new players face different price levels in the same game. Cover premium currency and key item categories separately, since they are separate economies. Report weekly with a monthly trend, which matches the timescale of the failure. Set an expected corridor rather than a fixed target, and alert on exit from it. And make the whole thing installable against the game's existing tables without a data project, which is what determines whether it ever gets deployed.

## Target Customer
Live game operators, live ops platform vendors, games analytics providers, and economy design teams.

## Impact If Built
The drift has no threshold at which it becomes wrong, so only the inflection is detectable — and nothing in the current stack computes a series to find one in. A price index over a representative basket is the instrument the category is missing.
