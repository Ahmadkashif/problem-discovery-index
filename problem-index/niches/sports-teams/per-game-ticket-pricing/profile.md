# Per-Game Ticket Pricing & Demand Forecasting

**Parent Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to set each game's price by seat tier before the resale market sets it for the club, and whoever raises a club's ticket revenue per available seat against its own prior season takes the account.

## Profile
**Market Size:** ~$300M a year of dynamic-pricing software, ticketer pricing services, fan-data platforms and in-house pricing analysts at North American clubs and college departments (estimate)
**Share of Parent Industry:** Pricing tools cost under 1% of club revenue; they set the single-game half of ticket revenue (estimate)
**Digital Adoption:** High in the big leagues, where prices move daily; low in the minors, where tiers are set once a season
**Target Buyer:** Vice president of ticketing or director of ticket operations; at a minor-league club, the general manager
**Automation Potential:** High — demand forecasts and price recommendations recur for every game and are graded by sales within days

## What Makes This a Distinct Niche
Every club sells the same seat dozens of times a season, and the resale market posts a price for every game whether the club does or not. Pricing a game is the most mechanical, repeatable revenue decision in the industry, and it is checked quickly: sell-through, resale spreads and no-show rates arrive within days. Big-league clubs buy it from their ticketer or a fan-data platform and staff analysts. Minor-league and lower-division clubs mostly do not price per game at all. This niche hosts the two-week MVP: a per-game demand and price-tier model for minor-league clubs built on MLB Stats API schedules and attendance, SeatGeek public listing prices and synthetic primary sales. The ticketer side of the market is analysed at [[niches/ticketing-agencies/primary-ticketing-contracts/profile|Primary Ticketing for Venues, Tours & Teams]].

## Current Tools & Gaps
Ticketmaster's and SeatGeek's pricing tools for their team clients, fan-data platforms (KORE in Two Circles, StellarAlgo), in-house analysts, and independent pricing consultants. Gaps: thin-data clubs cannot fit a model on their own history; promotions, weather and roster news (a rehab start, a star's injury) enter late or not at all; and price changes are rarely tested, so elasticity is assumed rather than measured.

## Problems
- [[niches/sports-teams/per-game-ticket-pricing/build|🔨 Build: A Pooled Demand Model for Thin-Data Clubs]]
- [[niches/sports-teams/per-game-ticket-pricing/buy|🛒 Buy: Hotel Revenue Management Fitted to a Ballpark]]
- [[niches/sports-teams/per-game-ticket-pricing/fix|🔧 Fix: The Price Change Nobody Tested]]
