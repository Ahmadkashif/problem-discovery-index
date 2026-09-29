# Twelve Variants of the Same Factory Colour and the Painter Picks by Eye

**Niche:** [[niches/auto-body-shops/paint-color-formulation-research/profile|Automotive Paint Colour Formulation Research]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Millions of spectrophotometer readings come back from the field recording how every factory colour actually drifted, and variant selection is still a judgment call made at the mixing bench.
**Tags:** #gradient-boosting #k-nearest-neighbors #evaluation-metrics #confidence-intervals #causal-inference

## The Problem
A refinish formula is not one formula. The same factory colour leaves different plants, in different model years, on different substrates, and weathers differently in Phoenix than in Duluth. So the colour house publishes a primary formula and a set of variants — sometimes a dozen — and the painter has to pick the one that matches the car in front of them.

That choice is the whole job. Get it right and the blend is invisible; get it wrong and the panel is redone, which costs the shop hours it cannot bill and costs the paint company a complaint. Pass 1 identifies colour matching as the highest-skill task on the shop floor for exactly this reason.

The colour houses are the only party who can fix it, and they hold the evidence. Shops read the vehicle with a spectrophotometer and the reading is returned to the manufacturer's colour system. Across the installed base that is millions of measurements of real vehicles, in real condition, at known age and geography — a record of how each OEM colour has actually drifted in the wild that no vehicle manufacturer possesses and no competitor can assemble.

What is built on it is retrieval. The tool matches the reading against the variant library and returns candidates ranked by colour difference. What is not built is prediction: given this vehicle's make, plant, build year, colour code, geography and age, which variant is most likely to be the match, and how confident should the painter be before mixing.

Nor is the outcome captured. Whether the chosen variant actually matched — whether the panel was accepted or redone — is the single most valuable label in the system and it is never recorded.

## Why Nobody Has Built This
The business sells paint. Colour research is a cost of selling it, and the tool exists to make the paint usable, so investment goes to reading accuracy and library coverage rather than to decision support that would be hard to price separately.

The variant library is also an editorial artefact built over decades by colour scientists, and treating it as a prediction problem rather than a reference problem is a different discipline from the one the department is staffed with.

And the shop-side loop is genuinely awkward. The painter is not the customer of record — the jobber is — and instrumenting whether a blend was accepted means asking a busy shop to report a failure.

## What to Build
Variant selection as a prediction with a confidence, fitted on the field readings the company already receives.

**Model variant probability from vehicle attributes.** Colour code, make, assembly plant where inferable from the VIN, build date, region, and vehicle age against the variant that matched. The features are on the repair order and the label is in the field readings.

**Model drift as a trajectory.** A colour ages. Predicting where a given code will sit after eight years in high-UV geography is a regression the corpus supports directly and the current library approximates with discrete variants.

**Return a confidence, and say when to spray a card.** The expensive failure is a confident wrong match. A system that says "this is ambiguous, make a let-down panel" saves more money than one that always answers.

**Capture the outcome.** One tap in the mixing software recording whether the blend was accepted. That is the label that makes everything above self-improving, and it costs a second.

**Publish match-rate evidence.** First-time match rate by make and age, measured. In a market where every colour house claims the best matching, being the one with a number is a genuinely different claim.

## Target Customer
Director of Colour Technology or VP Refinish at an automotive coatings manufacturer. The argument is that spectrophotometer hardware and library coverage have converged across the majors, and first-time match rate is the only differentiator a body shop actually feels.

## Impact If Built
Redone panels are pure loss shared between the shop, the insurer and the paint supplier, and the rework rate is driven by a variant choice made at a bench from a ranked list. Turning that choice into a calibrated prediction — with an honest signal about when to test first — attacks the single largest source of avoidable cost in refinish, using data the manufacturer already collects and currently only searches.
