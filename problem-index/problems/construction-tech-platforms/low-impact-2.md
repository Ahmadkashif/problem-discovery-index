# Trade-Specific Drawing Comparison

**Industry:** [[construction-tech-platforms|Construction Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sheet comparison between drawing revisions is a shipped, working feature in every platform, and it tells a plumbing foreman that four hundred things changed rather than the three that affect them.
**Tags:** #cnns #object-detection #semantic-segmentation #feature-engineering #evaluation-metrics #transfer-learning #worker-facing

## The Problem
Drawings are revised constantly. Every platform offers version comparison: overlay the new sheet on the old, highlight what moved. It works, it is fast, and it is universally available.

It is also nearly useless in the field, because it operates on pixels rather than on meaning. A revised architectural sheet with a re-issued title block, a renumbered detail callout and a shifted north arrow lights up almost entirely. Somewhere inside that a door swing changed, and that is the only thing the framing crew needs to know.

So the comparison is not trusted. Superintendents and foremen still find changes by reading the revision cloud, the delta triangle and the transmittal narrative — which is to say, by relying on the design team to have marked the change, which they do inconsistently. Changes that are missed become rework, and rework in the field is expensive and late.

## What Already Exists
Bluebeam's compare is the category standard and is genuinely good at what it does. Every major platform has an equivalent. BIM model comparison is stronger where a model exists, because the objects are semantic rather than drawn — but most subcontractors work from sheets, not models, and will for years. OCR on drawings is mature. Revision clouds and delta markers are a long-standing convention.

## The Customisation Gap
The gap is semantic and it is trade-shaped. A change matters to a specific trade or it does not. A plumbing foreman needs fixture locations, pipe routing and slab penetrations; a framer needs wall types, openings and dimensions; an electrician needs device locations, panel schedules and conduit runs. A comparison that filtered to the objects a trade cares about, and ignored title blocks, callout renumbering and sheet furniture, would be trusted and used.

That requires recognising drawing elements as objects rather than marks — detecting fixtures, doors, walls, dimension strings and equipment tags, and comparing those. The models to do this exist; nobody has assembled the labelled drawing corpus, and the vendors are the only parties holding one large enough at hundreds of thousands of projects.

The second half is impact routing: knowing that a changed sheet region intersects work that is already scheduled or already installed, and notifying the affected foreman rather than everyone on the distribution list.

## Impact If Solved
Missed drawing changes are a leading cause of field rework, and rework is the single largest avoidable cost in construction. The comparison feature is already in the product and already ignored; making it trustworthy is a quality improvement to something customers have already been sold.
