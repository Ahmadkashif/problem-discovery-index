# Value-Based Bidding From Performance Marketing

**Niche:** [[niches/lending-marketplaces/acquisition-economics/profile|Acquisition Economics]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Ecommerce advertisers moved from cost per acquisition to value-based bidding years ago, and lending marketplaces still bid to a lead.
**Tags:** #gradient-boosting #evaluation-metrics #revenue-impact #confidence-intervals #time-series-forecasting #causal-inference #logistic-regression #data-integration
**Contested on:** Every serious competitor in this niche is fighting to bid on a borrower's expected funded value rather than on their click probability — and whoever gets the funded signal into the bid takes the traffic everyone else is overpaying for.

## The Problem
Ecommerce advertisers stopped bidding to conversions and started bidding to predicted customer value: order value, margin, predicted lifetime value, with the platforms supporting value-based strategies natively. The tooling, the conversion value APIs and the measurement practice are all mature and widely used. Lending marketplaces, whose value dispersion per conversion is far larger than a typical retailer's, still send a conversion flag.

## What Already Exists
Value-based bidding strategies with platform support; predicted lifetime value modelling; conversion value APIs and offline conversion import; incrementality testing; and delayed conversion handling.

## The Customization Gap
The adaptation is to a value realised inside a third party. It requires: (1) value that depends on a lender's decision rather than on the advertiser's own transaction, which is the substantive difference and is why the standard practice has not simply been adopted; (2) long and variable delay between click and funding, where ecommerce delays are days and these are weeks; (3) value that must be predicted rather than observed for most of the volume, since funded data covers only part of it; (4) credit and privacy constraints on what may be sent back to ad platforms as conversion data; and (5) a regulated advertising surface where creative and targeting are constrained in ways retail is not.

## Target Customer
Performance marketing leadership, finance teams evaluating acquisition, and bid management and measurement vendors serving regulated advertisers.

## Impact If Solved
The practice and the platform support are mature and are being fed a constant. Predicting a value realised inside a lender, weeks later, is the adaptation, and the dispersion here makes it worth more than in the industries that pioneered it.
