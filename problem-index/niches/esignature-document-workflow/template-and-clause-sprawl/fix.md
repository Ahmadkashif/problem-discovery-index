# Nobody Knows Which Templates Are Used

**Niche:** [[niches/esignature-document-workflow/template-and-clause-sprawl/profile|Template & Clause Sprawl]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** A library of four hundred templates includes perhaps thirty in regular use, and because nobody reports usage, nobody will delete anything.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #k-means-clustering #quick-win #automation #compliance
**Contested on:** Every serious competitor in agreement content is fighting to guarantee that the clause in the document going out today is the one legal currently approves — and whoever can prove that across a whole library takes the legal operations account.

## The Problem
Legal operations wants to prune the template library. They cannot, because deleting a template somebody depends on is a visible failure and keeping a stale one is an invisible risk, and no report tells them which is which. So the library keeps growing, the search gets worse, users create new templates rather than find existing ones, and the ratio of live to dead content declines every quarter. Every envelope ever sent records the template it came from.

## Why It's Still Broken
Usage reporting on templates is an obvious feature that has not been built because template management is a secondary surface in every product and nobody's roadmap prioritises it. The reporting that exists is oriented to envelope volume and completion rather than to content provenance. And the asymmetry of consequence — visible failure for deleting, invisible risk for keeping — means that even where the data exists in raw form, nobody has the confidence to act without it being presented as an explicit recommendation.

## What a Fix Looks Like
Report usage, which requires no modelling. Envelopes sent per template over twelve months, by team and by user; last-used date; and completion rate by template, which is a bonus finding likely to show that some templates complete far worse than others for reasons worth investigating. Classify the library on that basis — active, occasional, dormant, dead — and propose archival rather than deletion for the dormant tail, since archival is reversible and is therefore an action people will actually take. Group near-duplicates and show usage across the group, which turns six variants into one keep-decision with evidence. Flag templates whose last edit predates the most recent approved clause revision, which is the risk list. And measure creation: how many new templates are created per month and how many of those are near-duplicates of existing ones, which quantifies the rate at which the problem is being made worse and is the argument for improving template search rather than only for pruning.

## Who Feels the Pain
Legal operations who cannot prune what they cannot measure; sales and deal desk users scrolling four hundred entries to find the one they need; and legal teams carrying unknown exposure in templates nobody has opened in two years.

## Impact If Fixed
Usage reporting is a query over data every platform already stores and is the single thing preventing anyone from acting on a problem they all recognise. Archival rather than deletion, plus duplicate grouping with usage attached, converts an unmakeable decision into a routine one.
