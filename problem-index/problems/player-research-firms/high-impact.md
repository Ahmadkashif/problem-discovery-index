# Findings Delivered, Outcomes Never Returned

**Industry:** [[player-research-firms|Player Research Firms]]
**Type:** High Impact
**One-liner:** A firm runs hundreds of studies a year, hands each one across an organisational boundary, and never learns which findings were implemented or whether the change worked.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #data-integration #tacit-knowledge-ml

## The Problem
A research study produces findings: this tutorial step loses players, this control scheme is misunderstood, this progression beat lands flat, this interface element is not seen. The report goes to the development team. The engagement ends.

What happens next is invisible to the researcher. Some findings are implemented, some are partially implemented, some are rejected for reasons that may be good, and some are simply lost in a backlog. When a change ships, the effect appears in telemetry owned by the studio — retention at the affected step, completion rates, time to first success — and nobody connects it to the finding that prompted it.

So the research firm cannot answer the questions that would make it better. Which kinds of finding predict a real behavioural effect and which do not. Whether a problem observed in twelve moderated sessions reliably appears in the live population. Whether the severity ratings researchers assign correspond to anything. Whether a particular method — moderated session, unmoderated remote test, telemetry analysis, survey — is more predictive for a particular class of question.

The consequence is that the field's accumulated knowledge is craft rather than evidence. Experienced researchers are genuinely good, and their expertise is a personal pattern library built from projects whose outcomes they mostly did not see, which means it is built partly on inference and partly on faith.

For the client the loss is equally real. A studio commissioning research has no basis for judging which research is worth commissioning, so budgets are set by whether the last report felt useful.

## Why It's Unsolved
The organisational boundary is the mechanism. The firm delivers and leaves; the telemetry belongs to the studio; the change is made by a team with no relationship to the researcher; and there is no contractual step that says anyone will look afterwards. Nobody is being obstructive — the loop simply was never designed.

The attribution problem is genuine. A game ships many changes at once, so isolating the effect of the one that came from a research finding requires either staged rollout or a model that handles the confounding, and neither is standard practice in games development where builds bundle everything.

The commercial structure discourages it. Research is bought per study, so a firm proposing to measure whether its previous study's recommendations worked is proposing unbilled work whose findings might be unflattering. In-house teams have a slightly better position and usually lack the analytical capacity to do it.

And the record is not kept. Findings are delivered as documents rather than as structured claims, so even a firm that wanted to check its own history would first have to reconstruct what it had claimed, from slide decks, across hundreds of studies.

## What a Solution Looks Like
Make findings structured claims. A finding recorded as a specific, testable statement — this step loses players, expected to affect completion at this point in the funnel — with a severity and a confidence, is something that can be checked later. Recorded as a slide, it is not. This change costs nothing and is the precondition for everything else.

Negotiate the outcome return. Studios can supply the relevant telemetry slice at agreed intervals, and most would if the ask were specific and narrow — completion at a named step, retention in a named window — rather than a general request for data. Framing it as the mechanism by which the next study gets better is the version clients accept.

Measure predictive validity. With claims and outcomes, the firm can ask which methods, which sample sizes and which severity ratings actually predict behavioural change, and publish it. That is the field's missing evidence base and it would be the strongest possible commercial differentiation in a market where every firm claims rigour.

Handle the attribution honestly. Where the change shipped alongside others, say so and report the uncertainty; where a staged rollout was possible, use it. A firm that reports "this finding was implemented in a build containing nine other changes and we cannot isolate it" is being more useful than one that claims credit.

## Impact If Solved
A discipline whose product is evidence has never assembled evidence about itself, because the outcome sits on the other side of an organisational boundary that a data-sharing clause would dissolve. Structured claims plus a negotiated telemetry return would let research firms learn which of their methods work, give clients a basis for deciding what research to buy, and convert a field's accumulated craft into something that compounds — which is the difference between senior researchers being valuable and their expertise being transferable.
