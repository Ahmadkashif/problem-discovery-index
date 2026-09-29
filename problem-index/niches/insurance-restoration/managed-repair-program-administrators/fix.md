# Auditors Know Which Contractors Pad and Which Estimates Are Honest

**Niche:** [[niches/insurance-restoration/managed-repair-program-administrators/profile|Managed Repair Programme Administrators]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Fix (Pain Point)
**One-liner:** An auditor recognizes a padded estimate from its shape in seconds, and the system records only the dollars they took out.
**Tags:** #tacit-knowledge-ml #anomaly-detection #large-language-models #worker-facing #data-integration

## The Problem
An estimate auditor who has reviewed thousands of files develops precise pattern recognition. That this contractor always adds the same three line items regardless of the loss. That a certain combination of demolition and detach-and-reset quantities means the scope was inflated after the fact. That equipment days claimed beyond a certain point for a given square footage are not credible. That a particular market's contractors all scope one repair a certain way and it is defensible even though it looks high.

The audit produces an adjustment: these line items reduced, this amount removed. The recognition that led there is not recorded. Neither is the equally valuable opposite — the auditor's judgment that an unusual-looking estimate was correct, and why.

So the next auditor rebuilds the same pattern recognition on the same contractors. And when an experienced auditor leaves, the network's ability to detect the specific ways its contractors deviate degrades immediately.

## Why It's Still Broken
The workflow ends at the adjustment. The system was built to process an audit to a dollar outcome under an SLA, and there is no object representing a pattern, a suspicion, or a judgment that something was fine.

Throughput pressure does the rest. Auditors are measured on files cleared, and recording why takes time that clears nothing.

And in a network where contractors are partners, a written record of staff suspicion about a specific company is uncomfortable, so that kind of observation stays verbal — which also makes it unaccumulable and untestable.

## What a Fix Looks Like
Capture the pattern, keep it internal, and test it against outcomes.

**Typed audit observations.** A short controlled vocabulary — line item combination inconsistent with the loss, quantities inconsistent with the property, equipment days beyond credible range, scope inflated on supplement, regional practice that looks high and is legitimate — recorded on the audit with a note. Seconds to enter, and it converts a private judgment into a record.

**Attached to the contractor and to the job type**, not only to the claim, because that is where the pattern lives and where the next auditor needs it.

**Validate against what happened.** Estimates flagged with a pattern can be checked against later supplements, reopens, and final settlements. Within a year the administrator would know which auditor patterns actually predict a problem — which no one in this industry can currently say — and the validated ones become legitimate inputs to audit targeting.

**Record the honest ones too.** An auditor determining that an unusual estimate was correct is preventing repeated review of a contractor doing nothing wrong, and it is the observation most likely to be lost.

**Surface at the point of audit.** An auditor opening a file should see what the network already knows about this contractor and this job type. That is the payoff, and it is what makes people record anything.

## Who Feels the Pain
Auditors, rebuilding knowledge colleagues already had. Network managers, whose detection capability is a set of tenures. Contractors, reviewed inconsistently depending on who drew the file. And carriers, paying for an accuracy check whose quality varies by staffing.

## Impact If Fixed
Audit is the administrator's core value to the carrier, and its effectiveness currently depends on individual auditors' accumulated pattern recognition in a role with real turnover. Capturing that, testing it against outcomes, and feeding the validated part back into targeting compounds the network's detection ability instead of resetting it with every departure.
