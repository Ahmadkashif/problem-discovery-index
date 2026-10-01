# Event-Study Practice for the First Take

**Niche:** [[niches/sell-side-equity-research/earnings-coverage/profile|Earnings Coverage]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Academic and quant finance have measured earnings-announcement reactions for decades; research departments do not apply the method to their own coverage.
**Tags:** #linear-regression #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to get a correct read of the print — which number the stock will trade on and whether the beat or miss is real — to clients before the open, and whoever does that best owns the morning call and the vote.

## The Problem
Whether a stock reacts to revenue, margin, a KPI or the guide is an empirical question with a standard answer method — the earnings-announcement event study — and quant teams on the buy side run it routinely. Sell-side analysts answer it by feel, per stock, each quarter.

## What Already Exists
Event-study tooling in academic and quant libraries; standardised unexpected earnings measures; vendor surprise datasets from LSEG, FactSet and S&P Global; buy-side quant research on post-earnings drift.

## The Customization Gap
Generic event studies use headline EPS and consensus. The department needs line-item surprise against its own estimate and against the guide, per company, with KPI definitions that change over time, on a sample of perhaps forty quarters per name — which needs pooling across similar companies and honest uncertainty. It must output a ranked, per-stock "what moves it" view inside the preview, not a research paper.

## Target Customer
Directors of research; quantitative research teams within brokers that already support fundamental analysts.

## Impact If Solved
A known, published method turned into a per-company decision aid, replacing the least reliable part of the analyst's tacit read with a measurable one.
