# Measuring Whether the Change Worked

**Niche:** [[niches/player-research-firms/outcome-telemetry-linkage/profile|Outcome Telemetry Linkage]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The evidence that would settle every research question is in the client's telemetry and nobody has asked for it.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #data-integration #compliance #descriptive-statistics #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to measure whether the change a finding produced actually improved anything, using telemetry the client holds — and whoever gets that arrangement working takes the account.

## The Problem
A researcher identifies a confusing tutorial step, the team redesigns it, the change ships, and the telemetry shows whether players still stop there. That measurement would validate or refute the finding, refine the method, and tell the firm something about the kinds of question it is good at. It requires access to data the client holds, a measure agreed before the study, and a design that separates this change from everything else that shipped alongside it. None of that is in any engagement.

## Why Nobody Has Built This
Telemetry access is a commercial ask nobody makes, largely because it has never been part of the offer. Attribution is genuinely hard when several changes ship together. Clients may not want their research supplier evaluating outcomes. And the firm is not staffed for causal measurement.

## What to Build
Design the measurement into the engagement before the study runs. Agree the outcome metric and the measurement window with the client before the study, which is the core — a measure chosen afterwards is a measure chosen to fit, and pre-specification is what makes the whole exercise credible. Negotiate aggregate telemetry access rather than record-level, since aggregate is usually acceptable where record-level is not. Design the comparison to account for concurrent changes, because a redesign that ships in a patch alongside six other things cannot be read naively. Use staged rollouts where the client can run them, which turns an observational comparison into an experiment. Handle the null result explicitly, as a finding that was implemented and changed nothing is the most valuable and least reported outcome. Accumulate results across studies to learn which question types and methods predict behaviour, which is the field-level prize. Offer it as a paid follow-on so it is commercially sustainable. Report to the client first, since their trust is the constraint and the results are about their product. Publish method-level conclusions without client specifics, which is how the discipline improves. And keep the measurement modest and honest rather than overclaiming, because an overstated causal claim here would end the arrangement permanently.

## Target Customer
Games user research firms and platforms, client data and analytics functions, publishers, and measurement and clean room vendors.

## Impact If Built
A measure chosen after the change is a measure chosen to fit. Pre-specifying the outcome and negotiating aggregate telemetry access is what makes it possible to learn which kinds of finding predict what players do.
