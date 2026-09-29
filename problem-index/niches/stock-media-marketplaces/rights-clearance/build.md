# Clearance Without Looking at Everything

**Niche:** [[niches/stock-media-marketplaces/rights-clearance/profile|Rights Clearance]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether an image can be sold depends on what is visible in it and what paperwork exists, and both are checked by a person squinting.
**Tags:** #object-detection #cnns #semantic-segmentation #evaluation-metrics #confidence-intervals #compliance #automation #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to determine whether an asset can be licensed commercially — releases, trademarks, property, editorial restrictions — without a person examining the image and the paperwork every time.

## The Problem
A reviewer looks at an image and must determine whether any recognisable person requires a release, whether any release supplied covers those people, whether a visible logo or product design creates a trademark issue, whether a building or location is protected, and whether the asset must therefore be restricted to editorial use. They do this in seconds, at enormous volume, from an image and a set of documents. Mistakes in one direction create legal exposure and in the other destroy contributor income.

## Why Nobody Has Built This
Clearance is a legal judgement, so it was assigned to human review and never decomposed into the detectable and the judgement-requiring parts — a task labelled legal resists automation even where most of its inputs are perceptual. Detection was historically unreliable. Over-restriction is invisible and under-restriction is a lawsuit, so the incentive runs one way. And nobody tracks which restrictions ever mattered.

## What to Build
Detect what is in the image and verify the paperwork against it. Detect faces, logos, trademarks, product designs, artworks and recognisable locations automatically, which is the core and is where most of the reviewer's attention goes. Match supplied releases against the people detected, since a release that does not cover the person in the frame is a common and currently unchecked failure. Validate release documents for completeness and signature rather than accepting an attachment, as an unusable release is functionally no release. Route only the ambiguous to a person, because the clear cases in both directions are the majority. Grade risk rather than applying a binary restriction, so a barely visible logo is treated differently from a prominent one. Track which restrictions were ever the subject of a complaint or claim, which is the evidence base for calibrating the policy and does not exist. Tell the contributor exactly what caused a restriction, since they can often supply the missing release and are currently told only the outcome. Tell the buyer what the risk actually is, as an editorial-only flag communicates a conclusion and not a reason. Handle the back catalogue, where older assets were cleared under different standards. And measure the cost of over-restriction in lost licensing, which is the side nobody counts.

## Target Customer
Rights and legal leadership, reviewers, contributors whose assets are restricted, and buyers carrying the residual risk.

## Impact If Built
A task labelled legal resists automation even where most of its inputs are perceptual. Detecting what is in the image and matching releases against the people found routes only the genuinely ambiguous cases to a person.
