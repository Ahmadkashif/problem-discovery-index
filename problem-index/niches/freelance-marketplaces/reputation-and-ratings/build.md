# Build: Rater-Calibrated Reputation

**Niche:** [[niches/freelance-marketplaces/reputation-and-ratings/profile|Reputation & Ratings]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Separate a freelancer's performance from the harshness of the clients who rated them, using the platform's own rating history and a hierarchical model with rater effects.
**Tags:** #bayesian-inference #hypothesis-testing #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #expectation-variance-covariance #worker-facing #revenue-impact
**Contested on:** Whether rater harshness can be estimated well enough to correct scores for freelancers with only a handful of ratings.

## The Problem

A rating is a measurement made by an instrument — a client — with its own zero point and its own scale. Some clients never give five stars. Some give five stars reflexively. Some rate a four for work they were entirely happy with because four seems like a good grade. The variance between clients on identical work is large, and on a marketplace it is the dominant source of variance in any freelancer's displayed score.

The platform averages these measurements and publishes the result as a property of the freelancer. For someone with two hundred ratings the rater effects wash out. For someone with eight — which is most of the supply side — the score is mostly noise about who hired them, and that noise determines their ranking, their tier and their rate.

## Why Nobody Has Built This

The simplest reason is that raw averages are legible and a corrected score is not. A platform that displays 4.6 when the ratings average 4.3 has to explain itself, to clients who will suspect inflation and to freelancers who will suspect manipulation, and the explanation involves hierarchical models.

There is a second reason that is more interesting. Correcting for rater harshness partially neutralises a demanding client's ability to punish, and platforms are cautious about anything that reduces the demand side's leverage — the clients are the ones bringing money. A calibrated score is, in a small way, a transfer of power toward the supply side, and nobody is paid to make that transfer.

And there is a genuine identification problem. Rater effects are only estimable where raters overlap — where the same clients rate multiple freelancers and the same freelancers are rated by multiple clients. On a marketplace with a long tail of clients who hire once and never return, a substantial share of ratings come from raters about whom nothing can be estimated, and pretending otherwise produces a confidently wrong correction.

## What to Build

A hierarchical rating model that estimates freelancer quality, client harshness and their uncertainties jointly, and that is honest about which ratings it can correct.

The core is standard and well understood: a model in which an observed rating is a function of a freelancer effect, a rater effect, a contract-type effect and noise, fitted across the platform's entire rating history. Bayesian estimation is the right frame because the quantity that matters operationally is not the point estimate but the interval — a freelancer with three ratings has a genuinely uncertain score and the system should say so rather than displaying a precise-looking average.

Handle the identification problem explicitly rather than around it. Clients with several ratings across different freelancers have estimable effects. Clients with one rating do not, and the correct treatment is to shrink them to the population prior and widen the interval accordingly. The connectivity structure of the rating bipartite graph determines how much correction is possible, and it is worth computing and reporting — on most marketplaces a surprisingly large connected core exists, built by repeat clients, and that core anchors the scale for everyone.

Add the covariates that are confounded with harshness so they are not absorbed into it. Contract value, project duration, category, whether the scope changed mid-contract, whether the client has rated harshly in categories where they have more experience. A client who rates low on every contract is harsh; a client who rates low only on contracts that ran over scope is telling you something real.

Present it with the uncertainty intact. A score with an interval, a sample size, and — crucially — a plain statement of what the correction did and why. The presentation is the hard part and it is where the project lives or dies: "4.6 (4.2–4.9, 8 ratings, adjusted for raters who rate below platform average)" is defensible in a way a bare corrected number is not.

Validate against outcomes, not against the raw average. The test is whether the calibrated score predicts subsequent contract completion, client repeat rate and dispute incidence better than the raw score does. It should, substantially, for low-count freelancers, and that improvement is the whole business case.

## Target Customer

Platform product leadership. The argument is matching quality rather than fairness, because matching quality is the one that gets funded: a calibrated score improves the ranking that consumes it, reduces the number of clients who hire someone who looked good and was not, and gives new freelancers a score that reflects their work rather than their luck in first clients.

## Impact If Built

The most consequential number on the platform starts measuring the thing it claims to measure. New freelancers stop being permanently disadvantaged by a harsh first client, and experienced freelancers stop being advantaged by generous ones. The ranking improves because its most heavily weighted input gets less noisy. And the platform gains the calibrated quality estimate that dispute triage, fraud detection and bid-award prediction all want and none of them currently have.
