# First-Time Fix and the Dispatch Match

**Industry:** [[field-service-software|Field Service Software]]
**Type:** High Impact
**One-liner:** The platform predicts what the job actually is from the customer's description and the equipment's history, then matches it to a technician with the right skill and the right part on the truck — turning dispatch from a card board into a decision with evidence.
**Tags:** #gradient-boosting #bert #transformers #word-embeddings #feature-engineering #cross-validation #evaluation-metrics #tacit-knowledge-ml #revenue-impact

## The Problem
A homeowner calls and says the air conditioning is not cooling. A commercial customer says the walk-in is running warm. That description is the entire input to a decision that determines the day's economics: which technician goes, when, and what they bring.

A good dispatcher does this well and cannot explain how. They know that this address had a compressor replaced two years ago, that this description usually means a capacitor and occasionally means something much worse, that this particular technician is fast on this equipment brand and this other one will spend three hours and call for help, that the part is on one truck and not the others, and that sending the wrong person means a return visit tomorrow.

Return visits are the failure mode that matters. A job that is not fixed the first time consumes a second slot, a second drive, a second set of overhead, and a large share of the customer's goodwill. First-time fix rate is the number that separates a service business that makes money from one that does not, and it moves on decisions made in thirty seconds from a two-sentence description.

The platform holds everything needed to make that decision better. Millions of prior visits with the reported symptom, the equipment make and model, the actual diagnosis, the parts used, the time taken, the technician, and whether anyone had to return. It presents a dispatch board.

## Why It's Unsolved
The dispatcher's knowledge is the classic tacit-knowledge problem, and it is genuinely multi-dimensional: symptom interpretation, technician capability by equipment type, parts inventory across trucks, drive time, customer relationship, and the commercial reality that some jobs are worth more than others. No single field captures any of it.

The training signal is also weaker than it looks. What was actually wrong is recorded in the technician's notes as free text of extremely variable quality, and the parts used are a proxy that misses diagnostic-only visits. Return visits are the cleanest label available, and even they are ambiguous — a second visit may be a planned follow-up, an unrelated failure, or a genuine miss, and the systems rarely distinguish.

There is also a hard constraint nobody in the category talks about: technician skill assessment. A model that ranks technicians by capability is, in a very direct sense, an employee evaluation system, and deploying it changes the labour relationship. That is a legitimate reason for caution and it is why the capability dimension is usually left out entirely, which is also why the models that have been attempted underperform the dispatcher.

## What a Solution Looks Like
A model that takes the customer's description, the address's service history, the equipment make, model and age, and the season, and predicts the likely diagnosis as a distribution — not a single answer, but the three things it probably is with their probabilities. From that follows the parts likely needed, the realistic duration, and the skill required.

The dispatch decision then becomes a match: which available technician has demonstrated competence on this equipment and this failure class, has the likely parts on the truck or can collect them en route, and can get there within the promised window. The output is a ranked set of options with the reasoning shown, and the dispatcher chooses.

Skill should be represented as demonstrated outcomes on specific equipment and failure classes rather than as a global ranking of people, both because it is more accurate and because it is the only version that a workforce will accept.

## Impact If Solved
A few points of first-time fix rate is the difference between a profitable service business and a struggling one, and it compounds — every avoided return visit is a slot that can be sold. The prediction rests on a cross-contractor service corpus that no individual company could assemble, which makes it the most defensible capability available in the category.
