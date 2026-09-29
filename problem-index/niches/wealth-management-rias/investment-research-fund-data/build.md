# Ratings Published for Forty Years and Scored by Everyone Except the Publisher

**Niche:** [[niches/wealth-management-rias/investment-research-fund-data/profile|Investment Research & Fund Data Providers]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has issued ratings on funds for decades against a complete performance record, and the definitive studies of whether those ratings predict anything are written by academics.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals

## The Problem
The product is a judgment: this fund belongs in this category, against this benchmark, with this risk profile, and it is worth this rating. Advisers build recommended lists from it, investment committees minute it, and money moves on it.

The outcome is observable in complete detail. Every rated fund's subsequent performance is recorded daily, forever, in the firm's own database. There is no ambiguity about what happened, no censoring problem beyond fund closure, and no delay.

The comparison is made — but largely by other people. The academic literature on whether fund ratings predict future performance is substantial and its conclusions are mixed to unflattering. Vendors publish periodic self-studies. What does not exist is a standing, methodologically serious performance record of the firm's own analytical output — by rating grade, category, time horizon, market regime and analyst — reported the way any other forecaster would be required to report.

Two related gaps sit alongside it. Categories are constructed by classification rules and revised by committee, and a fund's category determines its peer group, its percentile rank and often its rating — yet how well a category actually groups funds that behave alike is a testable property that is not routinely tested. And the risk statistics that populate every fact sheet are historical descriptions presented in a context where readers treat them as forward-looking, with no accompanying statement of how stable they have been.

## Why Nobody Has Built This
The rating is the brand. A firm that published a rigorous accounting of its own predictive performance would be handing every competitor and every sceptical adviser a citation, and the plausible finding — that ratings predict weakly, as the literature generally suggests — is commercially unwelcome even though everyone in the industry half-believes it already.

There is also a defensible methodological argument that fund ratings were never meant as return forecasts, that they describe past risk-adjusted performance and process quality, and that scoring them as predictions misreads the product. That argument is genuine and it has been allowed to preclude asking the question in the form the users actually understand the rating in.

And the analytical output is heterogeneous — quantitative star-type ratings, qualitative analyst ratings, category assignments — with different intents and different horizons, which makes a single scorecard harder to design than it looks.

## What to Build
A forecast performance system, treated as a research asset rather than a disclosure risk.

**Archive every published judgment.** Rating, category, benchmark, date, analyst, and the inputs at the time. Much of this exists in the historical database and needs assembling into a decision record rather than a state snapshot.

**Score with proper methods.** Rank correlation between rating and subsequent risk-adjusted return, by horizon and by cohort; survivorship handled explicitly, since closure and merger are the most common fates of poorly rated funds and ignoring them flatters everyone.

**Test the categories.** Within-category dispersion against between-category dispersion, and how often a fund's category assignment changes. A category whose members do not behave alike makes every percentile rank in the product misleading, and this is directly measurable.

**Model rating changes as events.** Upgrades and downgrades are dated interventions with observable subsequent flows and returns. That is a clean event study, it is the strongest evidence available about whether the analysis carries information, and it can be run today.

**Report stability, not just level.** Risk statistics presented with how much they have historically moved is a small product change with a large effect on how they are read.

**Publish, on the firm's own terms.** In a market where fund selection is under permanent fee pressure and passive alternatives compete on cost, the vendor that reports measured predictive value first sets the terms of the argument instead of answering it.

## Target Customer
Chief Research Officer or Head of Methodology at an investment research and fund data provider. The strategic argument is that fund data itself is commoditising, ratings are the differentiated product, and their value has never been established by the firm that sells them.

## Impact If Built
Fund ratings and categories shape the allocation of trillions of dollars of retail and advised assets, and the evidence about whether they help is written mostly by outsiders. A rigorous, published forecast record — including honest category diagnostics — would either establish the analytical franchise on demonstrated value or redirect it toward the parts that demonstrably work, and the data to do it has been sitting in the firm's own database for decades.
