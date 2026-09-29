# Drawing the Open-Core Boundary

**Industry:** [[open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Feature flagging and licence enforcement are entirely solved, and where the line between free and paid should sit is redrawn every year or two by argument, because nobody can measure which features actually drive purchase.
**Tags:** #causal-inference #logistic-regression #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
An open-core company must decide which capabilities are free and which are commercial. The decision determines both adoption and revenue, and the two pull against each other: a generous open edition drives adoption and may leave nothing worth buying, while a restrictive one drives revenue among those who convert and suppresses the distribution the strategy depends on.

The conventional heuristics — enterprise features like single sign-on, audit logging, fine-grained access control and multi-cluster management go in the paid tier — are folklore that has calcified into practice. They are approximately right and nobody knows how right, or which specific features are actually doing the work.

The decision is revisited under pressure, usually when growth disappoints or when a hyperscaler starts offering the software as a service. Then features move behind the licence, the community reacts, and the company discovers whether it guessed correctly by watching what happens next. Several licence changes across this category were precisely this, and some went badly.

Meanwhile the evidence is unavailable because free usage is unmeasured, which is the same problem as adoption invisibility appearing in its most expensive form.

## What Already Exists
Feature flagging and licence key enforcement are technically trivial and universally implemented. Trial and evaluation flows are standard. Usage-based licensing is available. Competitive analysis of where other companies drew the line is easy, since the boundaries are public. Sales teams have qualitative views about what customers ask for.

## The Customisation Gap
Attribution between a feature and a purchase is the missing measurement. Which capabilities customers actually adopt after buying, which they cite in evaluations, and which correlate with expansion and retention are all knowable from the commercial side and are rarely analysed with any rigour.

Trial behaviour is the most direct signal and is under-used. Which features are exercised during an evaluation, in what order, and which sessions convert, is a clean dataset that most of these companies hold and analyse impressionistically.

The counterfactual for a boundary change is genuinely hard and can be approached honestly. Moving a feature behind the licence is a change whose effect on adoption, conversion and community sentiment is observable if measurement is set up beforehand — and it never is, because the changes are made under pressure with no time to instrument.

Community sentiment measurement matters here more than in most categories, because the cost of a boundary change is partly reputational and is currently assessed by reading social media anxiously.

## Impact If Solved
The open-core boundary determines the economics of the entire category and is set by folklore and redrawn under duress. Measuring which features drive purchase — from trial behaviour, adoption after purchase and expansion — turns the most consequential recurring decision in these companies from an argument into an analysis.
