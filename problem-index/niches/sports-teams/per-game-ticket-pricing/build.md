# A Pooled Demand Model for Thin-Data Clubs

**Niche:** [[niches/sports-teams/per-game-ticket-pricing/profile|Per-Game Ticket Pricing & Demand Forecasting]]
**Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One minor-league club's history is too short to price per game, but 120 clubs' public schedules, attendance and resale prices together are enough.
**Tags:** #bayesian-inference #gradient-boosting #time-series-forecasting #feature-engineering #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each game's price by seat tier before the resale market sets it for the club, and whoever raises a club's ticket revenue per available seat against its own prior season takes the account.

## The Problem
A small club has maybe three seasons of usable sales data across ~200 dates, with promotions, weather and opponents all varying. A model fitted on that alone overfits.

## Why Nobody Has Built This
Big-league pricing tools are sold through ticketing contracts and tuned to deep data. Minor-league clubs are small buyers, and no vendor has pooled public data across them.

## What to Build
The two-week MVP, then a product. Week one: pull schedules, start times and announced attendance across affiliated levels from the MLB Stats API, promotions from club websites, weather history, and SeatGeek public-API lowest and highest listed prices per game. Week two: fit a hierarchical model (club, level and league effects with partial pooling) with gradient-boosted residuals, add a synthetic per-tier primary-sales generator calibrated to announced attendance, and recommend tier prices per date with backtests on a dozen clubs. Then replace the synthetic layer with a pilot club's real sales, and license MLB data for commercial use (its data notice restricts it, not checked here).

## Target Customer
General managers of affiliated and independent clubs; multi-club owners; ticketers wanting a pricing add-on for small clients.

## Impact If Built
A 5–8% lift on ~$3.9M of ticket revenue at a typical club (estimate) is ~$200–300K a year, and across 120 clubs ~$25–35M (estimate).
