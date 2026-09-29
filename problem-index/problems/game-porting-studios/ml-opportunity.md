# Machine Learning Opportunities — Game Porting Studios

**Industry:** [[game-porting-studios|Game Porting Studios]]
**Derived from:** [[problems/game-porting-studios/high-impact|High Impact]], [[problems/game-porting-studios/low-impact-1|Low Impact 1]], [[problems/game-porting-studios/low-impact-2|Low Impact 2]], [[problems/game-porting-studios/worker-life-1|Worker Life 1]], [[problems/game-porting-studios/worker-life-2|Worker Life 2]]

---

## 1. Port Effort Estimation From Codebase Analysis
#gradient-boosting #graph-neural-networks #bert #confidence-intervals #bayesian-inference #survival-analysis #evaluation-metrics #revenue-impact

**Problem statement:** Fixed-price bids are made on codebases the studio has not read, where effort depends on platform-specific code concentration, renderer structure, memory budget headroom and custom modules hiding under a standard engine — all invisible at bid time, and all capable of changing the cost by a multiple.

**ML task:** Predict effort by work category from automated codebase analysis, calibrated on the studio's own completed ports
**Input data:** Static analysis of source — size, structure, dependency and call graphs, platform-specific code concentration, renderer feature usage, threading and allocation patterns, custom module footprint, engine version and its supported targets; target platform characteristics; realised hours by category from completed projects; the specific problems each project hit and what they cost.
**Target:** Effort in hours by category — renderer, memory, certification, platform gameplay code, client churn — not a single total, because the categories are what make an estimate defensible and improvable.
**Evaluation metric:** Predicted versus actual on held-out projects, with the distribution's calibration mattering more than the point estimate: a bid needs a number and the business needs to know whether the plausible range runs to double. Report performance separately for the tail, since the commercial risk is entirely in the projects that overran badly and a model that fits the typical case and misses those has solved nothing.
**Scope:** A studio with forty completed ports has forty observations, which is enough given strong features and hierarchical structure — but only if effort was recorded by cause, which it currently is not. That process change is the prerequisite and is the unglamorous half of the project. The sales incentive works against calibration, since an accurate estimate higher than a competitor's loses the work, so this needs to be owned by someone whose objective is margin rather than revenue. 2 ML engineers plus a technical director, 9-12 months.
**Data availability:** Codebases are held for completed projects. Effort data exists as undifferentiated time tracking. Nobody in this sector treats completed projects as data.

---

## 2. Profile-to-Cause Attribution and Optimisation Return Estimation
#gradient-boosting #graph-neural-networks #change-point-detection #transfer-learning #confidence-intervals #time-series-forecasting #evaluation-metrics #feature-engineering

**Problem statement:** Profilers say where time goes and not what to do about it, and the performance phase — where port schedules are lost — is an open-ended search conducted by the scarcest engineers using pattern recognition from previous projects.

**ML task:** Map profile signatures plus codebase structure to likely causes and typical fixes, and estimate the frame time each fix would return before the work is done
**Input data:** Platform profiler captures with subsystem and GPU breakdowns; codebase structure around the implicated systems; asset budgets and streaming behaviour; the studio's portfolio of previous optimisation work with the causes found and the returns realised; target platform characteristics; comparable titles in the same genre on the same platform.
**Target:** The cause an engineer eventually identified, and the frame time recovered by the fix.
**Evaluation metric:** Top-3 cause accuracy rather than top-1, since an engineer can evaluate three hypotheses quickly and a confidently wrong attribution wastes days on a platform with limited debugging tooling. For return estimation, predicted against realised recovery — and calibration here directly determines whether an optimisation phase can be planned to a projected end state, which is the scheduling value. Cross-title baselines should report how far this title is from comparable ones, which tells a team whether they are near the achievable limit or missing something large.
**Scope:** The transferable asset is the studio's own portfolio of optimisation work, which currently exists as the experience of a handful of engineers and is transferred by apprenticeship. Fixes interact — memory work changes streaming, shader simplification shifts load to the CPU — so return estimates must account for sequence rather than being additive. 2 ML engineers plus a graphics engineer, 9-12 months.
**Data availability:** Profiler captures and codebases are retained. The cause-and-fix record is in engineers' heads and in commit messages, and extracting it is the first task.

---

## 3. Perceptual Cross-Platform Regression Detection
#cnns #contrastive-learning #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #automation #transfer-learning

**Problem statement:** Screenshot comparison is the standard automated visual check and is too brittle to use — non-deterministic rendering, dynamic lighting and animation timing produce constant false positives, so teams disable it and fall back to people playing the game.

**ML task:** Compare frames perceptually and structurally, tolerant of differences that do not matter and sensitive to defects, and distinguish expected platform differences from regressions
**Input data:** Captured frames across builds and platforms at matched camera positions; rendering configuration per platform; historical confirmed visual defects and confirmed expected differences; the studio's portfolio record of what differs legitimately between specific platform pairs.
**Target:** Whether a difference is a defect, as adjudicated by QA.
**Evaluation metric:** False positive rate is the metric that decides adoption — a visual regression system that fires on ordinary non-determinism gets switched off within a week, which is the fate of the current generation. Measure it under realistic conditions including dynamic lighting and animation, not on static scenes. Recall on confirmed defects matters second, and should be reported by defect class since missing textures, shader differences and lighting shifts have very different signatures.
**Scope:** Knowing what differs legitimately between two specific platforms is the knowledge that makes this work and it comes from a studio's own portfolio rather than from first principles. Change-aware test prioritisation is a cheaper companion: predicting which content a build's changes put at risk, from code-to-content mapping and historical regression patterns, puts sampled coverage where it matters. 2 ML engineers with vision experience, 6-9 months.
**Data availability:** Frames are capturable automatically. Adjudicated defect labels exist in QA records.

---

## 4. Codebase Comprehension and Platform Fault Localisation
#large-language-models #graph-neural-networks #bert #transformers #gradient-boosting #evaluation-metrics #worker-facing #tacit-knowledge-ml

**Problem statement:** Porting engineers inherit hundreds of thousands of lines written by people they will never speak to, with unrecorded architectural reasoning and deliberate oddities that are traps on a new platform — and the comprehension phase produces nothing visible, so nobody schedules it.

**ML task:** Generate architectural summaries of an unfamiliar codebase, identify and explain constructions that look wrong but are deliberate, and rank hypotheses for faults that appear only on the target platform
**Input data:** Source with dependency and call graphs; version history where supplied; platform-specific code paths; the observed fault with its platform context; the studio's accumulated record of traps and fixes across previous codebases, particularly from the same engine and publisher.
**Target:** For comprehension, summaries an engineer judges accurate and useful. For fault localisation, the cause eventually identified.
**Evaluation metric:** Comprehension is evaluated by time-to-first-meaningful-change on a new codebase against a matched baseline, which is the outcome that matters and is measurable. For fault localisation, top-3 accuracy on historical cross-platform bugs — the hypothesis classes are enumerable (API behaviour differences, alignment and endianness assumptions, threading races the source hardware masked, memory patterns fitting one budget) and ranking them against an observed fault is the achievable form.
**Scope:** The retained codebase record is the compounding asset: when the same publisher's next title arrives on the same engine with the same in-house systems, a structured record of that codebase's traps is the difference between a fresh start and a head start. Studios currently let that evaporate at project end. 2 ML engineers, 6-9 months.
**Data availability:** Codebases are retained under client agreements that vary and must be checked. The trap record does not exist and must start being kept.
