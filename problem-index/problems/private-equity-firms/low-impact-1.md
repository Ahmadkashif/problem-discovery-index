# IC Memo Assembly From the Data Room

**Industry:** [[private-equity-firms|Private Equity Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic AI document tools can summarise a data room; none of them writes the firm's own investment committee memo with every figure tied back to the QoE, the model and the source document.
**Tags:** #large-language-models #transformers #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration #automation

## The Problem
Every deal that reaches final investment committee produces a memo of 30–80 pages: thesis, business overview, market, customers, financials and adjustments, quality-of-earnings findings, model and returns cases, value creation plan, risks and mitigants, diligence summary by workstream. The deal team writes it in the final two weeks of exclusivity while diligence reports are still arriving, and rewrites the financial sections every time the QoE provider revises adjusted EBITDA or the model changes. The figures appear in a dozen places and must agree with each other, with the model and with the QoE report — and frequently do not, which is what IC members catch first.

## What Already Exists
LLM research tools — Hebbia, Rogo, AlphaSense's generative search, Microsoft Copilot over SharePoint — can read a data room and answer questions or draft summaries. VDR vendors such as Datasite have added AI-assisted indexing and redaction. Document automation tools (Macabacus, UpSlide) link Excel ranges into PowerPoint and Word.

## The Customisation Gap
The memo is not a summary; it is the firm's argument in the firm's template, and its credibility rests on internal consistency. The customisation needed is specific: the firm's own section structure and IC's known preferences (what this IC always asks about churn, or about add-on pipeline); a reconciliation layer that ties every number in prose to a named cell in the current model version and a page in the QoE report, and flags when either moves; carry-forward of the firm's prior memos in the same sector so the market section starts from what the firm already believes rather than from a blank page; and a diligence tracker that knows which findings from which provider are still outstanding. Generic tools answer questions about documents; the gap is a memo that stays true while its sources change underneath it.

## Impact If Solved
Deal teams spend a large share of their last fortnight before signing on assembly and reconciliation rather than judgement, and IC time is spent catching inconsistencies. A memo that is wired to its sources removes the most error-prone manual step in the deal process and gives IC a document whose numbers can be trusted on first read.
