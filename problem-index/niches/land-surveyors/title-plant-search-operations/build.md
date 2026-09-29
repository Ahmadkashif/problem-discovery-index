# A Century of Examination Decisions and No Model of What Actually Causes Claims

**Niche:** [[niches/land-surveyors/title-plant-search-operations/profile|Title Plant & Search Operations]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Examiners decide what to except and what to insure over millions of times a year, and nobody has matched those decisions to the claims that followed.
**Tags:** #gradient-boosting #binary-classification #graph-ml #evaluation-metrics #revenue-impact

## The Problem
A title examination is a risk judgment dressed as a document review. The examiner reads the chain, identifies defects — a gap in the chain, an unreleased mortgage, an ambiguous legal description, a possible heir — and decides for each whether to except it from coverage, require it cured before closing, or insure over it.

Except too much and the deal is obstructed and the customer goes elsewhere. Except too little and the underwriter pays a claim. Every examiner makes that trade hundreds of times a week, guided by underwriting guidelines and their own experience.

The company holds both halves of the answer. Millions of examinations, each with the defects found and the decisions made, and — through the underwriter — the claims that later arrived, with their cause. Nobody has joined them. Underwriting guidelines are written from claims experience in aggregate and from counsel's judgment, not from a measured relationship between what examiners actually did and what actually went wrong.

## Why Nobody Has Built This
Title is an old, legally-minded industry, and examination is understood as the practice of law-adjacent judgment rather than as a decision under uncertainty. Guidelines are drafted by underwriting counsel and refined when a claim pattern becomes obvious enough to notice.

The organizational split does the rest. Search and examination sit in operations, claims sit in the underwriter, and the plant sits in a data function. Joining them requires someone to want the answer badly enough to cross three boundaries.

And claims are rare. Title claim frequency is low, which makes the loop feel unmeasurable — while in fact low frequency over millions of transactions and decades is exactly the regime where only a systematic analysis can find the signal that individual experience cannot.

## What to Build
Join examination decisions to claim outcomes and model defect risk.

**Assemble the linked dataset.** Examination records with the defects identified and the disposition of each, joined to subsequent claims by parcel and policy. This is the foundational work and it is a data engineering project, not a research one.

**Estimate claim probability by defect type and context.** Which defects, in which jurisdictions, on which transaction types, actually produce claims — and at what severity. Examiners are trading risk against friction with no measured basis for the trade.

**Rank curative requirements by expected loss.** Some requirements prevent real claims and some are ritual inherited from a bulletin written in response to one bad matter in 1974. Distinguishing them removes friction from transactions without adding risk.

**Model chain complexity to route work.** Most searches are routine and some are genuinely hard. Predicting which is which from the plant before an examiner opens the file allocates the scarce expertise — senior examiners — to the files that need them.

**Measure examiner variation.** Comparable chains examined differently by different examiners, with different downstream outcomes, is a calibration and training signal that exists in the data now.

## Target Customer
Chief Data Officer or SVP of Title Operations at a national title underwriter or its plant operation. The commercial pressure is real: transaction volume is cyclical, cost per file is the competitive axis, and every large player is trying to automate examination without a measured basis for deciding what can safely be automated.

## Impact If Built
Title examination adds days and cost to every property transaction in the country, and its requirements are set by precedent rather than by measured risk. Knowing which defects actually cause claims lets the industry clear the ones that do not — faster closings on tens of millions of transactions — while concentrating scrutiny on the ones that do.
