# "My Wife Mary" in a 1988 Beneficiary Designation

**Niche:** [[niches/life-insurance-carriers/beneficiaries-unclaimed-benefits/profile|Beneficiaries & Unclaimed Death Benefits]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Beneficiary designations captured as free text decades ago are ambiguous or out of date, and the carrier learns this only after the insured dies.
**Tags:** #large-language-models #bert #data-integration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to find and pay the beneficiary of a policy whose insured has died, before the proceeds escheat to the state, and whoever pays the highest share of confirmed death matches to the right person within the statutory search window takes the account.

## The Problem
Designations like "my wife Mary", "my children" or a named person with no date of birth or address cannot be resolved without a search, and sometimes a court. Divorces, deaths and remarriages since issue make many of them wrong.

## Why It's Still Broken
Designations were captured as text on paper applications and keyed into admin fields with no structure. Carriers contact living policyholders for premiums and statements but rarely ask them to confirm beneficiaries.

## What a Fix Looks Like
Score every in-force designation for ambiguity and staleness. Prompt living policyholders to confirm or update at natural touchpoints (annual statements, service calls, premium notices), and store designations as structured, dated records.

## Who Feels the Pain
Grieving families waiting months; claims analysts doing genealogy; compliance teams facing escheatment audits.

## Impact If Fixed
Cleaner designations shorten claims for families and cut the unresolved cases that escheat.
