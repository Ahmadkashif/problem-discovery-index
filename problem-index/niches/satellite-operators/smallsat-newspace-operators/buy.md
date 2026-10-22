# Software Observability Stacks Fitted to Pass-Based Telemetry

**Niche:** [[niches/satellite-operators/smallsat-newspace-operators/profile|Small Satellite & NewSpace Operators]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** NewSpace teams already run Grafana-style dashboards and alerting for their satellites; the tools assume continuous data and fire on every gap between ground passes.
**Tags:** #time-series-forecasting #autoencoders #automation #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to take a startup's satellites from licence to steady operations without the startup building its own ground network or 24/7 operations team, and whoever bundles ground contacts, mission operations and the regulatory paperwork into one dependable service takes the startup's ground and operations contract.

## The Problem
A LEO satellite is in contact for a few minutes per pass and dumps stored telemetry when it is. Observability tools built for servers see a stream that stops and starts, data arriving out of order with onboard timestamps, and limits that vary by orbit phase and eclipse. Alerting either fires constantly or is switched off.

## What Already Exists
Software observability stacks (Grafana, Prometheus, Datadog, InfluxDB) used by most NewSpace engineering teams for both ground software and spacecraft data.

## The Customization Gap
The adaptation needs: ingestion of stored-and-forwarded telemetry with onboard time; contact-window awareness so gaps aren't alarms; limits conditioned on orbit phase, eclipse and operating mode; per-pass summaries; and linkage to the command log and the ground-station schedule.

## Target Customer
Flight software and operations engineers at small-satellite startups.

## Impact If Solved
Alerts that mean something, built on tools the team already knows, without buying a legacy mission control system.
