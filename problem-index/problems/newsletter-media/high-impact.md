# Inbox Placement as an Unobservable Outcome

**Industry:** [[newsletter-media|Newsletter Media]]
**Type:** High Impact
**One-liner:** Whether the product was delivered at all is decided by mailbox providers who report almost nothing, and the metric publishers used to infer it was broken by a privacy feature four years ago.
**Tags:** #gradient-boosting #time-series-forecasting #change-point-detection #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A publisher sends to a hundred thousand subscribers. Some emails land in the primary inbox. Some land in Promotions, where they are seen by a fraction of the people. Some are filtered to spam and are effectively undelivered. Some are throttled or deferred by the receiving provider.

The publisher sees a delivery rate, which counts acceptance by the receiving server and says nothing about placement. It sees opens, which since Apple's Mail Privacy Protection began pre-fetching tracking pixels for a large share of the audience no longer measure whether anyone read anything. It sees clicks, which are real but sparse and conflate placement with content quality. It sees postmaster data from Google and a few others, covering part of the audience with coarse granularity and a lag.

So the most important operational question in the business — did this reach people — is answered by inference from a degraded proxy.

The stakes rose in 2024. Gmail and Yahoo's bulk sender requirements introduced hard expectations: authenticated sending, one-click unsubscribe, and spam complaint rates kept below a stated threshold. Cross that threshold and delivery degrades sharply. The rate is measured by the provider and reported partially and after the fact.

The failure mode is quiet and compounding. A publisher whose placement is drifting toward Promotions sees engagement fall slowly and attributes it to content, seasonality or audience fatigue. By the time the cause is identified, reputation has degraded further, and repairing sender reputation is slow.

And the causes are numerous and interacting: sending volume changes, list acquisition sources, complaint rates, engagement distribution, authentication configuration, content characteristics including link density and image ratio, sending IP and domain history, and the mailbox provider's own changing models. A publisher trying to diagnose a decline is choosing among a dozen plausible explanations with no measurement to discriminate them.

## Why It's Unsolved
The providers do not report placement and will not, because doing so would help senders reverse-engineer the filters, including the senders the filters exist to stop. This asymmetry is deliberate and permanent.

Seed list testing, the industry's substitute, sends to a set of synthetic mailboxes and reports where they landed. The synthetic accounts have no engagement history, and placement is heavily personalised by the recipient's own behaviour, so the test measures something correlated with but not equal to what real subscribers experience.

Opens have degraded to the point of being actively misleading: Apple's pre-fetching inflates them and does so unevenly across segments, so a change in open rate can reflect a change in device mix rather than in reading behaviour. Many publishers have not adjusted their analysis to account for this.

Sender reputation is a stateful, slow-moving property with hysteresis. The relationship between an action and its effect is delayed by days or weeks, which makes learning from experience genuinely hard even for a diligent operator.

And the expertise is concentrated in a small deliverability consulting profession, is largely heuristic, and is expensive.

## What a Solution Looks Like
Infer placement from behaviour rather than trying to observe it. Click rate by provider and by segment, click timing distributions, and the ratio of engagement between provider cohorts carry substantial information about placement. A subscriber cohort on one provider whose click rate diverges from statistically comparable cohorts on another provider is the signal, and it uses data the publisher already has.

Treat opens correctly rather than discarding them. Pre-fetched opens have a distinct signature — immediate, machine-timed, from specific network ranges — and separating machine opens from human ones restores a substantial part of the metric's value. Very few publishers do this.

Change point detection on provider-segmented engagement. Placement changes are step functions, not gradual drifts, and detecting the break with a date lets a publisher look at what changed that day instead of guessing across a quarter.

Attribution to the actual cause. Volume spikes, acquisition source changes, complaint rate movements, content characteristic shifts and authentication events are all recorded, and relating them to provider-specific engagement breaks is a tractable diagnostic problem that currently requires a consultant.

Complaint risk predicted before sending. Which subscribers are likely to mark a given send as spam is estimable from their engagement history and acquisition source, and suppressing the highest-risk fraction of a send protects the reputation that governs everyone else's delivery.

Engagement-based sending policy driven by measured effect rather than by rule of thumb. Every publisher knows they should stop mailing dormant subscribers; almost none can say what the actual threshold should be for their list.

## Impact If Solved
Delivery is the product for a newsletter business, and it is governed by systems that do not report and cannot be observed directly. Inferring placement from provider-segmented behaviour, cleaning machine opens out of the engagement signal and detecting changes as dated breaks gives publishers the instrument the category has never had, entirely from data they already hold.
