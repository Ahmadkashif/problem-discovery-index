# The Inside Rep Re-Quoting the Same Deal

**Industry:** [[it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Worker Life Changing
**One-liner:** An inside account rep spends much of each week rebuilding quotes that went stale before the customer signed — a distributor cost moved, stock ran out, a registration expired, a promotion ended — and gets back the hours to sell when open quotes keep themselves current.
**Tags:** #large-language-models #time-series-forecasting #gradient-boosting #worker-facing #automation #workflow-orchestration #data-integration

## The Problem
An inside rep at a reseller carries forty to a hundred open quotes for laptops, monitors, docking stations, switches, licences and warranty extensions (estimate). Each was priced on a given day from a given distributor's cost and stock, with whatever registration or promotion applied that week. Customers take weeks to approve, and in that time the inputs move: the distributor's cost changes, the stock that was available at TD SYNNEX is gone and Ingram has it at a different price, a model reaches end of sale, a quarterly promotion lapses, a tariff change reprices a product family overnight. When the purchase order finally arrives the rep has to rebuild the quote — check every line against current cost and availability, swap substitutes, re-apply the registration, recompute the margin, ask the customer to re-approve — and then explain why the price changed.

The rebuild is mostly mechanical, and it lands at the worst time: at month-end and quarter-end, when customers spend budget and vendors push volume, a rep may re-quote a dozen deals a day (estimate). Some reps re-check open quotes every Monday morning by hand; most find out a quote is stale only when the order fails to convert at the quoted margin.

## Why It Matters to the Worker
The rep is paid on gross profit, so a stale quote that converts at the old price comes out of their commission, and one that has to be re-approved risks the deal itself. The repetition is the part of the job least connected to why they took it — knowing their customers, finding the right product, winning against the reseller down the road — and the pressure peaks exactly when there is least time to think.

It is also where blame lands. When a customer receives a revised quote with a higher price two weeks after the first, the rep takes the call. When a substitute model turns out to be wrong for the customer's fleet, the rep picked it under deadline.

## What a Solution Looks Like
Open quotes that watch themselves: every line re-checked overnight against each distributor's price and availability feed, registration expiry and promotion end dates, with a morning list of which quotes have drifted, by how much margin, and why. For each drifted quote, a refreshed draft with the best current source, a like-for-like substitute where stock has gone, and a one-paragraph customer note explaining the change, ready for the rep to approve. A simple forecast of which quotes are likely to convert this week tells the rep which ones to refresh first.

## Impact If Solved
Taking the mechanical re-check off the rep gives back ~4–6 hours a week (estimate), cuts quotes that convert below their quoted margin, and turns quarter-end from a re-keying marathon into a list of decisions — which customers to call, which substitute to recommend — that only the rep can make.
