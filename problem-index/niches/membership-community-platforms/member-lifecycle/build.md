# Measuring the Thing Being Sold

**Niche:** [[niches/membership-community-platforms/member-lifecycle/profile|Member Lifecycle]]
**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is belonging and the dashboard counts posts.
**Tags:** #graph-theory #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #causal-inference #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to keep a paying member who decides in a fortnight and cancels in a quarter — and the contest splits cleanly enough that it is not terminal.

## The Problem
A community platform holds the complete interaction graph of people who paid to be there: who replied to whom, who was ignored, who found a subgroup and who never did — and on the other side, who renewed. That is an unusually clean dataset for the question the category cannot answer, which is what causes someone to stay. The analytics report daily active users and post counts, inherited from social media where the objective was engagement volume rather than whether any individual felt included.

## Why Nobody Has Built This
The analytics were inherited from social platforms, so the metric set describes aggregate activity rather than individual inclusion — a measurement borrowed from a business with a different objective will measure that objective. Belonging sounds unmeasurable, which excused not trying. Churn arrives long after the cause, so nobody connected them. And activity counts go up when a community is loud, which is reassuring and frequently wrong.

## What to Build
Measure inclusion and act on both ends of the lifecycle. Define and compute member-level connection from the reply graph — did anyone answer them, did anyone address them by name, do they have reciprocal relationships, are they in a subgroup — which is the core and is the measurement the category lacks. Get the first fortnight right, since that is when the decision is made and it is a matching problem. Detect the silent disengagement, since that is where the revenue is lost and it is a prediction problem. Validate the connection measure against renewal, which is the clean outcome and makes the whole thing testable rather than theoretical. Report at member level rather than in aggregate, because a community can be busy and still be failing most of the people in it. Identify the members who are connected to nobody, which is a specific and short list in most communities. Distinguish the lurker who is content from the newcomer who was ignored, as they look identical in activity metrics and are opposite situations. Give the founder the list of people to reach rather than a dashboard, since that is what they can act on. Test interventions against renewal, as the surface is clean and nothing is currently tested. And replace activity metrics as the headline, because what is reported is what gets managed.

## Target Customer
Product and community leadership, community founders and operators, members who never connected, and community analytics vendors.

## Impact If Built
A measurement borrowed from a business with a different objective will measure that objective, which is why belonging is reported as post counts. The reply graph joined to renewal is the cleanest available test of what actually makes someone stay.
