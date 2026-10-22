# Capital Cost per Client Priced Before the Account Opens

**Niche:** [[niches/commodity-brokers/institutional-clearing-margin/profile|Institutional Clearing & Margin Financing]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** FCMs agree clearing terms with a fund before anyone has estimated how much of the FCM's capital that fund's book will consume through a cycle.
**Tags:** #monte-carlo-methods #gradient-boosting #time-series-forecasting #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to give a fund or commercial client the most margin capacity per dollar of the FCM's own capital, through cross-margin offsets, eligible collateral and intraday limits set on the client's real risk, and whoever carries the largest client book per dollar of capital without cutting clients off in a margin spike takes the account.

## The Problem
An FCM onboarding a CTA or a commercial hedger negotiates commissions, clearing fees and margin terms against what competitors offer. The client's capital cost to the FCM depends on how its margin will behave: how large, how volatile, how correlated with other clients, how often it will need intraday credit. That is only learned after months of clearing. Unprofitable relationships are discovered at annual review, once the capital has been tied up through a volatile quarter.

## Why Nobody Has Built This
Bank FCMs allocate capital through group-wide treasury models designed for the whole bank, not for futures clients. Non-bank FCMs have the data but not the quant teams. Back-office vendors compute margin and capital as they are, not as they will be, and nobody owns the client's projected book.

## What to Build
A pre-onboarding simulator that takes a prospect's described strategy, sample positions or track record, replays it through historical margin regimes, including 2020 and the 2022 rallies, under the clearing houses' methodologies, and projects margin, capital charge (8% of risk maintenance margin plus concentration add-ons), intraday credit use and expected revenue. After onboarding it updates with the client's actual book and flags relationships drifting below the hurdle return.

## Target Customer
Heads of futures clearing and client onboarding committees at non-bank FCMs such as StoneX, Marex, ADM Investor Services and Macquarie, and the futures businesses inside bank FCMs.

## Impact If Built
Terms are priced on projected capital use instead of competitor quotes. Unprofitable accounts are declined or repriced before they consume capital, and the same capital carries more profitable business.
