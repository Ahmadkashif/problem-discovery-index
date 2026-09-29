# Fix: The First Contract Is a Lottery

**Niche:** [[niches/freelance-marketplaces/onboarding-and-verification/profile|Onboarding & Verification]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** A capable newcomer and an incapable one are indistinguishable to every mechanism on the platform, so the first contract goes to whoever bids lowest.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #logistic-regression #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Whether the platform will spend a small amount of exposure to learn which newcomers are good, rather than leaving price to decide.

## The Problem

A new freelancer has no outcome history, so the ranking cannot place them, clients will not choose them, and the only available differentiator is price. They underbid, win a contract at a rate that will anchor their pricing for a year, and hope the first client rates generously. Whether they are capable or not barely enters into it.

The platform's own interest is damaged too. Its ranking is trained on outcomes, it observes outcomes only for people it ranks, and it ranks on outcomes — so the unproven pool stays unproven except for whoever underbids enough to escape it. The marketplace never learns which of its newcomers were good, and systematically converts capability into a price competition.

## Why It's Still Broken

Every mechanism on the platform assumes history. Ranking, reputation, tier assignment and bid-award prediction all take outcome features as input, and their treatment of a missing value is a default that sits near the bottom. Nobody designed this; it is the emergent behaviour of four independent systems all handling the same absence the same way.

Deliberately giving exposure to unproven freelancers is the obvious remedy and nobody funds it, because it costs measurable ranking quality now in exchange for a diffuse improvement later. The exploration trade is well understood in the abstract and is almost never made concrete enough to approve.

And the accumulated evidence outside the platform is ignored entirely. A newcomer frequently has years of relevant work, verifiable references and a substantial portfolio. None of it enters any mechanism, because there is no field for it.

## What a Fix Looks Like

Fund exploration explicitly, and use every scrap of signal that already exists.

Give unproven freelancers a bounded exposure allocation: a small, deliberate share of impressions in each category reserved for people without outcome history, matched to queries where their stated skills fit. Price it honestly as a ranking-quality cost and track its return — how many of the explored convert into freelancers who complete well. On most marketplaces this cost is small and the return has never been measured, which is why nobody can argue for it.

Use the graduated signals already available before any modelling. Profile completeness and specificity. Verified identity. Portfolio presence. Response latency on their first few messages, which is observable from the first day. Proposal quality, which is readable. Off-platform references where they offer them. None of these is strong on its own, and a composite prior built from them is far better than the default that currently applies.

Let the first contract be small on purpose. A structured first engagement — capped value, clear scope, milestone-based — reduces the client's risk of choosing an unproven freelancer, which is the actual barrier. Several categories support this naturally and no platform packages it.

Fix the ratings arithmetic for this population, which is the same problem as elsewhere and bites hardest here: a newcomer's first rating moves their score more than any later rating will, so display intervals and sample sizes and apply tier thresholds to the lower bound. A harsh first client should not be able to define someone's first year.

Measure the cohort. Track newcomer time-to-first-contract, first-contract rate relative to their quoted rate, and six-month survival, by category and corridor. No platform reports these, so nobody knows how badly the cold start performs or whether anything they did changed it.

## Who Feels the Pain

New freelancers, who are pushed into underbidding regardless of ability, and disproportionately those from lower-cost countries for whom price competition is the only entry the platform offers. Clients hiring from the unproven pool with no signal to go on. And the platform, which loses most of its new supply before it ever learns whether that supply was good — the single largest source of wasted acquisition in the industry.

## Impact If Fixed

Newcomers get a route to a first contract that runs on evidence rather than on price, which is the point where the market's downward rate pressure is generated. The platform starts measuring its own cold-start performance, which it currently cannot state. And the ranking gains outcome data on a population it has never observed, which improves it for everyone.
