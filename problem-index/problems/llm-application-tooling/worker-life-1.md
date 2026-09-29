# AI Engineer Bisecting a Quality Regression

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Type:** Worker Life Changing
**One-liner:** An applied AI engineer investigating why answers got worse must separate their own prompt changes from a provider's silent model update, a retrieval change, a data change and ordinary sampling noise, with no reliable baseline anywhere.
**Tags:** #hypothesis-testing #confidence-intervals #change-point-detection #descriptive-statistics #evaluation-metrics #large-language-models #workflow-orchestration #worker-facing

## The Problem
Quality has dropped. Users are complaining, or a metric moved, or someone noticed the answers seem worse.

The engineer starts with a small number of anecdotes and a large number of candidates. A prompt change shipped last week. The provider updated the model — announced or not, and behaviour has been observed to shift without announcement. The retrieval corpus was reindexed. A chunking parameter changed. The traffic mix shifted toward harder questions. Or nothing changed and the sample of complaints is noise.

Bisecting means holding things still, which is not possible: the model is not version-locked, production traffic cannot be replayed against a past provider state, and the evaluation set is too small to detect a modest regression.

The engineer runs their twenty test cases against the current and previous prompt, sees three differences, and cannot tell whether those three represent a regression or the usual variation.

Frequently the investigation ends without an answer. The team reverts the most recent change on suspicion, quality appears to recover, and nobody knows whether it did.

## Why It Matters to the Worker
The applied AI engineer role is new, ill-defined and carries responsibility for a quality outcome the engineer does not control end to end. The model is a third party's, it changes without notice, and the engineer is accountable for its behaviour.

The unfalsifiability is corrosive. Software engineers are used to being able to determine what broke, and this domain frequently does not permit it. Closing an investigation with a hypothesis is professionally uncomfortable and happens constantly.

The pressure is unbalanced. Reports of quality problems arrive from users and executives who experience the product; the engineer has anecdotes and a test set they know is inadequate, and must respond with confidence they do not have.

And the same investigation repeats, because nothing accumulates. There is no record of which past regressions turned out to be provider changes versus prompt changes, so each one starts from zero.

## What a Solution Looks Like
A stable baseline maintained deliberately. A fixed set of inputs run against a fixed configuration on a schedule, tracked over time, so that a provider's silent model change is visible as a change in the baseline before it becomes a user complaint. This is cheap and almost nobody does it.

Change attribution automated. When quality moves, listing every change in the window — prompt version, model version, retrieval configuration, index rebuild, traffic mix — collapses the candidate list immediately.

Production replay for comparison, using real historical inputs rather than a curated test set, which gives sample sizes large enough to detect the regressions that matter.

Statistical power stated up front. An engineer should know that their evaluation can detect a five-per-cent regression and not a two-per-cent one, so that a null result means something specific rather than nothing.

Traffic mix decomposition, so that a metric moving because questions got harder is distinguishable from the system getting worse — which is the first thing an engineer should check and currently cannot.

## Impact If Solved
Quality regression investigation is the defining recurring task of applied AI engineering and it frequently cannot be completed with the information available. A maintained baseline, automated attribution and adequately powered evaluation turn an unfalsifiable investigation into a diagnosis.
