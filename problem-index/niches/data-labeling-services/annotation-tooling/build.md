# Three Weeks Before the First Label

**Niche:** [[niches/data-labeling-services/annotation-tooling/profile|Annotation Tooling]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Annotation tooling for images, spans, audio and video is mature and excellent, and every genuinely new task type still means a solutions engineer building a bespoke interface before a single label is collected.
**Tags:** #large-language-models #bert #k-means-clustering #graph-theory #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor in annotation tooling is fighting to support a genuinely new task type without a solutions engineer building an interface first — and whoever does that takes the in-house teams, because the bespoke build is the delay before any data exists.

## The Problem
A model team needs annotations on a new task: given a document and a model's summary, mark each claim in the summary as supported, contradicted or unsupported by the document, with the supporting span linked where it exists. Every element of this is conceptually simple. No available interface does it. The vendor's solutions engineer quotes three weeks. The team builds something themselves in four days, which is worse to use, produces lower-quality annotations because the interface is awkward, and exists only for this task. Six weeks later they need a variant and repeat the exercise.

## Why Nobody Has Built This
The tooling matured by specialising: an image annotation interface that is excellent at images does not generalise, and the product strategy of building the best editor per modality was correct when the modalities were few and stable. Generalising requires a task definition language and interface generation, which is a different kind of product and a substantial rewrite rather than a feature. And the bespoke builds are billed as services, which makes them revenue rather than a gap.

## What to Build
Generate the interface from a declarative task definition. Define a task model covering the primitives the new work is made of — present these artefacts, ask for these judgements, link these elements, capture this rationale, permit partial and conditional verdicts — which is a bounded vocabulary and is what the bespoke interfaces keep reimplementing. Generate a polished interface from it, so a custom task gets the same annotator experience as a native one, which matters because interface quality affects annotation quality directly. Make the definition shareable, so the claim-verification task one team defined is available to the next rather than rebuilt — which is the compounding benefit and requires the definition to be data rather than code. Keep the specialised editors for the modalities where they are genuinely better and compose them as elements within a task rather than replacing them. Capture the process signals uniformly across generated and native interfaces, since the quality and corpus work depends on them and custom builds currently capture nothing. Support iteration, since a new task's definition is wrong the first time and the cost of changing it currently means it does not change. And measure time from task specification to first label, which is what this market is actually deciding on.

## Target Customer
In-house annotation teams at model developers, annotation platform vendors, and the research groups building their own tooling because nothing fits.

## Impact If Built
The bespoke build is the delay before any data exists, at the moment a model team most needs to move, and it is the reason capable teams build their own. A declarative task model with generated interfaces removes it, and shareable definitions mean the second team with a similar task waits for nothing.
