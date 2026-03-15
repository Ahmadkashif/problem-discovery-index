# Interconnection Queue Wait Time Prediction by Utility Territory

**Industry:** [[solar-installers|Solar Installers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic project timeline tools don't model the utility interconnection queue — the primary source of timeline uncertainty in solar projects — which varies by utility, queue backlog, and project size in ways that only firms with extensive local utility experience can estimate accurately.
**Tags:** #gradient-boosting #regression #tabular-ml #automation

## The Problem

Solar project timelines are dominated by two bureaucratic processes: permit approval by the local building department and interconnection approval by the utility. Interconnection timelines range from 30 days to 18 months depending on the utility, the local queue backlog, the project size (residential vs. commercial), and the type of interconnection required (simplified vs. standard review). A solar company promising customers a 60-day installation timeline in a utility territory that currently has a 6-month interconnection queue destroys customer relationships and generates expensive cancellations.

Experienced solar contractors in a specific utility territory develop accurate timeline estimates through experience with dozens of submissions to the same utility. Regional firms new to a territory or companies expanding geographically lack this knowledge and consistently over-promise on timelines.

## What Already Exists

SEPA (Smart Electric Power Alliance) publishes interconnection queue data for some utilities. GTM Research and Wood Mackenzie track interconnection trends at the grid level. No tool provides real-time interconnection timeline estimates at the utility-territory level for residential project type.

## The Customisation Gap

A solar interconnection timeline tool needs: (1) utility territory identification from the project address; (2) current queue backlog data for that utility (available through utility FERC filings and state PUC records); (3) historical timeline data from the solar contractor's own submission records for that utility; (4) a regression model that predicts timeline from project size, utility, and current queue depth. The utility-specific historical data is the differentiator — firms that have submitted 100+ projects to the same utility have the best timeline prediction accuracy.

## Impact If Solved

Accurate timeline promises reduce customer cancellations during the wait period. Each cancellation after permitting represents $3,000-$8,000 in sunk costs (design, permit fees, sales commissions). A firm processing 500 projects per year with a 5% cancellation rate from timeline disappointment loses $750,000-$2,000,000 annually.
