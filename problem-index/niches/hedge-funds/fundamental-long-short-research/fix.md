# The Pitch Memo Written After the Position

**Niche:** [[niches/hedge-funds/fundamental-long-short-research/profile|Fundamental Long/Short Equity Research]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** The formal write-up of a position is produced after the PM has already sized it, so the recorded reasoning is a rationalisation and the real reasoning is unrecorded.
**Tags:** #large-language-models #evaluation-metrics #hypothesis-testing #tacit-knowledge-ml #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to become the analyst's single research surface — filings, transcripts, expert calls, broker research and the fund's own prior notes searchable together — and whoever puts the fund's own research memory next to the external corpus takes the account.

## The Problem
Most funds require a pitch memo or thesis document for new positions. In practice the conversation that decides the trade happens verbally between analyst and PM, the position goes on, and the memo is written days later — often after the stock has moved — by an analyst who now knows part of the outcome. The memo describes a thesis that fits what happened. The falsifier, the catalyst date and the conviction at the moment of decision are rarely written down at all.

## Why It's Still Broken
Writing a memo before trading costs time the market does not give. PMs value speed over documentation, and nothing downstream uses the memo except compliance and the occasional post-mortem, so it is treated as paperwork.

## What a Fix Looks Like
Capture the minimum record at the moment of decision: a three-field thesis (why, what would change the view, by when) and a conviction score, drafted automatically from the analyst's most recent notes and the order ticket and confirmed in under a minute. Timestamp it against the trade. Let the full memo follow later, but keep the contemporaneous record immutable so it can be graded honestly.

## Who Feels the Pain
CIOs and risk managers who cannot tell skill from luck in their analysts; analysts whose good calls are indistinguishable from fortunate ones; and successors who inherit positions with no record of why they exist.

## Impact If Fixed
A contemporaneous, minimal thesis record is the precondition for every form of research grading, and it costs the analyst a minute per decision.
