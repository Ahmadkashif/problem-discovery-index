# The Mechanism: What Dynamic Matrix Control Actually Computed

**Origin:** [[origins/process-manufacturing/profile|Process Manufacturing]]
**Tags:** #optimization-fundamentals #convex-optimization #dynamic-programming #time-series-forecasting #systems-of-linear-equations #matrix-algebra #automation #data-integration #compliance

> This is the file an FDE should read to see the founding industrial case of model predictive control — the same family of ideas now used to plan robot trajectories and tune reinforcement-learning policies.

## The Question, Stated Properly

A process variable — say, a distillation column's outlet temperature — must stay near a target and inside a hard safety limit. It responds to manipulated variables (steam flow, reflux rate) with a delay, and the response is neither instantaneous nor simple. **Given where the process is now and where it is heading, what sequence of moves keeps the controlled variable on target and inside its limits, as cheaply and closely to the true constraint as possible?**

Conventional single-loop analog control reacts to error after it appears. DMC's innovation was to **predict** the error before it appears and act pre-emptively.

## The Decomposition

**1. Build a step-response model, empirically.** For each manipulated variable, record how the controlled variable moves over time in response to a step change. Stacked together, this becomes a **matrix of step-response coefficients** — the process's own measured behaviour, not a first-principles physical model. DMC does not require understanding the chemistry or thermodynamics of the process, only its measured input-output dynamics.

**2. Predict the future trajectory,** using the step-response matrix and the planned future move sequence, over a finite **horizon** — seconds to minutes ahead, depending on the process.

**3. Compute the optimal move sequence** that minimises a performance index — typically predicted deviation from target, penalised for aggressive moves — subject to real constraints: valve limits, safety bounds, rate-of-change limits. A constrained optimisation problem solved fresh at every control interval.

**4. Execute only the first move, then re-solve.** DMC applies only the first computed move, remeasures, and replans from the new state — **receding-horizon control**, the defining structural feature of the model-predictive-control family, and the same control-loop shape as [[origins/electric-utilities/the-mechanism|economic dispatch's continuous re-solve]] applied to a chemical process instead of a power grid.

**5. Push the constraint, deliberately.** Because the model predicts the future trajectory rather than merely reacting to the present, DMC lets operators run closer to the true physical limit with confidence, rather than leaving a wide margin to compensate for a controller that can only react after the fact. This is widely credited with meaningful cost savings across petrochemicals through tighter operation — **though rigorous, industry-wide, quantified ROI figures are genuinely harder to source than the qualitative consensus, and this file will not manufacture a number it cannot cite.**

## Why This Was Hard in the 1970s

The mathematics of receding-horizon optimisation is not exotic today, but running it in production required computing the prediction and re-solving the optimisation **within the process's own control interval**, on the hardware [[origins/process-manufacturing/origin-story|Honeywell's TDC 2000]] made available. The algorithm needed the platform — the same shape this series keeps finding: infrastructure that makes a capability possible tends to arrive years before anyone builds the capability on top of it.

## What It Gave Up

**Model fidelity was traded for empirical tractability.** DMC's step-response matrix is a measured approximation of the real process, good enough most of the time and silently wrong exactly when the process drifts outside the conditions under which the steps were originally measured.

**Safety margin was traded for cost, by design.** Constraint-pushing is the entire point of the technology — deliberately running closer to a true limit than a human operator, working from instinct and a wide personal margin, would ever choose to.

**Trust in the HMI was assumed, not verified.** DMC and the DCS beneath it both depend on the operator's screen showing what the process is actually doing. [[origins/process-manufacturing/the-fight|Stuxnet]] proved this assumption is not automatically safe — it is exactly the layer an attacker targeted, feeding false-nominal readings while the true process ran to failure underneath them.

## The Transferable Pattern

> **When a system's behaviour is measurable but its underlying physics is hard to model exactly, predicting forward from an empirical response model and re-solving at every step beats reacting to error after it appears — and the entire value of doing so depends on the measurement you are predicting from being true.**

**Sources:** AspenTech/DMC Corporation corporate history; Cutler's 1967 dissertation and its role in Dynamic Matrix Control; process-control literature on step-response modelling and receding-horizon control; Honeywell TDC 2000 patent and technical history.
