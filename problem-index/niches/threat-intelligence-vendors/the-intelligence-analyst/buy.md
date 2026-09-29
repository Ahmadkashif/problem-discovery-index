# Buy: Forecasting Calibration, Applied to Analysis

**Niche:** The Intelligence Analyst
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Forecasting research established that calibration improves with scored feedback and built the platforms to deliver it, and threat intelligence analysts make thousands of judgements with none.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #probability-distributions #descriptive-statistics #worker-facing
**Contested on:** Whether an analyst can ever learn whether their judgement was right.

## The Problem

Whether expert judgement can be measured and improved was an open question until a body of forecasting research settled it. The findings are robust and directly relevant: experts are systematically overconfident, accuracy improves substantially with scored feedback, and the people who improve most are those who record specific predictions and see them resolved.

The apparatus built around those findings is mature. Prediction platforms capture forecasts with explicit probabilities against resolvable questions. Proper scoring rules reward both accuracy and calibration. Individual and team calibration curves are tracked over time. And the practice of writing questions that can actually resolve is itself well developed.

Threat intelligence has the ideal conditions for this — numerate analysts, specific and consequential judgements, a professional culture that values rigour — and none of the apparatus. Assessments are published with confidence terms applied loosely, never scored, and never revisited.

## What Already Exists

Forecasting platforms: Metaculus, Good Judgment's tooling, INFER, and the internal prediction markets some organisations run — question framing, probabilistic capture, resolution and calibration scoring.

Forecasting research: the substantial literature on what makes forecasters accurate, the effect of feedback and training, and the design of proper scoring rules.

Government analytic standards: defined probability language so that likelihood terms have consistent meaning, which is the prerequisite for any scoring.

Structured analytic techniques: analysis of competing hypotheses, key assumptions checks and premortem analysis, documented and taught.

Threat intelligence practice: analytical platforms, publishing workflow, and confidence terminology applied inconsistently.

## The Customization Gap

**Assessments are not written as resolvable questions.** Forecasting platforms begin with a well-formed question. An intelligence report contains embedded judgements in prose. Extracting resolvable claims — and writing assessments so they can resolve — is the adaptation.

**Many claims never resolve.** Public forecasting questions resolve on a date. Attribution assessments may never be settled by any public evidence. The system must handle a large fraction of permanently open claims without becoming useless.

**Resolution requires monitoring, not a calendar.** Nothing tells an analyst that evidence has arrived bearing on a two-year-old claim. Automated monitoring for resolving evidence is what makes this practical and has no analogue in the forecasting platforms.

**Attribution resolution is contested.** Even with strong evidence, whether an attribution was correct can be argued. Scoring needs to handle partial and disputed resolution rather than a clean binary.

**Confidentiality constrains sharing.** Forecasting platforms are built around shared question pools. Intelligence assessments are commercial products, so any scoring must be per-firm and private.

**The incentive problem is real.** Forecasters opt in to having their accuracy measured. An analyst whose attribution record might be used in an appraisal will not, which means the framing as development rather than performance has to be genuine and credible.

## Target Customer

Vendor research leadership, where analytical quality is the product and calibration is the only mechanism known to improve it.

Government and large in-house intelligence teams, who already work within analytic standards and would find the extension natural.

Forecasting platform vendors as potential suppliers, since the scoring engine, question lifecycle and calibration mathematics transfer directly and what must be added is extraction, monitoring and confidentiality.

## Impact If Solved

An empirical finding as robust as any in judgement research — that calibration improves with feedback — reaches a profession that has never received any.

Consistent probability language is a style-guide change that costs nothing and is the precondition for everything else, including the customer being able to act on an assessment.

And automated monitoring for resolving evidence is the piece with no precedent in forecasting tooling and the one that makes scoring feasible in a domain where resolution arrives unpredictably, years later, from outside.
