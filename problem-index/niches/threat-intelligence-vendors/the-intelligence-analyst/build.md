# Build: Assessments as Scoreable Predictions

**Niche:** The Intelligence Analyst
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Record every assessment as a claim with a stated confidence and a resolution condition, so that when evidence eventually arrives the judgement can be scored and the analyst can calibrate.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #probability-distributions #graph-theory #worker-facing #tacit-knowledge-ml
**Contested on:** Whether an analyst can ever learn whether their judgement was right.

## The Problem

An analyst assesses, with moderate confidence, that a set of intrusions is the work of a particular group, based on infrastructure overlap, tooling similarity and targeting pattern. The assessment is published.

Eighteen months later an indictment, a leak or a competing vendor's reporting settles the question. Sometimes the analyst sees it. Often they do not, because they have moved to other work and nothing connects the new evidence to their old assessment.

Multiply by every judgement they make. Over a career, an analyst accumulates enormous experience and almost no feedback. Their confidence in their own attribution improves with repetition rather than with accuracy, which is the classic condition under which expert confidence and expert accuracy diverge.

The same applies to forward-looking judgements. An assessment that a campaign will expand to a new sector is a falsifiable prediction. It is published with a confidence level, is never revisited, and nobody knows whether this team's moderate-confidence predictions come true two thirds of the time or one third.

The material to fix this exists entirely inside the vendor. Every assessment is written down. Evidence arrives continuously. What is missing is the mechanism that connects the second to the first.

## Why Nobody Has Built This

**Scoring creates an accuracy record.** An analytical practice that discovers its attribution assessments are frequently wrong has generated a finding it must then manage, and analysts have reasonable concerns about how it would be used.

**Resolution is slow and often never happens.** Many assessments are never settled by any public evidence. A scoring system where most claims never resolve produces sparse data over years.

**Assessments are prose, not claims.** A report contains embedded judgements in narrative form. Extracting them as scoreable propositions is work, and asking analysts to state them separately feels like bureaucracy.

**Confidence language is applied loosely.** Without consistent meaning for likely and probable, scoring is meaningless — so the first fix is a style guide, not a system.

**Attribution is genuinely contested.** Even with an indictment, whether an assessment was right can be argued, particularly on cluster boundaries and the relationship between named groups.

**Nobody is asking.** Customers do not request accuracy records, competitors do not publish them, and no regulator requires them.

## What to Build

**Record assessments as structured claims.** Each judgement extracted from the report as a proposition with a stated confidence and, where possible, a resolution condition — what evidence would confirm or refute it. Captured at writing time, in a minute, alongside the prose.

**Standardise the confidence vocabulary first.** Defined probability ranges for each term, applied consistently. Without this nothing downstream means anything, and it costs a style guide and a habit.

**Watch for resolving evidence automatically.** Monitor indictments, public reporting, vendor publications and the firm's own subsequent collection for evidence bearing on open claims, and surface candidates for resolution to the analyst. This is what turns a scoring system from an administrative burden into something that runs itself.

**Score what resolves and report calibration privately.** Per analyst and per team: when this practice says likely, how often is it right. Held confidentially, framed as development, and explicitly excluded from performance management — because a calibration tool used for performance will be gamed and will then be worthless.

**Make the corpus of prior assessments queryable.** What has this team previously concluded about this actor, with what confidence, and what has since happened. Currently this requires reading old reports and depends on who remembers.

**Structure attribution reasoning.** The specific inferences underlying an attribution — infrastructure overlap, tooling, targeting, tradecraft — recorded as separate supported claims rather than as narrative. When a later contradiction arrives, the specific inference that failed becomes identifiable, which is how the reasoning improves.

**Apply structured techniques to the hard cases.** Analysis of competing hypotheses and key assumptions checks on major attribution calls, recorded. These are cheap, documented, and demonstrably reduce bias — and they are skipped under deadline.

## Target Customer

Vendor research leadership, where the argument is analytical quality and analyst development rather than a customer-facing feature — and where the calibration data would be the first evidence about the practice's own accuracy.

Analysts themselves, who are the users and would need to be convinced the scoring is for their development and not for their appraisal.

Customers as an eventual audience: a vendor able to state its own historical attribution accuracy would have a claim no competitor could match, which is the commercial case for building it.

## Impact If Built

A discipline built on calibrated judgement would acquire calibration. Forecasting research is consistent that accuracy improves with feedback, and this profession receives none.

Structuring attribution reasoning into separate inferences would let a practice learn which of its inference types are reliable — infrastructure overlap versus tooling similarity versus targeting — which is a question nobody can currently answer.

And a queryable corpus of prior assessments would turn a team's accumulated judgement into an asset rather than something held individually and lost when people leave.
