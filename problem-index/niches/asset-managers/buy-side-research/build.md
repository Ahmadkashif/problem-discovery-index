# A Research Floor With No Research Record

**Niche:** [[niches/asset-managers/buy-side-research/profile|Buy-Side Research]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An active manager spends tens of millions a year on research and keeps no event-level record of what its analysts concluded, when, and whether they were right.
**Tags:** #large-language-models #causal-inference #evaluation-metrics #confidence-intervals #data-integration #tacit-knowledge-ml #revenue-impact
**Contested on:** This niche is not terminal — an equity analyst forecasting upside from management and a credit analyst underwriting downside from documents are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Ask a director of research which of her analysts' recommendations over the past five years outperformed, and the honest answer is usually an impression. The recommendations exist — in a research management system for some analysts, in morning-meeting emails and model tabs for others — but they are recorded as current state (today's rating, today's target) rather than as dated events, and they are not joined to the PM's actions or to returns. The firm's performance system can attribute every basis point of portfolio return; nothing attributes it to the research that motivated the position.

## Why Nobody Has Built This
Research management systems were sold as note-taking and workflow tools, not as measurement systems, and analysts resist anything that looks like a scorecard. The data needed spans three systems with three owners: research, the order management system, and performance. Measurement done naively — raw returns on recommendations — rewards sector luck and is rightly rejected by the floor, which has given the whole idea a bad reputation.

## What to Build
An event ledger first: every recommendation, rating change and target price as a dated event with the analyst, the rationale text and the cited evidence, backfilled from emails and notes with language-model extraction and confirmed by the analyst. Join it daily to holdings and trades, so each event carries the PM's response, and to factor-adjusted returns, so each carries an outcome net of style and sector. Report hit rates per analyst, sector and recommendation type with confidence intervals wide enough to be honest — most individual records are too short for strong claims, and saying so is what earns trust. Then layer search over the whole record, so the firm can ask what it believed and why at any point in time. The two sub-niches specialise this differently for equity and credit.

## Target Customer
Directors of research and CIOs at active long-only managers with twenty or more analysts.

## Impact If Built
The firm gains evidence for the one claim it sells — that its research adds value — and the means to direct research budget, PM attention and analyst development by measured contribution rather than reputation.
