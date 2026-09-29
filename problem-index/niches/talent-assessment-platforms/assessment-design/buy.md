# Buy: Psychometric Tooling Adapted to Novel Formats

**Niche:** [[niches/talent-assessment-platforms/assessment-design/profile|Assessment Design & Content]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Item response theory and test assembly tooling assume discrete items with scored responses; a game-based or video assessment produces a behavioural stream with no items in it.
**Tags:** #maximum-likelihood-estimation #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #transformers #compliance #descriptive-statistics
**Contested on:** Whether psychometric machinery built for test items applies to instruments with no items.

## The Problem

Psychometric tooling is mature. Item response theory implementations, item banking, automated test assembly, adaptive testing engines, differential item functioning analysis and equating are all available and well understood, backed by decades of methodology.

All of it assumes items: discrete stimuli with scored responses, whose parameters can be estimated and whose properties can be compared. A game-based assessment produces a stream of behaviour. A video interview produces speech and, in some products, visual features. A work-sample simulation produces a trajectory. None of these decomposes into items in the way the machinery requires, which is a large part of why construct validity for these formats is considerably less established than their marketing suggests.

## What Already Exists

IRT libraries and commercial psychometric packages. Item banking and test assembly systems. Adaptive testing engines. DIF analysis tooling. The professional standards and methodology of the psychometrics tradition. On the other side, the ML tooling the newer formats are built with, which brings none of that tradition.

## The Customization Gap

**Behavioural streams need a defensible feature definition and the tooling assumes one exists.** Turning a game trajectory into scored quantities is a modelling choice that determines what the instrument measures, and it is made by engineers rather than by psychometricians in much of this market. Making that step explicit, documented and reviewable is the central adaptation.

**Reliability has no obvious analogue.** Internal consistency and test-retest reliability are well defined for item sets. For a behavioural stream, what constitutes a parallel form, or a retest, or an item, all need defining before reliability can be estimated at all — and an instrument whose reliability is unestimated should not be making prediction claims.

**Differential functioning analysis has to be reconstructed.** DIF is defined at the item level. For a continuous behavioural measure, the equivalent analysis — does this feature behave differently across groups conditional on the underlying construct — needs a method, and its absence is why disparities in these formats are found in audits rather than in development.

**Facial and vocal features carry specific risk.** Products have withdrawn features under scrutiny — HireVue removed facial analysis from its assessments in 2021 — and the general lesson is that features with weak construct justification and strong demographic correlation are both scientifically and legally untenable. A feature-level justification requirement is the control.

**The documentation standard is the tradition's, not the ML world's.** A technical manual meeting professional assessment standards is a different artefact from a model card, and the newer entrants generally produce neither.

## Target Customer

The newer assessment entrants building game-based, video-based and simulation instruments, who have ML tooling and no psychometric framework. Also the established publishers extending into these formats, and psychometric software vendors, for whom behavioural-stream instruments are the category's growth area and their tooling does not reach it.

## Impact If Solved

The IRT, banking, assembly and DIF machinery gets extended rather than abandoned, and the feature definition discipline, reliability analogues, continuous DIF, feature justification requirement and documentation standard get built. Concretely: novel formats with the evidentiary apparatus the tradition developed, which is what would make their validity claims checkable.
