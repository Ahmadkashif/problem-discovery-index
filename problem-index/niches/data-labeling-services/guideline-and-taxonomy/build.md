# The Specification Nobody Tests

**Niche:** [[niches/data-labeling-services/guideline-and-taxonomy/profile|Guideline & Taxonomy Iteration]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The guideline is the specification for every label in the project, is written by somebody who has not done the task, and is never tested or measured.
**Tags:** #bert #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor here is fighting to find the ambiguity in a guideline before it produces a batch of inconsistent data — and whoever does that takes project delivery, because guideline ambiguity is the single most common cause of the disagreement everyone attributes to annotators.

## The Problem
A guideline defines six categories. Two of them have a boundary that seems clear in the abstract and is not applicable to about a fifth of real items. Annotators encounter those items, decide differently, and produce disagreement. The disagreement is reported as an agreement statistic, read as annotator quality, and addressed by retraining the annotators — who all understood the guideline correctly and disagreed because it does not determine an answer. The pattern is visible in the data: the disagreement is concentrated almost entirely on that one boundary, which is the signature of a specification problem rather than a workforce problem, and nobody looks.

## Why Nobody Has Built This
The guideline is treated as documentation rather than as a specification to be tested, so no testing apparatus exists. Its author is frequently the customer or a taxonomy specialist working from the task's abstract structure rather than from real items, which is exactly the condition that produces boundaries that do not survive contact with data. Disagreement is analysed as a rate rather than as a distribution, which discards the structural information. And attributing quality problems to annotators is organisationally easier than attributing them to a customer-supplied specification.

## What to Build
Test the guideline and measure its revisions. Pilot before the main batch with a small set of items and several annotators, specifically to locate the boundaries that do not determine an answer — which is cheap, is standard practice in every adjacent field that writes instruments, and is skipped here. Analyse disagreement for structure continuously: concentrated on a category pair, a boundary, or an item type is a specification signal, and spread evenly is an annotator signal, and the distinction is a straightforward analysis that changes the response entirely. Mine the annotator question channel, since the questions are a direct enumeration of what the guideline fails to say and are currently answered individually and discarded. Cluster the contested items, which produces the examples the guideline should contain — drawn from what actually caused difficulty rather than from what the author imagined. Version the guideline against every item and measure each revision's effect on agreement, which is the evaluation that tells anybody whether the guideline work is doing anything. Propose clarifications from the contested clusters, since the specific wording that resolves a boundary is usually apparent once the contested items are grouped. And report the guideline's own contribution to disagreement, which reframes a quality conversation that currently blames the wrong party.

## Target Customer
Taxonomy authors and project leads at delivery organisations, the customers who write specifications, and the platform vendors whose quality analytics stop at an agreement rate.

## Impact If Built
Guideline ambiguity is probably the largest controllable cause of annotation disagreement and is systematically attributed to annotators, because disagreement is reported as a rate rather than as a distribution. Analysing its structure is straightforward and changes the diagnosis, and piloting before the main batch prevents the error propagating through an entire delivery.
