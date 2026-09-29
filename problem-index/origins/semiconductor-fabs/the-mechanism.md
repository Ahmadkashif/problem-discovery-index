# The Mechanism: Control Charts, Run-to-Run Control, and APC

**Origin:** [[origins/semiconductor-fabs/profile|Semiconductor Fabs]]
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #change-point-detection #optimization-fundamentals #data-integration #automation #evaluation-metrics

> This is the file an FDE should read twice. It is the industry that ran a full measure-detect-adjust loop in production, at scale, for decades, before "monitoring" was a word used outside a fab.

## The Question, Stated Properly

A wafer comes off a process step — say, a deposition step meant to lay down a film of a specific thickness. The measured thickness never matches the target exactly; there is always some variation. **Is this particular wafer's deviation ordinary noise, or a sign the process itself has shifted and needs correcting before the next several hundred wafers inherit the same fault?**

That is a hypothesis test, run continuously, against a process rather than a single sample.

## The Decomposition

**1. Establish what "normal" looks like.** Measure the process under known-good conditions and derive its ordinary variation — a mean and a spread. This is descriptive statistics doing load-bearing work: without a credible baseline, nothing downstream is meaningful.

**2. Set control limits, and treat crossing them as a signal.** A classical control chart sets limits at some multiple of the process's own standard deviation around its mean — conceptually the same logic as a confidence interval, applied to a process instead of a parameter estimate. A point outside the limits is treated as **evidence the process has changed**, not as an unlucky draw from the same distribution — which is exactly the logic of a hypothesis test: reject the "nothing has changed" null when the observation is improbable enough under it.

**3. Detect a shift, not just a single bad reading.** A process can drift gradually rather than jump — a slow trend in the mean well before any single point breaches a control limit. This is a **change-point detection** problem: identifying the point in a sequence where the underlying process changed, which fabs needed to solve operationally long before it had that name in the statistics literature.

**4. Close the loop: run-to-run control.** SEMATECH's early-1990s demonstration on CMP (chemical-mechanical planarisation) was the moment this stopped being passive monitoring and became active correction: measure the wafer that just finished, and if it deviated from target, **adjust the recipe for the next run** — polish time, pressure, chemical concentration — rather than leaving the next wafer to inherit the same drift. That adjustment is a small, constrained optimisation: choose the correction that minimises expected deviation from target, subject to the process's physical limits.

**5. Generalise into Advanced Process Control (APC).** Combine run-to-run correction with **fault detection and classification (FDC)** — flagging an excursion from real-time sensor data during the step itself, not just from the finished wafer's measurement afterward — across as many of a fab's several hundred steps as could be instrumented. That is a large **data-integration** problem: sensor streams, metrology readings and lot histories from many tools joined well enough to tell which tool, recipe, or prior step contributed to a given wafer's deviation.

**6. Automate the response.** By the mid-1990s, APC systems were closing this loop with minimal human intervention on many steps — the correction computed and applied automatically, with an engineer reviewing exceptions rather than every run.

## Why This Was Hard

The baseline itself drifts — tools age, chemicals age, and "normal" is not a fixed target; it has to be re-established periodically without also hiding a real fault. False alarms are expensive in both directions: stopping a healthy line chases noise and destroys throughput, while missing a real shift propagates a defect through hundreds of remaining steps before final test catches it, by which point the whole lot may be unrecoverable. And the correction itself can destabilise the process — an overcorrection to one run's deviation can push the next run the other way, which is why real R2R systems are tuned as control loops, with damping, rather than applying the full suggested correction every time.

## What It Gave Up — the trade-offs

Speed of detection was traded against certainty: tighter control limits catch real shifts sooner and also flag more noise as a shift, and every fab's chosen limits are a specific, deliberate trade along that curve. The loop optimises the step, not the finished chip — R2R control on one step does not know whether its correction interacts badly with a downstream step's own loop, a known failure mode that is why "factory-wide" APC, not step-by-step APC, became the stated goal by the early 2000s. And it assumes the physics of the tool is stable enough to model: a genuinely novel failure mode can sit outside every control limit the system has ever learned, and the loop will not catch what it has never been shown.

## The Transferable Pattern

> **Where a process is repeated at very high volume and a defect is catastrophically expensive to let propagate, the profitable investment is not a better single measurement — it is a closed loop: measure continuously, decide statistically whether this deviation is real, and feed the correction back into the next run automatically.**

An FDE meeting a production line, a call-centre quality process, or a model-serving pipeline that silently drifts is meeting this exact problem, forty years after the semiconductor industry was forced to solve it or lose the market.

**Sources:** *Handbook of Quality Integrated Circuit Manufacturing* (1991); Semiconductor Digest, *APC: A factory-wide strategy for ultimate yield improvement* (2003); ScienceDirect, *Semiconductor manufacturing process control and monitoring: A fab-wide framework*; Wikipedia, *SEMATECH*.
