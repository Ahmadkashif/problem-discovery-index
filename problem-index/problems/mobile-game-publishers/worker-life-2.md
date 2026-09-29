# The Product Manager Who Knows Where the Revenue Comes From

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Type:** Worker Life Changing
**One-liner:** A monetisation manager is targeted on revenue per player, can see that most of it comes from a very small group, and has no instrument that tells them whether any individual in that group is fine.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #causal-inference #evaluation-metrics #compliance #worker-facing

## The Problem
Revenue in free-to-play games is concentrated: a small percentage of players generate the majority of in-app purchase revenue, and within that group the distribution is concentrated again. This is well documented, understood by everyone in the industry, and is the basis of the business model.

A monetisation product manager is measured on revenue per daily active user and on the performance of offers, bundles, progression pacing and limited-time events. The levers that move those numbers work primarily on the high-spending minority, because that is where the money is. So the design work — offer timing, escalating bundles, randomised rewards, progression friction that a purchase relieves — is aimed at a group the manager can see in the data and cannot see in any other way.

The uncomfortable part is that the data distinguishes spending levels and nothing else. A player spending heavily because they are an enthusiast with disposable income and one spending heavily in a pattern that suggests distress look similar in a revenue dashboard, and the industry has built extensive instrumentation for the first question and essentially none for the second. Regulators in several European jurisdictions have taken an interest in randomised reward mechanics, consumer protection bodies elsewhere have examined offer design, and the industry's response has largely been compliance-shaped rather than measurement-shaped.

## Why It Matters to the Worker
This places a person in a genuine ethical position with no tools and no organisational permission to raise it. The manager is targeted on a number they know is produced disproportionately by a small group, and they have no way to distinguish enthusiastic spending from harmful spending, so the question cannot be answered even by someone who wants to answer it.

Many people in these roles do want to. The industry contains a great deal of private discomfort about specific mechanics, discussed among practitioners and rarely in product reviews, because raising it without evidence sounds like an objection to the business model rather than a proposal.

And the career incentive runs one way. Shipping a mechanic that raises revenue is legible and rewarded; proposing a limit on it requires arguing against a measurable gain using an unmeasured harm. That asymmetry is why the discomfort stays private and why the instrumentation never gets built.

## What a Solution Looks Like
Build the second metric. Spending patterns that indicate distress are characterisable from behaviour — rapid escalation, spending concentrated in short sessions at unusual hours, purchases immediately following a loss or a progression block, a sharp change from an established baseline, chargebacks and refund requests. None of this is diagnostic of an individual and all of it is measurable at a population level, which is enough to evaluate a design change.

Evaluate mechanics on both metrics. A limited-time offer that raises revenue and also raises the share of revenue coming from rapid-escalation patterns is a different proposition from one that raises revenue evenly, and reporting both makes that visible in the review where the decision is made. That is the change that converts private discomfort into a discussable fact.

Give the manager interventions that are not refusals. Spend pacing, cooling-off prompts, self-set limits that are easy to find, and suppression of high-pressure offers for players showing distress signatures are all shippable, and several have been shown to cost less revenue than expected — which is exactly the evidence the internal argument needs.

And make the position defensible. A manager who can show the welfare metric alongside the revenue metric is participating in a product decision rather than objecting to one, which is the difference between a concern being raised and a concern being actionable.

## Impact If Solved
This industry's revenue concentration is not in dispute and its effect on the concentrated minority is essentially unmeasured, which leaves a large number of practitioners making design decisions they are privately uneasy about. A population-level welfare metric reported alongside revenue in the same review is a small instrumentation change with a large effect on what gets shipped — and it is the form of self-regulation most likely to be credible when the regulatory attention already directed at this sector increases.
