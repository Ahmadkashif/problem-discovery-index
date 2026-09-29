# Prompt Changes Have Unbounded Blast Radius

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Type:** High Impact
**One-liner:** Editing a prompt to fix one case silently changes behaviour across every other case, and there is no regression test — so quality moves in both directions invisibly and teams ship on hope.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #transformers #change-point-detection #gradient-boosting #revenue-impact

## The Problem
A user reports that the assistant answered a question badly. An engineer reproduces it, adds a sentence to the system prompt, confirms the case is fixed, and ships.

That sentence altered behaviour across the entire input distribution. Perhaps it made responses more cautious, so a class of questions that previously got direct answers now gets hedged ones. Perhaps it shifted formatting in a way that breaks a downstream parser. Perhaps it introduced a conflict with an instruction added four months ago that nobody remembers.

Nothing catches this. Software regression testing works because behaviour is deterministic and assertions are exact. Here the output is different every time by design, the space of inputs is unbounded natural language, and correctness is frequently a judgement rather than a comparison.

So teams maintain a handful of test cases, run them manually, and ship changes they cannot evaluate. Quality moves in both directions and nobody knows the aggregate. The user complaint that prompted the change is a sample of one, and the changes that made things worse produce complaints weeks later that trigger further changes, and the prompt accumulates.

## Why It's Unsolved
Assertions are the wrong primitive. There is no exact expected output, so a test suite must compare against a reference with a similarity or judgement measure, and both are noisy enough that a small real regression is indistinguishable from measurement noise on a small test set.

Test sets are small because building them is expensive. Constructing a representative set of inputs with judged correct behaviour requires domain knowledge and effort, and it must be maintained as the product changes.

Judges are the standard shortcut and carry their own problems — inconsistency between runs, sensitivity to formatting, drift when the judge model is silently updated by its provider.

Sample size is the underappreciated obstacle. Detecting a two-per-cent regression with a noisy judge requires a test set far larger than the twenty cases most teams maintain, and nobody computes the power of their evaluation before trusting its result.

And the model changes underneath. A provider updates a model and behaviour shifts without any change on the team's side, which means the baseline is not stable, which undermines any before-and-after comparison.

## What a Solution Looks Like
Regression evaluation on production traffic rather than a curated test set. Replaying a sample of real historical inputs against the old and new prompt, and comparing outputs pairwise, tests the actual input distribution and requires no labelled reference. Pairwise comparison is also a much easier judgement than absolute scoring, for both judges and humans.

Statistical honesty about detection. Every reported change should carry an interval and a statement of what magnitude of regression the evaluation could have detected — most teams are running underpowered evaluations and concluding no change when they mean no evidence.

Staged rollout with online measurement. Shipping a prompt to a fraction of traffic and comparing outcome metrics is standard practice in every other part of software and is rare here, despite the tooling supporting it.

Change attribution over time. When quality moves, the system should list what changed — prompt version, model version, retrieval configuration, upstream data — and provider model updates should be tracked as first-class events because they are the most common invisible cause.

## Impact If Solved
Prompt changes are the highest-frequency deployment in an LLM application and the only one with no regression test. Production-replay comparison with honest statistics turns shipping a prompt from an act of hope into a measured change, which is the precondition for these applications being maintainable at all.
