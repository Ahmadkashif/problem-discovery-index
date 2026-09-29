# Complete Records That Reason About Nothing

**Niche:** [[niches/web-data-extraction-firms/request-log-intelligence/profile|Request Log Intelligence]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firms hold complete records of every request they make and have built almost nothing that reasons about them, which leaves every operational and governance question in the business answered by intuition.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to turn a complete record of every request the firm makes into knowledge about targets, cost and risk — and whoever does that operates on evidence while everyone else operates on the last incident.

## The Problem
A firm decides whether to take on a customer wanting a new set of targets. The questions are whether those targets are hostile, how much collection will cost per useful record, how often they will break, what the compliance exposure looks like, and whether the fleet has capacity. Every one is answerable from the request logs of similar targets the firm already collects. Instead the answer is an account manager's impression and an engineer's guess, the work is priced on a standard rate, and the firm discovers the truth over the following quarter.

## Why Nobody Has Built This
Logs were built for billing and debugging, so the schema fits neither analysis nor governance. The questions span operations, finance, legal and sales, and no single function owns the corpus. Growth has been fast enough that unit-level understanding felt deferrable. And each question individually looks like a small analysis rather than a standing capability, so it is answered ad hoc and forgotten.

## What to Build
Make the log corpus a standing capability. Build a target intelligence profile per host — defensive posture and its trend, block rate by address type, structural volatility, breakage frequency, cost per useful record, terms and directive history — which is a direct aggregation of existing logs and is the asset every other function in the firm needs. Predict breakage from structural volatility and change history, so fragile targets are monitored more closely and customers are told what to expect. Model cost per useful record per target per customer, which the infrastructure fix note uses and which is the foundation for pricing anything correctly. Score collection risk from governance features — personal data presence, terms language, jurisdiction, customer purpose, target litigiousness — so the compliance reviewer starts with a ranking rather than a blank form. Forecast fleet capacity and target load, so growth is planned rather than absorbed. Detect defensive changes at a target early from block rate shifts, which the fix note develops. Feed target difficulty into quoting, so a hard target is priced as one. And publish an aggregate target difficulty reference to customers, which is genuinely useful to them and is a differentiator no competitor can copy without the same logs.

## Target Customer
Extraction firms and every function inside them, and the customers who currently discover a target's difficulty after committing.

## Impact If Built
Every operational and governance question in the business is answerable from logs that reason about nothing. A per-host target intelligence profile is a direct aggregation of existing data and is the shared asset that operations, finance, legal and sales all separately lack.
