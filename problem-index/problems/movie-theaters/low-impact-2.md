# Concession Ordering Against a Film Slate

**Industry:** [[movie-theaters|Movie Theaters]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Restaurant inventory software forecasts from last week's sales, but a theatre's demand is set by which films open Friday and who they draw, so managers still order popcorn, cups, hot dogs and bar stock by feel.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #regularization #evaluation-metrics #data-integration #automation #revenue-impact

## The Problem
Concessions are where a theatre makes its margin: supplies cost ~20% of concession revenue at both AMC and Cinemark, and Cinemark's US patrons spent $8.30 each in 2025. But demand swings far more than in a restaurant. A family animation opening brings children who buy candy, kids' packs and slushies; an R-rated horror opener brings teenagers who buy large popcorn and soda; a prestige drama brings older patrons who buy wine at the bar. A Tuesday discount night runs at a fraction of opening Saturday's attendance with a different per-capita spend.

The general manager places weekly orders with a foodservice distributor and the beverage supplier and preps hot food each shift. Over-ordering perishables (hot dogs, pretzels, dine-in menu items) means waste. Under-ordering on an opening weekend means 86ing the combo that drives the per-cap. Most managers order from last week's usage and a look at what's opening.

## What Already Exists
Restaurant inventory and purchasing platforms such as MarketMan, Restaurant365 and Crunchtime forecast usage from sales history and recipes. Cinema point-of-sale systems (Vista, Veezi, RTS, Omniterm) record item sales by transaction and can produce usage reports. Foodservice distributors offer order guides and par-level tools.

## The Customisation Gap
The missing input is the film slate. Theatre-specific demand needs: the coming week's booked films and showtimes by auditorium; the expected audience mix per film (rating, genre, family share, format such as IMAX or Dolby, where per-caps differ); presales by showtime as they accumulate; and the local pattern of how each audience type buys at this site. Restaurant tools see the menu and last week's covers; they don't see that next Friday's opener is a PG animation with 40% of seats presold. A cinema version links the ticketing system's schedule and presales to item-level forecasts and par levels, and adjusts as presales come in. The FDA's menu-labelling rule for chains of 20 or more also ties the item master to calorie data, which circuit menu changes must carry.

## Impact If Solved
For a typical 10–14 screen theatre, forecasting concession demand from the slate rather than last week could cut perishable waste by a quarter and recover stock-out sales on opening weekends, worth an estimated ~1–2% of concession revenue (estimate). It also takes a weekly guessing task off a general manager who already runs the building.
