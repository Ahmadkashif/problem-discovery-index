# Buy: Forecast Calibration for Technical Judgement

**Niche:** Assessment Calibration
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Forecasting platforms have solved prediction capture, scoring and calibration feedback for analysts, and nothing has carried any of it into technical advisory.
**Tags:** #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #bayesian-linear-regression #probability-distributions #data-integration
**Contested on:** Whether an advisory practice retains its own assessments and their outcomes well enough to know which of its judgements have historically been right.

## The Problem

The problem of measuring whether an expert's judgements are right has been solved rigorously, in public, by another field. Forecasting research established proper scoring rules, demonstrated that calibration improves substantially with structured feedback, and produced platforms where analysts record predictions with confidence, outcomes resolve, and individual and team calibration is tracked over years.

Technical advisory has adopted none of it, despite being an unusually good fit: the predictions are specific and consequential, the outcomes are observable, the practitioners are numerate, and the buyer explicitly wants a confidence signal. A fractional CTO saying "this rebuild is nine months" is making a forecast with an implicit confidence interval, and no mechanism anywhere in the profession records it as one.

## What Already Exists

Forecasting and prediction platforms — Metaculus, Good Judgment's tooling, INFER, and the internal prediction markets some large technology firms run — handle question framing, confidence capture, resolution and calibration scoring, with mature practice around what makes a question resolvable.

Adjacent: professional services automation (Kantata, Scoro, Projectworks) tracks engagements, time and margin. Knowledge management platforms store documents. Estimation tooling in software project management handles schedule forecasting with reference-class techniques inside a single organisation. Actuarial and audit practice has decades of experience with retrospective accuracy review under professional standards.

## The Customization Gap

**Questions arrive as prose, not as questions.** A forecasting platform starts with a well-formed resolvable question and a stated confidence. An assessment starts with a forty-page narrative written to persuade a board. The extraction of resolvable claims from that narrative — and the discipline of writing claims that can resolve without making the document worse — is the entire adaptation, and it is the part no existing platform touches.

**Resolution is not automatic and not free.** Forecasting platforms resolve against public events. "Did the rebuild take nine months" resolves only if someone asks the client eighteen months later, through a relationship that has gone dormant. The product has to carry the follow-up workflow, not just the scoring.

**Resolution is ambiguous in a way public questions are not.** The client executed half the recommendation, changed the scope, and took fourteen months. Is the nine-month estimate wrong? Advisory needs partial and conditional resolution — execution fidelity recorded alongside outcome — which forecasting platforms do not model because their questions are constructed to avoid it.

**Confidentiality is a first-class requirement.** Forecasting platforms are built around shared, often public, question pools. An advisory corpus must be per-firm, de-identified at entry, and structurally incapable of leaking one client's situation into another's reference class in identifiable form.

**The reference class matters more than the score.** An analyst wants their Brier score. A practitioner wants to know what happened the last time the firm saw a system of this shape. That is retrieval over a structured corpus, not a leaderboard, and it is the feature that would drive daily use.

**Incentives point the wrong way.** Forecasting platforms assume participants want their accuracy measured. A senior advisory practitioner does not, particularly. Any adaptation has to be introduced as a firm asset and a client-facing credential rather than as individual performance measurement, or it will be quietly starved.

## Target Customer

Private equity technical operating groups are the best fit on every axis: they run enough diligences to generate a reference class, they own the portfolio companies so resolution is internal rather than a favour, and they are culturally comfortable with measured judgement because the rest of the firm already works that way.

Boutique advisory practices are the volume market and the harder sale, reachable mainly through the client-facing credential rather than the internal-improvement argument.

A forecasting platform vendor looking for enterprise revenue is the natural supplier — the scoring engine, question lifecycle and calibration mathematics all transfer, and what has to be added is extraction, follow-up workflow and per-firm confidentiality.

## Impact If Solved

Technical advisory acquires the thing forecasting gave intelligence analysis: a practitioner who knows their own bias. The evidence that calibration improves with feedback is strong, and this is a profession that has never received any.

For the buyer of an assessment, a firm that can state its historical accuracy changes what "reputation" means in the category. Reputation currently prices on narrative; this would let some of it price on record.

And it is the mechanism that would finally answer the profession's structural question — whether judgement sold by the day can be shown to be worth what it costs.
