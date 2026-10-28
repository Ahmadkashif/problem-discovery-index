# A Show-Up Model for Monthly Capacity

**Niche:** [[niches/parking-operators/monthly-accounts-validations/profile|Monthly Accounts, Access Cards & Validations]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Facility managers oversell monthly cards by rule of thumb, either leaving paid spaces empty or turning monthly parkers away on a busy Tuesday.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #monte-carlo-methods #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a facility's monthly-contract capacity sold and paid, and whoever bills and collects the highest share of that capacity each month takes the account.

## The Problem
Hybrid work changed how often monthly holders come in, but oversell ratios are still set by the manager's feel: sell 120 cards for 100 spaces, unless someone complains. Too few cards leaves contract revenue unsold; too many fills the deck before 9 am and loses tenants.

## Why Nobody Has Built This
Access-card logs sit in the PARCS and are rarely analysed by holder. Operators fear the complaint more than the empty space, and nobody has modelled the trade-off per facility.

## What to Build
A model of each holder's daily show-up probability by weekday and season, trained on access-card entries, combined by Monte Carlo into the distribution of peak monthly occupancy for any number of cards sold. It also models churn, the chance that a holder cancels, so sales targets anticipate attrition. The manager sees how many more cards can be sold at a chosen risk of turning anyone away.

## Target Customer
Facility and area managers at office and mixed-use garages; owners with large monthly bases.

## Impact If Built
Selling 5–10% more monthly cards at the same turn-away risk (estimate) on a 1,000-space office garage at ~$200 a card a month adds ~$120–240K a year of contract revenue for the owner.
