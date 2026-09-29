# Proposal & Bidding

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** Low Digitized
**Contested on:** Whether a freelancer can know, before writing a proposal, that the job will ever be awarded to anyone.

## Profile
**Market Size:** ~$1.96B — 14% of platform-intermediated gross services volume
**Share of Parent Industry:** ~14%
**Digital Adoption:** Low — the platform's contribution is a text box and a credit counter
**Target Buyer:** Platform product and monetisation leadership; freelancers directly
**Automation Potential:** High on the prediction side; the writing itself is deliberately not the target

## What Makes This a Distinct Niche

Bidding is where the supply side's unpaid labour accumulates. A freelancer writes a tailored proposal, often paying platform credits to submit it, against a job post that in a large fraction of cases is never awarded to anyone. The client posted to gather price information, or to compare against an internal estimate, or hired someone they already knew, or simply lost interest.

The platform knows which posts these are. It has years of job posts with their eventual outcomes, and the features that predict award — client hiring history, budget realism relative to the stated scope, post specificity, verification status, time of posting, how the client behaved on their last three posts — are all in its own database.

The niche is distinct because the contested resource is the freelancer's time, and because the platform's monetisation frequently runs directly against telling them the truth about it. On credit-based platforms, a bid is a unit of revenue, and a system that told freelancers which jobs were not worth bidding on would sell fewer of them.

## Current Tools & Gaps

Platforms show a job's proposal count, the client's total spend, their hire rate in some cases, and their verification status. A few surface "client is likely to hire" style hints derived from thin heuristics. Third-party tools scrape job feeds and offer filtering, and a cottage industry of proposal-writing services and AI assistants has grown up around the problem of producing more proposals faster — which is the opposite of the fix.

The gap is a calibrated per-post probability that the job will be awarded at all, shown before the freelancer commits time or credits. It is a well-posed prediction problem with abundant labels, and it does not exist because building it costs the platform revenue.

## Problems
- [[niches/freelance-marketplaces/proposal-and-bidding/build|🔨 Build: Award Probability Before the Proposal Is Written]]
- [[niches/freelance-marketplaces/proposal-and-bidding/buy|🛒 Buy: Lead Scoring Adapted to a Market Where the Lead Pays]]
- [[niches/freelance-marketplaces/proposal-and-bidding/fix|🔧 Fix: Six Proposals, No Replies, No Explanation]]
