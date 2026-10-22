# Take-Rate Forecasting From Pre-Registrations and Comparable Builds

**Niche:** [[niches/wired-broadband-providers/coop-and-municipal-entrants/profile|Electric Co-op & Municipal Fibre Entrants]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A co-op or city borrows against a take-rate assumption written once in a feasibility study and then manages the build without a live forecast of whether it will be met.
**Tags:** #bayesian-inference #gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #revenue-impact
**Contested on:** Every serious competitor serving this segment is fighting to run a first-time operator's network, billing and care up to the take rate its loan or bond model assumed, and whoever gets a new entrant to that take rate inside its first three years becomes its long-term operating partner.

## The Problem
The feasibility study assumed 40–50% take rate by year three (estimate, typical of such studies). Construction proceeds by phase; pre-registrations trickle in; nobody can say by month eighteen whether the plan is on track or which phases are lagging, until revenue falls short of debt service.

## Why Nobody Has Built This
Each entrant has only its own history, too little to model. The data that would help — take-rate curves of comparable rural builds by competitive situation and pricing — sits fragmented across operators and consultants.

## What to Build
A forecaster that updates take-rate expectations per construction phase from pre-registrations, sign-up velocity after "lit" dates, competitive availability per address from the FCC map, pricing and marketing effort, with priors from comparable builds pooled through an operating partner or vendor. It flags lagging phases early and recommends where to put marketing and install capacity.

## Target Customer
Co-op and municipal broadband general managers and boards, their lenders, and operating partners serving many entrants.

## Impact If Built
Shortfalls surface while there is still time to fix them, and lenders and boards see a forecast rather than a promise.
