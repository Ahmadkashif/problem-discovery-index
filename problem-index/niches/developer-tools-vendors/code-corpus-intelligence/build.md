# The Record of How Software Is Written

**Niche:** [[niches/developer-tools-vendors/code-corpus-intelligence/profile|Code Corpus Intelligence]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platforms observe how software is actually written across millions of developers and use that record to render diffs and draw contribution graphs.
**Tags:** #graph-theory #survival-analysis #gradient-boosting #k-means-clustering #causal-inference #evaluation-metrics #confidence-intervals #hypothesis-testing
**Contested on:** Every serious competitor that gets here is fighting to turn the record of how software is actually written across millions of repositories into a product — and whoever does it holds the only dataset from which the category's central question could be answered.

## The Problem
The industry argues continuously about practice: whether small changes are better, whether review latency matters more than review depth, whether a particular dependency is a liability, whether test coverage predicts anything, whether the assistant helped. Each argument is conducted with anecdote and conviction. The evidence that would settle several of them — millions of changes with their review histories, their subsequent modifications, their defect associations and their eventual fate — is held by a handful of vendors who use it to display a diff.

## Why Nobody Has Built This
Cross-customer analysis of source code is the most sensitive proposal a code host could make, and no vendor has done the work to define a form of it that customers would accept, so it is avoided entirely rather than designed carefully — even though metadata and structural analysis with no content would answer most of these questions. The analysis also requires causal design rather than correlation, and the obvious correlational versions are misleading enough to be worse than silence. And the vendors' commercial instinct is to sell seats and storage, where the value is obvious and the governance conversation does not arise.

## What to Build
The corpus as a governed research asset with products on top. Work from metadata and structure rather than content — change sizes, revision frequencies, review timings and outcomes, dependency graphs, defect associations, code survival — which answers most of the interesting questions and never touches a line of anybody's source, and is a position a vendor should be able to state publicly and defend. Build the outcome measures first, since almost everything here reduces to relating a practice to a consequence: rework within a window, defect association, code survival, incident involvement. Then answer the practice questions empirically — change size against defect rate, review depth against escaped defects, dependency characteristics against incident involvement — with proper attention to confounding, since the naive versions of all of these are dominated by the fact that hard code is different from easy code. Give each customer their own answer alongside the population one, since the useful statement is usually about their codebase. Publish the general findings, which is how a vendor earns the right to hold this corpus and is also the strongest differentiator available in a category arguing from conviction. And build the governance in: metadata only, aggregation thresholds, opt-in, and a public statement of what is analysed.

## Target Customer
The platform vendors themselves, engineering leadership seeking evidence for practice decisions, and the engineering analytics vendors limited to single-customer scale.

## Impact If Built
The corpus is unique and unexamined, and it is the only place the category's central question could be answered empirically. Metadata-only analysis answers most of the interesting questions without touching source, which is what makes the governance story true rather than asserted.
