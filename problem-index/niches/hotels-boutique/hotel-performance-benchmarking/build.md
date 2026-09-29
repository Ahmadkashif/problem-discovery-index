# Forty Years of Daily Data Used to Report Yesterday

**Niche:** [[niches/hotels-boutique/hotel-performance-benchmarking/profile|Hotel Performance Benchmarking & Demand Data]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most complete daily performance record in any industry anywhere is used almost entirely to tell hotels what already happened.
**Tags:** #ml-time-series #time-series-forecasting #gradient-boosting #causal-inference #evaluation-metrics #revenue-impact

## The Problem
This company receives daily occupancy, rate, and revenue from a very large share of the world's hotel rooms, and has done so for four decades. There is no comparable dataset in commercial real estate, in retail, or in most of transport. Every hotel manages to the index it produces; owners write management contracts around it and lenders write covenants against it.

The product is a report of what happened. Yesterday's occupancy, last week's index, last month's market. Forecasts exist as a separate market-level product on a monthly or quarterly cadence — useful for planning, useless for the decision a revenue manager makes at four o'clock every afternoon.

Meanwhile the underlying data is a panel of hundreds of thousands of properties observed daily for decades, with market, class, location, and competitive set structure attached. It contains the answer to questions nobody is being sold: which markets are turning before the turn shows up in monthly aggregates, what a competitor's rate move actually did to a property's occupancy, how much of a market's performance a given property should have captured and did not.

Pass 1 puts the problem plainly from the other side: a chain property has a twelve-person revenue team and the boutique GM has a spreadsheet. The data that would close that gap already sits in one place. It is being sold back as a scorecard.

## Why Nobody Has Built This
The reciprocity contract is the business, and it is conservative by construction. Hotels contribute their daily numbers on the understanding that they get comparison and nobody gets exposed. Every product decision for forty years has been filtered through what contributors will accept, and the safe answer has always been aggregate reporting.

That instinct has hardened past its purpose. Forecasting a market, or telling a property what its own trajectory implies, exposes no contributor at all — it uses aggregate structure to say something forward-looking rather than backward-looking. The constraint that genuinely binds is disclosure of individual competitor performance, and it does not touch most of what could be built.

The second reason is that nobody has pushed. The benchmark is effectively a standard, standards do not face substitution pressure, and a business with no competitor has limited reason to attempt the harder product.

## What to Build
A forecasting and diagnostic layer on the panel, sold alongside the benchmark.

**Property-level short-horizon forecasting.** Occupancy and rate seven to ninety days out, with intervals, using the property's own history, its competitive set, the market's current pace, and the seasonal and day-of-week structure the panel makes visible. This is the single most valuable thing an independent hotel does not have, and the panel supports it better than any client's own data could.

**Market turning points.** Decades of daily data across hundreds of markets contain many instances of markets accelerating and decelerating. Detecting the shape early — from pace, mix, and rate dispersion rather than from a monthly aggregate — is a well-posed problem with abundant labelled history.

**Decomposed index movement.** An index falling can mean the property lost share, the competitive set added supply, or the market softened. Today the hotel gets a number and works out which by hand. The panel can separate them.

**Rate response estimation.** With daily rate and occupancy for a property and its competitive set over years, the effect of a rate change on capture — and of competitors' moves on the property — is estimable. Confounded by demand, certainly, which is what makes it worth doing properly and worth paying for.

## Target Customer
Chief Data Officer or head of analytics at the benchmarking business. The strategic argument is about position rather than revenue: as long as the product describes the past, the forward-looking layer belongs to revenue management vendors and the OTAs, and the panel is a commodity input to someone else's product.

## Impact If Built
Twenty thousand US independents price reactively because demand-sensing is priced for chains. The panel is the one asset that could serve them at a price they can pay, and it is currently sold to them as a scorecard telling them they lost. For the business, it converts an unassailable data position into a product position, which is a materially different company.
