# The Annotator Labelling the Training Data

**Industry:** [[trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Worker Life Changing
**One-liner:** Before a classifier can detect harmful content, people have to look at a great deal of it and label it, and that workforce is even less visible than the moderators downstream.
**Tags:** #transformers #cnns #large-language-models #evaluation-metrics #confidence-intervals #compliance #worker-facing #gradient-boosting

## The Problem
Every harm classifier rests on labelled examples, and the labels are produced by people. Annotators review content across the categories the model must detect — violence, sexual content involving minors in the specialist pipelines, self-harm, harassment, extremism — and assign labels according to guidelines.

The exposure is comparable to content moderation and the attention paid to it is considerably less. Moderation workforces have been the subject of litigation, investigation and public scrutiny; the annotation workforces producing the training data have received far less, despite the work having the same character and frequently being performed under similar outsourced arrangements in similar labour markets.

The work also concentrates the worst material by design. A moderation queue contains whatever was reported; a training set is deliberately constructed to include sufficient examples of each harm category, which means an annotator working a harm category sees a density of it that no reviewer encounters.

Guidelines are the second difficulty. Labelling contested content requires judgement, the guidelines cannot anticipate everything, and annotators are measured on agreement — which teaches literal application in exactly the way audit-based quality measurement does for moderators.

And the labels shape everything downstream. A classifier's biases are the annotation guidelines' biases plus the annotator population's, and neither is typically documented alongside the model.

## Why It Matters to the Worker
This is documented-category occupational risk borne by a workforce with even less visibility than content moderation, which is itself the least visible part of the technology industry.

The deliberate concentration is the specific aggravating factor. Being assigned to label a harm category means encountering that category continuously for a shift, which is a different exposure profile from a mixed review queue and is not generally acknowledged in how the work is structured.

The support provisions, where they exist, are inherited from moderation practice and applied inconsistently, and the outsourced structure means the party specifying the work and the party employing the people are different — the same split that runs through content moderation services.

And the work is invisible in a way that affects how it is treated. A model's card describes its architecture and its performance; it rarely describes who labelled its training data, under what conditions, with what guidelines.

## What a Solution Looks Like
Reduce exposure with the same techniques that apply downstream. Active learning selects the examples that would most improve the model, which means far fewer items need labelling for the same performance — a direct reduction in human exposure and the clearest available win. Reduced-fidelity presentation, segment isolation and text summaries apply here as they do in moderation.

Use models to pre-label and humans to adjudicate. As classifiers improve, the annotator's role shifts toward confirming and correcting rather than labelling from scratch, which reduces both volume and the time spent on each item.

Manage cumulative exposure explicitly, and account for the concentration. Category assignment, rotation and enforced limits should reflect that a harm-category annotator sees a density no reviewer does.

Treat disagreement as information. Where annotators disagree, the case is genuinely contested, and recording that rather than forcing consensus produces better models — a distribution of labels supports a calibrated classifier where a forced single label supports an overconfident one — and removes the pressure to apply guidelines literally.

And document the provenance. Who labelled a model's training data, under what guidelines, with what agreement rates, published alongside the model, is basic transparency that would also make the resulting biases traceable.

## Impact If Solved
Harm classifiers rest on a workforce doing concentrated exposure work with less visibility and less protection than the moderators downstream. Active learning reduces the volume needed directly, model-assisted pre-labelling reduces the burden per item, exposure management accounts for the concentration this work involves, and recording disagreement rather than forcing consensus improves the models while removing a source of pressure on the people producing them.
