# Two Files and Two Assertions

**Niche:** [[niches/digital-goods-marketplaces/the-copyright-reviewer/profile|The Copyright Reviewer]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reviewer decides copyright and originality questions at volume, between two creators who both claim the work, on evidence consisting of two files and two assertions.
**Tags:** #worker-facing #contrastive-learning #graph-theory #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #transformers
**Contested on:** Every serious competitor in this niche is fighting to give the copyright reviewer evidence about which file came first and what was derived from what — and whoever supplies that turns an unanswerable adjudication into a determinable one.

## The Problem
Two listings are similar. One creator says the other copied them. The other says they made it independently, or that both derive from a common source, or that the accuser copied them. The reviewer has both files, both upload dates on this platform, and two paragraphs of assertion. They must decide within minutes whether to remove someone's listing and a portion of their income. There is no record of which existed first anywhere else, no analysis of whether one is structurally derived from the other, and no way to see that the same accuser has filed nineteen similar claims this month.

## Why Nobody Has Built This
Copyright adjudication is legally fraught and platforms prefer process compliance over substantive determination, which keeps the tooling minimal by design. The evidence that would settle most cases sits outside the platform. Structural comparison for templates, fonts and design files is unbuilt, because the tooling that exists targets images, audio and code. And review quality has no metric.

## What to Build
Give the reviewer determinable evidence. Establish priority from everything observable — upload history across marketplaces, web appearances, creator portfolios, file-embedded metadata and creation timestamps — which resolves a large share of cases outright and is the highest-value single component. Perform structural comparison appropriate to the asset type, since layer structure, glyph outlines, node graphs and parameter sets reveal derivation far more reliably than visual similarity and are the evidence nobody currently produces. Distinguish derivation from common ancestry, because both parties drawing on the same source is an extremely common and currently misjudged situation. Surface the accuser's and respondent's claim histories, as a party with a pattern of claims or of infringement is important context and is invisible today. Show a creator's own development history where recorded, which connects to the provenance work and is the single most convincing exculpatory evidence there is. Recommend an outcome with confidence and reasoning while leaving the decision human, since these determinations are consequential, contested and frequently genuinely ambiguous. Auto-resolve the clear cases — exact copies with unambiguous priority — which are a large share of the queue and consume reviewer attention that the hard cases need. Give both parties a structured route to submit evidence, rather than a free-text box. Record the decision, its basis and its outcome to build precedent, which is how consistency emerges in practice. And measure reversal rates rather than throughput, because a wrong determination here ends someone's livelihood.

## Target Customer
Trust and safety operations at digital goods marketplaces, the reviewers themselves, and creator communities whose originality disputes are currently arbitrated on assertions.

## Impact If Built
The decision removes a person's income and is made on two files and two assertions. Cross-platform priority evidence resolves a large share of cases outright, and structural comparison of layers, glyphs and node graphs is the derivation evidence no tool currently produces.
