# Bidding a Six-Month Payback on Three Days of a Coarse, Delayed Signal

**Industry:** [[app-marketing-firms|App Marketing Firms]]
**Type:** High Impact
**One-liner:** Acquisition economics require predicting six-month user value from the first few days, and on iOS those days arrive as a few bits, with a random delay, nulled out entirely when the campaign is small.
**Tags:** #survival-analysis #bayesian-inference #gradient-boosting #confidence-intervals #probability-distributions #maximum-likelihood-estimation #evaluation-metrics #revenue-impact

## The Problem
A user acquisition team pays to install today and recovers the cost over months through purchases, subscriptions or ad revenue. The decision of what to pay must be made now, which means predicting long-run value from early behaviour. Before 2021 that prediction used rich user-level data: which events a user fired, when, how often, from which campaign and creative.

App Tracking Transparency removed the identifier for most iOS users, and SKAdNetwork replaced user-level attribution with an aggregated postback. The postback carries a campaign identifier, a conversion value the developer defines within a small number of bits, and it arrives after a deliberately randomised delay. When a campaign's volume falls below a privacy threshold, the campaign identifier is suppressed and the postback arrives without saying where the install came from — which is exactly the situation for every new campaign, every small geography and every test.

So the model that sets bids is trained on a compressed, delayed, partially anonymised summary of the first day or two, to predict revenue six months out. The compression is chosen by the team, usually once, at launch. Every subsequent modelling improvement is bounded by how much information that schema preserved, and most teams have never measured what theirs throws away.

The measurement problem sits on top. Each network self-attributes and reports its own installs and revenue; the MMP applies its own logic; SKAN reports something aggregated and delayed; finance reports actual revenue. None reconcile. A UA manager allocating a substantial budget across networks is comparing numbers produced by parties with an interest in the comparison.

## Why It's Unsolved
The constraint is imposed by a platform owner for privacy reasons, is not negotiable, and is tightening rather than loosening — AdAttributionKit continues the design, and Android's Privacy Sandbox is heading the same way. There is no version of this problem where the data comes back.

The statistical difficulty is real. Predicting a heavy-tailed long-run outcome from a few days of compressed signal, where a small fraction of users generate most of the revenue, means the quantity that matters is concentrated in the tail that early signals identify worst. Add a randomised delay and threshold-based suppression and the training data is not merely noisy but missing non-randomly — small campaigns are systematically less observed, which biases exactly the exploration a UA programme depends on.

The conversion value schema is a genuinely hard design problem that has been treated as a configuration task. Choosing what a handful of bits should encode, so as to maximise the information available to a downstream predictive model, is an optimisation with a clear objective and an enormous search space, and it interacts with the app's own event taxonomy and revenue distribution. Almost nobody optimises it; they pick revenue buckets and move on.

And validation is largely absent. Network-reported ROAS is not checked against incrementality, and the tests that would check it — geo splits, public service announcement campaigns — are run by a minority, usually once, usually on the largest network, and usually not repeated.

## What a Solution Looks Like
Design the conversion value schema as an optimisation. Given the app's event taxonomy, revenue distribution and the bits available, choose the encoding that maximises mutual information with long-run value, evaluated on historical cohorts where the truth is known. This is directly computable, it is the highest-leverage single decision in the entire measurement stack, and revisiting it as the app changes is a quarterly exercise nobody performs.

Model the censoring and the suppression explicitly. Delay is known and its distribution is published; threshold suppression is a missingness mechanism that depends on campaign size, which means it can be modelled rather than ignored. A predictor that treats suppressed postbacks as absent data biases against small campaigns; one that models the mechanism recovers usable information from them.

Predict a distribution, not a point. Lifetime value in these apps is heavy-tailed and the decision is a bid, so what matters is the expected value including the tail and the uncertainty around it. Reporting a predicted ROAS point estimate for a three-day-old cohort is the single most common source of overconfident scaling decisions in the discipline.

Anchor to incrementality on a schedule. Geo holdouts and PSA tests give an unbiased read on what a network actually adds, and running them continuously across networks — rather than once, on the biggest one — turns self-reported performance into something with a known correction factor.

## Impact If Solved
This decision allocates the great majority of a mobile app's marketing budget and determines whether the business is buying growth or buying losses, on a signal that is structurally impoverished and getting more so. Schema optimisation alone typically recovers more predictive power than any amount of model tuning downstream, and it is a one-week analysis almost nobody has run. Combined with honest uncertainty and a standing incrementality correction, it is the difference between a UA programme that scales into a profitable cohort and one that discovers the truth at the six-month mark.
