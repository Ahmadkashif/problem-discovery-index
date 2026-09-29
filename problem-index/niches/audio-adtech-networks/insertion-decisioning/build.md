# Serving Solved, Deciding Basic

**Niche:** [[niches/audio-adtech-networks/insertion-decisioning/profile|Insertion Decisioning]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dynamic insertion can choose what plays in every slot for every listener, and the decision is made by a priority order and a frequency cap.
**Tags:** #convex-optimization #gradient-boosting #optimization-fundamentals #evaluation-metrics #confidence-intervals #revenue-impact #dynamic-programming #automation
**Contested on:** Every serious competitor in this niche is fighting to decide which advertisement goes into which slot of which episode for which listener — and whoever optimises that properly extracts more value from the same inventory than anyone bidding harder can.

## The Problem
The infrastructure can place any advertisement in any slot for any listener. What it is asked to do is fill slots in priority order, subject to a frequency cap and a targeting filter. Nobody optimises the joint decision: which advertiser's message suits this show's audience, whether the mid-roll or the pre-roll serves this campaign better, whether this listener has heard a competing product's advertisement in another show today, whether the advertisement sits jarringly against the content around it, and what the sequence within an episode should be. The capability is well ahead of the decisioning, which is unusual and is a straightforward opportunity.

## Why Nobody Has Built This
Serving was the hard engineering problem and once it worked the decisioning layer inherited the simplest possible logic — the infrastructure milestone became the product and nobody revisited what it should be asked to do. Better decisioning requires an objective, which requires the exposure and outcome measurement the channel lacks. Priority order is comprehensible to sellers and an optimiser is not. And revenue arrives either way.

## What to Build
Optimise the joint decision. Rank candidates by expected value to the publisher rather than by priority order, incorporating exposure probability at that position, the advertiser's payment and the listener's likely response — which is the core and is the same reformulation retail media needs, applied to a smaller and more tractable inventory. Choose the position within the episode rather than accepting a convention, since the position is a decision variable and the exposure model makes it optimisable. Sequence within an episode, because two advertisements in adjacent slots interact and nothing currently considers that. Cap frequency across the listener's whole audio consumption rather than per show, which is the most common listener complaint and is solvable because the platform sees the whole session history. Consider the surrounding content, since an advertisement landing against a jarring segment damages both the brand and the listening experience and is avoidable. Balance host-read and inserted inventory in the same decision, since they compete for the listener's tolerance even when they are sold separately. Model listener fatigue explicitly, connecting to the same problem in messaging, as audio tolerance is finite and is currently spent without accounting. Learn from response where any signal exists. Keep the mechanism explicable to sellers, since a decisioning layer nobody understands will be overridden. And measure yield per listening hour rather than per slot, because that is the honest unit of a finite listener resource.

## Target Customer
Audio platforms and hosting providers, publisher yield teams, and the networks whose serving capability exceeds their decisioning.

## Impact If Built
The serving milestone became the product and nobody revisited what the decisioning should be asked to do. Ranking by expected publisher value including exposure probability, and capping frequency across the listener's whole consumption, use capability that is already deployed.
