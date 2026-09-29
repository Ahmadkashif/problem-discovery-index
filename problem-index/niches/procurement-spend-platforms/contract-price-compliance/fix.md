# The Rebate Nobody Claims

**Niche:** [[niches/procurement-spend-platforms/contract-price-compliance/profile|Contract Price Compliance]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Volume rebates, growth incentives and early payment discounts are negotiated into contracts and are claimed by whoever remembers, which means a meaningful share of negotiated value is simply never collected.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #time-series-forecasting #compliance #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in procurement controls is fighting to check the invoiced price against the contracted price at the moment of payment — and whoever closes that gap takes the savings the organisation already negotiated.

## The Problem
A contract includes a rebate of a stated percentage on annual spend above a threshold, payable on request within ninety days of year end, plus a growth incentive if spend rises against the prior year. The category manager who negotiated it has moved roles. Nobody tracks the spend against the threshold during the year, nobody knows the claim window exists, and the rebate is claimed if the supplier mentions it — which some do and some do not. The value was negotiated, is contractually owed, and is not collected. This is among the most common and least discussed forms of value leakage in procurement.

## Why It's Still Broken
Rebate terms live in a contract document as prose and are not tracked anywhere as an entitlement with a threshold and a deadline. The person who negotiated the term is the only one who knows it exists, and procurement roles turn over. Claiming requires knowing the spend against the threshold, which requires the classification and supplier resolution that this industry's first niche describes. And the supplier has no obligation to volunteer it, which means the arrangement quietly favours whichever party is paying attention.

## What a Fix Looks Like
Track entitlements as objects with thresholds and clocks. Every rebate, incentive, discount and credit term extracted from the contract into a tracked entitlement: the basis, the threshold, the rate, the measurement period, the claim mechanism and the deadline. Spend against each threshold computed continuously from the resolved, classified transaction data, so the organisation knows mid-year whether it is on track — which is also a negotiating and buying-behaviour signal, since spend slightly below a threshold is worth redirecting. Claims generated automatically at period end with the calculation and the supporting data attached, rather than requiring someone to remember. Deadlines escalate before they lapse. And the standing report is entitlements earned, claimed and collected, which is a three-column comparison most organisations have never produced and which reliably shows a gap between the first two columns.

## Who Feels the Pain
Procurement functions whose negotiated value is not realised; finance, which budgets for savings that do not arrive; and the successor category manager who inherits a contract whose terms nobody explained.

## Impact If Fixed
Rebate entitlement tracking is extraction plus arithmetic and reliably recovers value that was already negotiated and is contractually owed. The mid-year threshold visibility is a second benefit that changes buying behaviour rather than only collection, since directing marginal volume to cross a threshold is a decision nobody can currently make.
