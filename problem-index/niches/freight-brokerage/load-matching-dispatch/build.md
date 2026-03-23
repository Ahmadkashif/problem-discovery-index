# Predictive Carrier Acceptance Engine

**Niche:** [[niches/freight-brokerage/load-matching-dispatch/profile|Load Matching & Dispatch Automation]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product uses a broker's own historical carrier interaction data — which carriers accepted which loads at what rates on which lanes — to predict carrier acceptance probability per load and generate a ranked outreach list that minimizes time-to-coverage.
**Tags:** #gradient-boosting #tacit-knowledge-ml #automation #revenue-impact

## The Problem
An experienced dispatcher knows that Carrier X always accepts Chicago-to-Dallas loads on Mondays at $2.00/mile, that Carrier Y only takes this lane when their rate hits $2.20, and that Carrier Z has been declining loads for 2 weeks (probably committed elsewhere). This knowledge — built through thousands of interactions — enables the experienced dispatcher to cover loads in 2-3 calls. A junior dispatcher on the same lane makes 8-10 calls to achieve coverage. This tacit carrier-matching knowledge is the core competitive advantage of an experienced dispatch desk, and it walks out the door when a dispatcher leaves.

## Why Nobody Has Built This
The training data exists inside each broker's TMS: carrier outreach records (who was contacted, did they accept, at what rate, on what lane). But TMS platforms don't expose this data in a ML-ready format, and most brokerages lack the data engineering capability to extract, clean, and model it. The carriers' acceptance patterns are broker-specific (a carrier's behavior with Broker A differs from their behavior with Broker B based on relationship quality), so industry-wide models from load board data are weaker than broker-specific models.

## What to Build
A ML engine that: (1) ingests the broker's carrier outreach history from their TMS (carrier, load, lane, rate offered, accepted/declined, timestamp); (2) trains a per-carrier acceptance model using lane, rate, day-of-week, and recent activity features; (3) for each new load, generates a ranked carrier list ordered by predicted acceptance probability at the target buy rate; (4) provides the dispatcher with a "smart outreach list" that replaces their manual mental ranking. The engine improves with each new interaction.

## Target Customer
Technology directors and dispatch managers at brokerages handling 100+ loads/day who want to scale coverage capacity without proportional dispatcher hiring. Approximately 1,000 brokerages operate at this volume.

## Impact If Built
Reducing average outreach attempts from 8 to 3 per load saves 15-20 minutes per load. On 100 daily loads, this recovers 25-33 dispatcher-hours per day — equivalent to 3-4 FTE in dispatcher capacity freed for relationship management and exception handling.
