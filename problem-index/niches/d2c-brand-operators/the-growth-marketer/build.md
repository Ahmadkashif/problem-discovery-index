# A Week Spent Producing a Report Nobody Believes

**Niche:** [[niches/d2c-brand-operators/the-growth-marketer/profile|The Growth Marketer]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A growth marketer spends a large share of every week reconciling numbers from platforms that disagree, producing a report whose central figures they do not believe, to inform decisions they will make on intuition anyway.
**Tags:** #data-integration #workflow-orchestration #automation #descriptive-statistics #evaluation-metrics #worker-facing #confidence-intervals #quick-win
**Contested on:** Every serious competitor in this niche is fighting to stop a skilled marketer spending their week assembling a report they do not believe — and whoever does that takes the account, because that week is the largest recurring waste in the function.

## The Problem
Monday morning: export spend and conversions from four ad platforms, pull orders from the commerce platform, pull email results, paste everything into the workbook, reapply the manual adjustments that reconcile last week's known discrepancies, refresh the pivot tables, rebuild the chart, and write three paragraphs explaining movements the marketer suspects are measurement noise. Five hours. The resulting deck is presented, the central return figure is questioned as it is every week, the marketer explains the caveats, and the budget decision is made on a mixture of the trend and somebody's judgement. Next Monday it happens again.

## Why Nobody Has Built This
Every brand's stack differs slightly, which makes the reconciliation feel bespoke and hides that the process is identical. Dashboard tools connect to the platforms and reproduce their numbers rather than reconciling them against orders, which is the hard part. The marketer is too busy doing it to automate it. And the time is invisible, buried inside a salaried role rather than appearing as a cost.

## What to Build
Automate the assembly and address the disbelief separately. Build the pipeline from the platforms and the commerce data into one reconciled model, refreshed automatically, which is ordinary data engineering and eliminates the five hours — this is the immediate win and it is not what dashboard tools currently do, because they stop at the platforms. Anchor everything to the brand's own orders as the single source of truth, so the report is built from what happened rather than from what was claimed. Persist the reconciliation logic rather than reapplying adjustments by hand, so last week's fixes are this week's code. Track the discrepancies over time as their own metric, which the fix note develops and which converts a weekly argument into a monitored quantity. Generate the commentary on movements, flagging which are outside normal variation and which are not, so the marketer writes about the real ones. Show uncertainty, so a movement inside the noise is presented as such rather than explained. Record which numbers informed which decision, so the connection between measurement and allocation can be reviewed later. Report the time saved, because that is what justifies the build to whoever funds it. And leave the judgement to the marketer, since their intuition is frequently better than the numbers and the problem is that it has to be exercised after five hours of unnecessary work.

## Target Customer
Growth organisations and their leadership, the marketers doing the assembly, and the analytics vendors whose products stop at the platform boundary.

## Impact If Built
Five hours a week per marketer goes to an assembly that is identical in every brand and is treated as bespoke. Anchoring the model to the brand's own orders is what the dashboard tools do not do, and it is what makes the resulting report worth the time it no longer takes.
