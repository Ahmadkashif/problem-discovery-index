# Seconds, Not Days, and to the Right Person

**Niche:** [[niches/scheduling-booking-platforms/revenue-meeting-routing/profile|Revenue Meeting Routing]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Inbound interest decays by the minute and the path from form submission to a booked meeting with the correct seller crosses three products, none of which owns the outcome.
**Tags:** #gradient-boosting #logistic-regression #graph-theory #convex-optimization #evaluation-metrics #confidence-intervals #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to get an inbound prospect onto the right seller's calendar in the seconds after they raise their hand — and whoever holds both the correctness and the latency takes the revenue operations account, because both halves are required and each vendor currently has one.

## The Problem
A prospect from a large existing customer submits a demand form. The enrichment lookup returns the parent company under a different name. The routing rules do not match, so the record falls to the round-robin queue. A seller who has never seen this account receives it, offers a scheduling link, and the prospect books eleven days out because that seller's calendar is full. The account's actual owner learns about it from a calendar invite. Every piece of information needed to route this correctly existed in the customer relationship system at the moment the form was submitted.

## Why Nobody Has Built This
The chain crosses three product categories with three vendors and three data models, and the seams are where the failures live. Routing vendors treat scheduling as a downstream link and scheduling vendors treat routing as an upstream decision, so neither measures the end-to-end outcome. Identity resolution — matching an email domain to the right account in a customer relationship system full of duplicates and subsidiaries — is genuinely hard and is the root cause of most misroutes, and it belongs to neither vendor. And success is measured as meetings booked, which is the wrong endpoint: a meeting booked with the wrong seller eleven days out counts identically to the right one tomorrow.

## What to Build
The chain as one system with one objective. Identity resolution first and properly, matching the submitter to a company and that company to the right account including its subsidiaries and aliases, with confidence — since this is where the failures originate and improving it improves everything downstream. An assignment decision combining ownership rules, segment and territory, specialisation, and actual current availability, since a rule that assigns to someone unavailable for four days is not a correct answer. An explicit trade-off between speed and fit, resolved by the expected value of the meeting rather than by a fixed policy — a large enterprise prospect may be worth waiting a day for the right person; a small one is not, and this is the decision no product makes. Immediate booking in the same interaction rather than a link sent by email, which is the mechanical difference between a meeting held and a lead chased. A defined fallback path when identity or availability fails, that notifies a human rather than silently defaulting. And attribution through to the meeting held and the opportunity created, since that is the only feedback that tells anyone whether the routing is right.

## Target Customer
Revenue operations at companies with meaningful inbound volume, scheduling platform vendors expanding into routing, and routing and lead management vendors who currently stop at the handoff.

## Impact If Built
Response latency and routing correctness both have direct, well-documented revenue consequences, and each is owned by a different vendor with no accountability for the whole. Identity resolution is the root of most failures, and the speed-versus-fit trade-off is a decision nobody currently makes deliberately.
