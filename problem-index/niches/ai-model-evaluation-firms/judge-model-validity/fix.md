# The Judge Model That Changed Underneath the Benchmark

**Niche:** [[niches/ai-model-evaluation-firms/judge-model-validity/profile|Judge Model Validity]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The grader is a hosted model that the provider updates without notice, which means the measuring instrument changes between runs and every historical comparison silently breaks.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to state how much a model grader agrees with the humans it replaced, per task and continuously — and whoever does that takes the account, because the dominant grading method in the industry is also the least validated.

## The Problem
A benchmark tracks a set of models over eighteen months using a hosted judge. The provider updates that judge four times in the period, sometimes behind an unchanged version label. The judge becomes slightly stricter, or develops a different preference about hedging. Every model evaluated after the change is measured on a different instrument from every model evaluated before it, and the results are plotted on one axis. Longitudinal claims — this model improved, the field advanced, this vendor regressed — are built on a ruler that changed length partway through, and nobody recorded when.

## Why It's Still Broken
Providers update hosted models for good reasons and have no obligation to freeze one for a benchmark's convenience. Version labels do not reliably track behaviour, so even a pinned version may move. Detecting the change requires a canary the benchmark does not run. And the historical comparisons are the benchmark's most cited output, so questioning their comparability undermines the thing people value most about it.

## What a Fix Looks Like
Watch the instrument and re-anchor when it moves. Run a fixed canary set through the judge continuously and alert on behavioural change, which detects silent updates within a day, costs almost nothing, and is the foundation of every other correction here. Record the judge's full identity with every score — model, version, settings, prompt, date — so that any historical comparison can be checked for comparability rather than assumed. Re-grade an anchor set of historical items whenever a change is detected, which quantifies the shift and allows a correction rather than an asterisk. Mark change points on every longitudinal chart, because an uncorrected trend across a known instrument change is a misleading artefact and marking it is the minimum honest response. Prefer a judge that can be pinned — a self-hosted open model — for longitudinal work, accepting a lower peak capability in exchange for a stable ruler, which is the right trade for a benchmark and the wrong one for a one-off evaluation. Maintain a small human-graded anchor set that survives every instrument change and is the ultimate reference. And publish instrument change events alongside results, so downstream users of the benchmark can reason about them.

## Who Feels the Pain
Benchmark maintainers whose longitudinal claims rest on a moving instrument; the labs and vendors whose apparent regression was a judge update; and everyone citing a trend that partly measures the grader.

## Impact If Fixed
A continuously-run canary set detects a silent judge update within a day for almost nothing, and it is the foundation for every correction. Preferring a pinnable self-hosted judge trades peak capability for a stable ruler, which is the correct trade for anything longitudinal.
