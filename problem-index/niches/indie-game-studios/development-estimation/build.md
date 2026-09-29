# Forecasting From What Actually Happened

**Niche:** [[niches/indie-game-studios/development-estimation/profile|Development Estimation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most common cause of studio failure is a schedule, and nobody in the sector forecasts one from their own data.
**Tags:** #time-series-forecasting #survival-analysis #monte-carlo-methods #evaluation-metrics #confidence-intervals #revenue-impact #gradient-boosting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a small team when their game will actually be finished — and whoever forecasts from recorded velocity rather than from optimism prevents the failure that kills more studios than bad games do.

## The Problem
A team plans eighteen months on the basis of what they hope, works at a velocity they never measure, discovers at month twenty that they are not close, and funds the remainder from savings until either the game ships or the studio does not. The information that would have produced a realistic forecast — how much they actually completed per month, how scope changed, how their estimates compared to their actuals — was generated continuously and recorded nowhere.

## Why Nobody Has Built This
Estimation feels antithetical to creative work, so process tools are resisted and the failure is attributed to the nature of making games — a discipline that believes its work is unestimable will not measure the work and therefore never discovers otherwise. Teams are too small to have a producer. Project management tools are built for organisations. And the overrun is normalised as a fact of the industry rather than examined as a cause of failure.

## What to Build
Record the velocity and forecast the runway. Record completion velocity automatically from the work itself — commits, assets, tasks, builds — which is the core and removes the tracking discipline nobody sustains. Forecast completion as a distribution rather than a date, since a range with a probability is honest and a date is not. Track scope growth explicitly, because the overrun is usually scope rather than slowness and the two need different responses. Model the runway against the forecast, as the decision that matters is whether the money reaches the finish and it is never computed. Warn early, since a team told at month eight that the schedule is doubling has options and one told at month twenty does not. Compare against the studio's own history and against comparable projects from the corpus, which is what makes a first-project forecast possible at all. Offer scope reduction scenarios rather than only a warning, because the realistic response is cutting and nobody frames it that way. Keep the instrumentation invisible, as anything requiring daily discipline will be abandoned. Report the estimate against the actual at the end, so the studio's next project starts with a calibration. And make it usable by a team of two, which is the only constraint that matters.

## Target Customer
Studio leadership, funders and publishers exposed to the overrun, platform holders whose ecosystem loses studios to it, and project forecasting vendors.

## Impact If Built
A discipline that believes its work is unestimable will not measure the work and therefore never discovers otherwise. Recording velocity from the work itself removes the tracking burden and makes the runway question answerable while there are still options.
