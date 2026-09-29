# Decades of Forecasts and Outcomes, and No Published Error

**Niche:** [[niches/oil-gas-field-services/reserve-engineering-firms/profile|Reserve Engineering Firms]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has been forecasting production for forty years and knows what actually happened, and reports neither.
**Tags:** #ml-time-series #survival-analysis #tabular-ml #evaluation-metrics #hypothesis-testing

## The Problem
A reserve report says how much a property will produce and what that is worth. Securities disclosure requires it, bank borrowing bases are sized on it, and acquisitions are priced against it. The engineer's estimate is the number the money moves on.

Reserve estimation is a professional discipline with defined categories, defined risking conventions, and a signature. What it does not have is a published error rate. The firm has issued thousands of reports over decades, and every property it evaluated then produced — so for every estimate, the outcome exists.

Nobody assembles it. Estimates live in report files organized by client and vintage, outcomes live in production data the firm also uses daily, and the comparison is not run. So no one can say whether proved developed producing estimates are systematically conservative or aggressive, whether the firm's undeveloped location assumptions have held, or whether estimation accuracy differs by basin, by operator, or by engineer.

## Why Nobody Has Built This
Reserve reporting is governed by definitions and by professional standards that emphasize method and reasonable certainty rather than measured accuracy. The categories are defined by confidence levels — proved is meant to have a high probability of being met or exceeded — and the profession has been content to treat that as an epistemic commitment rather than an empirical claim.

There is also a commercial reason not to look. A firm that published its own historical bias would hand a negotiating tool to every counterparty who ever disputed one of its reports.

And the outcomes arrive slowly enough, and are spread across enough clients, that no individual engagement ever prompts the question.

## What to Build
Backtest the firm's own history.

**Assemble estimate-outcome pairs.** Every historical report's reserve estimate at a given effective date, matched to what the properties actually produced afterwards. The data engineering is the work; the comparison is arithmetic.

**Measure bias and dispersion by category.** Are proved developed estimates meeting their confidence definition in practice? Are undeveloped locations converting at the rate assumed? These are the questions the definitions imply and nobody tests.

**Segment.** Accuracy by basin, by vintage, by operator, by production mechanism, and — internally — by engineer. Systematic differences are both a quality signal and a training input.

**Recalibrate risking.** Risk factors applied to undeveloped and non-producing categories are conventional. Fitting them to observed conversion rates makes them empirical, which is a materially stronger position in a report an auditor reads.

**Use it commercially, carefully.** A firm that can say its proved estimates have been met or exceeded at a measured rate over twenty years is making a claim no competitor can match, and it changes the conversation with lenders and auditors from method to evidence.

## Target Customer
Managing partner or practice leader at an independent petroleum engineering firm. The market context supports it: capital discipline has made lenders and investors more sceptical of reserve reporting, and evidence of forecasting accuracy is exactly what a sceptical audience wants.

## Impact If Built
Reserve estimates set what energy companies can borrow, what they report to investors, and what assets sell for. The profession asserts confidence levels and has never measured whether it meets them. A firm that does — and can show it — turns a commodity certification into an evidenced product.
