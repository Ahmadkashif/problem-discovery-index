# Build: The Practice Corpus

**Niche:** Assessment Calibration
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that extracts a comparable record from every assessment a practice writes, captures what actually happened afterwards, and turns a career of pattern recognition into an asset the firm owns.
**Tags:** #bert #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #k-means-clustering #word-embeddings #data-integration
**Contested on:** Whether an advisory practice retains its own assessments and their outcomes well enough to know which of its judgements have historically been right.

## The Problem

A practice sells calibrated judgement and has never measured its own calibration. Each assessment contains predictions — this rebuild takes nine months, this architecture will not survive the planned scale, this team can absorb three more engineers, this dependency is the acquisition's real risk — stated with implicit confidence to a buyer who will act on them. None of the predictions is recorded in a form that can be checked, and none is checked.

The absence compounds in three directions. The practitioner never learns, because feedback arrives, if at all, as an anecdote years later from a client who happened to stay in touch. The firm owns nothing, because thirty assessments a year become thirty documents in thirty client folders. And the client cannot evaluate what they are buying, because the only evidence of quality available at purchase is reputation.

The material exists. Every assessment is written down. Every client is reachable. The missing pieces are a comparable record extracted from bespoke prose, a follow-up habit, and somebody whose job it is to maintain both.

## Why Nobody Has Built This

**It pays nothing for a year.** The corpus has no value until it contains enough matched pairs of prediction and outcome to constitute a reference class — realistically two to three years for a mid-sized practice starting from scratch. Nothing about professional services economics rewards that patience, and a practice owner choosing between this and anything with a same-quarter return chooses the other thing every time.

**Confidentiality is the stated obstacle and mostly a reflex.** Engagement letters prohibit disclosing client information. They do not prohibit a firm from retaining, in de-identified form, the pattern of what it observed and concluded — and most explicitly permit it. Very few practices have done the legal work to establish where their line is, so the safe default is that nothing is retained, and the default is never revisited because nobody's job includes revisiting it.

**Utilisation crowds it out.** The assessment is billable. Structuring it for reuse is not. In a firm operating at seventy per cent utilisation, unbilled knowledge work loses every allocation argument.

**The senior practitioners resist.** The corpus converts individual pattern recognition into firm property. The people who must supply the material are the people whose negotiating position it weakens, and they are senior enough to decline without ever saying no.

**Outcome capture crosses a closed boundary.** The engagement ends, the relationship goes dormant, and asking eighteen months later what happened is a favour. It is a small favour — most clients are pleased to be asked — but nobody in the firm is responsible for asking, so it is never asked.

**And the answer might be bad.** A practice that measures its own calibration may discover its estimates are systematically optimistic. That is the finding with the most value and the least appetite.

## What to Build

**Extraction, not templating.** Take the assessment documents as written and extract a structured record beside them: client shape, system characteristics, problems identified, recommendations made, estimates with their units and confidence, risks flagged. De-identification happens at extraction, so what accumulates is already in the form the engagement letter permits. The narrative document stays exactly as it is, because forcing assessments into a rigid template makes them worse at the job they are paid for.

**Outcome capture as a client benefit.** A short structured check-in at six and eighteen months, offered free and framed as useful to the client — because it is. What was executed, what was not and why, what the result was, what surprised them. Ten minutes on a call, recorded against the original assessment. This is the single addition that converts a filing system into a record of predictions with results, and it is almost entirely a habit problem rather than a technical one.

**Scoring.** Once pairs exist, score them: estimate accuracy as a distribution with its bias and spread, hit rate on risk flags, execution rate on recommendations, and the conditions under which each degrades. Scoring rules for this are well established in forecasting practice and need no invention — the contribution is applying them to technical judgement, which nobody does.

**Reference class at the point of need.** When a practitioner scopes a new engagement, the firm's prior work on similar shapes surfaces — comparable systems, what was recommended, what followed. When an estimate is being written, the firm's historical distribution for that kind of estimate appears next to it. Not a recommendation engine and not an oracle: a reference class, which is the thing an expert most needs and least has.

**An owner.** Someone compensated for the corpus existing. Every version of this that relied on practitioner goodwill has failed, and it will fail again.

## Target Customer

Practice owners at boutiques of eight to fifty practitioners, where enough assessments flow annually to build a reference class within a few years and the owner has a direct interest in the firm owning something.

Private equity technical operating groups are the sharper buyer. They run many diligences a year, they *own the outcome* — the portfolio company is right there, so the follow-up boundary does not exist — and their calibration question is explicitly commercial: were our technical diligences right, and where do they systematically miss.

Professional liability insurers are a third, unusual channel. An advisory practice that can demonstrate measured calibration is a different risk from one that cannot, and premium differentiation is one of the few forces that reliably makes professions measure themselves.

## Impact If Built

The firm can answer the client's hardest question with evidence: of the last eleven times we made a recommendation of this shape, here is what happened. No competitor can answer it at all, and the asymmetry is durable because it takes years to build.

Calibration improves with feedback — this is one of the better-established findings in forecasting research — so the corpus does not merely describe the practice's judgement, it improves it. A practitioner who learns their nine-month estimates have historically run fourteen begins giving different estimates.

And the firm acquires an asset. A consultancy whose knowledge leaves at six each evening is a group of individuals sharing a brand; one whose reference class survives departures is a business with enterprise value.
