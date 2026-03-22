# Aurora Solar Static Savings Model Enhancement

**Niche:** [[niches/solar-installers/residential-rooftop/profile|Residential Rooftop Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aurora Solar's production modeling is excellent but its financial analysis uses a static utility rate escalation assumption — integrating dynamic rate forecasting and policy-change modeling would transform Aurora from a design tool into a financial advisory platform that produces the savings projections customers actually need to make informed decisions.
**Tags:** #time-series-forecasting #data-integration #revenue-impact #quick-win #gradient-boosting

## The Problem
Aurora Solar models system production with high accuracy (PVWatts-calibrated irradiance models, 3D shade analysis, module-level production simulation). But the financial projection takes this accurate production number and multiplies it by a simplistic rate assumption: "current utility rate x (1 + annual escalation %)^n for each year n." This means Aurora produces an accurate answer to "how many kWh will this system produce?" but an inaccurate answer to "how much money will this system save?" — and the customer's purchase decision is based on the money question, not the kWh question. When NEM policies change (as California's NEM 3.0 demonstrated), Aurora proposals generated under old assumptions become retroactively misleading.

## What Already Exists
Aurora Solar handles system design, shade analysis, production modeling, and proposal generation. Its production model is the industry's most trusted. The financial analysis module allows inputting utility rates and escalation percentages. Aurora's API supports integration with external data sources. The financial model framework exists — it just uses static inputs where dynamic inputs are needed.

## The Customization Gap
Three enhancements to Aurora's financial model: (1) dynamic rate integration — instead of a single escalation percentage, import the customer's actual current tariff (including TOU periods if applicable) from a utility rate database (OpenEI or a proprietary database), and model savings at the hourly level using production curves matched against TOU rate periods; (2) policy-change modeling — incorporate known NEM/net billing policy transitions with their effective dates and rate impacts, showing the customer "your savings under current NEM policy (years 1-3) and under the pending net billing policy (years 4-25)"; (3) rate scenario analysis — instead of one savings number, produce three scenarios (low/expected/high rate escalation) based on the specific utility's historical escalation pattern and pending rate cases. These could be built as Aurora-native features or as a third-party integration via Aurora's API.

## Target Customer
Aurora Solar's 8,000+ installer customers who want more defensible financial projections. Aurora as a platform seeking to move upmarket from design tool to complete sales platform.

## Impact If Solved
Produces savings projections within 5-10% of actual outcomes over the first 5 years, versus the current 20-40% deviation when rate assumptions are wrong. Reduces customer complaints about inaccurate savings projections. Gives sales reps a more credible financial story, increasing close rates. Positions Aurora as the end-to-end solar sales platform rather than just a design tool.
