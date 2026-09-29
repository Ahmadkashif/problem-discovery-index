# A Diverging Loss Curve at Hour Forty

**Niche:** [[niches/mlops-platforms/large-scale-training-runs/profile|Large-Scale Training Runs]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A team watching a loss curve wobble forty hours into a sixty-day run has to decide whether to intervene or wait, and the decision is made by whoever has seen the most curves.
**Tags:** #change-point-detection #time-series-forecasting #gaussian-processes #hypothesis-testing #confidence-intervals #evaluation-metrics #transfer-learning #loss-functions
**Contested on:** Every serious competitor in this sub-niche is fighting to tell an infrastructure team, while a sixty-day distributed run is still going, whether it is healthy and what to do about it — and whoever does that takes the account, because the run costs more than every tool in the stack combined.

## The Problem
Forty hours in, the loss spikes and partially recovers. Three engineers look at the same chart. One says it will settle, having seen this shape before. One says restart from the last checkpoint with a lower learning rate, losing eleven hours. One says it is a data issue in a specific shard. Nobody knows, the run continues, and either it recovers or two more days of accelerator time are spent on a run that was already lost. The same decision is made at every organisation doing this work, on the same signals, by pattern recognition that nobody has written down.

## Why Nobody Has Built This
The labelled data — runs with their eventual outcomes and what the intervention was — is held by a small number of organisations who regard it as competitive knowledge and do not publish. The failure shapes depend on architecture, scale and data, so folklore from one setting transfers imperfectly to another, which makes people distrust generalisation. The platforms serving this market are built for the classical workload and cannot ingest the telemetry that would support the analysis. And the teams who could build it are fully occupied running the jobs.

## What to Build
Observe the run as a system and say something useful while it is still running. Build the per-rank health view first: throughput, step time, memory, communication time and gradient statistics per rank, with automatic identification of the outlier — because a single straggling or degraded accelerator among a thousand slows the entire job and finding it manually is the most common operational task at this scale. Forecast the loss trajectory with uncertainty and flag departures from it, since an early warning that the run is off its own expected path is more robust than trying to classify failure types across settings. Classify recurring signatures where the corpus supports it — loss spikes that recover against those that do not, silent data corruption, communication degradation, numerical instability — and report a confidence with the evidence rather than a verdict, since an engineer can evaluate a hypothesis and cannot evaluate an assertion. Project cost to completion against the granted budget continuously, which is the number the person who approved the run keeps asking for and which nobody computes. Recommend an intervention with its expected cost: restart from which checkpoint, at what setting, losing how many hours. Detect data pipeline problems separately, since a starved loader and a compute problem look similar on a throughput chart and have unrelated fixes. And accumulate outcomes across runs, which is what makes the classifier improve rather than remaining folklore.

## Target Customer
ML infrastructure and training platform teams, the cloud and accelerator providers hosting these jobs, and the tracking vendors whose architecture currently rules them out.

## Impact If Built
The decision that costs the most is made by whoever has seen the most curves, and nobody has written it down. The per-rank health view is the immediately buildable part and addresses the most frequent operational task at this scale.
