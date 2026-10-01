# Reading Management Against the Analyst's Own Expectation

**Niche:** [[niches/asset-managers/fundamental-equity-research/profile|Fundamental Equity Research]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The valuable signal on an earnings call is the gap between what management said and what this analyst expected them to say, and no tool records the expectation.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #change-point-detection #evaluation-metrics #hypothesis-testing #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to capture and grade the analyst's read of management before the numbers confirm it — and whoever does that turns the most expensive judgment on the research floor into something the firm keeps when the analyst leaves.

## The Problem
During earnings season an analyst covering forty companies may face several calls a day. Vendor tools now summarise each call instantly — and identically for every subscriber. What the experienced analyst does that the summary does not is compare the call to her own model and her own memory: guidance language softer than last quarter, a KPI dropped from the prepared remarks, an answer to her own question from the last meeting that has changed. That comparison is the tacit skill, and it is formed in her head with no record.

## Why Nobody Has Built This
The expectation lives with the analyst, not in any document, and vendors build products from data they can access across all clients. Capturing it requires a workflow change on the research floor. And grading reads of management is confounded by everything else that moves a stock.

## What to Build
A pre-call expectation capture — a few structured fields per company from the analyst's model and notes, auto-proposed and confirmed in a minute — followed by a post-call comparison that ranks language and metric shifts against both the prior period and the recorded expectation. A ninety-second post-meeting rating of credibility and direction of change accumulates into a labelled history per company and analyst. Over time, a model learns which flagged shifts senior analysts treat as material, and an event study tests whether they precede estimate revisions. The data collection, labelling and deployment difficulties are the ones set out in the industry's machine-learning note, and the design must respect them: never record restricted meetings, measure analysts' agreement with their own past ratings before trusting labels, and deliver flags before the morning meeting or not at all.

## Target Customer
Directors of equity research and heads of equities at active managers.

## Impact If Built
The firm's interpretive edge becomes a recorded, testable asset rather than a property of individual analysts, and junior analysts see what seniors notice on every call.
