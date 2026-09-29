# Nobody Scores the Forecasters

**Niche:** [[niches/crm-platforms/enterprise-sales-forecasting/profile|Enterprise Sales Forecasting]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every deal eventually closes or does not, every participant made a prediction about it, and no organisation keeps a record of who predicted what — so the forecasting process has run for decades with no feedback.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #probability-distributions #workflow-orchestration #quick-win #worker-facing
**Contested on:** Every serious competitor in sales forecasting is fighting to produce a number a sales leader will submit without rebuilding it in a spreadsheet — and whoever forecasts most accurately from unfalsifiable behaviour rather than from self-reported stage takes the account.

## The Problem
At the start of the quarter a representative calls eleven deals as committed. A manager moves two out and one in. The leader takes 15% off the total. The quarter ends. The organisation compares the submitted number to the actual and discusses the variance, and then the cycle repeats — with no record of which of the eleven deals the representative was right about, whether the manager's two adjustments helped, or whether the leader's discount was the right size. The ground truth arrives every quarter and is never joined to the predictions that preceded it.

## Why It's Still Broken
Forecast submissions are treated as a management ritual rather than as data, and the intermediate predictions are overwritten as the quarter progresses — the CRM shows the current state, not the state on the first Monday. Retaining them is a snapshot and a schema decision that nobody made. There is also an obvious reluctance: a record of forecast accuracy is a record of who is reliably optimistic, and in an organisation where forecasting is entangled with compensation and status, that is an uncomfortable artefact to create.

## What a Fix Looks Like
Snapshot every forecast submission and score it against the outcome. Each participant's call on each deal, at each submission point, retained immutably. At quarter end, the scoring is arithmetic: hit rate on committed deals, calibration of stated probabilities, systematic bias by participant and by segment, and whether each layer of adjustment improved or degraded the number beneath it. Deliver it first to the individual as their own information, and in aggregate to leadership — the same design that makes the adjuster scorecard in the claims niche workable rather than punitive. Report bias and dispersion separately, since a consistently optimistic forecaster is correctable with an offset and an erratic one is not. And handle small samples honestly, because a manager with fourteen deals a quarter does not have a measurable pattern in one quarter and treating noise as skill is both wrong and corrosive.

## Who Feels the Pain
Representatives told their forecast is unreliable with no evidence about their own record; managers applying discounts by instinct with no way to know if the instinct is calibrated; and finance, receiving a number whose production process has never been evaluated.

## Impact If Fixed
Forecast snapshotting is a schema change and a scheduled job, and it produces the feedback loop that a decades-old organisational practice has run without. Most organisations discover that one layer of their forecast hierarchy adds nothing and another adds a great deal, which changes the process immediately — and it is the baseline any behavioural forecast has to beat to be adopted.
