# Held-Away Account Aggregation

**Industry:** [[robo-advisors|Robo-Advisors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The platform advises on the assets it holds while the client's actual financial position — the workplace plan, the spouse's accounts, the old employer rollover — sits outside the model.
**Tags:** #k-nearest-neighbors #bert #gradient-boosting #k-means-clustering #evaluation-metrics #feature-engineering #data-integration #workflow-orchestration

## The Problem
A client has $80,000 with the platform. They also have $240,000 in a current employer's 401(k), a rollover IRA at a prior custodian, a joint brokerage account with a spouse, restricted stock units vesting over four years, and a mortgage.

The platform allocates the $80,000 as though it were the portfolio. In reality it is a quarter of one, and the advice that would actually help — asset location across tax treatments, concentration risk from employer stock, overall equity exposure, sequencing withdrawals, which account to contribute to next — requires the whole picture.

Aggregation exists and depends on the client connecting accounts, which many do not. Connections break when a custodian changes authentication, and reconnection prompts are ignored. Coverage is worst exactly where the largest balances sit, because workplace plan recordkeepers are among the hardest institutions to aggregate reliably.

Even when data arrives, it is thin. A connected 401(k) may report a balance and a set of fund names, without the holdings detail needed to compute the client's actual factor exposure, or the contribution and match structure needed to advise on it.

So the platform's advice is precise about a quarter of the problem and silent on the rest, and the client interprets the precision as completeness.

## What Already Exists
Plaid, MX, Yodlee and Finicity provide aggregation with varying coverage and reliability. Some platforms offer held-away advice or 401(k) management as a premium tier. Fund holdings data is available from Morningstar and similar providers. Open banking frameworks are slowly improving connection stability.

## The Customisation Gap
Fund-level look-through is inconsistently done. A connected account reporting fund names can be resolved to underlying holdings and factor exposures using public data, which is the difference between knowing a client has $240,000 in three funds and knowing they are eighty percent US large cap and heavily overlapping with the platform's own allocation.

Concentration risk from employer stock and vesting equity is barely addressed, and it is the single largest idiosyncratic risk in most affluent clients' portfolios — the person whose salary, bonus and largest asset all depend on one company.

Inference where connection fails is unexploited. Employer, age, income and contribution patterns visible in the platform's own transaction data support a reasonable estimate of workplace plan structure, and a stated estimate the client can correct is more useful than a blank.

And connection maintenance is passive. Which clients to prompt, when, and with what framing is an optimisation nobody runs, despite connection rate being the binding constraint on the entire advisory proposition.

## Impact If Solved
The platform's advice is only as good as its view of the client's position, and for most clients it sees a minority of it while presenting itself as an adviser. Fund look-through, concentration analysis, inference where connection fails and active connection maintenance extend the advice to the whole balance sheet, which is also the only credible path to charging more than a handful of basis points.
