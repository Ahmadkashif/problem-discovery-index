# Beating Noon on the Segregation Computation

**Industry:** [[commodity-brokers|Commodity Brokers]]
**Type:** Worker Life Changing
**One-liner:** Every business day a small team of FCM accountants has until noon to prove, currency by currency, that customer money is all there, and they spend the morning chasing breaks rather than understanding them.
**Tags:** #time-series-forecasting #exponential-smoothing #feature-engineering #worker-facing #compliance #automation #data-integration

## The Problem
CFTC Rule 1.32 requires an FCM to compute, as of the close of each business day, the funds it holds in segregation for futures customers, the amount it is required to hold, and its own residual interest, on a currency-by-currency basis. The computation must be finished before noon on the next business day, with parallel computations for foreign-futures customers (Rule 30.7) and cleared-swap customers (Rule 22.2). The results go to the CFTC and the firm's DSRO, and the CFTC publishes the monthly figures firm by firm. In 2009 the CFTC found that JPMorgan Futures had violated Rule 1.32 by completing a computation late.

At a mid-size FCM the job falls to a handful of accountants, two to six (estimate). Each morning they pull balances from depository banks, clearing houses and carrying brokers. They pull the back office's view of customer net liquidating equity, deficits and debit balances, and the values of securities held as margin after haircuts. They reconcile all of it, investigate every break, decide which customer deficits can be offset by which collateral, and check the excess against the firm's own residual interest target. Since December 2025, under CFTC Letter 25-40, FCMs that accept digital-asset collateral have also had to apply DCO haircuts to bitcoin, ether and payment stablecoins in the same computation and report their holdings weekly.

## Why It Matters to the Worker
The deadline is personal. A late or wrong computation is a reportable regulatory failure, and the accountant who signs off carries it. The work peaks on exactly the days the market is wildest, when deficits multiply and wires arrive late. Most of the morning goes to mechanical matching across bank portals, clearing-house reports and back-office extracts, leaving little time to understand why the excess moved. That is the part a CFO or DSRO examiner will actually ask about.

## What a Solution Looks Like
Automated ingestion of the bank, clearing-house and back-office data overnight, with a pre-matched computation waiting at 7 a.m. and only true breaks queued for review, each with its likely cause. A forecast of the day's segregation requirement and excess, made from open positions, settlement prices and expected wires, so treasury can move residual interest before a shortfall rather than after. And a narrative of the day's movements drafted for the sign-off.

## Impact If Solved
Turning a three-to-five-hour scramble (estimate) into an hour of review gives the team back its mornings and cuts the risk of a late filing on volatile days. It also makes the segregation team the people who explain the firm's customer-funds position, not the people who type it.
