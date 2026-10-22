# A Beneficiary Location Engine for Matched Deaths

**Niche:** [[niches/life-insurance-carriers/beneficiaries-unclaimed-benefits/profile|Beneficiaries & Unclaimed Death Benefits]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers are good at matching an insured to a death record and poor at turning that match into a payment to the right living person.
**Tags:** #large-language-models #k-nearest-neighbors #logistic-regression #data-integration #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find and pay the beneficiary of a policy whose insured has died, before the proceeds escheat to the state, and whoever pays the highest share of confirmed death matches to the right person within the statutory search window takes the account.

## The Problem
A match comes back on a small whole life policy issued in 1979. The beneficiary is "spouse", the insured's address is decades old, and the policy file is an image. A claims analyst confirms the death, then begins a manual search. Each state's law sets the effort and timing required, and unresolved cases escheat, which ends the carrier's chance to pay the family directly and creates an audit exposure.

## Why Nobody Has Built This
Data vendors sell the match; skip-tracers sell the search; claims systems manage paid claims. The orchestration between them, including the designation reading, the family-tree reasoning and the state-rule tracking, sits with small compliance teams.

## What to Build
An engine that reads the designation and policy file, resolves relationships ("spouse", "children per stirpes") against public records and obituaries, ranks candidate beneficiaries with evidence, sequences outreach across mail, phone and email in language people trust, and records every step against each state's due-diligence requirement.

## Target Customer
Claims and unclaimed-property compliance leaders at carriers with large, old in-force blocks, and the in-force acquirers that inherit them.

## Impact If Built
More benefits reach families instead of state treasuries, with a defensible record for the next multistate audit.
