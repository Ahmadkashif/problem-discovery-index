# The Analyst With Five Sources of Truth

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Worker Life Changing
**One-liner:** The client-side analyst has platform numbers, site analytics, the attribution vendor, the mix model and finance, all disagreeing, and is asked which one is right before Thursday.
**Tags:** #change-point-detection #gradient-boosting #large-language-models #time-series-forecasting #confidence-intervals #evaluation-metrics #worker-facing #data-integration

## The Problem
A marketing analyst inside an advertiser holds the reconciliation problem. Each ad platform reports its own conversions on its own window. Site analytics reports sessions and last-click conversions, with attribution that changed when the consent banner was updated. The attribution vendor reports channel contributions. The mix model, refit quarterly, reports different ones. Finance reports orders and revenue, and finance is the only one anybody has to agree with.

None of these reconcile, and the analyst is the person asked why. The answers are technical — different attribution windows, different identity resolution, view-through inclusion, modelled conversions, returns netting, timezone boundaries, different definitions of a conversion — and they are correct, unsatisfying, and must be re-explained to a new stakeholder every few weeks.

Then there is the work of producing the numbers. Pulling from each platform, normalising taxonomies that diverge because campaign naming conventions were agreed once and drifted, joining to order data, and building the weekly view. When something looks wrong, the analyst must determine whether it is real or a pipeline fault, which means checking each source by hand.

## Why It Matters to the Worker
The analyst is the designated explainer of a contradiction they did not create and cannot resolve, which is a poor position to occupy permanently. Every stakeholder wants a single number; the honest answer is that there is no single number, and delivering that answer repeatedly makes the analyst seem obstructive rather than rigorous.

The role also sits at the collision point of other people's incentives. The channel owner wants the platform's number, finance wants the finance number, the CMO wants a consistent story, and the analyst is expected to produce something that satisfies all three. Whichever number they present, someone is disadvantaged by it, which turns a technical role into a political one without any of the authority that would make that survivable.

And the time goes to production. Assembling, normalising and reconciling consumes the week; the analysis that would genuinely help — understanding which customers are worth acquiring, where the business is actually growing — is what gets postponed. Analysts in this seat consistently describe the gap between the job they trained for and the one they do.

## What a Solution Looks Like
Make the disagreements explicit and standing. A reconciliation view that shows each source, its definition, and precisely why it differs from the others — window, identity, view-through, modelling, returns — turns a recurring argument into a reference document. The differences are computable and stable; explaining them once, in a form anyone can consult, removes most of the recurring conversation.

Anchor everything to finance. Orders and revenue are the number the business runs on, and any marketing measurement that does not reconcile to them is producing an internally consistent fiction. Reconciliation to finance as a hard constraint, with the unexplained residual reported rather than distributed, is the discipline that makes the rest credible.

Monitor the pipeline. Whether a number is real or a fault is answerable automatically: each stream forecast against itself, schema changes detected, naming taxonomy drift flagged on ingest. That removes the daily uncertainty about whether to trust what is on the screen.

And provide the standing answer to the recurring questions. Most of what stakeholders ask is a lookup with an explanation, and giving them a way to ask it directly — with the definitional caveat attached automatically — removes both the interruption and the misinterpretation.

## Impact If Solved
Reconciliation and explanation consume the majority of a marketing analyst's week and produce no decisions. Making the differences a standing artefact, anchoring to finance, and monitoring the pipeline converts the role from defending contradictions into analysing a business — which is both what the person was hired for and the work that would actually improve how the budget is spent.
