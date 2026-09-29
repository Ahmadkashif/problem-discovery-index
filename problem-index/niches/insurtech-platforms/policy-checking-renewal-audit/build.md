# Three-Way Comparison of Expiring, Requested and Issued

**Niche:** [[niches/insurtech-platforms/policy-checking-renewal-audit/profile|Policy Checking & Renewal Audit]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The check that matters is whether the policy the carrier issued matches what was requested and what expired, and it is performed by an experienced person reading three documents side by side, on the accounts big enough to justify it.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation #graph-theory
**Contested on:** Every serious competitor in policy checking is fighting to detect every material difference between an expiring policy, what was requested, and what the carrier actually issued — and whoever catches the most differences without a person reading both documents takes the account.

## The Problem
A renewal policy arrives. The agency requested the expiring terms with two changes — an added location and an increased limit. The issued policy has the new location, the increased limit, and, not mentioned anywhere in the correspondence, a newly added exclusion that the carrier applied at renewal across the class. Catching that means reading the whole policy against the expiring one, which takes an hour and a half for a moderately complex commercial account. The agency has four hundred renewals this quarter and the capacity to check perhaps the largest eighty. The exclusion goes unnoticed until a claim.

## Why Nobody Has Built This
Text-level document comparison produces unusable output on insurance policies, because forms are reissued with cosmetic changes constantly and a diff surfaces hundreds of irrelevant differences. Producing a useful comparison requires a structured coverage representation — the same capability the E&S niche needs — and extracting it has only recently become feasible. The request side is the other obstacle: the third document in the comparison is frequently an email thread or a marked-up application rather than a structured artefact, so there is nothing to compare against without extracting the request too.

## What to Build
A coverage representation extracted from all three documents and compared structurally. Expiring policy, requested terms and issued policy each resolve to a structured set of coverages, limits, deductibles, named insureds, scheduled items, endorsements and exclusions, with endorsement stacks resolved so the comparison is between operative terms rather than base forms. Differences are classified: requested and delivered, requested and not delivered, delivered but not requested, and changed from expiring without being requested — which is the category that matters most and is the hardest to find by reading. Each difference is rated for materiality against the client's exposures and cited to the clause. The output is a review list ordered by consequence, which an experienced person confirms in minutes rather than discovering in hours. Catch rate is measured against human checking during rollout, because an automated check that misses things silently is worse than no check and the agency needs to know which it has.

## Target Customer
Independent agencies and brokerages of all sizes, carrier quality assurance functions performing the same check from the other side, and the agency management system vendors.

## Impact If Built
The differences this catches are coverage gaps a client does not know they have and an agency is exposed on, and the current practice knowingly leaves most of the book unchecked for want of capacity. Bringing checking to the whole book rather than the largest accounts is the change, and it is available the moment the comparison stops requiring an hour of an experienced person's attention.
