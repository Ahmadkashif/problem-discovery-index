# Fix: Twenty-Five of Four Thousand

**Niche:** Audit Testing & Evidence
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The report says the control operated effectively, the basis is a sample the reader never sees, and the sample size was chosen by convention rather than by the population.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #descriptive-statistics #worker-facing
**Contested on:** Whether a control's operation is established from its full population or from twenty-five items because that is the convention.

## The Problem

A reader opens a SOC 2 report. Change management controls operated effectively throughout the period.

What happened is that an associate selected twenty-five change tickets from a population of several thousand, checked each for approval evidence, found them all approved, and recorded the test as passed.

The inference is standard, defensible and much weaker than the sentence suggests. A control failing on a meaningful fraction of changes has a substantial chance of producing twenty-five clean items. The confidence the test supports is a well-defined statistical quantity, it is not large, and it appears nowhere in the report.

The reader does not know the population size, the sample size, the sampling method or the resulting confidence. They know that a control operated effectively, which they reasonably read as a statement about all of it.

The same sample size appears across engagements of wildly different scale, because it is convention rather than a derivation from the population and the assurance sought. A company with forty employees and one with four thousand may receive samples of similar size for the same control.

Everyone in the profession understands the inference. No reader outside it does, and the report is written for the reader outside it.

## Why It's Still Broken

**The report format has nowhere to put it.** Attestation reports state opinions. Sample sizes and confidence levels are in the workpapers, which the reader never sees.

**The convention is defensible.** Sample sizes follow established guidance, which is a proper methodological basis and is not calibrated to each population.

**Disclosing it would weaken the artefact.** A reader told that the opinion rests on twenty-five of four thousand would weight the report differently, which is precisely the point and is not what the purchaser wants.

**The purchaser and the reader are different parties.** The company paying wants a clean report. The customer relying on it wants to know how searching the work was. Only the first is in the transaction.

**Nobody asks.** Enterprise vendor risk teams accept these reports at scale and do not ask about testing depth, because they do not know it varies.

**Competitors would be exposed.** A firm disclosing testing depth invites comparison, which is why no firm goes first.

## What a Fix Looks Like

**Disclose population and sample size per control.** An appendix table. It changes nothing about the opinion and transforms what a reader can do with it, and it is available within the existing report format today.

**Derive sample sizes from the population and the assurance sought.** Rather than applying a convention, compute what sample the desired confidence requires for this population. This is standard audit sampling method and is applied unevenly.

**Test everything where the data allows.** For controls whose population is available continuously, examine it all. Then the disclosure is simply that the full population was tested, which is a strong statement.

**Report exception rates where exceptions were found.** A control with three exceptions in four thousand items is meaningfully different from one with three in twenty-five, and the report currently cannot distinguish them.

**Explain the inference in the report.** A short standard paragraph explaining what sample-based testing establishes, written for a non-audit reader. Most readers have never been told.

**Relying parties should ask.** An enterprise vendor risk team requiring testing depth disclosure in the reports it accepts would change what firms provide, and it is a question they can start asking immediately.

**Standards bodies should require the disclosure.** This is the collective-action fix. Requiring population and sample disclosure makes the comparison possible and removes the penalty for the firm that would otherwise go first.

## Who Feels the Pain

The enterprise customer relying on the report to make a vendor decision, who reads a stronger statement than the evidence supports and has no way to know.

The auditor, who understands the inference precisely and issues a report whose language does not convey it.

Firms that test thoroughly, whose reports are indistinguishable from those of firms that do not, in a market that therefore competes on price.

And the company being audited, whose genuinely well-run controls produce the same artefact as a competitor's poorly-run ones.

## Impact If Fixed

A population and sample size table is an appendix, changes nothing about the opinion, and gives the reader the single piece of information they most need.

Deriving sample sizes from the population rather than from convention is existing method applied properly, and would substantially increase testing in the engagements where the populations are largest.

And a standards requirement to disclose testing depth is the collective fix, because it makes rigour visible and therefore purchasable — which is the missing mechanism in the entire market.
