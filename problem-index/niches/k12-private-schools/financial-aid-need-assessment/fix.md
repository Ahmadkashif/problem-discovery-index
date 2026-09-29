# Analysts Adjust for Circumstances the Formula Cannot See

**Niche:** [[niches/k12-private-schools/financial-aid-need-assessment/profile|Financial Aid Need Assessment Services]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Every family whose situation the formula handles badly gets a manual adjustment, and the pattern across thousands of them is never assembled.
**Tags:** #tacit-knowledge-ml #anomaly-detection #text-classification #worker-facing #data-integration

## The Problem
The methodology assumes a shape of family. A great many are not that shape: a parent whose income dropped after the tax year the return covers, a business owner whose paper income bears no relation to available cash, a family supporting a grandparent, medical costs the allowances do not reach, a divorce settlement that assigns tuition responsibility unusually.

Analysts handle these. They read the family's explanatory letter, apply judgment, and adjust — or flag the case to the school with a recommendation. Each resolution is sound, and each is made in isolation.

Nothing accumulates. The same circumstance recurs thousands of times a season and is reasoned about from scratch each time. Two analysts reach different adjustments on comparable facts. And the pattern across all of them — which is a precise map of where the methodology fails — is never assembled and never reaches the committee that revises it.

## Why It's Still Broken
The output format has no room for reasoning. The system stores the computed contribution and any override amount. Why the override was made lives in a free-text note or nowhere, and it is not retrievable by circumstance.

Season pressure makes it worse. Analysts are working through a queue against school deadlines, and recording the reasoning takes time that does not clear a file.

And methodology revision runs on a separate track. The committee that refines the formula works from principle, published research, and school feedback. The largest available evidence about where the formula struggles — the adjustments the company's own analysts make every season — is not part of the input.

## What a Fix Looks Like
Turn adjustments into a structured, aggregable record.

**Typed adjustment reasons.** A controlled vocabulary covering the recurring circumstances — income change since tax year, business income not available as cash, extraordinary medical, support of other dependants, unusual custody or tuition responsibility — with the amount and a short note. Seconds to enter, and it converts an isolated judgment into data.

**Precedent retrieval.** An analyst facing an unusual case should see how the organization has treated comparable ones, with the reasoning. This is the consistency fix and the training fix at once.

**Aggregate for the methodology committee.** Adjustment volume and magnitude by reason category is a quantified statement about which parts of the formula are systematically wrong, and it would replace anecdote in a revision process that currently has none.

**Track downstream outcomes by adjustment type.** With billing data available, the organization can see whether families whose contribution was adjusted for a given reason then enrolled and paid — which tells the committee whether the adjustment was right, not just common.

**Surface consistency gaps.** Comparable cases resolved differently by different analysts is a signal that exists in the data now and is never examined.

## Who Feels the Pain
Analysts, re-reasoning the same circumstances and unable to check their own consistency. The methodology committee, revising a formula without evidence about where it fails. Schools, receiving recommendations that vary by who processed the file. And families, whose award depends on which analyst read their letter.

## Impact If Fixed
The adjustments are the organization's most direct measurement of its own product's limits, generated free by trained staff every season and discarded. Capturing them makes awards consistent between families, gives the methodology an evidence base it has never had, and is built entirely from work that is already being done.
