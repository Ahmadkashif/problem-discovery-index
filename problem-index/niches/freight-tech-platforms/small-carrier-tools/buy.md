# Small Business Financial Tooling Applied to Cost Per Mile

**Niche:** [[niches/freight-tech-platforms/small-carrier-tools/profile|Small Carrier Tools]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bank feeds, card transaction categorisation and fuel card data are all commodity, and most small carriers cannot state their own cost per mile — which is the number every rate decision is supposed to be measured against.
**Tags:** #gradient-boosting #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor selling to small carriers is fighting to tell an owner what a load is actually worth to them, net of deadhead, fuel and the next load's prospects, before they accept it — and whoever answers that in one screen takes the segment.

## The Problem
Ask an owner-operator what it costs them to run a mile and the answer is a figure they heard, or a rough calculation from last year's tax return. The actual number — fuel at their own consumption rate, tyres, maintenance on their specific equipment amortised properly, insurance, permits, the truck payment, and the fixed costs spread over the miles they actually run — is computable from their own bank and fuel card records and is not computed. Without it, every rate decision is made against an unknown threshold, and a carrier can run hard for a year at rates below cost while appearing busy.

## What Already Exists
Bank feed aggregation and transaction categorisation are commodity services. Fuel card providers supply detailed transaction data including gallons, price and location. ELD systems supply miles by state and by trip. Maintenance records exist in shop invoices. Small business accounting products handle the general case well and several carrier-specific bookkeeping services exist. Every input is available and most are already flowing somewhere.

## The Customization Gap
The adaptation is to trucking's cost structure. It requires: (1) categorisation into trucking's own cost categories with fixed and variable separated properly, since the fixed-cost-per-mile figure depends on miles run and is the part owners get most wrong; (2) fuel economy computed per truck from fuel card gallons against ELD miles, which is both a cost input and the most actionable operational metric a small carrier has; (3) maintenance amortised over the interval it covers rather than expensed in the month it occurs, because a tyre set charged to one month makes that month look catastrophic and the next look wonderful; (4) IFTA fuel tax computed from the same data, which is a quarterly obligation currently done by hand or paid for as a service; and (5) the output expressed as the threshold the load valuation needs — this truck's cost per mile today, loaded and including deadhead — rather than as a financial report the owner will not open.

## Target Customer
Owner-operators and small fleets, the factoring and fuel card providers who already hold much of this data, and the bookkeeping services serving the segment.

## Impact If Solved
A true cost per mile converts every rate decision from a guess into a comparison, which is the precondition for the load valuation in the build note. The data is already flowing through cards, banks and ELDs; the work is in the trucking-specific categorisation and in producing one number rather than a report.
