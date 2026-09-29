# History: Robo-Advisors

**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** [[origins/exchanges-market-makers/profile|Exchanges & Market Makers]]
**Episode Tier:** 1
**Transferable Pattern:** Automating the 99% of a relationship that is mechanical does not remove the 1% that is not — it just concentrates it, unstaffed for, on the one day a year it actually happens.

## Before

Portfolio management was an advisor's business, priced as a percentage of assets (typically 1–2% a year) that only made sense once an account held enough money to be worth a human's ongoing attention. Below that threshold — the mass affluent, the young professional starting a Roth IRA — advice was either unavailable or delivered as a one-time sale of a mutual fund. This is the same arithmetic [[series/eras/wave-06-cloud-saas|Wave 6]] describes for a twelve-person dental practice: the fixed cost of serving a customer had to be amortised across a large account, so small accounts were not reachable, not badly served.

Underneath that commercial constraint sat a cost structure [[origins/exchanges-market-makers/legacy|this origin's legacy file]] traces directly: before decimalisation (2001) and the ECN-driven collapse of dealer spreads, trading was not cheap enough, per dollar managed, to justify frequent small rebalancing trades on a small account. A low-fee, automatically-rebalanced product for a $500 account was not a strategic choice anyone declined to make. It was arithmetically impossible until the spread-compression fight this origin's founders fought was substantially over.

## The Origin Event

Two companies, founded the same year, for different reasons, are this industry's origin. **Betterment** was founded in 2008 by Jon Stein and Eli Broverman, formally organised as a Delaware LLC on 7 April 2009, and launched publicly at TechCrunch Disrupt New York in mid-2010 — where it was named the event's "Biggest New York Disruptor" and signed up nearly 500 users within a day. **Wealthfront** was also founded in 2008, by Andy Rachleff and Dan Carroll, but started as "kaChing," a mutual-fund social-analysis platform, before pivoting to automated portfolio management. Wealthfront launched tax-loss harvesting for accounts over $100,000 in **December 2012** and extended it to smaller accounts via **direct indexing in 2013** — buying the individual securities inside an index rather than the index fund itself, so losses can be harvested security by security.

Neither company invented what it automated. **Harry Markowitz published "Portfolio Selection" in the Journal of Finance in March 1952**, establishing the mean-variance framework — trading expected return against variance — that underlies every robo-advisor's asset allocation; he shared the **1990 Nobel Memorial Prize in Economic Sciences** with Merton Miller and William Sharpe for it. Tax-loss harvesting is a decades-old feature of the US tax code, long used manually by institutional and high-net-worth managers. **The industry's genuine invention was not the technique. It was making both techniques run unattended, continuously, on an account with no advisor assigned to watch it.**

## What Became Cheap

Two things fell to near-zero at once, and the industry only exists because both did. Trading costs collapsed first, for reasons this vault's origin file for exchanges and market makers documents at length — one-cent tick sizes, sub-basis-point execution, decimalisation. Then, seven years into that trend, [[series/eras/wave-06-cloud-saas|cloud infrastructure]] collapsed the fixed cost of running a compliant, licensed advisory business at all: no branch, no in-person onboarding, a six-question form standing in for what a human advisor would have spent an hour asking.

## How It Was Actually Solved

The mechanism is genuinely elegant and genuinely narrow. A client answers a short risk questionnaire once, at signup. The platform maps the answer to a point on an efficient-frontier glide path, buys a low-cost ETF portfolio at that point, and then runs two automated loops continuously: a drift-band rebalancer that trades back toward target weights as markets move, and a tax-loss harvester that sells positions at a loss and replaces them with a correlated but not "substantially identical" holding, banking the loss against the client's tax bill while respecting the IRS's 30-day wash-sale rule. Both loops are genuinely automated and genuinely well-built. Both are also **blind outside the platform's own four walls** — a wash sale triggered by a trade in a spouse's account at a different broker, or in a workplace 401(k) the platform cannot see, silently invalidates a harvested loss the platform will still report as banked.

## The Contest — an ambiguous outcome

The visible fight was Betterment against Wealthfront: who reached account minimums lower, who shipped tax-loss harvesting first (Wealthfront, December 2012), who scaled faster. That fight never produced a clear winner, because a second, larger contest overtook it. **Vanguard launched a digital advisor in 2020; Schwab Intelligent Portfolios had been marketed since at least March 2015; Fidelity Go followed.** None of these firms needed to win new assets to compete — they already held them. Vanguard reported **$13.3 trillion in group assets under management in 2025**; Schwab reported **$11.9 trillion (2025), $10.10 trillion at the end of 2024**. Betterment reported **roughly $56 billion in 2025, growing past $70 billion by mid-2026**; Wealthfront reported **approximately $95 billion by May 2026**. Set against the incumbents' totals, the pure-play robo-advisors are smaller by two orders of magnitude — though that comparison is necessarily inexact, since Vanguard and Schwab do not break out their standalone digital-advice product's assets from the rest of their business, and this file cannot resolve that ambiguity cleanly.

The clearest single data point cuts against a tidy story either way. **UBS agreed to acquire Wealthfront for $1.4 billion in January 2022** — a major incumbent paying up for the pure-play model — and then the deal was **mutually terminated in September 2022**, with UBS instead placing $69.7 million into convertible notes at the same valuation. Wealthfront went on to **complete an IPO on Nasdaq in December 2025**, raising about $485 million at a roughly $2.6 billion valuation. Nobody bought the category outright. Nobody was starved out of it either. **Vanguard's own August 2026 acquisition of the direct-indexing and rebalancing platform Altruist, reported at $4 billion, is the same incumbents-buy-in pattern continuing in real time, unresolved, as this file is being written.**

## The Trade-Off

The entire cost structure depends on the interactions that matter most being the ones automation handles worst. Rebalancing and harvesting run untouched for years. Then a market falls sharply, and the same clients whose risk tolerance was captured once, at signup, in six questions, call in during the exact week the platform's small licensed advisory staff is least able to absorb the volume — precisely the worker-life pattern this vault's own hub note for the industry names. A platform can automate the routine 99% of a financial relationship or staff for the consequential 1%. Building for both at once, at the price point the category is sold at, has not been demonstrated by anyone in this file's research.

## What's Still Open

- [[problems/robo-advisors/high-impact|🔴 High Impact: Risk Tolerance Assessed Once and Never Validated]]
- [[niches/robo-advisors/risk-tolerance-measurement/profile|Risk Tolerance Measurement]] and [[niches/robo-advisors/outcome-measurement/profile|Outcome Measurement]] — the questionnaire against the behaviour the platform already recorded
- [[niches/robo-advisors/drawdown-intervention/profile|Drawdown Intervention]] — the trade-off above, as a live operating problem
- [[niches/robo-advisors/tax-loss-harvesting/profile|Tax-Loss Harvesting]] and [[niches/robo-advisors/held-away-assets/profile|Held-Away Assets]] — the wash-sale blind spot
- [[niches/robo-advisors/supervision-at-scale/profile|Supervision at Scale]]
- [[niches/robo-advisors/the-licensed-associate/profile|The Licensed Associate]] and [[niches/robo-advisors/the-small-balance-client/profile|The Small-Balance Client]]
- [[niches/robo-advisors/transfers-and-funding/profile|Transfers & Funding]]

## The Transferable Pattern

> **The algorithm was never the moat.** Mean-variance optimisation is seventy years old and public. Tax-loss harvesting is a feature of the tax code, not a trade secret. What a pure-play robo-advisor actually built was operational: running both, unattended, cheaply, for an account too small to have justified a human's time. That is a genuine and valuable thing to build — and it is also exactly the kind of capability a trillion-dollar incumbent with existing distribution and existing trust can absorb once the category has proven the model works.

An FDE should ask, of any "algorithmic" product built on a public, decades-old technique: what is actually being sold — the technique, or the willingness to run it automatically for a customer nobody else would have bothered serving? The second is defensible for a while. It is rarely defensible against the party that already had the customer.

**Sources:** Wikipedia, *Betterment (company)*, *Wealthfront*, *Modern portfolio theory*, *Portfolio optimization*, *Harry Markowitz*, *Vanguard Group*, *Charles Schwab Corporation*; this vault's `industries/robo-advisors.md` and `origins/exchanges-market-makers/legacy.md`.
