# The Attack Run by the Party Selling the Result

**Niche:** [[niches/synthetic-data-providers/evaluation-automation/profile|Evaluation Automation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Privacy attack results are produced by the vendor whose product is being attacked, with the attack strength as a free parameter, and reported as though they were an independent finding.
**Tags:** #hypothesis-testing #monte-carlo-methods #confidence-intervals #evaluation-metrics #compliance #descriptive-statistics #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to make evaluation a standard, reproducible run that a customer can execute themselves — and whoever does that takes the category's credibility, because a claim the buyer cannot reproduce is a claim they have to take on faith.

## The Problem
The report says a membership inference attack achieved accuracy close to chance. Attack success depends enormously on the method chosen, the auxiliary information the attacker is assumed to have, the number of shadow models, the threshold calibration and the population evaluated against. Every one of those was chosen by the vendor. A weak attack failing tells you almost nothing, and a weak attack is cheaper to run and produces a better number. The customer is shown a result whose informativeness was set by the party with an interest in it, presented in the register of an independent security finding.

## Why It's Still Broken
There is no specified protocol, so no choice is out of bounds. Running the strongest known attacks costs compute and produces worse numbers, which is a straightforward incentive. Customers cannot evaluate attack strength, so the question is never asked in the room where it matters. And the field's own literature shows wide variation in attack effectiveness, which means a vendor can cite a legitimate published method and still have chosen a weak one.

## What a Fix Looks Like
Specify the attack rather than the result. Publish a required attack suite at a specified strength — methods, shadow model counts, auxiliary information assumptions, calibration procedure — so that a reported result is a measurement rather than a choice, and this specification is the substance of the fix. State the adversary's assumed knowledge explicitly, since it is the single largest determinant of attack success and is almost never reported. Evaluate on the most vulnerable individuals rather than the average, because a guarantee exists for the outliers and aggregate accuracy near chance is entirely compatible with a handful of records being reliably identifiable. Report attack results with uncertainty, since attack accuracy varies across runs and single figures near chance are routinely within noise. Have attacks run by a party other than the vendor wherever the deal size justifies it, which is the structural fix and the one the category will resist longest. Publish the attack code alongside the result so it can be re-run and strengthened. And report negative results, since an attack that succeeded during development and was not included in the report is the failure mode this whole fix exists to close.

## Who Feels the Pain
Privacy officers relying on attack results as evidence; the individuals in the source data whose exposure a weak attack did not find; and the vendors running strong attacks honestly and losing comparisons because of it.

## Impact If Fixed
Attack strength is a free parameter chosen by the interested party, which makes the reported number uninformative in a known direction. A specified protocol with stated adversary knowledge, evaluated on the most vulnerable records, turns it into a measurement.
