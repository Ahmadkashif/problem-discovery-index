# A Prediction Problem Solved Once in Public and Rebuilt by Hand Everywhere Else

**Niche:** [[niches/plumbing-contractors/lead-service-line-inventory-consulting/profile|Lead Service Line Inventory & Replacement Consulting]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every water system in the country must determine what metal is buried under every address it serves, the statistical method for doing it well is published and famous, and most inventories are assembled with rules of thumb.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #causal-inference

## The Problem
Federal rules require every community water system to produce an inventory classifying each service line as lead, galvanized requiring replacement, non-lead, or unknown — and then to replace the lead ones on a schedule, with public notification obligations attached to unknowns.

The information needed to classify is fragmentary. Tap cards from the 1920s, permit files, meter installation records, main installation dates, the plumbing code in force in that neighbourhood in that decade, annexation history, and whatever the utility happens to have digitised. Physical verification means excavating or potholing at each end of the line, at real cost per address, across systems with tens or hundreds of thousands of connections.

So the job is inference: use records and construction-era attributes to predict material, and use excavation to verify. That framing is not speculative — it is the approach that made Flint's replacement programme work, it was published, and it demonstrated that a well-fitted model plus targeted digging finds lead far faster than digging in street order.

Most inventories are not built that way. They are built with deterministic rules — this era plus this record type equals this classification — applied by analysts, with unknowns left as unknowns and verification allocated by geography or convenience. The consultancies doing this work at scale hold verified determinations across hundreds of systems and have not turned them into a model.

## Why Nobody Has Built This
The deliverable is a regulatory submission, and regulatory submissions reward defensibility over accuracy. A deterministic rule is easy to explain to a state primacy agency and to a resident asking why their line was classified as it was. A probability is harder, even when it is better, and nobody wanted to be the first to submit one.

The work is also organised system by system. Each engagement is scoped to one utility, funded by that utility, and delivered to it. Nothing in the commercial structure funds building an asset that spans engagements, and the records themselves belong to each client.

And the deadline drove behaviour. Systems had a fixed date for an initial inventory and consultancies staffed to hit it. Doing the fast, defensible thing across many clients was the rational response to the calendar, and the calendar has not stopped — annual updates and replacement schedules continue for years.

## What to Build
A predictive material model, fitted on the accumulated verified determinations, with verification designed as sampling rather than allocated by geography.

**Model material probabilistically at address level.** Construction year, main installation era, code in force, parcel and building attributes, record fragments where present, neighbouring verified lines, and utility-specific history. The response is verified material, and the consultancy has verified material at address level across many systems.

**Design verification as a sampling problem.** Excavation budget is finite and each dig is an expensive label. Allocating digs to maximise information — highest uncertainty, highest leverage on the population estimate, or highest expected lead yield depending on the objective — is a well-understood design question that is currently answered by street order.

**Learn across systems and adapt to each one.** Materials practice is regional and era-specific, so a national model is wrong everywhere in a specific way. Fitting a shared model with system-level adjustment is the natural structure, and it lets a new client benefit from four hundred prior engagements on day one — which is the commercial argument for building it at all.

**Report calibrated probabilities and defend them.** A classification with a stated confidence, backed by a published validation record showing that lines predicted lead with high probability were lead, is more defensible to a primacy agency than a rule of thumb, not less. The work is producing the validation evidence before the submission, not after.

**Prioritise replacement on more than material.** Replacement order affects exposure. Combining material probability with household characteristics, water chemistry and system hydraulics changes who gets protected first, and it is the question the regulation is actually about.

## Target Customer
VP of Water Practice or Chief Engineer at a consultancy running service line inventory programmes across many utilities. The advantage is entirely in the accumulated verified determinations, which no new entrant can obtain.

## Impact If Built
Lead service line replacement is a multi-decade, tens-of-billions-of-dollars national programme in which the dominant cost is digging in the wrong place. A model that reallocates excavation from street order toward expected lead — with calibrated confidence a regulator will accept — changes how much lead comes out of the ground per dollar spent, in a programme whose entire purpose is getting lead out of the ground.
