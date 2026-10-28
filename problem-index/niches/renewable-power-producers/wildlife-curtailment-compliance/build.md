# Curtailment That Follows the Bats, Not the Calendar

**Niche:** [[niches/renewable-power-producers/wildlife-curtailment-compliance/profile|Wildlife Compliance & Curtailment]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Many wind farms stop every turbine below a set wind speed on every summer night whether or not bats are flying, and nobody has a permit-grade model that curtails only when the risk is real.
**Tags:** #gradient-boosting #logistic-regression #time-series-forecasting #feature-engineering #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep eagle and bat take inside permit limits while stopping turbines as little as possible, and whoever loses the fewest megawatt-hours to wildlife curtailment per turbine-year takes the account.

## The Problem
Blanket low-wind-speed curtailment protects bats by giving up energy on many nights when few are flying. The rule is set in the permit or habitat plan and programmed into the controller for the whole season.

## Why Nobody Has Built This
Regulators accept blanket rules because they are simple to verify. A smarter rule needs acoustic detectors on nacelles, weather data and years of fatality searches to prove it protects bats as well, and each site's evidence is held by the owner and its consultant.

## What to Build
A per-turbine, per-interval bat activity model using nacelle acoustic detections, temperature, wind speed, humidity, time of night and season, which raises the cut-in speed only when predicted activity crosses a threshold agreed with the agency. Fatality search results calibrate it each season, and a compliance report shows take against the permit and energy saved against the blanket rule.

## Target Customer
Environmental compliance directors at owners of wind farms with bat curtailment conditions.

## Impact If Built
If blanket curtailment costs a 200 MW site ~1–2% of annual output (estimate) and a risk-based rule halves that, the site gains ~3,000–6,000 MWh, ~$130K–$270K a year at $45/MWh.
