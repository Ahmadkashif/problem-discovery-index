# Bid-Day Cost Prediction for Park Projects

**Niche:** [[niches/landscape-architecture-firms/park-capital-project-delivery/profile|Park Capital Project Delivery]]
**Industry:** [[industries/landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Park bid tabulations are public records full of unit prices from real bids, and no landscape architect uses them to predict what the next park will bid at.
**Tags:** #gradient-boosting #linear-regression #regularization #time-series-forecasting #confidence-intervals #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce park bid documents that come in within the construction budget at the first bid opening without missing a grant deadline, and whoever delivers parks that bid on budget takes the account.

## The Problem
The engineer's estimate on a park project is built from the firm's past spreadsheets, RSMeans site-work data and a few manufacturer quotes. On bid day the low bid lands well above it — overruns of ~15–30% are a common story (estimate) — often enough that every park designer has redesigned a project to cut a splash pad or a shade structure. The real prices — every bidder's unit price on every line item — are published in bid tabulations by thousands of agencies, as scanned PDFs.

## Why Nobody Has Built This
Bid tabs are fragmented across agency websites and council packets, item descriptions are inconsistent, and the market of park designers is small and spread thin. Cost data publishers build from contractor surveys and cover park-specific items poorly.

## What to Build
A pipeline that harvests public bid tabulations, extracts line items and unit prices, normalises them to a park item taxonomy (play structures by size, poured-in-place surfacing per square foot, sports lighting per pole, synthetic turf, concrete flatwork, planting by size), and models expected low-bid unit prices by region, season, quantity, bidder count and market conditions, with prediction intervals. Feed it into the firm's estimate so each line shows the expected range at bid.

## Target Customer
Principals and project landscape architects at park-focused firms; agency capital project managers who want a second opinion before advertising.

## Impact If Built
Fewer rejected bids and redesign cycles, more parks built in the season they were funded for, and a credible answer to the selection panel question every firm dreads: did your last project bid on budget?
