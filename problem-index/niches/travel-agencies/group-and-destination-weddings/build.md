# A Release Decision Before the Cut-Off

**Niche:** [[niches/travel-agencies/group-and-destination-weddings/profile|Group & Destination Wedding Travel]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Advisors decide whether to release unsold rooms or hold them from a gut feel about how wedding guests book, and pay for being wrong either way.
**Tags:** #survival-analysis #gradient-boosting #bayesian-inference #time-series-forecasting #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill a contracted room or cabin block without paying attrition, and whoever forecasts pickup early enough to release or extend space before the supplier's cut-off takes the account.

## The Problem
Forty rooms are blocked for a wedding in Punta Cana; twelve weeks before the release date, nineteen are booked. The advisor must decide whether to release ten, hold, or ask the resort to extend. Wedding guests book late and in bursts after save-the-dates and the bridal shower; church groups book early and drop out; alumni trips stall then fill. Attrition allowances are typically ~10-20% of the block (estimate), and the cost of a wrong call is either empty-room charges or guests turned away.

## Why Nobody Has Built This
Each advisor runs too few groups to see the pattern, the pickup history sits in supplier portals and spreadsheets, and suppliers have no reason to help agencies release space earlier.

## What to Build
A pickup forecaster pooled across a host's or consortium's groups: booking curves by group type, destination, season, lead time and guest-list size, updated with each booking and payment, giving the probability of breaching attrition at each date and a recommended release or extension. Contract terms are extracted from the block PDF so the deadlines drive the forecast.

## Target Customer
Group desks at host agencies and consortia; advisors specialising in destination weddings and group cruises.

## Impact If Built
Fewer attrition charges and fewer premature releases, with release decisions made weeks earlier on evidence rather than on the night before the cut-off.
