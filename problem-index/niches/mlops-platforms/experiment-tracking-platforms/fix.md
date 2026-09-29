# Recorded Faithfully, Not Reproducible

**Niche:** [[niches/mlops-platforms/experiment-tracking-platforms/profile|Experiment Tracking Platforms]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Platforms record every hyperparameter, metric and artefact with real fidelity, and a researcher still cannot reliably rerun a result from six months ago.
**Tags:** #evaluation-metrics #data-integration #compliance #automation #descriptive-statistics #worker-facing #quick-win #workflow-orchestration
**Contested on:** Not terminal — the contest differs by workload scale, and the decomposition is recorded in the profile.

## The Problem
A result from six months ago needs to be rerun, because a reviewer asked or because a regression needs to be bisected. The platform has the hyperparameters, the metrics, the loss curves and the checkpoint. It does not have the exact data snapshot, which has since been appended to; the exact library versions, which have moved twice; the preprocessing code, which lived outside the tracked repository; the environment variables; or the uncommitted changes in the researcher's working directory at launch. The rerun produces a different number, and a week disappears into establishing which of those differences caused it.

## Why It's Still Broken
The platform captures what it is told to capture, and the un-captured things are precisely the ones nobody thinks to declare. Enforcing a clean working tree at launch annoys researchers during exploration, which is when most launches happen, so it is not enforced. Data snapshots are large and versioning them is somebody else's system. And the failure only surfaces months later, at which point nobody attributes it to a tooling decision made during a hurried experiment.

## What a Fix Looks Like
Capture the environment automatically instead of asking. Snapshot the full dependency set including accelerator libraries and drivers at launch, which is mechanical, cheap and covers the most common cause of divergence. Capture uncommitted changes as a patch rather than refusing to run, since blocking the researcher guarantees the feature gets bypassed and a stored diff preserves the information at no cost to them. Pin the data by reference to an immutable snapshot rather than by path, because a path that pointed at a growing table is the second most common cause and is invisible at the time. Record the random seeds and the sources of non-determinism actually in play, and report honestly which of them cannot be controlled on this hardware. Score each run for reproducibility at launch time and show it, since a researcher who sees a low score before spending the compute will frequently fix it in thirty seconds, while the same person six months later cannot fix it at all. Offer a one-command rerun that reconstitutes the captured environment, which is the test of whether any of this worked. And report what diverged when a rerun does not match, rather than leaving the bisect to the person.

## Who Feels the Pain
Researchers who cannot reproduce their own work; reviewers and regulated organisations who need provenance they were told existed; and teams bisecting a regression across six months of runs that are not comparable.

## Impact If Fixed
Everything the platform records is faithful and insufficient. Scoring reproducibility at launch and showing it to the researcher converts a problem that is unfixable in six months into a thirty-second fix today.
