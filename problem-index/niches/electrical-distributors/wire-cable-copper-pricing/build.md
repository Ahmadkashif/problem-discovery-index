# Hold Periods Priced From Copper Volatility

**Niche:** [[niches/electrical-distributors/wire-cable-copper-pricing/profile|Wire & Cable Pricing Against COMEX Copper]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A seven-day hold on a wire quote is an option the distributor gives away free, and nobody prices it.
**Tags:** #time-series-forecasting #monte-carlo-methods #exponential-smoothing #linear-regression #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price every wire and cable quote and order to the day's copper with hold terms the contractor accepts, and whoever keeps wire margin flat through a copper swing without losing the bid takes the account.

## The Problem
Contractors want wire prices held while they win and schedule jobs; distributors grant holds by habit — a day for the counter, a week for a project — regardless of how volatile copper is that month. In a calm month the hold costs little; in a tariff-driven spike it wipes out the margin on every held quote.

## Why Nobody Has Built This
Pricing software treats cost as stable between updates, and distributors lack the data discipline to record hold terms. The arithmetic is simple; the plumbing between price sheets, reels, quotes and releases is not.

## What to Build
A pricing service that forecasts copper volatility over each quote's hold window, simulates margin at release from the distributor's reel and replacement costs and the manufacturer's sheet behaviour, and sets the price and hold period to keep expected margin above floor. It offers the salesperson a choice — a longer hold at a higher price, or a shorter one at a sharper price — and records whichever the contractor takes.

## Target Customer
Pricing and wire product managers at distributors with large wire volumes.

## Impact If Built
Wire margin is protected in volatile months without losing bids in calm ones: holding ~1–2 points of margin on ~$30M of wire sales at a large regional distributor (estimate) is ~$0.3–0.6M a year (estimate), with a recorded hold term on every quote.
