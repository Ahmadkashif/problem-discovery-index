# Trust Accounting with Benefit Eligibility Awareness

**Niche:** [[niches/estate-planning/special-needs-trusts/profile|Special Needs Trusts]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Trust accounting software tracks every dollar in and out of a trust — but no product flags when a distribution pattern threatens the beneficiary's SSI or Medicaid eligibility.
**Tags:** #decision-trees #logistic-regression #feature-engineering #evaluation-metrics #compliance #data-integration

## The Problem
Professional SNT trustees use trust accounting software (FAS, Surety, QuickBooks adapted for trusts) to track distributions, generate beneficiary statements, and prepare tax returns. These tools treat the trust as a financial account — they know the balance, the transactions, and the tax implications. They have zero awareness of SSI/Medicaid eligibility rules. A trustee could process a distribution that pushes the beneficiary over the $2,000 resource limit, and the accounting software would record it without any warning. The compliance layer exists entirely in the trustee's head or in a separate manual review process.

## What Already Exists
Trust accounting platforms (FAS, Fiduciary Accounting Solutions) are purpose-built for trust financial administration: they handle principal/income accounting, tax lot tracking, beneficiary statements, and court accounting reports. QuickBooks is used by smaller trustees with custom chart-of-accounts configurations. These tools are mature for their intended purpose but completely unaware of the benefit eligibility constraints that make SNT administration uniquely risky.

## The Customization Gap
The missing layer adds benefit eligibility monitoring to existing trust accounting workflows. When a trustee records a distribution, the system should: (1) categorize it under SSA's framework (not ISM, ISM under one-third rule, ISM under PMV rule, resource-affecting), (2) calculate the cumulative ISM impact on the beneficiary's SSI for the current month, (3) alert if the distribution would push the trust's countable resources (those attributable to the beneficiary) over the $2,000 limit, and (4) generate the compliance documentation required for the trust's records and annual reporting. This requires mapping trust accounting categories to SSA benefit categories — a translation layer that neither trust accounting vendors nor SSA has built.

## Target Customer
Professional trust companies managing 50-500 SNTs who use trust accounting software daily but run a separate manual compliance check process for every distribution, creating duplicate work and compliance risk when the manual check is skipped.

## Impact If Solved
Eliminates the separate compliance review step for routine distributions, saving 15-30 minutes per distribution across thousands of annual distributions per trust company. Catches compliance issues at the point of transaction entry rather than during quarterly reviews, preventing benefit-disqualifying distributions before they happen rather than discovering them after the fact.
