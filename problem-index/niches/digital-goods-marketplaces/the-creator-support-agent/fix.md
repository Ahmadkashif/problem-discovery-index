# The Hold on a Good Month

**Niche:** [[niches/digital-goods-marketplaces/the-creator-support-agent/profile|The Creator Support Agent]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** A creator's asset is featured, sales rise tenfold, the risk system reads it as fraud, and the best month of their career becomes the month they were not paid.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #quick-win #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to let the support agent explain a risk decision to the person it affects — and whoever makes automated holds explainable turns the category's worst customer interaction into an ordinary one.

## The Problem
A creator's work is featured in a newsletter, or picked up on social media, or included in a bundle. Sales go from forty a month to six hundred in a week. The risk model, which learned that sudden volume spikes accompany fraud, places a hold. The creator — six years on the platform, clean history, real identity, genuine work — is told their earnings are unavailable for an unspecified period, at the exact moment their business finally worked. The platform caused the spike by featuring them. Nothing in the risk decision considered that.

## Why It's Still Broken
Velocity is a strong generic fraud feature and is applied without conditioning on what the platform itself did, which is the specific defect. Risk models are trained on fraud labels where sudden volume genuinely is predictive, and the legitimate spike population is small enough to be absorbed as false positives. Merchandising, marketing and risk do not share state. And the harm is invisible in aggregate model metrics.

## What a Fix Looks Like
Condition the risk decision on what the platform knows it caused. Feed featuring, bundling, newsletter placement and promotion events into the risk system, which is the fix, is a straightforward integration, and removes a large share of the worst false positives outright — the platform caused the spike and should not be surprised by it. Weight account tenure and history properly, since a six-year clean account and a two-week-old one presenting the same velocity are not the same risk and treating them alike is the model's laziest failure. Use graduated responses instead of a full hold: partial release, a delayed portion, or extra verification, since the binary is disproportionate for a probabilistic signal. Release progressively as the spike is corroborated by clean deliveries, low refunds and satisfied buyers, which is evidence arriving continuously and currently ignored. Detect the organic spike pattern specifically, as viral legitimate growth and fraud velocity have different shapes across buyer diversity, geography and payment methods and are separable. Trigger a proactive contact before the hold rather than after, which turns a distressing surprise into a manageable check. Track false positive rate on holds by account segment, which is not currently reported and is the number that would force the change. Fast-path resolution for accounts with long clean histories, since the expected loss is small and the relationship damage is large. Measure creator churn following holds, which is the real cost and is currently unattributed. And review the worst cases as incidents, because a creator paid nothing in their best month is a product failure rather than a model outcome.

## Who Feels the Pain
Creators penalised for success; support agents defending a decision they know is wrong; and platforms losing exactly the creators whose work was good enough to break through.

## Impact If Fixed
The platform caused the spike by featuring the creator and its risk system was surprised by it. Feeding promotion events into the risk decision is a straightforward integration that removes the worst false positives, and progressive release as deliveries clear uses evidence already arriving.
