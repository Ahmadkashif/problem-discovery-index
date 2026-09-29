# Progress Verification Adapted to Percentage Complete

**Niche:** [[niches/general-contractors/construction-fund-control-inspection/profile|Construction Fund Control & Draw Inspection]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reality capture products document what a site looks like; a draw inspection has to convert that into a defensible percentage complete per schedule-of-values line, which is a judgment nobody automates.
**Tags:** #cnns #object-detection #semantic-segmentation #transformers #evaluation-metrics #confidence-intervals #feature-engineering #transfer-learning #automation #data-integration

## The Problem
An inspector walks a site and assigns a completion percentage to each line of the schedule of values — foundations, framing, mechanical rough-in, drywall — and those percentages determine how much money is released. The judgment is quick, experienced, and unevidenced beyond photographs. It is also where the disputes are: a contractor billing ninety percent on a line the inspector calls seventy has a real financial argument, and the inspector's basis is professional opinion. Consistency between inspectors on comparable work is unmeasured, and a lender relying on the percentages cannot see how firmly each is established.

## What Already Exists
Site documentation tooling is capable and inexpensive. Reality capture platforms produce navigable site records from a phone or helmet camera; photogrammetry generates dimensioned models; the construction management platforms handle photo organization and markup with location tagging.

## The Customization Gap
All of it documents; none of it quantifies against a schedule of values. The needed capability is estimating installed quantity of a defined scope from what is visible, expressed as a percentage of a contracted line item — which requires knowing what the line item covers, what the finished state looks like for that trade, and what is hidden behind completed work. The adaptation is trade-specific completion estimation tied to the schedule of values, with confidence stated per line, so an inspector's judgment is supported by an independent estimate and the divergences are where their attention goes. Hidden work needs explicit handling: much of what a draw pays for is behind drywall by the time anyone looks, so the system must reason from the sequence of prior captures rather than from the current one alone. And the output must be defensible to a contractor disputing it, which means citing the visual evidence rather than asserting a number.

## Target Customer
Heads of inspection operations at fund control firms, and the lenders whose draw decisions rest on percentages they cannot independently check.

## Impact If Solved
Puts evidence behind the number that releases money, which is where the disputes are and where the firm's liability sits. Consistency between inspectors also becomes measurable for the first time, which is the quality control a firm running hundreds of field staff currently lacks entirely.
