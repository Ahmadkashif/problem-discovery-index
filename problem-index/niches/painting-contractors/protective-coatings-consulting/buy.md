# Condition Ratings Assigned by Eye Against a Standard Nobody Calibrates

**Niche:** [[niches/painting-contractors/protective-coatings-consulting/profile|Protective Coatings Consulting & Failure Analysis]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Two qualified inspectors survey the same tank and return different per cent breakdown numbers, and nothing in the process ever finds out.
**Tags:** #cnns #semantic-segmentation #evaluation-metrics #transfer-learning #workflow-orchestration

## The Problem
A coating condition survey produces numbers: per cent of surface showing rust, blistering density and size, cracking and flaking grade, chalking rating. Those numbers drive the recommendation, and the recommendation drives a capital decision.

They are assigned by a person looking at a surface and comparing it to reference photographs in a standard. The reference sets are coarse, the intervals between grades are wide, and the judgment of whether a large surface averages one grade or another is genuinely difficult. Inspectors are trained and certified, but certification tests knowledge of the standard, not agreement with other inspectors on real surfaces.

The result is variance that nobody measures. A structure rated by one inspector this cycle and another next cycle can appear to deteriorate or improve for reasons that have nothing to do with the coating. Since remaining-life recommendations are built on the change between surveys, inspector-to-inspector variance propagates directly into capital plans.

Photographs are taken on every survey. They are filed as evidence for the report and used for nothing else.

## What Already Exists
Image segmentation for corrosion and coating defects is a solved problem class in the research literature and appears in commercial drone inspection products for bridges and tanks. Those products are built for asset owners doing visual inspection at scale, not for a consultancy producing a rated survey to a coatings standard.

Generic defect detection returns a mask of rusted pixels. That is not what the deliverable needs. The deliverable needs a rating on a specific consensus scale, applied to a defined survey unit, with the reference-photo semantics of that scale honoured — including the awkward parts, like whether scattered pinpoint rust over a wide area rates the same as concentrated breakdown covering the same total area.

## The Customization Gap
**The scale is the product, not the pixels.** The output must be a grade on the standard the specification references, because the specification, the bid documents and the warranty all speak that language. A percentage of rusted area is a different quantity from a rust grade and the mapping between them is defined by convention, not arithmetic.

**Survey units are structural, not photographic.** Ratings apply to defined areas — a tank course, a bridge span, a specific member — and a photograph covers part of one. Aggregating image-level output into the survey unit an inspector rates is where the vertical work is.

**Field images are not inspection-rig images.** Handheld photographs at varying distance, angle, lighting and weather, often of wet or dirty surfaces, and often shot to document a specific defect rather than to sample a surface representatively. A model trained on clean drone imagery degrades on exactly this material.

**Agreement is the metric.** The right evaluation is not accuracy against a single label but agreement with the consensus of several experienced inspectors — and generating that consensus set is the first piece of work, because it also gives the firm the first real measurement of its own inspector variance.

**The archive is the training set.** Decades of survey photographs already carry inspector-assigned ratings for the survey unit they came from. That is a labelled corpus a competitor cannot assemble.

## Target Customer
Director of Consulting Services or Chief Technical Officer at a coatings consultancy running a field inspection staff of dozens.

## Impact If Solved
Consistent, defensible condition ratings across inspectors and across survey cycles, which is what makes a deterioration trend real rather than an artefact of who held the camera. It also converts the photograph archive from evidence into an asset, and gives the firm a measured statement about its own reliability that no competitor can match.
