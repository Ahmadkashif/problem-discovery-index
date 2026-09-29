# The Trip as the Unit of Planning and Pricing

**Niche:** [[niches/field-service-software/rural-service-territories/profile|Rural & Long-Drive Service Territories]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** In a low-density territory the economic unit is the trip rather than the job, and every field service product in the market plans, prices and measures jobs.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #time-series-forecasting
**Contested on:** Every serious competitor selling into low-density territories is fighting to make a day of service profitable when half of it is spent driving — and whoever raises revenue per drive hour most takes the account.

## The Problem
A customer ninety minutes away calls with a non-urgent problem. Sending someone today means a technician spends three hours driving for a one-hour job, and the day is gone. The right answer is almost always to wait until there is enough work in that direction to justify a trip, and to tell the customer when that will be — but no system supports it. The dispatcher holds a mental list of pending work by area, guesses when a trip will be worthwhile, and frequently sends someone early because a customer pressed. Meanwhile the business's pricing does not distinguish between a customer eight minutes away and one ninety minutes away, so the distant jobs are priced at a loss and the close ones subsidise them invisibly.

## Why Nobody Has Built This
Field service products were built for urban and suburban density, where drive time is a cost to minimise rather than the structure of the business, and the rural segment is too small and too price-sensitive to have pulled a product toward it. Batching also requires telling a customer they will be seen next Tuesday rather than tomorrow, which vendors have treated as a service failure rather than as the honest and economically correct answer that it is in this setting. And the pricing question — charging differently by distance — is commercially sensitive in small communities and has therefore been left alone.

## What to Build
Planning and pricing around the trip. Pending work is held as a geographic backlog with each item's urgency and deadline, and the system computes when a trip to each area becomes worthwhile — enough accumulated work, or an item whose deadline forces it — and proposes the trip with its full route. Customers in distant areas are offered a scheduled window when the trip is planned, which is a better experience than a vague promise and is what most of them expect anyway. Pricing is computed per job including the true marginal travel cost, with the trip's costs allocated across its jobs, so the business can see what a distant job actually earns and decide deliberately whether to charge for travel, batch it, or decline it. Emergency response is priced explicitly as what it is: a broken trip, with the cost of the disrupted day attached.

## Target Customer
Service businesses operating in low-density territories across the trades, equipment service and utilities contracting, and the platform vendors who currently sell them an urban product.

## Impact If Built
Batching converts the dominant cost in these businesses from unavoidable to managed, and operators who plan trips deliberately rather than reactively typically lift jobs per drive hour substantially. Trip-allocated pricing is the more uncomfortable output and the more valuable one, since it usually shows that a portion of the territory has been served at a loss for years, subsidised by nearby customers who could be served for less.
