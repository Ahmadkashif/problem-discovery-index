# Event Profitability Estimation at Proposal Stage

**Industry:** [[catering-companies|Catering Companies]]
**Type:** High Impact
**One-liner:** Every catering proposal becomes a reliable P&L forecast instead of a gut-feel gamble, eliminating the 15-25% cost estimation error that sinks new operators.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Catering companies quote events days or weeks before execution, committing to a price before they know actual food costs, labor hours, rental fees, travel time, or waste. Experienced catering sales managers can read a client inquiry — venue type, guest count, service style, time of year, corporate vs. social — and estimate true costs within 5% of actuals. They instinctively know that a 200-person outdoor wedding in July will have 12% higher protein waste than a 200-person indoor corporate dinner, that cocktail receptions consume 40% less per-head on entrees but 3x on passed appetizers, and that certain venue combinations with certain service styles require an extra service captain. New operators, or experienced operators quoting unfamiliar event types, miss by 15-25%, and those misses compound across a season into five-figure profit leakage.

## Why It's Unsolved
The estimation knowledge lives entirely in the heads of operators with 10+ years of experience quoting hundreds of events. It is tacit: they cannot articulate the full set of adjustment factors they apply. The data to train a model exists — every completed event has a proposal, actuals, and a variance — but it sits in disconnected spreadsheets, handwritten notes, and accounting systems that were never designed to link proposal-level detail to line-item actuals. Labeling is also asymmetric: operators remember the disasters (the event that lost $8K) but not the routine wins, biasing any self-reported dataset. Building the feature set requires encoding venue characteristics, service style taxonomy, seasonal food cost indices, and client behavioral signals that most catering software does not capture in structured form.

## What a Solution Looks Like
A model trained on historical event data (proposals, BEOs, invoices, purchasing records, post-event P&L) that takes a new proposal's parameters — guest count, venue, menu selections, service style, date, client history — and outputs an expected cost breakdown with confidence intervals. The sales manager sees a projected margin alongside the quote before sending it, with flags for line items where the model's uncertainty is high (e.g., "protein costs for this menu at this guest count have varied 18-32% historically"). Over time, the model ingests each completed event's actuals to tighten its estimates.

## Impact If Solved
A mid-size caterer doing 400 events/year at $15K average could recover $600K-$1.2M in annual margin by eliminating systematic under-quoting and reducing over-prep waste by 10-15%. New sales managers reach estimation accuracy parity with 10-year veterans within their first quarter.
