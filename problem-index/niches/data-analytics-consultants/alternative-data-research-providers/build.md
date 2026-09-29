# Estimate Error History as the Coverage Engine

**Niche:** [[niches/data-analytics-consultants/alternative-data-research-providers/profile|Alternative Data Research Providers]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every estimate is settled by the company's own earnings release within weeks, which makes this the most cleanly resolvable forecasting business in the vault — and the error history is not maintained as an asset.
**Tags:** #time-series-forecasting #gradient-boosting #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #feature-engineering #change-point-detection #data-integration #revenue-impact

## The Problem
The product is a number for a company's quarter, published before the company reports it. Weeks later the company reports and the estimate is settled exactly. Across hundreds of covered names and multiple quarters a year, the firm generates a dense, unambiguous accuracy record and does not maintain it as an analytical asset. Error is looked at anecdotally when a miss is large enough to draw client complaints. What is not done is systematic: decomposing error by name, sector, panel source, coverage tenure, and estimate horizon, so the firm knows where it is reliable and where it is guessing; identifying which panel signals actually carry information for which business models; and detecting the point at which a name's mapping has degraded, which happens routinely as companies change their mix, their channel, or their reporting definitions.

## Why Nobody Has Built This
Estimates live in a publishing system as current values with revision history kept for audit rather than analysis, so reconstructing what was published when is possible and awkward. Attribution of error is also genuinely hard — a miss can come from panel drift, a mapping that stopped holding, a company reporting change, or a genuine surprise, and separating them requires structure nobody has built. And the commercial instinct in a research business selling to investors is to emphasize wins, which has meant the error record exists only as whatever clients happen to remember.

## What to Build
An error attribution system treating every published estimate as a resolvable claim. Estimates are versioned with the panel data, mapping, and adjustments that produced them; resolution is automatic on the earnings release; and error is decomposed into its sources — panel coverage change, mapping degradation, definitional change at the company, and irreducible surprise. That decomposition is the whole point, because the four call for completely different responses and are currently indistinguishable. On that foundation the firm gains capabilities it lacks entirely: coverage prioritization driven by measured reliability rather than by client request, early detection of mapping degradation before it produces a public miss, calibrated confidence published with every estimate — which sophisticated clients value more than a marginally tighter point — and a demonstrable track record, which in a market where every provider claims accuracy is the only defensible commercial claim.

## Target Customer
Heads of research and chief data officers at alternative data providers running 200-1,000 analysts, and the portfolio managers who position on these estimates and reconstruct provider accuracy themselves, badly, from memory.

## Impact If Built
Turns the industry's cleanest feedback loop from an anecdote into an instrument. Because resolution is automatic and fast, the record compounds every quarter and cannot be replicated by a competitor without the same coverage history — which makes it the most durable asset available in a segment where panel access is increasingly contested and rarely exclusive for long.
