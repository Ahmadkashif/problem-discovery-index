# Fix: The Sample of Three

**Niche:** Technology Selection Advice
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** An advisor's technology opinions are formed by the accidents of their own employment history, and neither they nor the client has any way to see the shape of that bias.
**Tags:** #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #probability-distributions #worker-facing
**Contested on:** Whether a platform recommendation rests on operational evidence from comparable deployments or on vendor documentation and the advisor's last three projects.

## The Problem

Ask an experienced fractional CTO why they recommend a particular technology and the honest answer, underneath whatever research is cited, is that they have used it and it worked, or they have used the alternative and it did not. This is not a failure of rigour. It is the only high-quality evidence they have, because direct operational experience genuinely is better evidence than vendor documentation.

The problem is the sample. A practitioner's experience comprises perhaps eight to fifteen substantial systems across a career, chosen by where they happened to work — which means by industry, by era, by scale, and by the technology choices other people made before they arrived. They know one message broker deeply because a company they joined in 2017 had already chosen it. They distrust a particular database because one deployment went badly, in a context that may have been the real cause.

Nobody involved can see the shape of this. The client hears a confident recommendation and reasonably interprets confidence as evidence. The advisor experiences their opinion as expertise, because it is built on real operational scars, and the fact that it rests on three data points selected non-randomly is not available to introspection. And a practitioner whose formative experience ended five years ago is advising on technologies whose operational character has changed substantially since.

## Why It's Still Broken

**The sample is invisible from inside.** Availability bias does not feel like bias; it feels like knowing. The practitioner cannot enumerate the evidence base for their own opinion because it is not stored as evidence, it is stored as intuition.

**Confidence is the product.** Clients pay for a clear recommendation. An advisor who says "my view here rests on two deployments, one of which was a decade ago" is being more honest and will be perceived as less valuable, which is a real cost borne by the individual for a benefit that accrues to the client.

**No feedback ever arrives.** The recommendation's consequences appear two years later at a company the advisor has left, so the sample never even self-corrects. The eight data points stay eight, and confidence in them grows with repetition rather than with evidence.

**Recency has no mechanism.** Technologies change materially in three years. An opinion formed on a 2019 deployment may be simply out of date, and nothing prompts a practitioner to ask when they last actually operated the thing they are recommending.

**There is nothing to substitute.** Even a practitioner who fully recognises the problem has no better source available — which is the honest reason this persists, and why it needs [[niches/fractional-cto-services/technology-selection/build|🔨 Build: Operational Outcomes at Decision Granularity]] to be genuinely fixable rather than merely disclosed.

## What a Fix Looks Like

**Make the basis explicit in the recommendation.** A standard structure that states, alongside each technology recommendation, what it rests on: direct operational experience and how many deployments and how recently, indirect experience, documented evidence, or vendor material. Not a confession — a provenance line, the way any other professional opinion carries its basis. This is available to any practitioner today at no cost, and it is the intervention with the best ratio of effect to effort.

**Force a recency check.** When did I last operate this in production, at what scale, and what has changed in the product since. A practitioner who cannot answer has learned something useful about their own opinion before the client has to.

**Structured adversarial review inside the practice.** The strongest cheap correction is a colleague with a different history arguing the other side. Firms with more than a handful of practitioners can require it on any recommendation above a threshold, and the diversity of employment histories within a firm is an asset almost none of them use deliberately.

**Record the recommendation as a prediction.** Which technology, on what basis, with the expected operational consequences. Then the six- and eighteen-month check-in from [[niches/fractional-cto-services/assessment-calibration/fix|🔧 Fix: The Recommendation Nobody Follows Up]] applies directly, and the sample of three starts growing for the first time in the practitioner's career.

**Prefer reversibility where evidence is thin.** When the recommendation rests on a weak basis, say so and design for reversal — abstraction at the boundary, a migration path costed in advance, a smaller first commitment. Matching the reversibility of the decision to the strength of the evidence behind it is standard practice in other advisory professions and essentially absent here.

## Who Feels the Pain

The client, who commits years of operational consequence on the basis of an opinion whose evidentiary weight they cannot see and would be surprised by.

The practitioner, who is professionally exposed on recommendations they cannot fully defend, and who over a career is building confidence rather than accuracy because no correction ever reaches them.

The technologies that lost on the basis of one bad deployment in circumstances that were not their fault, and the ones that won because they happened to be present at a company that succeeded for unrelated reasons.

And the next practitioner, who inherits the profession's accumulated folklore without any of the context that produced it.

## Impact If Fixed

A provenance line on recommendations costs nothing and changes the conversation. The client learns which parts of the advice are load-bearing and which are informed guesses, and can weight their own decision accordingly — which is what they were paying for in the first place.

Adversarial review inside a practice surfaces the cases where two experienced people disagree, and disagreement between experts is the single best available signal that the evidence is genuinely thin and the decision should be made reversible.

And recording recommendations as predictions starts the only process that can actually grow the sample: a practitioner who learns, at eighteen months, what happened, has four data points instead of three — and after a decade of that, a materially different quality of judgement from a peer who never looked.
