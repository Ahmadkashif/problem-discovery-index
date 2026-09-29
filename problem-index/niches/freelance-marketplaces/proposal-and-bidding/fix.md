# Fix: Six Proposals, No Replies, No Explanation

**Niche:** [[niches/freelance-marketplaces/proposal-and-bidding/profile|Proposal & Bidding]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** An evening spent writing six tailored proposals, paid for in platform credits, produces no replies and no explanation, and next week it happens again.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #logistic-regression #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Whether the platform will tell a freelancer what happened to the proposals they already paid to send.

## The Problem

A freelancer sends six proposals on a Tuesday evening. Each one took twenty minutes to tailor. Each cost credits. By the following week: no replies. Not rejections — silence. The proposals sit in a list marked as submitted, indefinitely.

What actually happened to each of them is recorded in the platform's database. The job was awarded to someone else on Thursday. The job was never awarded and the post expired. The client never opened a single proposal. The client viewed this proposal for four seconds. The post was removed for policy reasons. Each of these is a completely different piece of information for the freelancer, and none of them is shown.

The absence is not a modelling gap. It is a status field that exists and is not displayed.

## Why It's Still Broken

Partly it is a product oversight that has calcified: the proposal list was built as a submission record rather than a pipeline view, and nobody revisited it. Partly it is a concern about the demand side — clients might post less freely if they knew freelancers could see that they never opened anything, and platforms protect client posting volume above nearly everything.

And partly it is that the aggregate version of this information is uncomfortable. A freelancer who could see that eleven of their last twenty proposals went to posts nobody was ever hired for would draw an obvious conclusion about what the credits bought, and might draw it out loud.

## What a Fix Looks Like

Show the outcome of every proposal, as a status that updates, from data already in the database.

Per proposal: viewed or not, with time; shortlisted or not; the post's outcome — awarded to someone else, expired unawarded, withdrawn by the client, removed — with a date. No modelling, no new data collection, no client-identifying detail beyond what the platform already publishes. The decisive distinction, and the one worth building the feature for on its own, is between *awarded to someone else* and *never awarded to anyone*, because those two outcomes should lead a freelancer to completely different conclusions about their proposal and they currently look identical.

Then aggregate it back to them honestly. Of your last fifty proposals: this many were viewed, this many shortlisted, this many went to posts that hired nobody at all. Alongside the same three numbers for the median freelancer in their category, so the freelancer can tell whether the problem is their proposals or the feed they are bidding into. These are counts over a table, computable today.

Refund or credit automatically where the platform monetises bids and the post was never awarded, or was removed for policy reasons. A freelancer charged to bid on a job the platform later determined was not real, or on a post that expired without a hire, has an obvious claim, and handling it automatically costs less than handling it through support and far less than handling it through resentment.

Close the loop on the client side too: a client whose posts routinely expire unawarded should hear about it, because in most cases it reflects a fixable post rather than bad intent.

## Who Feels the Pain

Freelancers, especially newer ones with thin pipelines who cannot absorb wasted evenings and are the most likely to leave. Support agents who take "why did nobody reply" tickets and have no view into proposal state either. And the platform, which funds its bid revenue out of supply-side goodwill and does not measure the balance.

## Impact If Fixed

A freelancer learns which of their proposals failed on merit and which failed because there was nothing to win, which is the difference between improving and quitting. The feature is a status display over existing fields, which makes it among the cheapest meaningful improvements available anywhere in this industry, and its absence is the clearest statement of whose interests the bidding flow is designed around.
