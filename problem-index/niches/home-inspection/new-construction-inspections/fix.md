# Builder Punch List Tracking and Verification

**Niche:** [[niches/home-inspection/new-construction-inspections/profile|New Construction Inspections]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Fix (Pain Point)
**One-liner:** When a new construction inspection identifies defects, the builder agrees to fix them before the next phase — but these commitments are tracked via text messages and verbal promises, and 20-30% of agreed repairs are never verified because nobody maintains a structured record of what was found, what was agreed, and what was actually corrected.
**Tags:** #automation #workflow-orchestration #worker-facing #compliance

## The Problem
A Phase 1 inspection might identify 15-25 items needing correction: missing fire blocking at 3 locations, undersized header at the garage, improperly flashed window rough openings at 4 windows, reversed floor joist hangers at 2 locations, etc. The inspector emails this list to the buyer, who forwards it to the builder, who verbally commits to fixing everything before drywall. At Phase 2 (pre-drywall), the inspector returns to verify corrections — but the original email has been buried under weeks of other communications, the inspector can't remember which 4 windows had flashing issues, and the builder claims "we fixed everything" without documentation. The inspector spot-checks what they can remember and moves on, missing 3-4 uncorrected items that get walled in behind drywall. Six months later, one of those improperly flashed windows leaks, and the homeowner discovers a $5,000 repair that the builder should have corrected during construction.

## Why It's Still Broken
There is no shared punch list platform between the inspector, buyer, and builder. Email is the default communication channel, but it lacks structure — items get buried in threads, correction status isn't tracked, and photo evidence of corrections is mixed with general correspondence. Builders have their own QC processes but don't share status with the buyer's inspector. The inspector's report is a PDF delivered to the buyer — it's not a living document that tracks correction status. Construction management platforms (Procore, CoConstruct) handle builder punch lists but are not accessible to the buyer's independent inspector.

## What a Fix Looks Like
A shared punch list portal where the inspector creates items with photo evidence during each phase, the builder marks items as corrected with photo evidence of the fix, and the inspector verifies corrections at the next phase visit. Each item has a status lifecycle: identified → acknowledged → corrected → verified (or: identified → disputed → resolved). The portal generates a correction history for each item — the inspector photographed the missing fire block at Phase 1, the builder photographed the installed fire block two weeks later, and the inspector verified it in-person at Phase 2. At project closeout, the buyer has a complete record of every defect found and its resolution status — a document that serves as both a quality record and a warranty reference.

## Who Feels the Pain
Inspectors who return for Phase 2 and can't efficiently verify 15-25 corrections from Phase 1 because their only record is a PDF report and their memory. Buyers who assume everything was fixed because the builder said so, only to discover uncorrected defects after closing. Builders who fix items but have no way to document the correction for the inspector — they're unfairly accused of not fixing things they actually fixed.

## Impact If Fixed
Ensures 95%+ of identified defects are verified as corrected before they're covered by drywall, versus the current 70-80% rate. Creates an auditable construction quality record that protects the buyer's warranty rights. Reduces friction between inspectors and builders by providing a structured, mutually visible record rather than adversarial email chains. Adds $100-200 in value per new construction inspection through the punch list management service.
