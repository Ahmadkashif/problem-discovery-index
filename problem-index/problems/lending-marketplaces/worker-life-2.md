# The Partner Manager Between Two Complaints

**Industry:** [[lending-marketplaces|Lending Marketplaces]]
**Type:** Worker Life Changing
**One-liner:** Partner managers defend lead quality to lenders and negotiate bids upward, using reports that cannot answer the lender's actual question because the answer lives in the lender's own systems.
**Tags:** #gradient-boosting #causal-inference #bert #confidence-intervals #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

## The Problem
The lender says the leads are bad. Approval rates are down, cost per funded loan is up, and they want a lower price or fewer leads or a different mix.

The partner manager has the marketplace's data: volume delivered, credit band distribution, source mix, and whatever funding notifications the lender returns. What they cannot see is the lender's own decisions — which leads were declined and why, what the underwriting changed, whether the shift is in the traffic or in the lender's own criteria.

Often it is the lender's criteria. They tightened underwriting, or a model was retrained, or their funding cost moved, and the resulting decline in approvals arrives as a complaint about lead quality. The partner manager suspects this and cannot demonstrate it.

Meanwhile the internal conversation runs the other way. Revenue teams want bids raised and volume increased. Compliance wants contact practices constrained. Product wants ranking changes the lender will not like.

The negotiations are frequent, high-stakes and evidence-poor. Renewals turn on a conversation about quality in which neither side can show the other the data that would settle it.

## Why It Matters to the Worker
The role is accountable for a relationship whose central metric is computed in someone else's system. Being blamed for something you cannot measure, repeatedly, by the person who holds the measurement, is a specific and grinding form of professional frustration.

Escalation is unpleasant in both directions. Telling a lender their own underwriting changed requires evidence the partner manager does not have; telling internal teams that a demanded volume increase will damage the relationship requires the same.

Concentration makes it worse. A handful of lenders usually account for most revenue, so a single relationship deteriorating is a company-level event carried by one person.

And the analysis is manual. Each of these conversations is preceded by hours of assembling numbers by hand, which is the part of the job with the least judgement and the most time.

## What a Solution Looks Like
Decomposition of approval rate changes into traffic mix versus lender behaviour. If the profile distribution is unchanged and approvals fell, the change is on the lender's side, and that is computable from data the marketplace holds even without decision returns. It is the single most valuable artefact this role could be given.

Cohort-consistent reporting. Comparing like traffic across periods rather than raw aggregates removes most of the disputes, because most of them are composition effects nobody has controlled for.

Cross-lender benchmarking, presented carefully. The marketplace knows how comparable lenders convert similar profiles, and even an anonymised percentile tells a lender whether their problem is the traffic or themselves.

Early warning on relationship health. Bid changes, volume acceptance, response latency and complaint tone all move before a renewal goes badly, and a ranked relationship risk list turns a surprise into a plan.

Automated preparation. The recurring quarterly review deck is an assembly job that consumes hours and should be generated, leaving the manager to do the part that requires them.

## Impact If Solved
Partner relationships are where marketplace revenue is actually determined, and they are negotiated with reports that cannot address the question being asked. Decomposing approval changes into traffic and lender components gives the role its missing argument, and early relationship risk detection converts the worst surprises in the business into something manageable.
