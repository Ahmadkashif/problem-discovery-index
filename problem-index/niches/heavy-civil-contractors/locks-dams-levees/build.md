# River-Stage Risk Priced From the Gauge Record

**Niche:** [[niches/heavy-civil-contractors/locks-dams-levees/profile|Locks, Dams & Levee Construction]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every in-the-wet bid prices the chance the river overtops the cofferdam, usually from a glance at a few historical hydrographs; a century of gauge data could price it properly.
**Tags:** #monte-carlo-methods #probability-distributions #time-series-forecasting #bayesian-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price and control in-the-wet risk on federal and utility water projects (cofferdams, river stages, foundation conditions, navigation kept open), and whoever bids the lowest contingency that the river and the ground don't overrun takes the account.

## The Problem
The cofferdam height, the season the in-river work is scheduled for, and the contingency all hinge on the river-stage distribution. Estimators set them by experience.

## Why Nobody Has Built This
Hydrology lives with the owner's engineers, estimating with the contractor, and the joint venture assembles its risk register in spreadsheets during bid weeks.

## What to Build
A simulation that samples historical and synthetic stage sequences from USGS gauge records for the site. It applies them to the proposed work sequence and cofferdam design, and returns lost workdays, overtopping probability and cost distributions for each option. A two-week demo can run on any USGS gauge with a long record.

## Target Customer
Chief estimators and risk managers on lock, dam and levee bids, usually joint ventures.

## Impact If Built
If contingency on a $300M lock job (illustrative) is set within a tighter band, say ±2% instead of ±5% (estimate), the JV bids several million dollars sharper without taking more risk.
