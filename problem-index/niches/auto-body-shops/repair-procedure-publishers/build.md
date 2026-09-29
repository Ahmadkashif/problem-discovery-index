# Search Failure as a Map of Where Procedures Are Ambiguous

**Niche:** [[niches/auto-body-shops/repair-procedure-publishers/profile|Repair Procedure & Service Information Publishers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Millions of technician searches a year end without the technician finding what they needed, and the abandonment pattern is the most precise available map of where manufacturer documentation fails — logged, retained, and never analyzed.
**Tags:** #bert #transformers #large-language-models #word-embeddings #contrastive-learning #k-means-clustering #evaluation-metrics #feature-engineering #tacit-knowledge-ml #data-integration

## The Problem
A technician with a vehicle on the lift searches the subscription for a specific answer — can this rail be sectioned, does replacing this bracket require a recalibration, what is the torque sequence for this joint. Sometimes the answer is there and findable. Sometimes it is there and phrased in terms the technician did not search for. Sometimes it is genuinely absent because the manufacturer never documented it. All three produce the same visible event: a search, some reformulations, then abandonment, and frequently a call to technical support. The platform records every one of these. Nobody analyzes them. The publisher's content roadmap is set by model year coverage and OEM release schedules, which is a supply-side plan, while the demand-side evidence — precisely which questions the industry cannot get answered — accumulates in logs and is discarded on a retention schedule.

## Why Nobody Has Built This
Search logs are treated as infrastructure telemetry rather than as editorial evidence, so they live with the platform team and are retained for operational rather than analytical periods. Interpreting them is also non-trivial: technicians search in shorthand and inconsistent vocabulary, and an abandoned search is ambiguous between "not found," "found and answered quickly," and "gave up and asked a colleague." Distinguishing those requires modelling the session rather than the query. And the editorial organization has no mechanism to act on demand-side signal even if it had it, because its production calendar is driven by the OEM release schedule it has always followed.

## What to Build
An engine that turns search and support interaction into a structured demand signal against the content corpus. Sessions are reconstructed and classified — resolved quickly, resolved after reformulation, abandoned, escalated to support — and the intent behind each is resolved to a vehicle, system, and repair operation rather than left as a text string. That produces a demand map over the corpus with three distinguishable failure modes: content exists but is not findable under the terms technicians use, which is a retrieval and vocabulary problem; content exists and is insufficient, which is an editorial problem; and content does not exist because the manufacturer never published it, which is the most valuable finding of all. That third category is a documented gap in OEM documentation, evidenced by field demand, and it is directly actionable — as original research the publisher can produce and sell, and as a substantiated inquiry to the manufacturer. Support call transcripts join the same map, since a call is the strongest possible signal that self-service failed.

## Target Customer
VPs of content and directors of automotive research at procedure publishers running 100-400 technical writers, and the technical support managers whose call volume is the current, lagging proxy for content failure.

## Impact If Built
Redirects a large editorial organization from supply-driven coverage to demand-driven coverage, which changes what subscribers experience without changing headcount. The gap map is also the publisher's route out of pure dependence on OEM-licensed source material: content that answers questions the manufacturer never documented is original, defensible, and the only part of the corpus a competitor with the same OEM licence cannot replicate.
