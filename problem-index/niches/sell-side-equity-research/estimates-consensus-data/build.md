# Forty Years of Analyst Forecasts and No Model of Who Is Right When

**Niche:** [[niches/sell-side-equity-research/estimates-consensus-data/profile|Analyst Estimates & Consensus Data Providers]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendor holds every analyst's dated forecast on every line item alongside the reported result, and the consensus it sells is still mostly an average.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #feature-engineering #evaluation-metrics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to deliver the most accurate expectation of each reported line item before the release — and whoever does that best becomes the benchmark every earnings surprise is measured against.

## The Problem
Consensus is the expectation the market measures every result against. It is built from contributed estimates — each one dated, attributed to an analyst and broker, and later scored by the reported number. LSEG I/B/E/S has collected this since the 1970s; FactSet, Bloomberg and Visible Alpha hold comparable histories at increasing line-item depth.

Some of that history is used: LSEG's StarMine SmartEstimate already weights analysts by historical accuracy and recency at the EPS and revenue level. But the deeper pattern in the record is barely touched. Some analysts are reliably right on margins and wrong on revenue; some lead revisions after guidance and others follow; some are accurate when management guides conservatively and not when it does not. That is the sell side's tacit knowledge, expressed in data, and the vendor is the only party that holds it across every broker.

## Why Nobody Has Built This
Estimate vendors have been run as collection and normalisation businesses: the product is completeness and timeliness, and the content team is sized for that. Line-item model data at scale is recent. Contributor relationships make vendors cautious about publishing anything that reads as ranking a contributor's analysts. And per-company, per-line-item histories are short enough that naive analyst-level weighting overfits.

## What to Build
A line-item expectation model trained on the full point-in-time history: hierarchical estimates of each analyst's bias and skill by line item, sector, horizon and guidance regime; detection of leading versus following revisions; a guidance-bias profile per management team learned across all covering analysts; and calibrated distributions, not just a point, for every line item before every release. Sold as an enhanced consensus with published, out-of-sample accuracy against the simple mean.

## Target Customer
Head of Estimates Content or the estimates product leader at a consensus provider; the buyers behind them are quant funds, fundamental investors and corporate IR teams.

## Impact If Built
The benchmark every earnings surprise is measured against becomes measurably more accurate, and the vendor turns a commoditising collection business into a forecasting product built on a corpus nobody else can reproduce.
