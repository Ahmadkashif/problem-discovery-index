# Fix: Full Fidelity Is a Default Nobody Chose

**Niche:** Presentation & Dosimetry
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Fix (Pain Point)
**One-liner:** Protective viewing controls exist, are optional, and are barely used — because a reviewer who uses them gets marked wrong by an auditor watching at full fidelity.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #worker-facing #compliance #automation
**Contested on:** Whether the intensity of each unavoidable exposure, and its accumulation across a shift and a career, is deliberately controlled or left to a full-fidelity default nobody chose.

## The Problem

Several of the larger review tools already offer greyscale, blur, audio muting and frame-stepping. The controls work. They measurably reduce the visceral impact of the material. And they are used far less than anyone expects, for a reason that has nothing to do with reviewer preference.

The quality metric is agreement with an auditor. The auditor watches at full fidelity, in colour, with sound, in full. A reviewer working in greyscale with audio off will occasionally miss a detail that determined the correct call — a colour cue, a background sound, something in a frame they sampled past. When that happens they are marked wrong. The score is what the contract measures, the score determines their standing and sometimes their pay, and so the rational individual choice is to work at full fidelity and absorb the material.

The protective control is available and carries a private penalty. Every reviewer works this out within weeks. The result is a system that provides the appearance of protection while making its use personally costly, which is arguably worse than not offering it — the controls exist, so their non-use reads as a choice freely made.

There is a second layer. The defaults reset. A reviewer who sets greyscale finds the next item rendered in colour, so protection requires a deliberate act on every single item, hundreds of times a day, in the two seconds before the material is already on screen and already seen.

## Why It's Still Broken

**Auditing was designed against the artefact, not the working conditions.** The audit process asks whether the decision was correct given the content, which is a reasonable question that happens to make the protective controls costly. Nobody designed this trade; it fell out of two systems built separately.

**Quality is contractual and exposure is not.** Accuracy is a specified, priced term in the client agreement. Reviewer fidelity is not mentioned anywhere. When an unspecified good competes with a specified one, the specified one wins every time.

**Reduced fidelity genuinely does lose information sometimes.** This is a real trade, not an imaginary one — some decisions turn on colour, some on audio. The answer is to route those cases differently and audit at review fidelity, not to pretend the trade does not exist.

**Defaults are a product decision in someone else's product.** The review interface usually belongs to the platform. A vendor cannot change the default rendering even where it employs everyone using it.

**Reviewers are not asked.** The people who know precisely which controls help, on which categories, at what cost to accuracy, have no channel into the design of either the tool or the audit standard.

## What a Fix Looks Like

**Audit at the fidelity the reviewer worked at.** This is the intervention, and everything else is secondary. The auditor sees what the reviewer saw, with the same escalation option, and grades on that basis. Where the auditor needed full fidelity to reach the correct answer, that is recorded as a signal about the item — it belonged in a different queue — rather than as an error by the reviewer. This removes the private penalty entirely and costs nothing but an audit-tooling change.

**Invert the default.** Protective rendering as standard, full fidelity as a deliberate single action. The reviewer who needs colour to decide asks for colour; the reviewer who does not never sees it. Defaults are the whole ballgame in interface design, and this one is currently set to maximum harm for no considered reason.

**Make defaults persistent and per-category.** A reviewer's settings should survive the item boundary, and should be configurable per content category, because the right controls for graphic violence differ from those for child safety material.

**Isolate the segment.** Classifiers already localise most violations. Showing the reviewer the relevant seconds rather than the whole file is technically trivial and is probably the largest single reduction in exposure intensity available, and it rarely costs accuracy because the rest of the file was irrelevant to the decision.

**Ask the reviewers.** A structured channel from the people doing the work into tool design and audit standards. They know which controls cost accuracy on which categories, and that knowledge is currently discarded.

**Contract for it.** Presentation defaults and audit fidelity written into the statement of work, so the protective choice stops competing against a specified term and becomes one.

## Who Feels the Pain

The reviewer, who is offered protection and charged for using it, and who over months learns that the charge is not worth paying.

The vendor, which can point to the existence of the controls in a dispute and would find that position considerably weaker if anyone examined the usage rates and asked why.

The quality of moderation, since a reviewer optimising for audit agreement at full fidelity is spending attention on self-protection from a scoring system rather than on the judgement.

And every future claim, because "the controls were available" is a defence that collapses the moment the incentive structure around them is described.

## Impact If Fixed

Auditing at review fidelity is a small change to an internal process that removes the entire disincentive. It is the cheapest meaningful improvement in this niche and requires no new technology whatsoever.

Inverting the default changes the exposure of every reviewer on every item immediately, without asking anyone to do anything.

And segment isolation, already technically available, would cut the duration of exposure across the industry substantially — the reviewer sees the eleven seconds that determine the decision instead of the twenty minutes surrounding them.
