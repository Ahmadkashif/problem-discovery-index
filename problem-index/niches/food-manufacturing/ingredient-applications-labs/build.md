# Every Formulation That Ever Launched, and No Model of Which Ones Sold

**Niche:** [[niches/food-manufacturing/ingredient-applications-labs/profile|Ingredient Applications Laboratories]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The house holds decades of formulations, the sensory profiles they hit, and which of them a customer actually took to market — and treats the library as an archive to search rather than a dataset to learn from.
**Tags:** #gradient-boosting #transformers #evaluation-metrics #causal-inference #dimensionality-reduction

## The Problem
An applications lab exists to solve a customer's problem: match this target profile, hold this flavour through retort, replace the ingredient we just removed, hit this cost. A team develops prototypes, the customer tastes them, and one is selected — or none is, and the brief comes back.

Across the largest houses this happens continuously, at a scale of thousands of briefs a year, supported by formulation libraries built over decades. Those libraries are among the most guarded assets in food, and the reason is sound: they encode what works.

What they do not encode is what worked *commercially*. The house knows which prototype the customer selected. It knows, from its own ingredient sales, which selected formulations went into products that scaled and which quietly stopped ordering after eighteen months. That is an outcome label attached to a formulation, at industrial scale, held by nobody else — and it is not joined to the formulation record.

The consequence is that the most expensive judgment in the lab — which two or three prototypes to put in front of the customer out of the dozens that could be made — is made from a flavourist's sense of what will win. Sometimes brilliantly. Never measurably.

The reformulation case is sharper still. Ingredient removals are constant: a sweetener out, a colour out, a preservative out, sodium down, cost down. Each is a search for a formulation that lands in the same sensory neighbourhood under a new constraint. The library contains thousands of prior solutions to structurally similar searches, and it is queried by memory and by whoever has been there longest.

## Why Nobody Has Built This
Revenue is ingredient volume. The lab is a cost of selling it, so the department is funded to serve briefs rather than to build a research asset out of its own history — and a model that reduced prototype iterations would reduce billable-looking activity in a function that is already free.

The libraries are also fragmented by design. Formulations sit in electronic notebooks, sensory results in a separate panel system, stability in another, and commercial outcome in the sales ledger. Nobody owns the join because no single deliverable requires it.

And there is a real cultural argument that flavour creation is craft, not prediction — which is true of the top of the range and much less true of the reformulation and matching work that fills most of the queue.

## What to Build
The formulation library as a supervised corpus.

**Join formulation to fate.** Prototype, sensory profile, customer, brief type, selection outcome, and subsequent volume trajectory. The join is a data engineering project the house can do entirely with its own records.

**Model brief-to-solution retrieval.** Given a target profile and a constraint, retrieve the nearest prior solutions from the library — not by ingredient name but by sensory and functional position. This is the flavourist's own reasoning made searchable, and it is most valuable to the people with the least experience.

**Predict which prototypes win.** Selection is a labelled outcome. Predicting it from sensory distance to target, brief type, cost position and customer history is a supervised problem that could cut iterations on routine matching work.

**Model reformulation as constrained search.** Remove this ingredient, preserve this profile, respect this cost and this process. The library is a set of worked examples of exactly this, and it is used as a memory aid.

**Score sensory prediction.** Where instrumental measurements exist alongside panel results, the relationship between them is estimable and would let the lab pre-screen before consuming scarce panel capacity.

## Target Customer
Chief Science Officer or VP of Applications at a flavour and ingredient house. The argument is that applications capability is the reason a manufacturer buys from one house rather than another, and it is currently defended by hiring rather than by any asset that compounds.

## Impact If Built
This is one of the largest and best-funded research organisations found anywhere in the vault, and it exists to sell ingredients. Turning its own formulation history into a predictive asset shortens the iteration cycle on the routine two-thirds of the queue, frees senior flavourists for the work that genuinely is craft, and produces the one form of evidence a competitor cannot hire away.
