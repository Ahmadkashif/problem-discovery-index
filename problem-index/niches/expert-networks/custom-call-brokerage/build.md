# The Match Nobody Grades

**Niche:** [[niches/expert-networks/custom-call-brokerage/profile|Custom Call Brokerage]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A network learns within an hour whether the expert it forwarded could answer the question, and records the answer as a billing event rather than a label.
**Tags:** #tacit-knowledge-ml #gradient-boosting #k-nearest-neighbors #causal-inference #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** This niche is not terminal — finding an expert for a fund that covers the same tickers every quarter and finding forty experts on a private target inside a two-week deal clock are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Each completed call carries its outcome with it: the client rated it, cut it short, disputed it, rebooked the expert, or asked for a similar person next week. Each forwarded profile carries the decision that produced it: the associate's search, the screener answers, the project manager's choice. The network holds both and does not join them, so nobody knows which screener questions predict a good call, which former employers produce knowledgeable experts on which topics, or which associates forward well.

## Why Nobody Has Built This
The business is run on speed and volume, and the metrics that reach management are calls completed and revenue per associate. A disputed call is resolved by client service as a credit and closed. Matching quality is assumed to be a property of experienced people, which is true and is also why it walks out the door. And the outcome labels are messy — a bad call can be the client's fault — which makes the measurement look harder than it is.

## What to Build
A decision-outcome record per call: the request, the candidate set, the screeners, the forward decision, the client's selection, and the outcome signals. Grade screener questions and sourcing paths against it. Train a fit model with explicit correction for which candidates were forwarded, and expose it as a rank and reason inside the associate's existing tool. Capture senior reviewers' judgement on a calibration sample so the model is measured against the people it is meant to help. Return per-associate outcome feedback, which needs no model at all.

## Target Customer
COO and head of operations at an expert network; heads of research operations at transcript platforms that host their own calls.

## Impact If Built
Matching quality is the variable that decides which network a client calls first, and it is currently managed by anecdote. Grading it against outcomes the network already observes turns the best project managers' instinct into a measurable, teachable asset.
