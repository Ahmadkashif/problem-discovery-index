# Build: Pay Composition at the Moment of the Offer

**Niche:** [[niches/gig-delivery-platforms/pay-composition-disclosure/profile|Pay Composition Disclosure]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Serialise the pay model's own components into the offer, so the courier sees base, distance, promotion, guarantee and tip estimate before deciding rather than after delivering.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #data-integration #worker-facing #quick-win #automation
**Contested on:** Whether the platform will show a decomposition it already holds in full at the moment the offer is constructed.

## The Problem

A courier is shown a guaranteed amount. That amount was assembled seconds earlier from named components inside the pay model. The courier does not see them, and the difference between two offers of the same size can be enormous: one that is mostly base pay is stable, one that is mostly an estimated tip may not survive the customer's post-delivery adjustment, and one that is mostly a promotional overlay disappears the moment the promotion ends.

The courier's ability to reason about their own work depends on this decomposition. Whether to work this zone tomorrow, whether this merchant is worth the drive, whether the market is genuinely paying better or just running a promotion — all of these require knowing what the numbers are made of, and none is answerable from a single figure.

## Why Nobody Has Built This

There is no technical reason whatsoever, which is what distinguishes this from every other problem in the industry. The values exist as fields in the offer-generation code path.

The reasons are commercial and legal. Disclosure removes pricing discretion: a platform that shows the base component cannot quietly reduce it while holding the headline constant, and the headline is what acceptance responds to. Disclosure of the tip component in particular was the subject of sustained public controversy and regulatory action precisely because the undisclosed configuration allowed customer tips to offset platform contribution, and no platform wants to reopen a settled reputational wound by displaying the mechanism.

There is also a classification concern that gets raised in every discussion of this: detailed pay composition disclosure looks like the kind of pay statement an employer provides, and platforms have been advised that anything resembling employment infrastructure carries risk given that contractor classification remains genuinely contested in law and varies by jurisdiction.

## What to Build

The disclosure itself is one screen. The build is the surrounding system that makes it consistent, jurisdiction-aware and defensible.

Serialise the components into the offer payload: base, distance or effort, peak or promotional overlay with its expiry, any guarantee and its conditions, and any tip estimate clearly marked as an estimate that can change with the historical realisation rate for comparable orders attached. Each labelled in plain language, at the moment of the offer.

Build the jurisdictional policy layer, because this is where the real engineering is. Requirements differ materially between jurisdictions — what must be disclosed, when, in what form, whether tips must be shown separately, whether minimum earnings standards apply to engaged time or to total time. The offer path needs a policy engine evaluating the courier's jurisdiction at construction time, applying the applicable disclosure and constraint set, and writing an auditable record of exactly what was computed and shown. Platforms operating in twenty markets currently handle this with per-market forks, which is both expensive and fragile.

Make the audit record the product's spine. For every offer: the components, the policy applied, the disclosure rendered, the courier's response. That record is what satisfies an auditor, defends against a claim, and supports the minimum-earnings reconciliation that several jurisdictions now require. Without it the disclosure is a UI feature; with it, it is a compliance system.

Then treat the aggregate disclosure as the second deliverable. A weekly statement showing the courier what share of their earnings came from base, distance, promotion and tips, by market and time, is the version that supports their planning rather than a single decision — and it is a group-by over the same records.

## Target Customer

Platform compliance and legal leadership, in the growing set of jurisdictions where this is mandatory and where the current answer is a per-market engineering fork. The strategic buyer is a platform choosing to standardise ahead of the regulation rather than behind it, which is cheaper than the alternative and is the version that reads as a choice rather than a concession.

## Impact If Built

The courier can reason about their own income: which components are durable, which are promotional, which are conditional. The platform gets one system instead of twenty forks, with an audit record that answers the questions regulators are already asking. And the industry's most persistent worker grievance — a number with no stated basis — is addressed by displaying data that has always existed.
