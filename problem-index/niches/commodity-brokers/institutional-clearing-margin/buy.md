# Bank Balance-Sheet Allocation Tools Adapted to FCM Capital Rules

**Niche:** [[niches/commodity-brokers/institutional-clearing-margin/profile|Institutional Clearing & Margin Financing]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks have mature tools for charging each business line for the balance sheet it uses, but futures clearing's capital rules and margin dynamics fit them poorly.
**Tags:** #optimization-fundamentals #linear-regression #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give a fund or commercial client the most margin capacity per dollar of the FCM's own capital, through cross-margin offsets, eligible collateral and intraday limits set on the client's real risk, and whoever carries the largest client book per dollar of capital without cutting clients off in a margin spike takes the account.

## The Problem
Client profitability in futures clearing is a net of commissions, fees and interest on balances, minus the cost of the capital the client consumes and the default fund contributions it drives. Most FCMs compute it monthly in spreadsheets, with capital allocated by rough share of margin.

## What Already Exists
Funds transfer pricing and balance-sheet allocation platforms used by bank treasuries, and client profitability modules in prime brokerage, which charge business lines for liquidity, leverage and risk-weighted assets.

## The Customization Gap
The adaptation needs the CFTC's FCM net capital rule (the greater of $1M, 8% of customer and non-customer risk maintenance margin, or the SEC requirement for dual registrants) rather than bank RWA. It needs clearing-house default fund and concentration charges. It needs interest on segregated balances and the residual interest the FCM keeps in segregation. It needs cross-margin offsets across clearing houses. And it needs daily rather than monthly attribution, because a client's capital use can triple within a week of margin hikes.

## Target Customer
CFOs and heads of clearing at mid-size and large FCMs, particularly dual-registered broker-dealer FCMs that already run bank-style treasury systems.

## Impact If Solved
A daily, rule-correct view of return on capital per client, available in the clearing committee rather than at year end.
