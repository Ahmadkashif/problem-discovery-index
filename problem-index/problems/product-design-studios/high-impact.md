# The Redesign Ships and the Studio Never Sees the Number

**Industry:** [[product-design-studios|Product Design Studios]]
**Type:** High Impact
**One-liner:** A studio sells the claim that this design will work better, ships it, and the evidence that would settle the question lands in the client's analytics after the contract has closed.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #time-series-forecasting #revenue-impact #tacit-knowledge-ml

## The Problem
A studio is engaged to redesign a checkout, an onboarding flow, a dashboard. They research, they design, they test with a handful of users, they hand over specifications, and the client's engineering team builds it over the following two quarters. The studio is off the engagement before the first cohort of real users touches the live product.

Everything that would grade the work happens after that point. Completion rate on the flow, drop-off by step, time to first value, support contacts about the redesigned area, retention of the cohort that arrived after launch — all of it accumulates in the client's product analytics, owned by the client's product team, and none of it comes back.

So the studio's evidence base is a portfolio. They know what they made and how it looked; they do not know which of it worked. A designer who has shipped forty onboarding flows has forty opinions about onboarding and zero measurements, and when the forty-first client asks whether the sign-up should be one step or three, the answer is drawn from taste, from what tested well in a five-person usability session, and from what the most senior person in the room believes.

The failure compounds in a specific way. Because the studio cannot demonstrate outcomes, it cannot price on them, so it sells time. Selling time makes the commercial conversation about day rates and headcount rather than about results, which is the reason design services are persistently compared on cost and the reason procurement treats studios as interchangeable.

And when something does go wrong, the studio usually does not learn that either. The most common failure — the redesign gradually reverting as the client's own team makes changes against it — happens entirely after handover and reaches the studio, if at all, as a client who does not return.

## Why It's Unsolved
The engagement structure ends at delivery and nobody has a reason to extend it. The client has no obligation to share performance data, some genuine reluctance to share commercially sensitive numbers with a vendor who also works for competitors, and frequently no clean way to isolate the redesign's effect from everything else that shipped that quarter.

The measurement itself is harder than it looks. A redesign ships alongside pricing changes, marketing campaigns, seasonal effects and a dozen unrelated releases. Establishing what the design did requires either an experiment — which most clients do not run on a full redesign, because a staged rollout of an entire flow is operationally awkward — or a careful quasi-experimental comparison that nobody on either side is staffed to perform.

There is also a commercial disincentive that is rarely said out loud. A studio that measures rigorously will find that some of its work did nothing, and a portfolio of honest results is a harder sell than a portfolio of beautiful screens and a client quote. The first studio to publish outcome data competes against a field that does not have to.

And the knowledge that does exist is tacit and personal. Senior designers carry real pattern knowledge accumulated over years, and it lives in their judgement rather than in anything the firm owns — which is why studios are so dependent on a few individuals and why their quality is so hard to scale.

## What a Solution Looks Like
Contract for the measurement. A post-launch measurement window, with agreed metrics defined before the design work starts and access to the relevant analytics, is a clause rather than a technology. Studios that ask for it find clients more willing than expected, because the client also wants to know.

Design for the comparison. A staged rollout, a holdback cohort, or at minimum a clean pre-post window with the confounding releases enumerated, turns an unanswerable question into an answerable one. This has to be agreed at the start of the engagement, because it constrains how the client ships, and it is the single highest-value thing a studio can negotiate for.

Accumulate at the pattern level, not the project level. Individual projects are too confounded and too few to learn from directly. What transfers is the pattern — steps in a flow, disclosure strategy, defaults, error handling — evaluated across many engagements in comparable contexts. That is the studio's version of the corpus everyone else in this cluster is missing, and it is buildable from thirty engagements rather than three hundred.

Follow the decay. Periodically re-examining a shipped design against the live product tells a studio what survived and what reverted, which is both a service the client will pay for and the only way the studio learns what its handover process actually delivers.

## Impact If Solved
This is the difference between a firm selling taste and a firm selling evidence. Outcome measurement changes what a studio can charge for and how it defends its recommendations, and pattern-level accumulation turns a decade of engagements into an asset the firm owns rather than knowledge that leaves with its principals. For clients it addresses the complaint that runs through every procurement conversation about design services, which is that nobody can say what they bought.
