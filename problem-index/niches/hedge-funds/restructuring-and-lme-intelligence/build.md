# Recovery Waterfalls From Precedent, Not From Scratch

**Niche:** [[niches/hedge-funds/restructuring-and-lme-intelligence/profile|Restructuring & LME Intelligence]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every distressed situation gets a recovery model built from a blank spreadsheet, while hundreds of resolved restructurings sit unused as evidence.
**Tags:** #gradient-boosting #survival-analysis #k-nearest-neighbors #evaluation-metrics #tacit-knowledge-ml #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know, before the docket shows it, which creditor group is organising and how a restructuring or liability management exercise will treat each tranche — and whoever reads the documents and the creditor dynamics fastest prices the recovery.

## The Problem
A distressed analyst values each tranche by building a waterfall under scenarios — out-of-court exchange, LME, Chapter 11 plan — and assigning probabilities largely by experience. That experience is real tacit knowledge: senior distressed investors recognise how situations with a given sponsor, adviser set and document structure tend to resolve. It is not recorded, and the precedent set of resolved situations is not structured.

## Why Nobody Has Built This
Each restructuring is idiosyncratic and the sample of resolved cases is small, which discourages modelling. Data on outcomes is scattered across dockets, plan documents and news.

## What to Build
A structured precedent base of resolved restructurings and LMEs — capital structure, document features, sponsor, advisers, path taken, time to resolution, recoveries by class — and a retrieval layer that, for a new situation, surfaces the most similar precedents and their outcomes. Survival models for time to resolution. The analyst's scenario probabilities recorded alongside so they can later be compared with outcomes.

## Target Customer
Distressed and special-situations funds and the restructuring desks of multi-strategy funds.

## Impact If Built
Recovery analysis starts from evidence about how similar situations resolved, and the fund's distressed judgement becomes measurable and transferable.
