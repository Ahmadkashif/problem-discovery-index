# Reporting Latency as a Measured Property, Not an Assumption

**Niche:** [[niches/funeral-homes/death-verification-data-providers/profile|Death Verification Data Providers]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every customer decision assumes that a death not in the file has not happened, and the interval between a death and its appearance varies from days to months depending on where and how the person died.
**Tags:** #survival-analysis #probability-distributions #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #feature-engineering #data-integration #compliance

## The Problem
The product is used to decide whether to continue paying an annuity, release a benefit, or extend credit, and every one of those decisions treats absence from the file as evidence of life. That inference is only as good as the reporting pipeline, and the pipeline is wildly uneven: a death certified quickly in one state and reported by a cooperative funeral home may appear in days, while a death under medical examiner investigation, or in a jurisdiction with slow registration, may take months. The provider knows this exists and does not quantify it. So a customer cannot tell whether a clean check means the person is alive or means the record has not arrived yet, and the difference is an improper payment or an unpaid beneficiary.

## Why Nobody Has Built This
Measuring latency requires knowing the true date of death for records that had not yet arrived, which is available only retrospectively — but that is precisely what makes it tractable, because every record eventually arrives with a date of death attached and the arrival timestamp is recorded. The analysis is straightforward once someone decides to run it; nobody has, because the product has always been sold on coverage counts and match rates, and a latency distribution is an unflattering complication.

## What to Build
A latency model estimated from the provider's own arrival history: for each record, the interval between date of death and date of availability, modelled by jurisdiction, source type, cause and manner where known, decedent demographics, and season. That produces the quantity every customer actually needs — given a search returning no match today, the probability that the person is alive versus the probability that a death has occurred and not yet reported, expressed as a curve over elapsed time. Customers can then set thresholds appropriate to their own risk: a pension administrator can hold a payment where latency risk is high, and release confidently where it is low. Internally the same model directs source acquisition at the jurisdictions and death types where reporting is slowest, which is where the improper payments actually concentrate and where coverage counts say nothing.

## Target Customer
Chief data officers and heads of data products at death data providers, and the pension, annuity, and benefit administrators who treat absence of a record as proof of life.

## Impact If Built
Converts the product's central unstated assumption into a quantified one, which is directly actionable for every customer and cannot be replicated by a competitor without the same arrival history. It also redirects source acquisition — the dominant cost — from coverage breadth to latency reduction, which is what customers are actually paying to solve.
