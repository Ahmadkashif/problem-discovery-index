# The Whole Financial Life, Shown as a Balance

**Niche:** [[niches/neobanks/cash-flow-intelligence/profile|Cash-Flow Intelligence]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The institution sees every deposit, every bill and the whole shape of a customer's month, and shows them a balance and a list of transactions.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #revenue-impact #recurrent-forecasting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a complete view of a customer's financial life into something that helps them rather than into a balance screen — and whoever does that earns the primacy the whole model depends on.

## The Problem
The institution knows when this customer is paid, how much, what leaves the account and when, which commitments are recurring, how the month typically shapes, and how close to the edge it usually gets. It can see a fortnight ahead with reasonable confidence. What the customer sees is a number and a list. When they run short it is a surprise to them and was not a surprise to the data. The institution's whole commercial model depends on being the primary account, the primary account is the one that helps, and the help available from the data is almost entirely unbuilt.

## Why Nobody Has Built This
The same ledger is used intensively for risk and barely for the customer, because risk is a loss line and customer help is a product investment with a diffuse return — the data was pointed at the institution's problem rather than the customer's. Categorisation is unreliable enough that features built on it disappoint, which discouraged the attempt. Forecasting that is wrong is worse than none, so the bar feels high. And overdraft and fee income in some models are earned when the customer runs short, which is an uncomfortable conflict.

## What to Build
Forecast the month and act on it. Build a cash-flow forecast per customer from their own history — income timing and amount, recurring commitments, typical discretionary pattern — which is well-posed on a complete ledger and is the foundation for everything else. Identify recurring commitments reliably, including the ones the customer has forgotten, since a subscription nobody uses is money found and is the most immediately appreciated feature in this space. Warn about a shortfall with enough notice to act, which is the fix note's subject and is the difference between help and commentary. Detect income disruption early, because a missed or reduced deposit is the strongest predictor of difficulty and is visible immediately. Suggest specific actions rather than displaying a forecast, since a customer facing a shortfall needs options and not a chart. Handle the irregular-income customer, who is a large share of this population and whom every conventional budgeting tool serves badly. Improve categorisation as infrastructure, since everything here depends on it and its unreliability is what has held the category back. Connect to the risk side, so a customer under financial stress is understood as such rather than flagged as anomalous — which is the same data serving both purposes correctly. Be honest about the conflict where fee income depends on shortfalls, because a product that helps customers avoid fees is the right one and should be built deliberately. And measure whether customers who use these features stay and deepen, since that is the commercial case and it is checkable.

## Target Customer
Product leadership at digital banks, the customers whose financial life the institution can see and does not use, and the financial health vendors serving the segment.

## Impact If Built
The ledger was pointed at the institution's problem rather than the customer's, so the same data polices and does not help. A cash-flow forecast with enough notice to act is well-posed on a complete ledger and is what turns a balance screen into the reason the account stays primary.
