# The Narrative Written From Scratch

**Niche:** [[niches/crypto-exchanges/the-blockchain-analyst/profile|The Blockchain Analyst]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** Every report is a paragraph describing the same handful of patterns, retyped by an analyst who has written it two hundred times.
**Tags:** #large-language-models #worker-facing #quick-win #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to make one analyst's hour of hop-by-hop tracing produce a defensible conclusion instead of a narrative — and whoever gives them the tooling to work at the case level rather than the hop level changes what the function can cover.

## The Problem
The narrative section of a filing describes what was observed and why it is suspicious. The patterns recur — funds through a mixing service, rapid pass-through, structuring across deposits, a counterparty with a known characterisation — and the language is essentially fixed. The analyst retypes it, adapting amounts and dates, for every case. A significant fraction of a skilled person's week is spent producing prose whose structure never varies, and the quality drifts with fatigue.

## Why It's Still Broken
The narrative is a regulatory artefact and templating it felt like weakening it, so the writing stayed manual — the caution was reasonable and was never revisited once drafting became reliable. The evidence needed to draft it lives in the graph tool rather than in the filing system. Analyst time is not measured against output. And nobody assembled the recurring patterns into a taxonomy.

## What a Fix Looks Like
Draft from the evidence and let the analyst edit. Build the pattern taxonomy from the existing filings, which is the fix and is a straightforward reading of documents the exchange already holds. Draft the narrative from the case evidence with the analyst reviewing and signing, since the structure is fixed and the facts are structured. Pull amounts, dates, addresses and counterparty characterisations automatically, because transcription is where errors enter. Keep the analyst's judgement explicit and separate from the generated description, so the regulatory substance remains a person's. Flag the case that does not match a known pattern, as that is where the writing genuinely matters. Track narrative consistency, which reveals both drift and disagreement. Maintain the phrasing library centrally rather than in personal documents, since every analyst has their own and they diverge. Review drafts by sampling rather than universally, because that is how quality assurance works elsewhere and it is not applied here. Record which pattern each filing represents, which gives the function its first descriptive picture of what it actually sees. And measure drafting time, since it is a large, invisible and entirely addressable cost.

## Who Feels the Pain
Analysts spending their week retyping fixed prose; quality reviewers reading inconsistent narratives; and compliance functions whose capacity is consumed by transcription.

## Impact If Fixed
Templating a regulatory artefact felt like weakening it, and the caution was never revisited once drafting became reliable. The filings already contain the pattern taxonomy, and drafting from structured evidence returns a large share of a skilled week.
