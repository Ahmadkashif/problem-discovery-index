# Explainability From Regulated Modelling

**Niche:** [[niches/ugc-video-platforms/decision-explanation/profile|Decision Explanation]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit and healthcare modelling produce individual-level explanations because they are required to, and content classifiers produce a label.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #large-language-models #cnns #hypothesis-testing #descriptive-statistics #transformers
**Contested on:** Every serious competitor in this niche is fighting to make a classifier state which passage of a video triggered its decision and how confident it was — and whoever does it turns an unaccountable determination into one a person can act on.

## The Problem
Domains where a model's output affects an individual and the law requires an explanation — consumer credit, some clinical decision support, employment screening — developed individual-level explanation practice: reason codes, attribution methods for complex models, validation that the explanation reflects the model, and documentation standards. Content enforcement affects individuals at least as consequentially and produces a category label.

## What Already Exists
Reason code derivation; individual-level attribution for complex models; explanation validation and faithfulness testing; model documentation standards; and supervisory expectations for explanation accuracy.

## The Customization Gap
The adaptation is to video and audio rather than tabular features. It requires: (1) explanation localised in time and space within media rather than attributed across features, which is a different technical problem and is where the platforms' own segmentation and detection capabilities apply — this is the substantive adaptation; (2) an adversary who will use the explanation, which credit explanation does not face in the same way; (3) millions of decisions daily, so explanation must be generated rather than authored; (4) a multimodal decision combining video, audio, text and metadata, so the explanation must say which modality fired; and (5) no established regulatory standard yet, so the bar is being set now.

## Target Customer
Trust and safety engineering and policy leadership, creators, regulators, and model explainability vendors.

## Impact If Solved
Regulated modelling built individual explanation because the law required it and the methods are mature for tabular data. Localising an explanation inside video and audio is the genuinely new part, and these platforms have the best tools for it.
