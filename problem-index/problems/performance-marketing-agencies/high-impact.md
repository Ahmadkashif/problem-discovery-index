# Every Platform Reports Its Own Conversions and They Sum to More Than the Business Made

**Industry:** [[performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** High Impact
**One-liner:** The allocation decision an agency is paid to make is made against numbers each platform reports about itself, which double-count, use incompatible windows, and cannot be added together.
**Tags:** #causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #time-series-forecasting #evaluation-metrics #revenue-impact

## The Problem
A client spends across Google, Meta, TikTok, Amazon and a demand-side platform. Each reports conversions it claims credit for, on its own attribution window — seven-day click and one-day view here, thirty-day click there — using its own identity graph and its own modelled conversions filling the gaps where tracking failed. Add them up and the total exceeds the orders the business actually took, often substantially. Every practitioner knows this. Every weekly report contains the sum anyway, sometimes with a note.

From that the agency must decide where the next dollar goes. There is no valid comparison available: a platform that counts view-through will always look better than one that does not, a platform with better logged-in coverage will always claim more of a shared customer, and a platform that models unobserved conversions is reporting a number partly produced by its own model of its own value. The incentive gradient runs one way and every platform is on it.

The workarounds all have a known failure. Last-click in the client's analytics undercounts everything upper-funnel and rewards branded search, which is mostly demand the client already had. Multi-touch attribution is correlational and assigns credit according to whatever rule was configured. Platform-reported ROAS is the number in the QBR because it is the number the platform shows.

Marketing mix modelling has returned as the serious answer, and it is genuinely better — but it is slow, needs years of history, produces channel-level answers when the decision is campaign-level, and is sensitive to specification in ways most implementations do not report. An agency that runs one annually is answering last year's question.

## Why It's Unsolved
The measurement each platform provides is a product feature of a company selling the media, and there is no neutral referee. The industry-standard fix — incrementality experiments — costs money the client must agree not to spend, and produces answers that are frequently unwelcome to the agency as well, since a channel shown to be non-incremental is a channel with a smaller budget and therefore a smaller fee.

Statistical power is a real barrier at the scale most advertisers operate. A geo holdout on a mid-sized account detects only large effects; a conversion-lift test inside a platform is run by the platform and measures what the platform chooses to measure. Getting a defensible answer for a single client, from that client's own data alone, is often genuinely impossible.

And the client's real outcome data — orders, margin, repeat purchase, returns — is in their warehouse and is often not shared with the agency at the grain that would make measurement possible, sometimes for good reasons and sometimes because nobody asked.

The structural piece is the fee. An agency paid a percentage of spend has no commercial mechanism to be rewarded for discovering that less should be spent, which is why the honest answer keeps not being pursued by the party best placed to pursue it.

## What a Solution Looks Like
Use the portfolio. One client cannot achieve power; two hundred clients can. An agency that runs geo experiments and platform holdouts across its whole base accumulates a set of causal estimates by platform, vertical, purchase cycle and spend level, from which a hierarchical prior can be built: how much this platform typically overstates for a business like this one. A new client then starts with a calibrated correction rather than the platform's raw number, and their own experiments update it. This is the single most valuable asset an agency could build and none of them are building it.

Reconcile to the business, always. Total orders and revenue are known. A measurement system whose first constraint is that the parts must sum to the whole eliminates the double-count by construction, and forces the allocation of the difference to be explicit and contestable rather than ignored.

Make experiments continuous and cheap. Rotating geo holdouts, staggered switch-ons, and spend-level variation across markets are all runnable without stopping a programme, and they turn measurement from an annual project into an instrument. The result is a stream of estimates that a mix model can be calibrated against — which is the combination that works, rather than either alone.

Report the uncertainty and act on it anyway. Allocation under uncertain channel effects is a portfolio problem with a known shape: weight toward the estimate, reserve for exploration, and revisit as evidence accumulates. That is a defensible process that survives being wrong, which the current one does not.

And change what is sold. An agency confident in its measurement can price on outcomes rather than on spend, which realigns the one incentive that currently guarantees the question stays unanswered.

## Impact If Solved
Allocation across platforms is the decision an agency exists to make, and it is currently made with numbers that cannot legitimately be compared. A portfolio-calibrated measurement layer changes where a substantial share of client budget goes and is the only defensible product in a market where the buying craft has been automated by the platforms and the reporting has been commoditised by data pipeline vendors. It is also the exit from the spend-percentage fee, which is the structural problem underneath everything else in this business.
