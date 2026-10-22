# Production Forecasts From the Crew's Own Record

**Niche:** [[niches/geophysical-survey-firms/onshore-seismic-acquisition-crews/profile|Onshore Seismic Acquisition Crews]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A contractor bids a program on points per day it expects to record, from a bid manager's memory of similar jobs, while years of its own daily production records sit unanalysed.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to record the most clean source and receiver points per crew-day across permit gaps, weather and terrain, and whoever keeps a large-channel crew productive at the lowest cost per square mile wins the library and operator programs.

## The Problem
Every seismic bid rests on a production rate: how many source points a day the crew will shoot given terrain, access, vegetation, permit density, season and equipment. Bid managers estimate it from experience. If they are optimistic, the program loses money; if pessimistic, a competitor wins it. During the job, nobody knows until late whether the crew is on track for the bid.

## Why Nobody Has Built This
Daily production lives in recorder logs and party-chief reports, terrain and access in GIS, permits in spreadsheets, and weather in no system at all. Contractors are small and cyclical; when work is scarce they cut staff, not build tools.

## What to Build
A production model trained on the contractor's own crew-days: points recorded per day explained by terrain class, slope, vegetation, road access, permit and skid density, source type, crew size, weather and season. Use it to price bids with an honest range rather than a point estimate, and during the program to forecast completion date and margin from the first week's actuals, flagging the factor driving any shortfall.

## Target Customer
Bid managers and VPs of operations at onshore seismic contractors running one to six crews.

## Impact If Built
A bid priced within a few percent of actual production, and a mid-job warning when it isn't, protects margins in a business where one program can make or lose the year.
