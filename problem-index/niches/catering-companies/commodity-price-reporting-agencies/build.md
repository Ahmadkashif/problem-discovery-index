# The Assessment Record Behind Every Published Price

**Niche:** [[niches/catering-companies/commodity-price-reporting-agencies/profile|Food Commodity Price Reporting Agencies]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contracts worth billions settle on a number a reporter assessed from a dozen phone calls, and the calls, the trades cited, and the reasoning that produced the number are not recorded anywhere retrievable.
**Tags:** #large-language-models #bert #transformers #word-embeddings #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #tacit-knowledge-ml #compliance #data-integration

## The Problem
A price assessment is a judgment, not a calculation. In markets with no exchange, a reporter spends the day talking to buyers and sellers, hears about trades and bids and offers of varying reliability, discounts what is stale or self-serving, weighs volume against representativeness, and publishes a number. Everything supporting that judgment — which trades were cited, which were discounted and why, how thin the day was, how much the reporter's own read moved the figure — exists as notes in a personal system or not at all. The published number becomes a contract settlement price. When a subscriber challenges it, or a regulator asks how it was formed, or a new reporter inherits the market, the record is a number and a memory. For a business whose entire value is the credibility of its judgment, that is a remarkable position to be in.

## Why Nobody Has Built This
The practice grew out of a trade-press tradition where the reporter's word was the product and documentation was neither expected nor, under a daily deadline, affordable. Sources also speak on the understanding that their information is not attributable, which makes any capture system a confidentiality question before it is a technical one. And the market's structure works against it: reporters compete on the depth of their contacts, so a system that makes their sourcing visible internally can read as surveillance of the person whose network is the asset. Those objections have kept a genuinely valuable record from ever being assembled.

## What to Build
An assessment record captured as a by-product of the reporting day rather than as documentation after it. Each assessment carries the inputs the reporter actually used — trades, bids, offers, with volume, counterparty type, and reliability weighting, held under access controls that preserve source confidentiality — plus the discounting decisions made, an explicit liquidity indicator for the day, and the reasoning where the published figure departs from what the raw inputs would suggest. Costing the reporter almost nothing is the design constraint; anything that adds meaningfully to a deadline day will not be used. Once the record exists, several things follow that are impossible today. Assessments become defensible on demand, which matters increasingly as commodity benchmarks come under regulatory attention. Liquidity becomes a published property, so subscribers know when a quotation rests on three trades rather than thirty — information they currently have no way to obtain and would price against. Consistency between reporters covering adjacent markets becomes measurable. And the accumulated record becomes the training material a new reporter learns from, rather than sitting beside a senior one for two years.

## Target Customer
Editors-in-chief and heads of market reporting at price reporting agencies running 50-250 reporters, and the compliance functions now facing benchmark governance expectations imported from energy and financial price reporting.

## Impact If Built
Converts the agency's core product from an assertion into an evidenced assessment, which is the direction regulatory scrutiny of commodity benchmarks has moved everywhere it has arrived. It also addresses the succession problem that quietly threatens every price reporting agency — market expertise concentrated in individuals with no institutional record of how they exercise it.
