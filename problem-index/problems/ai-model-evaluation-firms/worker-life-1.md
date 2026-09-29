# Evaluation Engineer Chasing Flaky Graders

**Industry:** [[ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Worker Life Changing
**One-liner:** Evaluation engineers spend their days establishing whether a score moved because the model changed or because the grader is non-deterministic, the parser broke, or the rubric was interpreted differently this run.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #large-language-models #descriptive-statistics #workflow-orchestration #worker-facing

## The Problem
An evaluation runs and the score moves three points. The engineer must determine why, and the candidate explanations are numerous.

The model genuinely changed. Or the LLM-as-judge returned different verdicts on identical inputs, because it is sampled and not deterministic. Or the judge model itself was silently updated by its provider. Or the output parser failed on a formatting variation and scored those items as wrong. Or a subset of items errored on a timeout and were dropped, changing the denominator. Or the prompt template was modified in a way that looked cosmetic.

Establishing which requires re-running with fixed seeds where possible, checking parse failure rates, comparing judge verdicts on repeated items, diffing prompt templates and inspecting the error log. It takes hours. It happens constantly, because evaluation is run continuously and every movement demands an explanation.

The parser failures are the most maddening. A model that formats its answer slightly differently is scored as wrong by a regular expression, and the engineer discovers this by reading transcripts of items that look correct.

## Why It Matters to the Worker
The role attracts people who care about measurement and consists largely of defending against measurement artefacts. The interesting work — designing an evaluation that actually captures a capability — is a small fraction of the time.

The credibility exposure is the specific pressure. An evaluation engineer reports numbers that inform expensive decisions, and if a reported movement turns out to be a parser bug, the whole evaluation function loses standing. So every result is checked defensively, which is slow and still incomplete.

There is a compounding frustration in the judge dependency. The grader is a model owned by someone else, it changes without notice, and its behaviour on the rubric is not fully characterised. An engineer is building a measurement instrument on top of an instrument they do not control.

And the work is invisible when done well. Nobody notices an evaluation that did not produce a spurious result.

## What a Solution Looks Like
Variance decomposition as a standard output. Every reported score should come with its components: sampling variance from the model, variance from the judge, parse failure rate, item coverage. A three-point move against a judge variance of four points is not a finding, and stating that automatically ends most investigations before they start.

Parse failure surfaced rather than silently scored. Items that failed to parse should be a reported category, never counted as incorrect, and a rising parse failure rate should be an alert in itself.

Judge stability monitoring. Repeated items graded periodically detect judge drift — including silent provider updates — before it contaminates a comparison.

Change attribution built in. When a score moves, the system should list what else changed between runs: model version, judge version, prompt template, harness version, item set.

Deterministic replay wherever the stack allows, so that a rerun isolates the variable under investigation.

## Impact If Solved
Evaluation is the field's measurement instrument and the people maintaining it spend most of their effort on artefacts rather than on measurement design. Decomposing variance and attributing change automatically removes the investigations, and it prevents the spurious results that quietly destroy an evaluation function's credibility.
