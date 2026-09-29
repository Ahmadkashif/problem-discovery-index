# Recognition That Assists Instead of Completing

**Niche:** [[niches/recommerce-platforms/catalogue-attribute-automation/profile|Catalogue & Attribute Automation]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vision systems identify the item and the processor still types the listing, so the automation removed the difficulty and left the labour, which is the part that costs money.
**Tags:** #cnns #large-language-models #object-detection #evaluation-metrics #automation #word-embeddings #transfer-learning #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to turn a photograph into a complete, findable listing without a person typing — and whoever does that takes the cost out, because listing labour is a fixed cost on every item regardless of what it is worth.

## The Problem
The vision system recognises the item as a mid-weight wool coat from a known brand and suggests a category. The processor confirms it, selects the size from the label, types a title, picks four attributes from dropdowns, chooses a description template and edits it, and confirms the photographs. Ninety seconds. The recognition removed the hard part — identifying what the thing is — and left every piece of the mechanical work that follows from it. The processing cost, which is the reason the unit economics are difficult, is unchanged.

## Why Nobody Has Built This
Recognition was adopted as an accuracy aid rather than as a labour reduction, so it was integrated into the existing flow rather than replacing it. Trust in full automation is limited by the accuracy of the weakest attribute, which leads to a review step that reintroduces most of the labour. Title and description generation was not feasible until recently and the flow has not been revisited. And the labour is spread thinly across every item, so no single step looks like the problem.

## What to Build
Generate the whole listing and review by exception. Produce the complete listing from the photographs and the label — category, brand, size, material, colour, style attributes, a title written for retrieval and a description — which is now achievable and is the build; the point is that the processor confirms rather than composes. Route by confidence, so a high-confidence listing is published with a glance and a low-confidence one gets attention, which is what makes exception review work and is the difference between assisting and completing. Generate the title from what buyers actually search rather than from a template, since findability is what determines whether the item sells and a template title is optimised for nothing. Decide the photograph set per item — which angles and details matter for this category and this condition — rather than shooting a fixed set, which improves both cost and conversion. Extract condition observations alongside attributes, feeding the grading and pricing work from the same pass. Measure listing completeness against what makes comparable items findable, which the fix note develops. Report labour per listing as the metric this build exists to move. And keep the processor's judgement where it matters — condition, authenticity, unusual items — by removing the work that does not need it.

## Target Customer
Catalogue and intake operations, platform finance, and the resale-as-a-service providers whose margin is the processing cost.

## Impact If Built
Recognition removed the hard part and left the labour, which is the part that costs money. Generating the complete listing with confidence-routed exception review is what turns assistance into completion, and a title written for retrieval rather than from a template is what makes the item findable.
