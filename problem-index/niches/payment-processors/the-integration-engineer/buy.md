# Developer Experience Practice

**Niche:** [[niches/payment-processors/the-integration-engineer/profile|The Integration Engineer]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Developer experience became a discipline that measures friction and removes it, and payments support answers the same questions forever.
**Tags:** #worker-facing #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #data-integration #quick-win #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to stop the same twenty questions arriving forever — and whoever fixes the product so they are not asked changes what a support function is for.

## The Problem
Developer experience is now a practised discipline. Teams instrument the integration journey, measure time to first successful call, identify where developers get stuck, treat recurring support questions as product defects, and close the loop from support volume back into design. The best developer platforms run this seriously and their support volume per customer falls over time. Payments support at many processors is a large, growing function answering a stable set of recurring questions, which is the signature of a loop that is not closed.

## What Already Exists
Integration journey instrumentation; time-to-first-call measurement; friction point identification; support volume categorisation feeding product backlogs; and documentation effectiveness measurement.

## The Customization Gap
The adaptation is to a domain with irreducible complexity and money at stake. It requires: (1) genuine domain complexity that cannot be designed away, since payments involves real subtleties about idempotency, asynchrony, currency and regulation — distinguishing the complexity that must be taught from the friction that should be removed is the substantive judgement and most processors do not make it; (2) failures that cost the merchant revenue in production, which raises the stakes above a developer being confused; (3) the integration living in the merchant's codebase, so instrumentation depends on the client library and on what the merchant permits; (4) compliance constraints on what can be logged and shown, which limits the diagnostic surface; and (5) long-lived integrations that are written once and maintained rarely, so a design improvement reaches existing merchants slowly.

## Target Customer
Developer support and platform leadership at processors, and developer experience practitioners for whom payments is an unusually high-stakes application.

## Impact If Solved
A stable set of recurring questions is the signature of a loop that is not closed, and the discipline for closing it exists. Distinguishing irreducible payments complexity from removable friction is the judgement most processors have not made.
