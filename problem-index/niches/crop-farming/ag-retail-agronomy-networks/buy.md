# Scouting Reports Are Photographs and a Paragraph Typed in a Pickup

**Niche:** [[niches/crop-farming/ag-retail-agronomy-networks/profile|Agricultural Retail Agronomy Networks]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The observation that triggers every recommendation is captured as free text and a phone photo, and never becomes data.
**Tags:** #cnns #object-detection #transformers #transfer-learning #data-integration

## The Problem
Everything upstream of a prescription starts with a scouting visit. An agronomist walks a field, counts stand, checks nodes, digs roots, identifies what is feeding on what and how badly, and records it. Across a national retailer that happens hundreds of thousands of times a season.

The record is a photograph, a pin on a map, and a sentence. Sometimes a structured pest count, more often a description. It is written for one purpose — to justify the recommendation to this grower this week — and it succeeds at that.

As data it is close to unusable. Pest and disease identification is inconsistent between advisers and between regions. Severity is a word. Growth stage is recorded when someone remembers. The same condition is described five ways across five agronomists in the same county on the same day.

So the retailer sits on an enormous, continuous, geographically dense observation network — arguably the best real-time picture of crop condition and pest pressure in the country — and cannot aggregate it. Regional pest pressure is inferred from what advisers happen to mention in sales meetings. Disease onset is noticed when it is already widespread. And the scouting record cannot serve as the input layer for the outcome measurement above it, because the observations are not comparable.

## What Already Exists
Plant disease and pest identification from images is a mature applied research area with strong published results and several commercial products aimed at growers. Field data collection apps are abundant. Satellite and aerial imagery vendors sell vegetative index products at field resolution, and the major farm management platforms all have scouting modules.

None of them produces what the advisory workflow needs. Grower-facing identification apps answer "what is this" for a single leaf; the retailer needs a severity-graded, growth-stage-anchored observation tied to a management zone within a field. Generic field apps capture forms; they do not enforce the taxonomy that would make one adviser's observation comparable to another's. And remote sensing sees stress without seeing cause — it flags an anomaly that still requires someone to walk out and look.

## The Customization Gap
**The taxonomy is the product.** Pest, disease, deficiency and injury, with a severity scale that means the same thing to every adviser in every region, anchored to a growth stage scale. Building and enforcing that vocabulary is the work, and it is specific to the retailer's crops and geography.

**Capture must cost seconds, in a field, on a phone, offline.** An agronomist is on foot in a hot field with a queue of visits. Anything requiring more than a photograph and two taps will be filled in from memory that evening, which is worse than nothing.

**Identification must carry confidence and defer.** An adviser is a professional; a model that overrides them will be ignored, and a model that quietly guesses will corrupt the corpus. The right output is a ranked suggestion with confidence, and an easy path to disagree that records the disagreement.

**Observations must be spatially anchored to management zones.** A pin is not enough. Recommendations are written by zone, so observations have to attach to the same geometry, which means integrating with the retailer's own field boundary and zone layer.

**The image archive is the training set.** Years of adviser photographs with the diagnosis the adviser recorded is a labelled corpus specific to this retailer's crops and regions, and no vendor has it.

**Adviser disagreement is signal, not noise.** Where two advisers grade the same condition differently, that is a calibration event and should be surfaced, not averaged away.

## Target Customer
Director of Agronomic Technology or VP of Agronomy at a national retailer, owning both the adviser workforce and the field data platform.

## Impact If Solved
Structured scouting turns the largest crop-observation network in the country from anecdote into a dataset — which gives the retailer regional pest and disease nowcasting nobody else can produce, and supplies the comparable input layer without which prescription-outcome measurement cannot be attempted at all.
