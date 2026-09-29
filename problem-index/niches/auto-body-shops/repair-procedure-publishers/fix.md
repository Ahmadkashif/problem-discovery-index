# Nobody Knows Which Procedures Changed Between Model Years

**Niche:** [[niches/auto-body-shops/repair-procedure-publishers/profile|Repair Procedure & Service Information Publishers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Manufacturers reissue documentation without a reliable change log, so the publisher republishes wholesale each year and neither it nor its subscribers can say what actually became different.
**Tags:** #change-point-detection #bert #transformers #graph-neural-networks #object-detection #evaluation-metrics #dimensionality-reduction #compliance #data-integration #worker-facing

## The Problem
Between model years a vehicle's repair procedures change in a small number of consequential ways and a large number of immaterial ones, and the manufacturer does not reliably distinguish them. The publisher receives a reissued corpus and treats it as new, republishing rather than diffing. The consequence lands on the technician: a shop that has repaired the outgoing model for three years has no signal that the incoming one requires a different sectioning approach, or that a fastener is now single-use, or that a bracket relocation added a calibration requirement. The information is present in the corpus and invisible as a change. Because insurers increasingly require documented OEM-procedure adherence, and because procedure changes are exactly where adherence fails, the cost of this shows up as failed repairs and disputed claims rather than as a content complaint.

## Why It's Still Broken
The publishing model is inherited from print, where an edition superseded its predecessor and change tracking was neither expected nor possible. The corpus is stored as current-state content keyed by vehicle, with prior years retained as separate documents rather than as versions of the same object — so there is no identity across years to diff against. Manufacturer practice makes it harder: the same procedure may be renumbered, re-illustrated, or relocated between years with no substantive change, which defeats naive comparison and has convinced successive teams that reliable diffing is not achievable. And no subscriber has ever been able to ask for what-changed, because none of them knows it is a thing that could exist.

## What a Fix Looks Like
Procedure identity that persists across model years, so that a procedure is a single object with a version history rather than a fresh document each cycle. Establishing it is the substantive work: matching procedures across years by content and structure rather than by identifier, robust to renumbering and re-illustration, and correctly declining to match where a procedure genuinely has no predecessor. With identity established, comparison happens at the level of the structured elements that matter — specifications, applicability conditions, sequence, warnings, part references — rather than at the level of prose, so editorial rewording does not register as change and a single altered torque value does. Each detected change is classified by materiality using the publisher's own history of which changes mattered. The output is a per-vehicle change summary that becomes a first-class subscriber-facing product: what is different about repairing this year's model, ranked by consequence, delivered before the vehicle reaches shops.

## Who Feels the Pain
Technicians repairing an unfamiliar model year on assumptions carried over from the last one; shops facing rework and liability when a changed procedure was not followed; insurers disputing repairs that failed for reasons nobody flagged; and the publisher, whose most valuable possible product is latent in a corpus it already owns.

## Impact If Fixed
Creates a genuinely new product from existing content — a what-changed service is the single most requested thing in collision repair training and does not exist because the underlying diff does not exist. It also improves the corpus itself, because reliable cross-year identity exposes the places where the publisher's own coverage silently regressed between editions, which today nobody can see at all.
