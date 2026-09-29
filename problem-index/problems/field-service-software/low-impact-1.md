# Flat-Rate Price Book Maintenance

**Industry:** [[field-service-software|Field Service Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Flat-rate price books are a mature licensed product and every contractor still spends weeks customising one, because a national average price for a capacitor replacement is wrong in every specific market.
**Tags:** #gradient-boosting #linear-regression #descriptive-statistics #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
Residential trades sell at flat rates: a task has a price, the customer approves it before work starts, and the technician is not negotiating on a driveway. Building the price book is the precondition for the whole model.

A price book has hundreds to thousands of tasks, each needing a labour time, a materials cost, an overhead allocation and a margin. Contractors buy a licensed book, then discover that its labour times reflect somebody else's technicians, its material costs reflect last year and another region's supply house, and its prices reflect a market with different wage rates and different willingness to pay. So they customise — line by line, over weeks, usually with an outside consultant, and then they never revisit it, so it drifts until the next painful overhaul.

Underpricing destroys margin invisibly. Overpricing loses jobs at the door, which is also invisible because nobody records why a customer declined.

## What Already Exists
Licensed flat-rate content (Profit Rhino, Callahan, New Flat Rate) is well-established and integrates with the major platforms. Every field service platform ships price book management. Supply house catalogues and pricing feeds are available. Industry labour time standards exist for common trades. Consultants who build price books for contractors are a small established profession.

## The Customisation Gap
The licensed book is a national artefact applied to a local business, and every dimension that matters is local: wage rates, drive times, supply house pricing, competitive density, customer income, and the equipment mix actually installed in that housing stock.

The platform can close all of it. It observes actual labour time per task across thousands of contractors, so it knows the real distribution rather than a published standard — and it knows how that distribution varies by market and by equipment age. It observes actual material costs from invoices. It observes what contractors in comparable markets charge. And, uniquely, it observes acceptance: which quoted prices were approved and which were declined, per task, per market, per ticket size.

That last one turns price book construction from a costing exercise into an empirical one. Price sensitivity per task per market is measurable from data the vendor already has, and it is the question every contractor is guessing at.

Maintenance is the other half. Material costs move, wages move, and a book set once a year is wrong for eleven months of it. Continuous updating with contractor approval is straightforward once the inputs are live.

## Impact If Solved
Pricing is the most direct lever on a service contractor's profitability and is currently set from a national average adjusted by intuition. It is also the most-cited reason contractors switch platforms, which makes it commercially load-bearing for the vendor as well as for the customer.
