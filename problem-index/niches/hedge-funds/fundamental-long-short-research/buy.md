# Enterprise Search Meets the Research Record

**Niche:** [[niches/hedge-funds/fundamental-long-short-research/profile|Fundamental Long/Short Equity Research]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise retrieval tools are mature and generic; a hedge fund's research record needs security-aware, time-aware, position-aware retrieval that generic tools do not provide.
**Tags:** #large-language-models #word-embeddings #transformers #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to become the analyst's single research surface — filings, transcripts, expert calls, broker research and the fund's own prior notes searchable together — and whoever puts the fund's own research memory next to the external corpus takes the account.

## The Problem
Funds that try to make their internal research searchable usually start with a general enterprise search or retrieval-augmented generation product. It indexes documents, answers questions, and fails in ways specific to investment research: it returns a note from five years ago as if it were current, ignores which analyst wrote it, cannot distinguish a thesis from a meeting summary, and has no concept of an information barrier.

## What Already Exists
Enterprise search and RAG platforms (Microsoft Copilot over SharePoint, Glean, Elastic), the external research platforms' own "upload your documents" features, and research management systems with keyword search.

## The Customization Gap
The vertical adaptation needs: time-awareness, so retrieval prefers the most recent view and shows how it evolved; position-awareness, linking each document to the fund's holdings and sizing at the time; document-type awareness, separating theses, model changes, call notes and post-mortems; Excel model diffing, since the model is where much of the reasoning lives; and compliance controls that enforce restricted lists and wall-crossings at query time with an audit trail.

## Target Customer
Heads of research technology and CTOs at funds with an internal engineering team willing to adapt a platform rather than buy a finished product.

## Impact If Solved
A customised retrieval layer converts an existing enterprise licence into a research tool analysts actually use, at a fraction of the cost of building from scratch.
