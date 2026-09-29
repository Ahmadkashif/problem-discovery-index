# Build: Forecasting Under a Shifting Arrival Process

**Niche:** [[niches/digital-bpo-operations/workforce-forecasting/profile|Workforce Forecasting & Scheduling]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forecast the residual demand that reaches a human by modelling the deflection layer explicitly, per contact type, rather than extrapolating a historical arrival curve.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #confidence-intervals #monte-carlo-methods #evaluation-metrics #recurrent-forecasting #automation
**Contested on:** Whether demand can be forecast when the thing removing volume from it changes every month.

## The Problem

Arrival forecasting rests on the assumption that the process generating contacts is stable enough for last year's pattern to inform next week's. That assumption has been broken by deflection.

Self-service and automated resolution remove volume selectively — heavily from simple, high-volume contact types and barely from complex ones — and the deflection capability itself improves in steps as the client ships changes. So the arrival curve flattens unevenly, the mix shifts toward longer contacts, the handle time distribution moves, and every model fitted on the previous twelve months describes a world that no longer exists.

Forecast accuracy degrades. The degradation is attributed to volatility. And the cost lands as cut hours or unmanned queues.

## Why Nobody Has Built This

WFM is a well-established discipline with mature tooling and experienced planners, and the models work well under stable conditions. The response to instability has been to shorten the training window and add manual overrides, which helps and does not address the structural problem.

Modelling the deflection layer explicitly requires data from the client's self-service and automation systems — what was attempted, what succeeded, what escalated — which sits outside the BPO's platform. That integration has not been prioritised because nobody framed the forecasting problem this way.

And planners are measured on forecast accuracy against actuals, not on the consequences of error, so the asymmetry never enters the model.

## What to Build

A two-stage forecast that models total demand and the deflection filter separately.

**Forecast total contact intent, not arrivals.** Underlying customer demand — the volume of people with an issue — is far more stable than the volume reaching an agent, and it is observable as attempts across all channels including self-service. Forecasting intent and then applying a deflection model is structurally right and robust to deflection changes in a way a single arrival model is not.

**Model deflection per contact type.** Deflection rate by type, by channel and by time, with change-point detection so a step improvement after a client release is detected within days rather than absorbed as noise. Each client release is an intervention and should be treated as one.

**Forecast handle time distributions, not averages.** As the mix shifts, the distribution changes shape, not just its mean. Staffing models that take an average handle time understate variability precisely when the tail is growing, and staffing to a distribution is what prevents the underestimates that produce queues.

**Make the loss function asymmetric and explicit.** Over-forecasting costs paid idle time or cut hours; under-forecasting costs a service level breach and agent strain. These are different costs with different recipients, and the staffing decision should optimise against both rather than minimise a symmetric error. Stating the trade-off explicitly is the most consequential change here.

**Simulate rather than assume.** Erlang assumes Poisson arrivals and exponential handle times, neither of which holds in a deflection-filtered process with a long-tailed handle time distribution. Simulation over the forecast distributions gives an honest service level probability instead of a formula's answer to a different question.

**Report forecast accuracy by direction and by consequence.** How often the forecast was low, by how much, and how many agent hours were cut versus how many service level intervals were breached. This is the reporting that makes the asymmetry visible and it is not what any WFM dashboard shows.

## Target Customer

WFM planning leadership at BPOs, where forecast accuracy has visibly degraded and the cause is misattributed to volatility. Also client-side operations, since the deflection data needed sits with them and they have an interest in the queue behaviour it drives.

## Impact If Built

Forecasting works on a demand process that is actually stable, with deflection modelled as the filter it is. Step changes after client releases are detected in days. And the asymmetric cost of error becomes an explicit input rather than an invisible allocation of harm to whoever was scheduled that day.
