# App Store Listing Optimisation

**Industry:** [[app-marketing-firms|App Marketing Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The store listing converts every paid click and every organic browse, is optimised with keyword tools built on estimated volumes, and is tested with store experiments most teams run once a quarter.
**Tags:** #bert #word-embeddings #bayesian-inference #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #cnns

## The Problem
Every install passes through a store listing. Icon, screenshots, video, title, subtitle, keyword field, description and rating all determine whether a click becomes an install, and the same listing serves paid traffic from a dozen sources and organic traffic from search and browse — populations with entirely different intent.

Optimisation has two halves and both are weak. Keyword work relies on third-party volume and difficulty estimates derived from panels and scraping, with error characteristics nobody publishes, in a store that exposes almost nothing directly. Creative work relies on store-side experiments, which are available on both platforms, are slow, allow few concurrent variants, and are run infrequently because each one occupies the test slot for weeks.

Custom product pages made the problem more interesting and more neglected: a team can serve a different listing per traffic source, matching the ad's promise to the page. Most teams create a handful and leave them, because building and testing them properly is manual work that competes with the weekly UA fire.

## What Already Exists
AppTweak, Sensor Tower, data.ai and Appfigures provide keyword research, rank tracking and competitive intelligence. SplitMetrics and Storemaven run off-store testing that approximates store experiments with faster turnaround. Both platforms provide native experimentation — Apple's product page optimisation and Google's store listing experiments — and custom product page support. Console analytics report impressions, page views and conversion by source at a coarse grain.

## The Customisation Gap
The tooling treats the listing as one artefact to optimise globally, when the actual opportunity is per-source matching: the screenshots that convert a user arriving from a playable ad about one game mechanic are not the ones that convert a search user who typed a category term. Custom product pages make that addressable and nothing helps a team decide how many pages to build, what each should emphasise, or how to allocate test capacity between them.

Test capacity is the real constraint and is treated as a given. With few concurrent variants and multi-week runs, the sequence of what to test matters enormously, and that is a sequential experimental design problem — which variant to run next given what has been learned and how much traffic is available — that no tool poses. Teams instead test whatever was most recently argued about in a meeting.

Keyword estimates need the same honesty fix as web search tooling: intervals rather than integers, and per-app calibration against the true impression data in the team's own console, which is the only ground truth available and is almost never used to correct the vendor's estimate.

And the creative side could learn from the listing corpus. What distinguishes converting screenshots within a genre — first-screen content, text density, device framing, whether gameplay or outcome is shown — is learnable across many apps and is currently the domain of designer intuition and a quarterly test.

## Impact If Solved
The listing multiplies everything: a conversion rate improvement applies to paid and organic traffic simultaneously and compounds with every dollar of acquisition spend. Sequential test design squeezes far more learning out of a fixed and scarce test capacity, per-source page matching addresses an opportunity the platforms opened and most teams have not exploited, and calibrated keyword estimates stop the planning being built on unstated error.
