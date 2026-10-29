# Minor-League Price Tiers Set Once a Season

**Industry:** [[sports-teams|Sports Teams & Clubs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Dynamic pricing is sold to every big-league club, but a minor-league ticket manager with seventy home dates still sets four price tiers in a spreadsheet in February and finds out game by game whether fireworks night needed a higher price.
**Tags:** #gradient-boosting #bayesian-inference #time-series-forecasting #feature-engineering #quick-win #revenue-impact

## The Problem
An affiliated minor-league club plays ~60–70 home dates a season (estimate) in a 4,000–10,000-seat ballpark. Demand swings with things a big-league pricing engine was not built for: Friday fireworks, a bobblehead giveaway, a school-night Tuesday in April, a 7 p.m. start in July heat, a rain forecast at noon, a rehab start by a major-league pitcher announced two days out, and whether the local college has a home football game. The ticket operations manager, often also the box-office manager, sets single-game prices by tier (box, reserved, lawn, berm) before the season, maybe with a premium for a few "prime" dates, and leaves them. The best clubs draw well: the Lehigh Valley IronPigs led the minors in 2025 with 585,167 fans, an average of 8,242 a game (search summary). Most clubs sell a fraction of capacity on weeknights and turn fans away on holiday weekends at the same price.

The resale market already prices each game. SeatGeek and StubHub listings for a sold-out Saturday sit above face value while the club's own price stays flat, and on a dead Tuesday the club's walk-up price sits above resale.

## What Already Exists
Big-league clubs buy dynamic pricing from their primary ticketer (Ticketmaster's and SeatGeek's pricing tools) or from fan-data platforms such as KORE (Two Circles) and StellarAlgo, and many run in-house analysts. Generic revenue-management software exists for hotels and airlines. Independent pricing consultants also sell season-pricing projects, but they are small firms, already profiled at [[niches/ticketing-agencies/independent-pricing-consultants/profile|Independent Ticket Pricing & Ticketing RFP Advisors]].

## The Customisation Gap
The big-league tools assume a deep resale market, tens of thousands of seats and an analyst to watch them. A minor-league club needs something different. The model has to work from a schedule, a promotions calendar and weather rather than a long sales history. It needs a demand prior pooled across 120 clubs and many seasons, so that a club with three seasons of data borrows strength from others. Group and theme-night allocations must be held out of the public price, and resale signals have to be read from a thin market where a dozen listings is a lot. It must also respect the club's community pricing promises (the $10 lawn seat it advertises). A two-week MVP is buildable on public data: game schedules and announced attendance from the MLB Stats API, lowest and highest listed prices from SeatGeek's public API (search summary), weather history, and a synthetic primary-sales generator per tier standing in for the club's own sales until a pilot club shares them. MLB's data notice restricts commercial and bulk use (not checked here), so a product needs a licence or the club's own feed.

## Impact If Solved
For a club averaging ~4,000 paid at ~$14 across 70 dates, ticket revenue is ~$3.9M a season (estimate). A 5–8% lift from raising prime-date prices and filling weeknights is ~$200–300K a year, which is two or three front-office salaries at a club this size.
