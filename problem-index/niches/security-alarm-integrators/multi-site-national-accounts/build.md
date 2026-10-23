# An Estate-Wide Site Health Score From Device Telemetry

**Niche:** [[niches/security-alarm-integrators/multi-site-national-accounts/profile|Multi-Site National Account Service Programmes]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A national security programme is judged on whether every site's devices work, and nobody can say on a given morning how many do.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep hundreds of a retailer's, bank's or restaurant chain's sites with working alarms, cameras and access points at the service level the client's loss-prevention team audits, and whoever proves the most sites healthy at the lowest service cost per site takes the account.

## The Problem
Health data exists in pieces. The VMS reports camera offline and recording gaps, the central station sees panels that miss their test timer, and the access platform logs door controller faults. Each sits in a different console. Programme reviews with loss prevention are built by hand from tickets, and failures are found when the client asks for footage that doesn't exist.

## Why Nobody Has Built This
Every device platform reports on its own devices, and national sites mix brands from acquisitions and past refreshes. Integrators sell service hours, so a health score that exposes failures before the client finds them is a commitment they have hesitated to make.

## What to Build
A health layer that ingests VMS, panel-supervision and access-platform telemetry for every site and scores each site daily: recording coverage, panel communication, door faults, storage headroom. Behind it, a survival model of device failure by model, age and environment drives refresh planning and pre-emptive truck rolls. Subcontractor tickets close only when telemetry confirms the fix.

## Target Customer
National-account leaders at integrators serving chains of 300+ sites, and the loss-prevention VPs who buy the programmes.

## Impact If Built
The integrator walks into every quarterly review with proof of estate health and a failure-based refresh plan. That is the evidence that wins the renewal, and it moves service from reactive dispatch to planned visits at lower cost per site.
