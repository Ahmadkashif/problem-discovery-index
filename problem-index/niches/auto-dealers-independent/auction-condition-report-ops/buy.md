# Every Vehicle Is Photographed From Every Angle and the Damage Is Typed by Hand

**Niche:** [[niches/auto-dealers-independent/auction-condition-report-ops/profile|Wholesale Auction Condition Report Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The imagery that would document condition is captured on every car and the condition record is still keyed by an inspector walking around it.
**Tags:** #cnns #object-detection #semantic-segmentation #evaluation-metrics #transfer-learning

## The Problem
Wholesale inspection is a photographic process already. Vehicles are shot comprehensively — exterior panels, wheels, interior, engine bay, undercarriage in some lanes — because buyers need to see them. Alongside that, an inspector records damage: which panel, what type, what severity, what it will cost to fix.

The two are produced separately. The photographs go to the listing; the damage record is keyed from the inspector's walkaround. Nothing systematically ties a recorded scratch to the pixels that show it.

The consequences run through everything. Consistency depends entirely on the inspector, because there is no second observer. Buyers scrutinising the photographs frequently see damage the report does not mention, which is a substantial share of arbitration. And the imagery archive — millions of vehicles, every panel, joined to a human damage record and to arbitration outcomes — is one of the largest labelled vehicle condition corpora anywhere, sitting unused as listing content.

Throughput pressure makes it worse. Inspection is timed against the lane schedule, and a thorough walkaround competes with the number of vehicles that must be processed before the sale.

## What Already Exists
Automated vehicle damage detection is a real commercial category, deployed by insurers for claims triage and by rental and remarketing operators for check-in and check-out. Segmentation models for panel-level damage are well developed, and several vendors sell exactly this capability.

The gap is the specification. Insurance damage models are tuned for repair cost estimation on collision damage. Wholesale condition assessment is a different question: it grades cosmetic wear against a commercial standard, it distinguishes what must be announced from what need not be, and it feeds a composite grade defined by the auction's own rules — none of which a claims model expresses.

## The Customization Gap
**The output is a grade-relevant finding, not a damage mask.** The auction's own condition standard defines severity thresholds, what counts as a reportable defect and how findings roll into a composite grade. That taxonomy is the target and only the auction holds it.

**Announcement-triggering conditions are the high-stakes subset.** Frame damage, flood, salvage history and structural repair are the findings that produce arbitration and legal exposure. A model that is merely good at scratches is missing the part that matters.

**Capture conditions are fixed and exploitable.** Unlike insurance photographs, auction imagery is shot in consistent lanes with consistent framing. That is a large advantage over general models and it should be designed into the system rather than ignored.

**Arbitration is the training label, not the inspector.** Fitting to inspector-recorded damage reproduces inspector bias. Fitting and evaluating against arbitration outcomes is what makes the model better than the person.

**The role is a second observer, not a replacement.** The workable deployment is a check on the human record — findings visible in imagery that the inspector did not record — which resolves the throughput problem and the labour problem at once.

**Confidence must reach the buyer.** A finding surfaced with a confidence, alongside the human report, is what a sight-unseen buyer actually needs.

## Target Customer
VP of Inspection Services or Chief Technology Officer at a wholesale auction group.

## Impact If Solved
The imagery is captured, the labels exist in the arbitration record, and the condition report — the entire basis of sight-unseen wholesale buying — is still a single unverified human observation made against a lane clock. Adding a second observer from pixels already collected attacks the largest source of arbitration directly.
