# Form and Survey Generation, Already Solved

**Niche:** [[niches/data-labeling-services/annotation-tooling/profile|Annotation Tooling]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generating a usable interface from a declarative schema is what form builders, survey platforms and low-code tools do, and annotation tooling builds each new task by hand.
**Tags:** #graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #worker-facing #automation #transfer-learning
**Contested on:** Every serious competitor in annotation tooling is fighting to support a genuinely new task type without a solutions engineer building an interface first — and whoever does that takes the in-house teams, because the bespoke build is the delay before any data exists.

## The Problem
Turning a declarative description of what to ask into a working, validated, accessible interface is solved: form builders, survey platforms, low-code application builders and schema-driven form libraries all do it, at scale, with good results. Annotation tasks are structurally similar — present something, ask for judgements, validate the response — and are built as bespoke applications.

## What Already Exists
Schema-driven form generation libraries; survey platform builders with branching and validation; low-code interface generation; JSON schema and its tooling; and the specialised media annotation components which are open source and embeddable.

## The Customization Gap
The adaptation is to annotation rather than to data entry. It requires: (1) media and structured artefacts as first-class elements, since an annotation task presents a document, a video, a model trace or a pair of outputs, and a form builder assumes text and selections — embedding the existing specialised viewers as schema elements is the practical route; (2) linking and referencing between the artefact and the judgement, because much annotation is about marking a part of something rather than answering about the whole, which forms do not express; (3) efficiency for repetition, since an annotator does this hundreds of times and a form designed for a single respondent is intolerably slow — keyboard operation, sensible defaults and minimal pointing are what distinguish an annotation interface from a form; (4) process instrumentation built into the generated interface, since the quality work needs time, revisions and attention signals and a generic form captures none; and (5) versioning of the definition, because the task changes mid-project and the labels collected under each version must remain distinguishable.

## Target Customer
Annotation platform vendors, in-house tooling teams, and the open annotation tool projects.

## Impact If Solved
Interface generation from a schema is thoroughly solved in adjacent categories and annotation builds by hand. Efficiency for repetition is the adaptation that separates a usable annotation interface from a form, and it is a known and bounded set of interaction requirements.
