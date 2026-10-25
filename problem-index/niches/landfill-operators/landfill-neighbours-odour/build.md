# Complaint-to-Source Attribution

**Niche:** [[niches/landfill-operators/landfill-neighbours-odour/profile|Landfill Neighbours & Odour Complaints]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a neighbour complains, the landfill guesses which activity caused it; joining complaints to wind, sensors and site operations would point at the source within an hour.
**Tags:** #bayesian-inference #gaussian-processes #gradient-boosting #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to stop landfill odour reaching the neighbours, and whoever has the fewest verified odour complaints per month takes the account.

## The Problem
Odour complaints are timed and geolocated, but the landfill's activities — where the face is, which cell is being capped, when leachate tanks were opened, which wells are off — are not, so the cause is argued rather than identified.

## Why Nobody Has Built This
Sensor vendors sell monitoring hardware and dispersion maps; site activities live in logs and memory; and complaints sit with the agency.

## What to Build
A model that back-traces each complaint against wind and stability data to candidate sources on the site, scores each source by its activity at the time (face location and size, cap work, leachate handling, gas system status) and sensor readings, and learns from confirmed causes. It produces a ranked cause within the hour and monthly patterns by activity and weather.

## Target Customer
Landfill managers at sites near housing, facing expansion hearings or enforcement.

## Impact If Built
If attribution lets a site cut confirmed complaints by ~30% (estimate), a landfill drawing ~20 nuisance notices a year at ~$10K each in penalties and response (estimate) saves ~$60K and strengthens its expansion case.
