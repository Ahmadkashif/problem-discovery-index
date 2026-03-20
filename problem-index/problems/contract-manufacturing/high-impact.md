# First-Pass Yield Prediction and Process Parameter Optimization

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Type:** High Impact
**One-liner:** Contract manufacturers running new programs at initial production rates who don't know which process parameter combinations will produce acceptable yield until they've already generated scrap get a predictive model that identifies the parameter window most likely to achieve target yield before production runs — protecting margin on fixed-price programs where scrap cost is the CM's problem.
**Tags:** #gradient-boosting #gaussian-processes #linear-regression #bayesian-optimization #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #maximum-likelihood-estimation #revenue-impact

## The Problem

First-pass yield — the percentage of units that pass quality inspection without rework on the first production pass — directly determines whether a program is profitable. A contract manufacturer who quoted a program assuming 97% yield but achieves 93% in production absorbs the scrap cost on 4% of output. On a $10M/year program, that's $400,000 in unplanned cost absorbed by 5-12% EBITDA margins.

Yield varies with process parameters (temperature profiles, pressure settings, cycle times, speed settings), incoming material lot variation, machine state (calibration drift, tooling wear), and operator technique. Experienced process engineers develop intuition for which parameter adjustments improve yield for a specific material lot on a specific machine. This knowledge is rebuilt from scratch each time a new engineer joins, each time a process is transferred to a new facility, or each time material supplier changes.

The production floor generates enormous amounts of process data — SPC data, MES production records, quality inspection results — but this data is typically used reactively: after a yield problem emerges, engineers dig through records to find the parameter drift that caused it. Predictive use of the same data — to optimize parameters before production runs — is rare because it requires the ML infrastructure to connect process parameter inputs to yield outcomes across production history.

## Why It's High Impact

Yield improvement is the highest-leverage lever in contract manufacturing economics. The CM absorbs all incremental scrap cost on a fixed-price program. For a CM with $50M in production revenue and current average 95% yield, improving to 97% recovers $1M in annual scrap cost — approximately 40% of a typical 5% EBITDA. The model also enables systematic process transfer: when a program moves to a new machine or facility, the yield prediction model identifies the parameter settings most likely to replicate the original process performance, rather than requiring a new empirical optimization cycle.

## What a Solution Looks Like

A Gaussian process regression or gradient boosting model trained on historical production run records: process parameters as inputs (temperature, pressure, speed settings, cycle times), material lot characteristics (incoming material inspection data, lot number-encoded material variation), machine state indicators (calibration age, tooling hours, maintenance recency), and first-pass yield as the target. At inference time: given a new production run specification, predict expected yield for each candidate parameter combination and recommend the parameter set most likely to achieve target yield. Integrates with the MES for data pull and displays recommendations as a process engineer decision support tool.

## Implementation Path

Training data: historical MES production records with process parameters, quality inspection results (pass/fail per unit), and material lot tracking. Target: first-pass yield rate per production lot. Feature engineering: process parameter values, lot-level incoming material characteristics, machine maintenance history features. Gradient boosting baseline in 4-6 weeks for any CM with MES data and 2+ years of production history. Gaussian process for uncertainty quantification (critical for recommending parameter ranges, not just point estimates). Integration with Rockwell FactoryTalk, Siemens Opcenter, or Plex Systems via API or database direct connection.
