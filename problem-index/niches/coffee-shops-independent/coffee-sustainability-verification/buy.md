# Field Survey Tooling Adapted to Statistical Inference

**Niche:** [[niches/coffee-shops-independent/coffee-sustainability-verification/profile|Coffee Origin Verification & Traceability Services]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mobile data collection platforms are excellent at capturing responses in the field and indifferent to whether the responses that came back support the inference the whole exercise exists to make.
**Tags:** #bayesian-inference #probability-distributions #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #automation #workflow-orchestration #data-integration #compliance

## The Problem
Fieldwork is expensive, seasonal, and unrepeatable — a surveyor sent to a remote origin during harvest is not going back next week. Whether a round produced a usable estimate depends on which strata were actually reached, how substitution was handled when a sampled farm could not be visited, and how much non-response accumulated where. Those questions are answered after the round, in analysis, when nothing can be done about them. Field teams work to a target count rather than to an inferential requirement, so a round can hit its total and still leave a stratum too thin to support the claim the client is paying for.

## What Already Exists
Field data collection is a mature, cheap, well-supported category. SurveyCTO, KoBoToolbox, ODK, and CommCare all handle offline collection, complex skip logic, GPS capture, media attachment, enumerator management, and quality checks including audio audits and duplicate detection. Development and humanitarian organizations run enormous programmes on them successfully.

## The Customization Gap
Every one of them is built around the form and the submission. None models the sample design, so none can tell a field team what the effect of a substitution or a non-response is on the estimate they are collecting toward. Progress is reported as submissions received against a target, which is the wrong denominator: what matters is precision achieved per stratum against the precision required, and that requires the sampling frame, the design weights, and the inferential target to be first-class objects inside the collection system rather than living in an analyst's script afterward. The adaptation makes them first-class: sampled units carry their stratum and weight; substitutions are recorded as design events with their implications recomputed rather than as replacements; non-response is tracked by stratum with the resulting bias risk surfaced daily; and the field dashboard reports achieved precision and remaining requirement rather than raw counts. That converts a fixed fieldwork plan into an adaptive one, which is the single largest efficiency available in an operation whose dominant cost is sending people to remote places.

## Target Customer
Heads of field operations and methodology leads at verification services, and the survey managers who currently discover a round's inferential problems weeks after the field teams have gone home.

## Impact If Solved
Turns the largest cost line into an adaptive one — effort moves toward the strata that need it while teams are still in the field, which either improves precision at the same cost or holds precision at lower cost. It also removes the failure mode that is most expensive and least visible: a completed round that cannot support the claim it was commissioned to make.
