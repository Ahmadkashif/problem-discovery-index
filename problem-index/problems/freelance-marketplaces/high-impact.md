# The Ranking Sets the Income and Nobody Will Explain It

**Industry:** [[freelance-marketplaces|Freelance Marketplaces]]
**Type:** High Impact
**One-liner:** A freelancer's earnings depend on where an algorithm places them, the placement changes without notice, and the explanation available is a help article about best practices.
**Tags:** #gradient-boosting #graph-neural-networks #confidence-intervals #causal-inference #evaluation-metrics #hypothesis-testing #compliance #worker-facing

## The Problem
On a marketplace, visibility is income. A freelancer who appears on the first page of search results for their category receives invitations and proposals convert; one who does not, does not. That position is set by a ranking system combining job success metrics, response rate, earnings history, recency of activity, client ratings, badge tier, and whatever else the platform weights.

Freelancers experience the system as weather. Earnings drop by half over a month with no change in their behaviour, and the available explanations are a help centre page listing general best practices and a support agent who cannot see the ranking inputs either. Community forums fill with theories, and the theories are frequently wrong in ways that lead people to change things that were not the problem.

The tier and badge systems concentrate the effect. Qualifying for a top tier materially changes visibility, the qualification criteria include metrics with thresholds, and falling below a threshold — sometimes because of a single client interaction — removes the tier and the income with it. The mechanism is a cliff, and a cliff applied to someone's livelihood by an automated calculation they cannot inspect is a serious thing.

Ratings feed into all of it and carry their own problems. Distributions are compressed near the maximum, so a single four-star rating is a substantial negative signal; low-volume freelancers are therefore extremely exposed to one difficult client. And ratings reflect client behaviour as well as freelancer performance — a client who rates everyone harshly, or who rates differently depending on who they are dealing with, injects that into the score. Rating disparities by demographic characteristics are a documented phenomenon in platform work, and the platforms hold the data that would establish whether it occurs on their own marketplaces.

## Why It's Unsolved
The platform's stated reason is gaming: a ranking whose weights are published will be optimised against, and marketplaces already fight substantial manipulation — fake reviews, account selling, collusive transactions. That concern is real.

It is also incomplete as a justification, because it argues against publishing weights and not against explaining an individual's change. Telling someone that their ranking fell primarily because their response time rose in a specific period does not hand anyone a manipulation strategy they did not already have, and it is the difference between a person who can act and a person guessing.

The deeper obstacle is that the platform and the freelancer are not aligned here. A marketplace optimises for client outcomes and transaction volume; a freelancer wants durable, explicable earnings. The ranking is tuned for the first, and its instability is a cost borne entirely by the second.

Rating bias is the most uncomfortable item. Analysing whether ratings differ systematically by freelancer demographics or by country, controlling for work quality, is technically straightforward for a platform and legally and reputationally hazardous, since a finding of disparity creates an obligation to act on it. That asymmetry is a strong reason not to look.

## What a Solution Looks Like
Explain the individual change, not the model. When a freelancer's ranking or tier moves, the platform should say which inputs drove it and in what direction, over what period. This is attribution against a model the platform already computes, it is deliverable per person, and it does not require publishing weights.

Calibrate ratings for the rater. A client's rating distribution is observable across all their engagements, and adjusting a freelancer's score for rater harshness is an ordinary statistical correction that would make reputation a better signal of the freelancer and a worse signal of who they happened to work with. Platforms have the data and do not do it.

Report uncertainty on low-volume profiles. A score from four ratings is not comparable to one from four hundred, and presenting both as a number with one decimal place misleads clients and punishes new entrants. A shrunken estimate with an interval is more honest and removes the single-bad-rating cliff.

Audit for disparity and publish it. Whether ratings and rankings differ by demographic characteristics, controlling for observable work outcomes, is answerable from the platform's own data. Publishing it is uncomfortable and is the only thing that makes the system accountable rather than merely opaque.

And soften the cliffs. Tier thresholds that produce discontinuous income changes should be graduated, with warning before a threshold is crossed and a defined path back — which is a product decision rather than a technical one.

## Impact If Solved
This determines the earnings stability of a large working population whose income is allocated by a system they cannot see. Individual-level explanation converts a capricious experience into an actionable one, rater calibration and shrunken estimates make reputation measure the freelancer rather than their luck with clients, and disparity auditing is the accountability mechanism that currently does not exist anywhere in this market.
