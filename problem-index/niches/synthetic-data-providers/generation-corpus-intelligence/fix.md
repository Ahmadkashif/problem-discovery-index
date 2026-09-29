# Configuration Knowledge That Lives in Four People

**Niche:** [[niches/synthetic-data-providers/generation-corpus-intelligence/profile|Generation Corpus Intelligence]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Knowing which settings work for which shape of data is the vendor's most valuable operational knowledge, and it exists only as the experience of a few senior engineers.
**Tags:** #tacit-knowledge-ml #descriptive-statistics #evaluation-metrics #gradient-boosting #feature-engineering #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn the accumulated record of generation runs and their outcomes into a certification standard the field lacks — and whoever assembles it defines how the category is judged, which is worth more than any individual product in it.

## The Problem
A senior engineer looks at a customer schema and knows, within a minute, that this one will need the temporal handling turned up, that the skewed identifier column will need special treatment, and that the privacy setting the customer asked for will not survive contact with their downstream task. They are right, consistently, and they cannot fully explain why. Three people in the company can do this. Everyone else runs the search from defaults. When one of the three leaves, the capability leaves with them, and the run logs that encode the same knowledge sit unread in an object store.

## Why It's Still Broken
The knowledge is genuinely tacit — pattern recognition over hundreds of datasets — and the people who hold it are too busy applying it to document it. Documentation would also be stale within two model versions. The run logs that contain the same information in recoverable form are treated as operational exhaust rather than as the asset they are. And nobody owns the problem: it is not research, not product, and not a customer deliverable, so it sits between functions.

## What a Fix Looks Like
Recover the knowledge from the logs rather than from the people. Instrument every run to capture the source profile, the configuration, the outcome and the human adjustments made along the way, which is a small change to the pipeline and is the precondition for everything else. Mine the configuration-to-outcome relationship from the accumulated history, which converts the same expertise into something queryable and does not depend on anyone writing it down. Capture the adjustments explicitly — what the engineer changed after the first run and why — since the correction is where the tacit knowledge is most concentrated and a one-line reason field collects it at near-zero cost. Surface a recommendation with the similar past runs attached, so a junior engineer sees the evidence and learns rather than being handed an opaque setting. Record failures as first-class, because the folklore is mostly about what does not work and failures are systematically discarded. Review the recommender against the senior engineers periodically, which both validates it and is the mechanism by which their disagreements become new features. And make it a named responsibility, since the reason this has not happened is that it currently belongs to no one.

## Who Feels the Pain
Junior engineers searching from defaults for work a colleague could scope in a minute; the senior engineers who are the bottleneck on every non-standard account; and the vendors who lose the capability when one person resigns.

## Impact If Fixed
The knowledge is already in the run logs and is read by nobody. Capturing the engineer's post-run adjustment and its reason is a near-free change that collects the most concentrated form of the expertise, and recording failures matters more than recording successes.
