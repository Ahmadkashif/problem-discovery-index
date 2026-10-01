# Credit Documents as Structured Data

**Niche:** [[niches/hedge-funds/credit-and-distressed-research/profile|Credit & Distressed Research]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A credit fund's edge sits in what its documents permit, and those documents are read one at a time and summarised in prose.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #feature-engineering #data-integration #automation
**Contested on:** This niche is not terminal — reading the documents of a performing credit portfolio for what borrowers are permitted to do, and anticipating how a restructuring or liability management exercise will treat each tranche, are different contests with different winners, stated separately in the sub-niches.

## The Problem
Every bond and loan a credit fund holds is governed by documents that define what the borrower can do: incur debt, move assets, pay dividends, designate unrestricted subsidiaries, amend with a simple majority. Analysts and in-house lawyers read them and write summaries. The summaries are prose, inconsistent across analysts, and not comparable across the book, so the fund cannot answer "which of our holdings permit a drop-down transaction" without re-reading.

## Why Nobody Has Built This
Specialist vendors produce covenant analysis on widely held credits, but private credit and smaller issues are not covered, and the fund's own interpretations — which encode its legal view — are not in any vendor product. The documents are long, cross-referential and negotiated, which defeated earlier extraction approaches.

## What to Build
Structured extraction of the terms that drive value — debt and lien capacity, restricted payments, investment baskets, unrestricted subsidiary provisions, amendment thresholds, sacred rights — into a comparable record per instrument, with every field linked to its clause. Diff amendments against the prior state. Let the fund's lawyers annotate interpretations so they persist. The specific contests for performing and distressed credit are developed in the sub-niches.

## Target Customer
Heads of credit research and in-house counsel at credit, distressed and multi-strategy funds.

## Impact If Built
Portfolio-level questions about document risk become queries rather than reading projects, and the fund's legal judgement accumulates instead of being re-derived.
