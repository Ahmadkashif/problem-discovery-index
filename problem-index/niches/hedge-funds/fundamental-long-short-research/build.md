# The Firm's Own Research Is the One Corpus Nobody Can Search

**Niche:** [[niches/hedge-funds/fundamental-long-short-research/profile|Fundamental Long/Short Equity Research]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An analyst can search every filing, transcript and expert call ever published about a company in seconds, and cannot find what their own fund concluded about it eighteen months ago.
**Tags:** #large-language-models #transformers #word-embeddings #k-nearest-neighbors #evaluation-metrics #tacit-knowledge-ml #data-integration
**Contested on:** Every serious competitor in this niche is fighting to become the analyst's single research surface — filings, transcripts, expert calls, broker research and the fund's own prior notes searchable together — and whoever puts the fund's own research memory next to the external corpus takes the account.

## The Problem
A fund's most differentiated research asset is its own: years of notes, model versions, pitch memos, call annotations and post-mortems on positions. It is the only corpus no competitor can buy. It sits in a research management system with weak search, in personal OneNote files, in email threads with the PM, and in Excel files on a shared drive with names like "model_v7_final2.xlsx". When an analyst picks up a name again, or inherits it, the fund's prior thinking is effectively lost.

## Why Nobody Has Built This
External-content vendors are paid to aggregate content they can resell; the fund's internal corpus is not resellable and comes with confidentiality and MNPI sensitivity, so it sits outside their business model. Research management vendors built filing systems around note entry, not retrieval or reasoning. And funds have historically been reluctant to centralise analyst notes, partly for security and partly because analysts treat them as personal property.

## What to Build
A retrieval and reasoning layer over the fund's own research record that runs alongside, not inside, the external search tool. Index notes, model versions (with what changed between them), memos and annotated transcripts at passage level, attributed and dated. Answer questions in the analyst's terms — "what did we think about their pricing power last time margins compressed" — with citations to the firm's own material. Show prior theses on a name with their outcomes, so retrieval carries a track record. Respect information barriers: wall-crossed material and restricted names must be excluded by policy, not by convention. Deploy inside the fund's environment, since no fund will send its research record to a multi-tenant index.

## Target Customer
Directors of research and heads of research technology at fundamental long/short funds and multi-manager platforms with five or more years of accumulated research.

## Impact If Built
The firm's own past research becomes the first thing an analyst sees rather than the last thing anyone finds, which is the only research input that is genuinely proprietary and the one that most directly shortens the time to a differentiated view.
