# Buy: Speech Analytics Adapted to Resolution Rather Than Compliance

**Niche:** [[niches/digital-bpo-operations/quality-and-resolution/profile|Quality & Resolution Measurement]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Speech analytics platforms already process every contact; they are configured to detect compliance phrases and sentiment, not to judge whether the problem was solved.
**Tags:** #large-language-models #transformers #evaluation-metrics #confidence-intervals #bert #descriptive-statistics #automation #compliance
**Contested on:** Whether interaction analytics tuned for compliance detection can be repointed at outcome assessment.

## The Problem

Interaction analytics is a mature category with deep deployment in this industry. Every major BPO runs speech and text analytics across its contacts, with transcription, phrase detection, sentiment scoring, silence and talk-over analysis, and category tagging.

What it is configured to find is compliance: was the disclosure read, was the greeting used, was the mandatory phrase spoken, did sentiment go negative. These are detection tasks against known patterns. Whether the customer's problem was resolved is a judgement about the substance of the interaction, which the platforms were not built for and which was not feasible until recently.

## What Already Exists

NICE, Verint, CallMiner, Genesys and the interaction analytics category. Transcription at scale with diarisation. Phrase and category detection. Sentiment and emotion scoring. Quality management modules with rubric scoring and analyst calibration. Agent scorecards and coaching workflow. The infrastructure processes everything already.

## The Customization Gap

**Detection versus judgement.** Phrase detection asks whether a known string occurred. Resolution asks whether an issue was understood and addressed, which is a generative judgement with a rubric. Adding it means a model layer on top of the transcripts with anchored, checkable outputs — the platforms supply the transcripts and not the judgement.

**Sentiment is not resolution and is routinely confused with it.** A customer can end a contact pleasantly with an unresolved issue, and can end it curtly with a fully resolved one. Sentiment is the available proxy, it is weakly correlated with the thing of interest, and building on it produces a measure that rewards pleasantness.

**The outcome signal is downstream and outside the platform.** Repeat contact within a window is the strongest evidence and requires the client's cross-channel contact history, frequently across systems the BPO does not own. That integration is the substantive work and no analytics platform provides it.

**Rubrics reward script adherence because that is what is detectable.** Existing quality rubrics are built around what phrase detection can verify, which is why they weight the greeting and the disclosure. A resolution-oriented rubric weights problem identification, appropriateness of the solution and commitment follow-through — none of which the existing configuration can score.

**Agent-level statistics need honest uncertainty.** Analytics platforms report agent scores as numbers. At full population the volumes support real inference, and the platforms have no convention for reporting intervals — which matters enormously when the score affects pay and employment.

## Target Customer

BPO quality leadership already licensing interaction analytics and getting compliance detection from it. Also the analytics vendors, for whom generative resolution scoring is the obvious next capability over a corpus they already process.

## Impact If Solved

The transcription, storage, category and scorecard infrastructure gets reused, and the resolution judgement layer, the downstream repeat-contact integration, the reformed rubric and the statistical honesty get built. Concretely: the platform that already reads every contact starts answering the question the client is paying for.
