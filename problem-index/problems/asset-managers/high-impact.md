# The Analyst's Judgment That Leaves With the Analyst

**Industry:** [[asset-managers|Asset Managers]]
**Type:** High Impact
**One-liner:** A buy-side analyst's read of a management team, a covenant or an industry — built over hundreds of meetings — is recorded as loose notes, never graded against what happened, and walks out of the door at resignation.
**Tags:** #large-language-models #transformers #gradient-boosting #causal-inference #evaluation-metrics #tacit-knowledge-ml #data-integration #revenue-impact

## The Problem
A senior equity analyst at a long-only manager covers forty companies. In a year she sits through two to three hundred management meetings, earnings calls, site visits and broker-hosted conferences. Over a decade she develops something the firm is in practice paying her for: she can tell when a CFO is managing guidance down to beat it, when a new CEO's "strategic review" means a write-down is coming, when a capital allocation story has quietly changed between investor days. A credit analyst at the same firm reads a new issue's offering memorandum and knows, before running the numbers, that the restricted-payments basket is wider than the market is pricing.

That judgment reaches the portfolio as a recommendation, a target price or an internal rating, and a paragraph of rationale. The meeting notes behind it sit in FactSet RMS, Bipsync or Tamale if the analyst is disciplined, in OneNote or a notebook if not. The PM acts on the recommendation, partially acts, or ignores it, and the reason is rarely written down. Prices then move.

Nobody joins the three. The firm does not know which analysts' upgrades are followed by outperformance, which kinds of meeting changed a view in a direction that turned out right, or whether the PM's habit of ignoring one analyst's sells has cost or saved money. When the analyst leaves for a competitor — and buy-side turnover is a constant — the successor inherits a coverage list and a folder, not a judgment.

## Why It's Unsolved
This is tacit knowledge in the strict sense, and it carries all three of the hard parts.

**Data collection.** The signal is generated in conversations the firm does not record — compliance policies often prohibit recording management meetings, and expert-style calls carry their own restrictions. What is captured is the analyst's written summary, which is already a compression of the judgment, written at varying length and discipline. Earnings call transcripts are available for every listed company, but the analyst's read of a call is the delta between what was said and what she expected, and the expectation is never written down.

**Labelling.** The ground truth is noisy and delayed. A view on management credibility might be vindicated in two quarters or two years, and the stock price mixes the analyst's insight with everything else that happened. Analysts disagree with their own past selves: asked to re-rate an old meeting with the outcome hidden, an analyst frequently gives a different score. And the most valuable calls — avoiding a blow-up — are rare events.

**Deployment.** A PM will not read a model output that tells him an analyst is wrong; he will read one that saves him time before a meeting. Any system must be faster than walking to the analyst's desk, must never surface material non-public information across an information barrier, and must survive the cultural objection that investment judgment cannot be measured — an objection that has protected the absence of measurement for decades.

## What a Solution Looks Like
Start with a recommendation ledger, not a model: every recommendation, rating change and target price, timestamped, with the analyst, the rationale text, the meetings and documents cited, and the PM's response, joined daily to subsequent returns. That alone gives each analyst and PM a graded record, and most firms have never seen one.

On top of it, capture the tacit layer structurally. After each management meeting, a short structured prompt — credibility, change versus last meeting, what would change the view — takes the analyst ninety seconds and turns prose into a labelled time series. Language models then read transcripts and the analyst's own notes together to flag where management language has shifted against the analyst's recorded expectation, which is the pattern the best analysts notice and newer ones miss.

The successor analyst inherits a coverage history with what the predecessor believed, why, what would have changed it, and how each call turned out — searchable, citeable, and scoped by information barrier.

## Impact If Solved
The research floor is the most expensive department in an active manager and the only one whose output has never been measured at the level of the individual decision. A recommendation ledger with tacit-signal capture converts analyst turnover from a loss of franchise into a handover, gives PMs evidence for how much weight each analyst's call deserves, and gives the firm the one thing it cannot currently give a consultant: proof that its research adds value beyond the index it is benchmarked against.
