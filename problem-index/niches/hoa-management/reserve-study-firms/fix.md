# The Analyst's Field Judgment Never Reaches the Model

**Niche:** [[niches/hoa-management/reserve-study-firms/profile|Reserve Study Firms]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst standing on a roof knows things about it that the report records as a number between 1 and 5.
**Tags:** #tacit-knowledge-ml #computer-vision #worker-facing #data-integration #transfer-learning

## The Problem
The site inspection is where the value is created. An experienced reserve analyst walking a property sees granule loss concentrated on the south slope, a flashing detail that was done badly at installation, ponding that will shorten the membrane regardless of its age, a maintenance history visible in what has and has not been patched. From that they form a view of this roof — not roofs in general — and adjust the remaining life accordingly.

The report captures the adjusted number. Occasionally a condition rating and a photo. The reasoning that produced the adjustment is not recorded anywhere, so it cannot be checked, compared, taught, or learned from. Five years later, when the roof fails early or lasts longer than projected, there is no way to know which observation was the one that mattered.

The firm's most valuable capability lives in the heads of a handful of senior analysts and is transferred by having juniors walk properties alongside them for two or three years.

## Why It's Still Broken
The deliverable never asked for it. A reserve study report presents component, condition, remaining life, cost, and a funding plan. Nobody reading it wants the analyst's reasoning about flashing details, so the reporting software has no field for it, and work that has no field does not get recorded.

Photographs make it look solved. Firms take hundreds per inspection and file them by component, which preserves the evidence and none of the interpretation. A photograph of a roof does not say what the analyst concluded from it.

And the feedback loop is thirty years long. In a business where the prediction is validated after the analyst has retired, nobody has ever been able to say which judgments were good, so there has been no pressure to record them.

## What a Fix Looks Like
Capture the observation as structured evidence at the moment it is made, and close the loop against replacements.

**Structured field observations**, not free text: the component, the specific condition seen, its extent and location, and the life adjustment the analyst made because of it. A short controlled vocabulary per component type covers most of what analysts actually say, and building it is a matter of asking three senior people what they look at.

**Photographs tied to the observation**, not to the component. A photo attached to a claim about south-slope granule loss is evidence; a photo in a folder labelled "roof" is decoration.

**A replacement register.** Whenever the firm learns a component was replaced — on a follow-up study, from a client, from an invoice — record it. This is the only source of ground truth in the business and most firms capture it incidentally or not at all.

**Feed the loop back.** With observations structured and replacements recorded, the firm can eventually say which observations predicted early failure and which did not, and that is the first time anyone in this industry would be able to make that statement empirically. It is also how a junior analyst learns in a year what currently takes three.

## Who Feels the Pain
Junior analysts, learning by apprenticeship because the knowledge exists in no other form. Senior analysts, who are the firm's capacity ceiling and cannot be replicated. Firm owners, watching that capability approach retirement. And associations, whose thirty-year funding plan rests on judgments nobody has ever been able to evaluate.

## Impact If Fixed
Training time drops sharply in a market where statutory mandates have created more demand than there are qualified analysts. Estimates become consistent between analysts. And the firm acquires the only thing that would let it improve — a record of what it saw, what it predicted, and what actually happened.
