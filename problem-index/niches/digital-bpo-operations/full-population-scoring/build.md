# Build: Automated Resolution Assessment on Every Contact

**Niche:** [[niches/digital-bpo-operations/full-population-scoring/profile|Full-Population Resolution Scoring]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Score every contact against a resolution rubric from its transcript, validated against human analysts and against repeat-contact outcomes.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #survival-analysis #automation
**Contested on:** Whether automated assessment can agree with expert analysts closely enough to replace the sample rather than supplement it.

## The Problem

Quality assessment covers two percent of contacts because a human has to listen to each one. Everything downstream inherits that constraint: agent scores are noisy, coaching material is whatever was sampled, and the operation's actual quality distribution is unknown.

The remaining ninety-eight percent are transcribed and sitting in a data lake. Each one contains the evidence of whether the customer's issue was understood, whether the response addressed it, whether a commitment was made and whether the customer indicated satisfaction. Reading them is now cheap enough to do all of them.

## Why Nobody Has Built This

The capability is recent. Judging whether a support interaction resolved an issue requires reading the exchange and forming a view, which was a human task until very recently and is now a routine one for a language model.

Adoption is slower than capability for two reasons. Validation is not trivial — an automated score that disagrees with analysts in unclear ways will be rejected by the workforce and rightly so, and establishing agreement rigorously is real work. And the result is uncomfortable: a full-population score will show a quality distribution the operation has never seen, will identify agents whose sampled scores were flattering, and will make the handle-time tension measurable.

## What to Build

An assessment pipeline with validation at its centre.

**Write a resolution rubric that can be judged from a transcript.** Was the customer's issue correctly identified. Was the response appropriate to it. Were the necessary steps taken or committed. Was the customer's understanding confirmed. Was there an unnecessary transfer or escalation. Each item scored with the supporting passage cited, so every judgement is checkable in seconds.

**Anchor every output.** A score with no citation is unarguable and will not be trusted by an agent whose bonus depends on it. A score citing the exact exchange is one they can dispute specifically, which is what makes the system legitimate.

**Validate against analysts properly.** Have experienced analysts score several thousand contacts on the same rubric. Measure agreement item by item, by contact type, by channel and by agent tenure. Publish it to the workforce. Agreement should be comparable to inter-analyst agreement — which is itself imperfect, and measuring that is part of the validation, because the honest benchmark is not perfection but the humans being replaced.

**Validate against outcomes too.** Contacts scored as resolved should have lower repeat-contact rates. If they do not, the rubric is measuring something else, and that check is available from data the operation can obtain.

**Report agent-level scores with intervals** and over full monthly volume, which at several hundred contacts is a genuine measurement rather than a sample. This is the improvement agents care most about.

**Route the human analysts to where they add value.** Disputed scores, low-confidence assessments, contacts flagged as unusual, and calibration sampling. The analyst role becomes adjudication and rubric maintenance rather than volume listening, which is better work.

**Run the handle-time analysis.** Resolution against handle time, by contact type, with the confound of contact difficulty controlled. This is the question the whole industry turns on and this pipeline is what makes it answerable.

## Target Customer

BPO quality leadership, where the case is coverage and coaching effectiveness and the differentiation case is strong. Also the interaction analytics vendors, for whom this is the natural next product over a corpus they already process, and client-side vendor management wanting quality evidence beyond a survey.

## Impact If Built

Quality assessment stops being a lottery and becomes a measurement, on every contact, with intervals. Coaching draws on the contacts that actually went wrong. Analysts move from listening to adjudicating. And the industry's central empirical question — whether handle time targets cost resolution — becomes answerable with data the operation already holds.
