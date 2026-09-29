# Acceptance Is Not Correctness

**Niche:** [[niches/developer-tools-vendors/ai-coding-assistants/profile|AI Coding Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category reports acceptance rate, which measures whether a developer took a suggestion, and says nothing about whether the suggestion survived review, worked, or was still there a month later.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #survival-analysis #cross-validation #causal-inference #automation
**Contested on:** Every serious competitor here is fighting to be the assistant an engineering organisation actually runs on — and that contest is decided twice, by the developer and by the security function, which is why this niche is not terminal and is decomposed below.

## The Problem
A vendor reports that thirty-eight percent of its suggestions are accepted, and this is presented as the measure of value. A developer accepts a suggestion because it is approximately right and faster to edit than to write, because they are tired, or because tabbing is the path of least resistance. What happens next — whether it was modified immediately, whether it survived review, whether it was reverted within the week, whether the code it produced is implicated in an incident, whether anyone can explain it six months later — is where the value actually is, and none of it is reported by anyone.

## Why Nobody Has Built This
Acceptance is the metric the runtime produces for free, and the category adopted it for the same reason support adopted deflection and signature adopted envelopes sent: it is available and it flatters. Measuring survival requires following a suggestion through commit, review, release and revision, which needs the assistant's output to be traceable into the repository — an instrumentation decision nobody made early and which is awkward to retrofit. And the honest metrics would be less impressive, in a market currently being repriced on impressive numbers.

## What to Build
Follow the suggestion rather than counting it. Trace accepted output through to commit, review outcome, release and subsequent modification, which requires marking generated regions at acceptance and is the enabling instrumentation. Report survival: what proportion of accepted code is unmodified after a day, a week, a month — a survival curve rather than a rate, which is both more informative and harder to game. Report review outcomes on generated regions against hand-written ones, including comment density and change requests, which is where the shifted burden becomes visible. Report defect and incident association, which needs care given the confounding but is the question that matters. Measure comprehension explicitly, since code nobody wrote by hand and nobody can explain is a maintenance liability that no current metric captures and that engineers report as a real concern. And build the whole thing to be reported to the customer about their own codebase rather than published as a vendor benchmark, because the effect plausibly varies enormously by codebase and the buyer's question is about theirs.

## Target Customer
Engineering leadership evaluating or renewing assistant spend, the assistant vendors confident enough to be measured honestly, and the engineering analytics vendors for whom this is the natural extension.

## Impact If Built
Acceptance is the category's headline metric and measures the least interesting thing available, while the data to measure survival and review burden is one instrumentation decision away. The comprehension question is the one engineers raise most and that no metric currently addresses.
