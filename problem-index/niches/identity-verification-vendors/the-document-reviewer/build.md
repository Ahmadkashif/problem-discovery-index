# A Minute, Properly Supported

**Niche:** [[niches/identity-verification-vendors/the-document-reviewer/profile|The Document Reviewer]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reviewer is asked to authenticate a document from a jurisdiction they have never seen, with a specimen image and sixty seconds.
**Tags:** #worker-facing #cnns #object-detection #evaluation-metrics #confidence-intervals #large-language-models #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to make a minute enough to judge a stranger's document correctly — and whoever equips and calibrates that judgement improves the cases the model already failed on.

## The Problem
The case reached review because the model was uncertain. The reviewer sees a photograph of a document, possibly poorly lit, from a jurisdiction that issues a design they may never have encountered, with security features they have not been trained on. They must decide in under a minute whether it is genuine, whether the face matches, and whether the person is who they claim. The support available is a specimen image and general guidance, and the decision is final for that person.

## Why Nobody Has Built This
Review was staffed as capacity rather than as expertise, so tooling optimises throughput — a function measured in cases per hour receives a faster interface rather than better reference material. The model's job was considered finished at routing. Reviewer accuracy cannot be measured without outcomes, so it is unmanaged. And review is frequently outsourced, which distances it from product development.

## What to Build
Put the expertise on the screen. Show document-specific guidance at the moment of decision — this jurisdiction's security features, this revision's layout, the known forgery patterns for this type — which is the core and turns general training into specific knowledge exactly when it is needed. Highlight what the model found anomalous, since knowing which region of the image is suspicious directs the eye immediately. Show comparable genuine and known-fraudulent examples of the same document type, as comparison is how document examination actually works and reviewers rely on memory. Enhance the image rather than presenting it raw, because much of the difficulty is capture quality and enhancement is mechanical. Measure reviewer agreement on duplicated cases, which is the only quality signal obtainable without outcomes and is not collected. Return outcomes wherever they exist — confirmed fraud, successful appeal, later account behaviour — since the role currently learns nothing. Capture the reason for each decision, which is training data and audit evidence at once. Route by document familiarity where volume allows, as repeated exposure is how expertise builds. Remove throughput as the primary metric on the hardest queue. And track decision consistency over time, since drift and fatigue are real and invisible.

## Target Customer
Review operations leadership, the reviewers themselves, institutions relying on these decisions, and outsourced review providers competing on quality.

## Impact If Built
A function measured in cases per hour receives a faster interface rather than better reference material. Document-specific guidance and comparable examples at the point of decision are what a minute needs to be enough.
