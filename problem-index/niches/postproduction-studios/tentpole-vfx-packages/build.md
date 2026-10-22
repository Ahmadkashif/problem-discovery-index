# Artist Demand Forecast That Expects the Late Turnover

**Niche:** [[niches/postproduction-studios/tentpole-vfx-packages/profile|Tentpole Feature VFX Packages]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Large vendors staff to the turnover dates in the award, and turnovers almost always slip, so they either idle artists or crunch them.
**Tags:** #time-series-forecasting #survival-analysis #monte-carlo-methods #bayesian-inference #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to commit hundreds of artists, in the jurisdiction with the richest VFX credit, to a studio's fixed release date under a supervisor the studio trusts, and whoever can guarantee that capacity without idling it between turnovers takes the award.

## The Problem
A tentpole award comes with a schedule: turnover dates per sequence, a final delivery date, and an expected shot count by department. The vendor hires and books artists against it, often across three or four sites. Then the edit keeps moving, sequences turn over weeks late, shot counts change, and the delivery date doesn't. The vendor carries idle teams for weeks, then crunches them to hit the date.

## Why Nobody Has Built This
Resourcing is done by heads of production in spreadsheets, per show. The history needed to forecast slippage (planned versus actual turnover dates by studio, director and show phase) exists in trackers and emails but has never been assembled, and studios do not share their edit status.

## What to Build
A probabilistic demand forecast per department and site, built from the vendor's own history of how turnovers slip by studio and by stage of the edit. It uses survival models for time-to-turnover and Monte Carlo simulation of shot counts and effort across every awarded and likely show. Heads of production see a range, not a line, and can test what happens if a sequence slips three weeks or a pipeline show is awarded.

## Target Customer
Heads of production and CFOs at the 20–40 vendors worldwide large enough to bid tentpole packages (estimate).

## Impact If Built
Fewer idle weeks and fewer crunch weeks. Utilisation is the margin in this tier, and a few points of utilisation across a 1,000-artist vendor is worth millions a year (estimate).
