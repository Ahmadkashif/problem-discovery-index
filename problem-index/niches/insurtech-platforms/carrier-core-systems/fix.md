# The Data Conversion Nobody Validates Clinically

**Niche:** [[niches/insurtech-platforms/carrier-core-systems/profile|Carrier Core Systems]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A core system replacement converts decades of policy, billing and claims history from a legacy system, and conversion is validated by record counts and financial totals rather than by whether the converted policies actually mean the same thing.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #dimensionality-reduction #compliance #data-integration #automation
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A conversion moves two million policies. Counts match, premium totals reconcile, and the programme declares success. Six months later it emerges that a coverage option that existed on the legacy system as a flag was mapped to a default value for a subset of policies written before a particular year, that a class of endorsements lost their effective dates, and that a claims reserve category was consolidated in a way that makes historical development analysis unusable. Each was discoverable before go-live by a comparison nobody performed, because the validation was financial rather than semantic.

## Why It's Still Broken
Conversion validation was inherited from financial systems practice, where totals reconciling is genuinely the test. Insurance policies are structured objects whose meaning lives in coverage, limits, exclusions, endorsements and effective dates, and a total tells you nothing about whether those survived. Semantic validation requires defining what should be preserved, which requires product knowledge that conversion teams — staffed with data specialists — do not have and product teams are too busy to supply. And a conversion programme under deadline has every incentive to accept a validation that passes.

## What a Fix Looks Like
Validate clinically rather than financially. Define the properties that must hold — a policy's coverage set and limits are identical, endorsements retain their effective dates, claims retain their reserve category structure, renewal chains remain linked — as testable assertions and run them across the whole population rather than on a sample. Compare distributions by cohort rather than in aggregate, since defects cluster in subpopulations defined by the era or the configuration of the legacy system and vanish in a total. Stratify the human review deliberately toward the old, the complex and the structurally unusual policies instead of sampling uniformly. Reprice a sample of converted policies through the new rating configuration and compare against the legacy premium, which catches a whole class of defects that no structural comparison finds. And produce a signed fidelity report, which is what turns go-live from an act of faith into an accepted deliverable.

## Who Feels the Pain
Underwriters and service staff who find the defects one policy at a time in the months after go-live; actuaries whose historical analysis is corrupted by a mapping decision nobody recorded; and policyholders whose coverage silently changed.

## Impact If Fixed
Semantic validation finds systematic conversion defects before go-live rather than in production, which is the difference between a correction and a remediation programme. Most of the assertions are reusable across conversions, which means the investment is made once by a vendor or an implementation partner and applies to every subsequent programme.
